# Tutoriales lote 2 — short design addendum

Fecha: 2026-11-24
Extiende: `docs/superpowers/specs/2026-11-24-tutoriales-design.md` (mismo formato híbrido, mismo patrón `web-tools`).
Estado: propuesta para aprobación

## Intent / por qué
Atacar `partes de un beat` (pos 2.0) con guía dedicada de título exacto, y sumar la guía de bass lines (video pt2 real del canal). El autor confirma que NO tiene video de cuantizar: no se inventa contenido que el video no cubre. La query `como cuantizar en fl studio` (pos 4.0) queda aparcada hasta tener video base.

## Goals
- `/tutoriales/partes-de-un-beat/` ES+EN con video base pt1 `7LfwEb4ds4` (Como hacer Beats en FL Studio | La forma sencilla!, 10:50).
- `/tutoriales/bass-lines-fl-studio/` ES+EN con video base pt2 `1mFZIt85qLE` (Como hacer Beats en FL Studio pt 2 | Bass Lines, 11:56).
- Cada guía: 400-600 palabras, título fiel al video, embed youtube-nocookie + fallback, HowTo + VideoObject, CTA a tool relacionada, FAQ con queries del cluster (`partes de un beat`, `bass lines fl studio`, `como hacer bass lines`).
- Índice `/tutoriales/` ES+EN: activar las 2 cards (quitar `Próximamente`/`Soon`, enlazar rutas reales). La 3ª card (cuantizar) se elimina del índice — sin video base no hay card.

## Non-goals
- No guía 4 todavía (TRAKKCONVERTER/`roland fl studio` es ajuste SEO de página existente, 10 min, separado).
- No EN más allá de traducción directa. No cambios al piloto `fl-studio-ia` (uploadDate placeholder sigue aparcado).

## Constraints (heredados del lote 1)
- GTM `GTM-NMVJZ8VL` + consent `sb-consent` por página; footer marca + CC BY-NC-SA 4.0; ES+EN con canonical/hreflang; apps `GPL-3.0-only` (sin menciones MIT); UTF-8 estricto (verificado con python en lote 1).

## Approaches
- Solo viable: mismo híbrido del lote 1 (probado, QA en verde, mergeado). Sin alternativas — el patrón ya está aprobado y en producción.

## Queda al builder
- Títulos exactos: ES `Partes de un beat: estructura de intro, verso y hook | ShardBeats` / `Cómo hacer bass lines en FL Studio | ShardBeats` (EN espejo). Ajuste menor permitido si el builder propone mejor keyword match, reportado.
- CTA: partes → `/tools/trakkname/` (nombrar secciones) o `/tools/` general; bass lines → sin tool directa (CTA a `/tools/` + resto de la serie FL Studio).
