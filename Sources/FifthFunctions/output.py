



def available_languages(transcript_subtitles):
    language = transcript_subtitles.translation_languages

    available_lang = ", ".join(
        f"{languages.language} ({languages.language_code})"
        for languages in language
    )

    return available_lang


def transcript_fetch(transcript_subtitles):
    snippets = transcript_subtitles.fetch()

    full_text = "\n\n".join(snippet.text for snippet in snippets)

    return full_text

def output(transcript_subtitles, available_lang, full_text):
    print(f"{transcript_subtitles.video_id}\n"
        f"{transcript_subtitles.language}, {transcript_subtitles.language_code}\n"
        f"Available languages: {available_lang}\n"
        f"Transcript:"
        f"\n\n\n{full_text}")