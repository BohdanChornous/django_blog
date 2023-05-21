from django.shortcuts import render
from .forms import TestSolvForm
from django.views import View
import openai
import cv2
import pytesseract
from .image_utils import imread
# Create your views here.


openai.api_key = "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"


class TestSolvView(View):

    def chat_answer(self, text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0.9,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["!Stop!"]
        )
        return response['choices'][0]['text']

    def text_from_image(self, image_path):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR/tesseract.exe"
        # r'/usr/bin/tesseract'

        lang = 'eng'  # Replace with the appropriate language code
        img = imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        _, result = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
        adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 55)
        custom_config = f'--oem 3 --psm 6'
        text = pytesseract.image_to_string(adaptive, lang=lang, config=custom_config)
        return text

    def get(self, request, **kwargs):

        context = {
            "comment_form": TestSolvForm(),
            "ams_fild": False,
            **kwargs
        }
        return render(request, "GPT_test_solver/index.html", context=context)

    def post(self, request):

        comment_form = TestSolvForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment_form.save()
            image_name = comment_form.data["test_name"]
            image = comment_form.instance.image
            img_text = self.text_from_image(image.path)
            answer = self.chat_answer(img_text)
            context = {
                "test_name": image_name,
                "test_answer": answer,
                "ams_fild": True,
                "image": comment_form.instance.image
            }
            return self.get(request, **context)
        return self.get(request, comment_form=comment_form)
