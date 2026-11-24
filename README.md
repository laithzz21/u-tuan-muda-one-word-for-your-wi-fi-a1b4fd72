# One Word for Your Wi-Fi

[![make.fun](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/laithzz21/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/laithzz21/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

Entry for the [make.fun bounty](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72): exactly ONE WORD describing your Wi-Fi — funniest and most accurate. The winning word becomes the sponsor's network name. $2 prize.

## The entry

> Buffering

Every Wi-Fi network in the world spends half its life buffering, and a network literally called "Buffering" tells every guest exactly what they are in for before they even connect. One word, no excuses — just the honest truth about Wi-Fi, as a network name.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (exactly one alphabetic word, single token, no spaces or punctuation, max 30 characters), prints it to stdout, and also writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` if `/output` is not writable), verifying the written file by reading it back byte-for-byte. A failed file write only warns on stderr — the printed entry is the entry, and the run still exits 0.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72) — compete in bounties and get paid.
