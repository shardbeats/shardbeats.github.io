# Mini-guías pilares (cluster SEO para packs + TRAKK) — design

Fecha: 2026-11-25
Estado: propuesta para aprobación (nada se construye sin tu OK)

## Intent / por qué
Convertir la BIBLIOTECA privada en 7 páginas públicas que rankeen keywords fáciles (long-tail ES), traigan impresiones y empujen sample packs + herramientas TRAKK. Todo reescrito en tu voz: síntesis original, sin copiar fichas ni citar settings de terceros como propios.

## Goals
- 7 pilares ES+EN (14 páginas) de 550-700 palabras, texto-only sin depender de videos de YouTube.
- Cada pilar = 1 keyword principal + 2-3 secundarias, 1 receta accionable con tus settings verificados, CTA a pack y/o herramienta TRAKK.
- Las 7 páginas viven en `/tutoriales/` (igual que las guías con video): `/tutoriales/<slug>/` + `/tutoriales/en/<slug>/`. Sin sección nueva.
- Índice `/tutoriales/` + `/en/` con filtro por etiquetas: selector a la derecha (píldoras o dropdown) que filtra cards por tema sin recargar (JS mínimo, data-tags por card). Las 8 guías con video existentes reciben etiqueta `Video` + su tema; los pilares llevan `Receta` + su tema.
- Schema HowTo (5 pasos) + FAQ (3) por página, sin VideoObject (no hay video base; evita `uploadDate` inventados).
- Sitemap raíz: 7 ES (weekly 0.8) + 7 EN (monthly 0.7). Sin hubs nuevos (decisión tuya: todo en `/tutoriales/`).

## Non-goals
- No publicar fichas tal cual ni transcripciones (ni KXVI, ni Navie D, ni Illfinite, ni PDFs).
- No páginas de inventario (Kontakt instaladas/pendientes, listas de 296 efectos): no rankean ni venden.
- No negocio genérico ($10k/mes, email marketing): fuera de intención de búsqueda musical.
- No tocar las 8 guías `/tutoriales/` existentes salvo cross-link al hub.

## Anti-goals
- Contenido delgado o duplicado entre pilares (cada keyword 1 sola URL; canibalización = fracaso aunque indexe).
- Presentar settings de terceros como propios o inventar datos dudosos (`(?)` de la biblioteca se omite, no se publica).
- Progresiones/acordes imposibles de tocar o settings que no tienes verificado en tu stock.

## Constraints (heredados del sitio)
- Estático sin build; plantilla de `tutoriales/` adaptada (hero + receta + pasos + FAQ + CTA).
- ES+EN siempre, canonical + hreflang es/en/x-default recíprocos.
- GTM `GTM-NMVJZ8VL` + consent `sb-consent` default denied, uno por página.
- Footer marca + CC BY-NC-SA 4.0; apps `GPL-3.0-only` (0 MIT); UTF-8 estricto.
- SEO: title 50-60 chars con keyword, meta description con beneficio + CTA, 1 H1, H2 por sección, thumb OG genérica del sitio (no hay video-ID).

## Approaches
- **A. Recetas cortas en volumen** (30-40 × 250-350 palabras): máximo alcance, pero alto riesgo de thin content y de publicar datos sin verificar por ir rápido. Descartada por tu elección.
- **B. Pilares por cluster (ELEGIDA)**: 7 páginas medias que sintetizan varias fichas en 1 método propio. Menos URLs pero cada una con peso real, receta verificable y CTA claro a pack/tool. Es la que mejor equilibra rankeo fácil + promoción.
- **C. Cheatsheets descargables**: conversión directa pero casi duplicadas entre sí y exigen producir el MIDI/WAV antes. Descartada; los descargables quedan como CTA futuro, no como página.

## Los 7 pilares (qué cubre cada uno y a qué empuja)
Fuente = solo insumo privado de síntesis; en público NO se cita ni se nombra al autor tercero.

