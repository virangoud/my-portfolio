import { useState } from "react";
import SectionTitle from "./SectionTitle.jsx";
import portfolio from "../data/portfolio.js";

const EMPTY = { name: "", email: "", message: "" };

export default function Contact() {
  const { email, githubUrl, githubUsername, linkedinUrl } = portfolio;
  const [form, setForm] = useState(EMPTY);
  const [status, setStatus] = useState(null); // { type: "success" | "warning" | "error", text }
  const [sending, setSending] = useState(false);

  const update = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  async function handleSubmit(e) {
    e.preventDefault();
    if (!form.name.trim() || !form.email.trim() || !form.message.trim()) {
      setStatus({ type: "error", text: "Please fill in all fields before submitting." });
      return;
    }

    setSending(true);
    setStatus(null);
    try {
      const res = await fetch(`https://formsubmit.co/ajax/${email}`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({
          ...form,
          _subject: `Portfolio Contact from ${form.name}`,
          _captcha: "false",
        }),
      });
      if (res.ok) {
        setStatus({ type: "success", text: `✅ Message sent! I'll get back to you soon at ${email}` });
        setForm(EMPTY);
      } else {
        setStatus({ type: "warning", text: `⚠️ Could not deliver right now. Please email me directly at ${email}` });
      }
    } catch {
      setStatus({ type: "warning", text: `⚠️ Network issue. Please email me directly at ${email}` });
    } finally {
      setSending(false);
    }
  }

  return (
    <section id="contact">
      <SectionTitle emoji="✉️">Contact Me</SectionTitle>
      <div className="grid-2">
        <div className="glass-card">
          <h3 style={{ color: "#d4af37", marginTop: 0 }}>Get in Touch</h3>
          <p className="body-text" style={{ marginBottom: 25 }}>
            Have a project in mind, a job opportunity, or a dashboard you need built? Feel free to send a message or
            contact me directly via email. I look forward to working with you!
          </p>
          <div className="contact-line">
            <strong><i className="fas fa-envelope" style={{ marginRight: 10 }} /> Email:</strong>
            <br />
            <a href={`mailto:${email}`}>{email}</a>
          </div>
          <div className="contact-line">
            <strong><i className="fab fa-github" style={{ marginRight: 10 }} /> GitHub:</strong>
            <br />
            <a href={githubUrl} target="_blank" rel="noopener noreferrer">github.com/{githubUsername}</a>
          </div>
          <div className="contact-line">
            <strong><i className="fab fa-linkedin" style={{ marginRight: 10 }} /> LinkedIn:</strong>
            <br />
            <a href={linkedinUrl} target="_blank" rel="noopener noreferrer">{linkedinUrl.replace("https://www.", "")}</a>
          </div>
        </div>

        <div className="glass-card">
          <h3 style={{ color: "#f5e27a", marginTop: 0, marginBottom: 15 }}>Send a Message</h3>
          <form className="contact-form" onSubmit={handleSubmit} noValidate>
            <label>
              Your Name
              <input type="text" name="name" value={form.name} onChange={update} />
            </label>
            <label>
              Your Email Address
              <input type="email" name="email" value={form.email} onChange={update} />
            </label>
            <label>
              Your Message
              <textarea
                name="message"
                rows={5}
                value={form.message}
                onChange={update}
                placeholder="Tell me about your project or enquiry..."
              />
            </label>
            <button type="submit" className="btn-glow" disabled={sending}>
              {sending ? "Sending..." : "📨 Send Message"}
            </button>
            {status && <div className={`form-status ${status.type}`}>{status.text}</div>}
          </form>
        </div>
      </div>
    </section>
  );
}
