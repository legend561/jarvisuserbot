from jarvis import topfunc
from jarvis.jconfig import Config
from jarvis.utils import admin_cmd
from var import Var

idgen = topfunc.id_generator
findnemo = topfunc.stark_finder
sudousing = Config.SUDO_USERS
pmlogss = Config.PM_LOGGR_BOT_API_ID
isdbfine = Var.DB_URI
updaterok = Var.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
currentversion = "3.2"
if sudousing:
    ssudo = "Active ✅"
else:
    ssudo = "Inactive ❌"

if pmlogss:
    pmllogs = "Connected ✅"
else:
    pmllogs = "Dis-Connected ❌"

if updaterok:
    updaterr = "Connected ✅"
else:
    updaterr = "Not Connected ❌"

if gdriveisshit:
    wearenoob = "Active ✅"
else:
    wearenoob = "Inactive ❌"

if rmbg:
    gendu = "Added ✅"
else:
    gendu = "Not Added ❌"

if isdbfine:
    dbstats = "Fine ✅"
else:
    dbstats = "Not Fine ❌"

inlinestats = (
    f"✘ SHOWING JARVIS STATS ✘\n"
    f"VERSION = {currentversion} \n"
    f"DATABASE = {dbstats} \n"
    f"SUDO = {ssudo} \n"
    f"PM LOGS = {pmllogs} \n"
    f"HEROKU = {updaterr} \n"
    f"G-DRIVE = {wearenoob}"
)