1. `progresiones-boombap-faciles` — I-vi-IV-V, ii-V-I soul, gospel lift, dorian funk; voicings 7+9 y regla del 7. Fuentes: 19 + 04 + CHEATs. CTA: pack MIDI/samples + TRAKKNAME.
2. `drums-808-que-pegan` — kick/snare/hats, 808 pegado al kick, slides, saturación leve, swing. Fuentes: 23 + 11B + 12E. CTA: drumkit pack + TRAKKCONVERTER (wavs listos).
3. `sampling-chops-limpios` — elegir sample, chop por frase (no por transient), tiempo/stretch, dejar aire a la voz. Fuentes: 22 + 41 (solo método propio). CTA: TRAKKCONVERTER + sample pack.
4. `mezcla-home-studio-por-familia` — keys/drums/guitar/strings/acentos + panning canon + tape. Fuentes: 11A-11F + 14 + 12. CTA: TRAKK SUITE + pack stems.
5. `workflow-fl-studio-vintage-boombap` — orden de sesión, combos goto, FX equivalentes con stock, bounce DRY/WET. Fuentes: 05 + 08 + 10 + 12 + 17. CTA: TRAKK SUITE.
6. `exportar-vender-beats-packs` — WAV 44.1/24, naming BPM_Key, stems, type beats con tags. Fuentes: 07 + 21 + 32. CTA: TRAKKNAME + TRAKKCONVERTER + packs.
7. `efectos-clave-sin-comprar-nada` — reverb/delay, distorsión, EQ correctivo, automatización con stock FL. Fuentes: 01 + 46 + 48 + 10. CTA: TRAKK SUITE (gratis, sin comprar).

Keywords ejemplo (ES principal / EN espejo): "progresiones boombap fáciles / easy boombap chord progressions", "808 que pega / punchy 808", "chops limpios sampling / clean sample chops", "mezcla por familia home studio / mix by instrument family", "workflow fl studio boombap / fl studio boombap workflow", "exportar beats para vender / export beats to sell", "efectos fl studio stock / fl studio stock effects".

## Decidido (tuyo + mío)
- Enfoque B, 7 pilares, texto-only, ES+EN, todo dentro de `/tutoriales/` (tu decisión: sin sección `/guias/`; filtro por etiquetas en el índice en su lugar).
- Reescritura total: sin etiquetas de fuente ([KXVI], [ND]…), sin nombres de terceros como autoridad, sin datos `(?)`.
- Sin VideoObject; HowTo + FAQ sí. CTA siempre a pack y/o TRAKK, nunca a comprar plugins.
- Recetas verificadas: yo extraigo 7 fichas de receta de la BIBLIOTECA (solo valores verificados de tu stock: 06, 12, 15) y tú las validas antes de construir; los implementadores trabajan solo desde esos briefs, nunca leen la BIBLIOTECA.
- URLs TRAKK exactas (verificadas en repo): ES `../../tools/trakkconverter/`, `../../tools/trakkname/`, `../../tools/trakkout/`, `../../tools/` (hub); EN `../../../tools/en/trakkconverter/` etc. Mapeo: pilar 3→trakkconverter, pilar 6→trakkname+trakkconverter, pilares 4/5/7→hub TRAKK, pilar 1→trakkname.
- Mapeo packs aprobado por ti: progresiones→Timeless Boombap 2 (MIDI), drums/808→Timeless Boombap 3 o Lo-Fi Drum Kit, sampling→pack gratis `/landing/`, mezcla→stems/packs BeatStars, workflow→solo TRAKK, export→TRAKKNAME (+packs), efectos→solo TRAKK.
- `/tutoriales/` nuevas páginas se registran en el `sitemap.xml` raíz (igual que las guías existentes).
- EN: mismo patrón que lotes 1-4 — traducción directa del implementador, mismos slugs bajo `/tutoriales/en/`, hreflang recíproco.
- Frontera anti-canibalización (tu decisión): sin separar secciones; las cards se distinguen por etiqueta (`Video` vs `Receta`) + tema, y cada pilar apunta a keyword/ángulo de receta distintos de la guía con video correspondiente, con cross-link mutuo.

## Queda al builder
- Titles exactos ≤60 chars, meta descriptions, H2s y FAQs finales.
- Orden de las 15 cards y copy de teasers del índice.
- Taxonomía final de etiquetas (propuesta: Acordes, Drums/808, Sampling, Mezcla, Workflow, Vender, Efectos + tipo Video/Receta) y JS mínimo del filtro (data-tags, sin recarga, accesible por teclado).
- `changefreq/priority` exactos de las 14 URLs nuevas.
- Og-image por pilar (genérica del sitio o una por cluster).
