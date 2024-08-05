from flask import Blueprint, render_template, request
from src.models.language_model import LanguageModel
from deep_translator import GoogleTranslator
import logging
logging.basicConfig(level=logging.DEBUG)

translate_controller = Blueprint('translate_controller', __name__)


@translate_controller.route("/", methods=["GET"])
def index():
    languages = LanguageModel.list_dicts()
    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated
    )


@translate_controller.route("/", methods=["POST"])
def translate():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translator = GoogleTranslator(source=translate_from, target=translate_to)

    try:
        translated_text = translator.translate(text_to_translate)
    except Exception as e:
        translated_text = f"Erro na tradução: {str(e)}"

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated_text
    )


@translate_controller.route("/reverse", methods=["POST"])
def reverse_translate():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    reversed_translate_from = translate_to
    reversed_translate_to = translate_from

    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=translated,
        translated=text_to_translate,
        translate_from=reversed_translate_from,
        translate_to=reversed_translate_to
    )