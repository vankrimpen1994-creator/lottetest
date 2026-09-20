# Sample Posts — written for the pitch

Three posts, three pillars, three ICPs. Show these on the call. They're the fastest way
to prove the voice is right before anyone has to trust a plan.

> Every factual claim below is sourced in `01-strategy/client-profile.md`. Nothing is invented.

---

## 1 · Trust & Control — ICP A (buyers) · text + stat card · founder profile

> Would you give an autonomous process your company card?
>
> Nobody says yes to that question. But 165 million agent payments happened on x402 last year, and almost none of them had a hard spend cap.
>
> That gap is the whole problem with agent payments right now. The tooling raced ahead of the controls.
>
> Three questions worth asking of anything you let an agent pay with:
>
> 1. Is the spend policy checked before the transaction is signed, or after it fails?
> 2. Where does the private key actually live? If the answer is "our servers", you've outsourced custody without calling it that.
> 3. Is there a receipt? Not a dashboard you can log into — a record you hold.
>
> We built vAPI Network around those three answers, because we couldn't find a tool that gave all three. Key stays encrypted on your machine. Policy applies before signing. Every payment writes to a local append-only ledger.
>
> None of that is exciting. It's just what has to be true before finance signs off.
>
> What's stopping you from letting an agent spend money today — the tech, or the audit trail?
>
> #x402 #agenticpayments #agenteconomy

**Visual:** stat card — "165,000,000 agent payments. Almost no spend caps."
**First comment:** link to the Hacken audit + the repo.
**Why it works:** opens with the reader's fear, answers with mechanisms, ends with a
question that is genuine ICP research. No product pitch until line 8.

---

## 2 · The Agent Economy — ICP A + B · carousel, 8 slides · company page

**Title:** *x402, explained for people who don't work in crypto*

| Slide | Copy |
|---|---|
| 1 | **x402, explained for people who don't work in crypto.** There's a payments standard behind AI agents. Your board has probably heard of the members. |
| 2 | HTTP has always had a status code reserved for this. **402: Payment Required.** It sat unused for about 30 years. |
| 3 | x402 finally uses it. A server answers a request with "402 — this costs $0.004." The client pays. The request goes through. No account. No login. No invoice. |
| 4 | **Why now:** agents. A human can fill in a billing form. An autonomous process at 3am cannot. |
| 5 | **Who's behind it:** Coinbase launched it in 2025. Governance moved to the **Linux Foundation in April 2026** — 22 launch members including Google, Visa, Mastercard, Stripe, AWS and Circle. |
| 6 | **The scale so far:** 69,000 active agents. 165 million transactions. Over 80% settling on Base, almost all in USDC. |
| 7 | **What it changes:** an API can be sold per request, to a machine, for fractions of a cent — with no billing page and no chasing payment. |
| 8 | vAPI Network is one wallet for every x402 API. Non-custodial, spend-capped, audited, Apache 2.0. **Link in the comments.** |

**Why it works:** vendor-neutral for 7 of 8 slides, so it travels. The Linux Foundation
slide is the one that gets screenshotted — it's what reframes this from "crypto" to
"standard". Carousels get the best dwell time on LinkedIn.

---

## 3 · Supply-Side — ICP B (sellers) · text + image · company page

> Your API made four-tenths of a cent last night, and you didn't do anything.
>
> That's the part that takes a while to get used to.
>
> If you run an API today, monetising it means a billing provider, a pricing page, a login wall, invoicing, and someone chasing a $40 invoice for three weeks. For a call worth $0.004, the overhead is comically larger than the payment.
>
> So most people don't bother. The API stays internal, or free, or behind a wall that only enterprise customers get past.
>
> x402 removes the overhead. A machine requests your endpoint, gets told the price, pays it, and gets the response. No account created. No invoice raised. Money settles directly to you in USDC.
>
> There are roughly 69,000 active agents already doing this, across 165 million transactions.
>
> vAPI Network is how they find you and pay you.
>
> If you've got an API sitting behind a login wall because billing wasn't worth the effort — that reason expired.
>
> What would you list first?
>
> #x402 #apimonetization #agenteconomy

**Visual:** simple receipt graphic — one line item, `$0.004`, 03:41 UTC, settled.
**Why it works:** concrete scene as the hook, names the exact operational pain the ICP
lives with, and the close is a low-friction question rather than a demo request.
