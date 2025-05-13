captcha_button = """
function captchaSuccess() {
    checkbox = document.getElementById('captcha-box');
    paragraph = document.getElementById('robotP');
    if (checkbox.checked) {
        paragraph.innerText = 'Success! Loading...';
    } else {
        paragraph.innerText = 'I was a robot after all...';
    }
}
"""
captcha_message = """
function captchaMessage() {
    checkbox = document.getElementById('captcha-box');
    paragraph = document.getElementById('robotP');
    if (checkbox.checked) {
        paragraph.innerText = 'I am not a robot!';
    } else {
        paragraph.innerText = 'I am a robot!';
    }
}
"""