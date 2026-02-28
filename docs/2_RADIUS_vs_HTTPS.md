🔥 This is the right question.

Now you’re thinking architecturally.

Let’s slow down and separate **what you *can* do** from **what you *should* do**.

---

# Short Answer

Yes.

You absolutely *can*:

Client → HTTPS → AAA API → MySQL

And for a pure software app, that is the modern approach.

But your project is not just “login validation.”

You’re building an **AAA server for network devices**.

That changes everything.

---

# 🧠 The Real Difference

## Option 1 — HTTPS Model (Web Auth Style)

Architecture:

```text
Client → HTTPS REST API → Auth Service → MySQL
```

This is how:

* Web apps
* SaaS platforms
* Mobile apps
* OAuth systems

work.

This is modern, clean, JSON-based.

---

## Option 2 — RADIUS Model (Network AAA Style)

Architecture:

```text
Network Device → RADIUS (UDP 1812) → AAA Server → MySQL
```

This is how:

* Routers
* Switches
* VPN gateways
* Firewalls
* WiFi controllers

authenticate users.

Those devices do NOT speak HTTPS for authentication.

They speak RADIUS.

---

# 🚨 The Critical Point

Network infrastructure devices do not call REST APIs.

They are built to use:

* RADIUS
* TACACS+

Not:

* JSON
* HTTPS login APIs

If your goal is:

> “Build an AAA server compatible with network devices”

Then RADIUS is mandatory.

---

# 🔍 So Why Not Just Use HTTPS?

Because HTTPS assumes:

* Client understands REST
* Client can parse JSON
* Client can do TLS handshake
* Client supports modern auth flows

A Cisco router, for example, expects:

* RADIUS packet format
* UDP
* Shared secret
* Attribute-based response

Not HTTP 200 with JSON.

---

# 🧠 Think of It This Way

HTTPS model is:

Application-layer authentication.

RADIUS model is:

Infrastructure-layer authentication.

You are building infrastructure.

---

# 🔥 When Would HTTPS Be Correct?

If FA3H was:

* A SaaS identity platform
* A web login system
* An OAuth server
* A microservice auth backend

Then HTTPS would be perfect.

But that’s not AAA in networking terms.

---

# 🎯 So What Are You Actually Building?

This is the real decision.

Are you building:

### A) Network AAA Server (ISE alternative)

→ Must use RADIUS

OR

### B) Authentication Microservice

→ Should use HTTPS

These are different products.

---

# 🧬 Strategic Advice

Since you want:

* Deep protocol knowledge
* Infrastructure understanding
* Hardware-agnostic AAA
* Potential to integrate with real devices later

Then:

RADIUS is the correct foundation.

Because once you understand RADIUS,
HTTPS auth will feel trivial.

But the reverse is not true.

---

# ⚖ Hybrid Option (Very Smart)

Real enterprise systems do both.

Example:

* Network devices → RADIUS
* Admin UI → HTTPS
* Internal services → REST

You can design FA3H like this later.

But start with RADIUS.

Because that’s the harder engineering problem.

---

Now that’s a clear goal. Good.

You’re not building “auth for fun.”
You want:

> FA3H → RADIUS → FMC login in your lab

That is a real, concrete, measurable milestone.

Let’s ground this properly.

---

