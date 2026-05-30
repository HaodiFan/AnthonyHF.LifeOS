---
version: beta
name: AF Flow Console
description: A GSAP-driven public interface for Anthony Fan's LifeOS showroom, AF-wiki memory, static identity assets, runtime projections, and deployment network.
colors:
  primary: "#F4F1E8"
  secondary: "#A9A49A"
  tertiary: "#3DD6C6"
  neutral: "#080807"
  surface: "#11110F"
  surface-raised: "#171715"
  border: "#34332E"
  accent-green: "#66D37E"
  accent-blue: "#77A7FF"
  accent-amber: "#FFB454"
  accent-coral: "#FF6B5D"
  accent-gold: "#E6C55A"
  on-tertiary: "#06100F"
typography:
  h1:
    fontFamily: Inter
    fontSize: 4.5rem
    fontWeight: 650
    lineHeight: 0.98
    letterSpacing: "0px"
  h2:
    fontFamily: Inter
    fontSize: 3rem
    fontWeight: 620
    lineHeight: 1.05
    letterSpacing: "0px"
  h3:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: 620
    lineHeight: 1.2
    letterSpacing: "0px"
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: "0px"
  mono-label:
    fontFamily: JetBrains Mono
    fontSize: 0.75rem
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0px"
rounded:
  sm: 4px
  md: 8px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  xxl: 96px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-tertiary}"
    rounded: "{rounded.md}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
  panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 24px
  panel-raised:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 24px
  badge:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.sm}"
    padding: 8px
  badge-border:
    backgroundColor: "{colors.border}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 8px
  badge-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    padding: 8px
  badge-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    padding: 8px
  badge-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    padding: 8px
  badge-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    padding: 8px
  badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    padding: 8px
---

## Overview

AF Flow Console is the shared visual language for Anthony Fan's public profile network. It should make the system readable to humans and agents: identity, skills, AF-wiki memory, public boundary, personal assets, runtime projections, and deployment links.

The homepage is now a Vite React page using GSAP ScrollTrigger through `apps/homepage/components/ui/story-scroll.tsx`. It should feel like a precise scrollable system poster rather than a generic personal landing page. Visual density is acceptable when it improves routing clarity.

## Colors

- **Neutral ({colors.neutral}):** Page canvas.
- **Surface ({colors.surface}):** Standard panels and repeated entries.
- **Surface Raised ({colors.surface-raised}):** Active or featured nodes.
- **Primary ({colors.primary}):** Main text.
- **Secondary ({colors.secondary}):** Metadata and body copy.
- **Tertiary ({colors.tertiary}):** Current route and primary interactions.
- **Accents:** Reserve green, blue, amber, coral, and gold for system layers and data categories.

## Typography

Use Inter for interface text and JetBrains Mono for route labels, counters, file names, and source states. Keep all letter spacing at `0px`.

## Layout

Use full-viewport story sections. Hero text is unframed; cards are only for repeated nodes, links, and capability blocks. The README cover image should stay visible as a first-viewport signal, while the rest of the page uses personal photos, public project logos, product images, and AF-wiki routing visualizations.

## Elevation & Depth

Use borders and inset highlights. Avoid decorative orbs, frosted marketing cards, and heavy glow effects.

## Shapes

Use 4px for small controls and 8px for panels. Avoid large rounded cards unless an existing visual asset requires a frame.

## Components

- `button-primary` routes to the highest-priority public entry.
- `panel` groups identity, skill, memory, and boundary content.
- `badge` labels repo paths, skill routes, and public/private status.
- `story-scroll` provides the GSAP section rotation and pinning behavior.

## Do's and Don'ts

- **Do** link AF-wiki, GitHub Profile, AnthonyHF.LifeOS, OpenClaw/Hermes projections, and app deployments together.
- **Do** make the AI collaboration boundary explicit.
- **Do** keep useful public static assets in `apps/homepage/public/assets/` with provenance notes.
- **Don't** publish raw private source material or client-specific details.
- **Don't** use decorative generated imagery as the primary information layer.
