"""Take screenshot of any website
Syntax: .screenlong <Website URL>"""

import io
import traceback
from datetime import datetime

from selenium import webdriver

from jarvis.utils import j_cmd, eor, sudo_cmd


@jarvis.on(j_cmd("screenlong (.*)", outgoing=True))
@jarvis.on(sudo_cmd("screenlong (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.GOOGLE_CHROME_BIN is None:
        await eor(event, "need to install Google Chrome. Module Stopping.")
        return
    jevent = await eor(event, "Processing ...")
    start = datetime.now()
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--headless")
        # https://stackoverflow.com/a/53073789/4723940
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
        await jevent.edit("Starting Google Chrome BIN")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        input_str = event.pattern_match.group(1)
        driver.get(input_str)
        await jevent.edit("Calculating Page Dimensions")
        height = driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);"
        )
        width = driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);"
        )
        await jevent.edit("Painting web-page")
        driver.set_window_size(width + 100, height + 100)
        # Add some pixels on top of the calculated dimensions
        # for good measure to make the scroll bars disappear
        im_png = driver.get_screenshot_as_png()
        # saves screenshot of entire page
        driver.close()
        await jevent.edit("Stopping Google Chrome BIN")
        message_id = event.message.id
        if event.reply_to_msg_id:
            message_id = event.reply_to_msg_id
        with io.BytesIO(im_png) as out_file:
            out_file.name = "@UniBorg.ScreenCapture.PNG"
            await jarvis.send_file(
                event.chat_id,
                out_file,
                caption=input_str,
                force_document=True,
                reply_to=message_id,
                allow_cache=False,
                silent=True,
            )
        end = datetime.now()
        ms = (end - start).seconds
        await jevent.edit(f"Completed screencapture Process in {ms} seconds")
    except Exception:
        await jevent.edit(traceback.format_exc())
