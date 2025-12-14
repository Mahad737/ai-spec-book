import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

export default function Home() {
  return (
    <Layout
      title="AI / Spec-Driven Book"
      description="AI-generated book with RAG chatbot and spec-driven workflows"
    >
      <main
        style={{
          minHeight: '80vh',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '4rem 2rem',
        }}
      >
        <div
          style={{
            maxWidth: '1000px',
            display: 'grid',
            gridTemplateColumns: '1.2fr 1fr',
            gap: '3rem',
            alignItems: 'center',
          }}
        >
          {/* LEFT TEXT */}
          <div>
            <h1 style={{ fontSize: '3rem', marginBottom: '1rem' }}>
              AI / Spec-Driven Book
            </h1>

            <p style={{ fontSize: '1.2rem', lineHeight: 1.6 }}>
              A modern, AI-native book generated using
              <strong> Claude Code</strong>,
              <strong> Spec-Kit Plus</strong> and
              <strong> open-source LLMs</strong>.
            </p>

            <p style={{ marginTop: '1rem', opacity: 0.8 }}>
              Learn how specifications, Retrieval-Augmented Generation,
              and automation can produce real production-grade knowledge.
            </p>

            <Link
              className="button button--primary button--lg"
              to="/docs/intro"
              style={{ marginTop: '2rem' }}
            >
              Read the Book →
            </Link>
          </div>

          {/* RIGHT IMAGE */}
          <div style={{ textAlign: 'center' }}>
            <img
              src="/img/hero-ai-book.png"
              alt="AI Spec Book"
              style={{
                maxWidth: '100%',
                borderRadius: '12px',
                boxShadow: '0 20px 40px rgba(0,0,0,0.3)',
              }}
            />
          </div>
        </div>
      </main>
    </Layout>
  );
}
