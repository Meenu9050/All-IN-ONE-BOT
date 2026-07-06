# All-IN-ONE-BOT merged with music

Base repo: `Meenu9050/All-IN-ONE-BOT` branch `ALONE`

Music repo merged from: `Meenu9050/all-in-one-music` branch `ALONE`

## What changed

- Added the music bot code under `AloneXMusic/` to avoid overwriting the existing `AloneX/` group management code.
- Connected music startup from `AloneX/__main__.py`.
- Preserved the existing Heroku startup: `web: python3 -m AloneX`.
- Added music dependencies to `requirements.txt`.
- Added music Heroku env variables to `app.json`.
- Music config supports both old music names and main bot names:
  - `BOT_TOKEN` or `TOKEN`
  - `MONGO_URL` or `DB_URL`
  - `SESSION` or `USER_STRING`
  - `LOGGER_ID` or `LOG_GROUP_ID`
  - `OWNER_ID` or `ALONE_OWNER_ID`

## Required Heroku variables

Keep the existing main bot variables and add:

- `USER_STRING`: Pyrogram string session for music assistant
- `MUSIC_ENABLED`: `True`

Optional:

- `SESSION2`
- `SESSION3`
- `YOUTUBE_API_KEY`
- `COOKIES_URL`

If music config is incomplete, set `MUSIC_ENABLED=False` to run only group management while you fix variables.
