export default function SectionTitle({ emoji, children }) {
  return (
    <h2 className="section-title section-anchor">
      {emoji && <span className="section-emoji" aria-hidden="true">{emoji}</span>}
      <span className="section-text">{children}</span>
    </h2>
  );
}
