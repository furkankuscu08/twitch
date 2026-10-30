# Demo-day checklist

- [ ] Confirm `.env` privately: `DEEPGRAM_API_KEY`, region/backend, `TWITCH_CLIENT_ID`, `TWITCH_BROADCASTER_LOGIN` and `TWITCH_BOT_LOGIN`. Keep credentials out of the recording.
- [ ] Confirm the configured bot is a channel moderator and its saved login works. Use `TWITCH_TEST_LOGIN` for automated live checks before the demo.
- [ ] Run `./scripts/run_all.sh`. Open the printed mic URL in Windows Chrome, allow access, choose the correct mic and start capture.
- [ ] Check dock health: mic, engine, Deepgram, EventSub and tunnel. Confirm the current plant URL/QR; restart URLs are temporary.
- [ ] Set the OBS overlay browser source to 1920×1080 and the dock to about 400 px. Confirm transparency, enable browser-source audio through OBS and balance the boom below speech.
- [ ] Start a round. Open the plant link on a phone over mobile data, pick a card and paste `!mine CODE` in the Twitch app. Wait for arming, then steer the conversation naturally.
- [ ] Keep the dock visible: False alarm is available for 10 seconds after a mistaken boom. End the round to show survivors and the recap.
- [ ] If speech recognition fails, use typed mode from the dock; if necessary restart with `STT_BACKEND=nova3`. For a completely offline presentation, use `./scripts/run_all.sh --demo`, debug planting and `/overlay?demo=1`.
- [ ] After the demo, end the round and press Ctrl+C in the launcher. Confirm the local pages and public tunnel have stopped. Keep requested rehearsal hypotheses private under `data/` for later diagnosis.
