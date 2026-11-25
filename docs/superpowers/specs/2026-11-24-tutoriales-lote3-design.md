# Tutoriales lote 3 — short design addendum

Fecha: 2026-11-24
Extiende: `docs/superpowers/specs/2026-11-24-tutoriales-design.md` y lote 2 (`docs/superpowers/specs/2026-11-24-tutoriales-lote2-design.md`).
Estado: propuesta para aprobación

## Intent / por qué
Atacar `roland fl studio` (TikTok GSC pos 3.0, 2 imp) con guía dedicada cuyo video base YA existe en @ShardBtmking y cuyo CTA es TRAKKCONVERTER. Cierra el gap 3 del análisis Lytics (TRAKKCONVERTER solo rankea sin keyword en título).

## Goals
- `/tutoriales/sp-404-mk2-preparar-samples/` ES+EN con video base `UAMboy8mtro` (SP-404 MK2 TUTORIAL | Prepara tus samples en la SD rápido, 2:51).
- Cada guía: 400-600 palabras, título fiel al video / query, embed youtube-nocookie + fallback, HowTo 5 pasos + VideoObject, FAQ 3, CTA a `../../tools/trakkconverter/` (+ `../../tools/`), canonical + hreflang recíprocos, GTM + consent + footer.
- Índice `/tutoriales/` ES+EN: activar 4ª card (SP-404) como `Disponible`, enlazar ruta real. Las 3 anteriores quedan live (fl-studio-ia, partes, bass lines).
- Sitemap raíz: 2 loc nuevas (ES weekly 0.8, EN monthly 0.7) para la guía.

## Non-goals
- No guía de subir-beats / mezclas / lo-fi / efectos en este lote (quedan para lote 4 si se decide).
- No cambios a guías mergeadas (fl-studio-ia/partes/bass lines) salvo índice.
- No ajuste SEO extra de la página de TRAKKCONVERTER más allá del CTA de la guía (el retoque dedicado de 10 min queda como follow-up separado).

## Constraints (heredados)
- GTM `GTM-NMVJZ8VL` + consent `sb-consent` default denied, uno por página.
- Footer marca + CC BY-NC-SA 4.0; ES+EN; apps `GPL-3.0-only` (sin MIT); UTF-8 estricto verificado con python.
- Embed responsive (`landing/index.html` 241-243), thumbnail `https://i.ytimg.com/vi/UAMboy8mtro/hqdefault.jpg`, watch `https://www.youtube.com/watch?v=UAMboy8mtro`.

## Approaches
- Solo viable: mismo híbrido probado lotes 1-2 (mergeado y QA en verde). Sin alternativas.

## Queda al builder
- Título ES: `SP-404 MK2: prepara tus samples en la SD rápido | ShardBeats` (EN `SP-404 MK2: prepare your samples on the SD card fast | ShardBeats`). Ajuste menor permitido si mejora keyword `roland fl studio` / `sp 404 mk2 samples`, reportado.
- Pasos: insertar SD, estructura carpetas ROLAND/SP404, formato WAV TRAKKCONVERTER (16/24-bit), copiar + importar, pitfalls (nombres largos, carpeta equivocada).
