# Tutoriales — guías SEO con video base (short design)

Fecha: 2026-11-24
Estado: propuesta para aprobación

## Intent / por qué
Capturar queries donde ya rankeas sin contenido (`fl studio ia` 25 imp pos 6.9, `partes de un beat` pos 2, `como cuantizar en fl studio` pos 4, `roland fl studio` pos 3) con guías escritas que posicionen en Google y empujen tu canal de tutoriales + TRAKK SUITE.

## Goals
- Nueva sección `/tutoriales/` ES+EN con índice + 1 guía piloto `fl-studio-ia` ES+EN.
- Cada guía: texto paso-a-paso 400-600 palabras con título = query exacta, embed `youtube-nocookie` de tu video como base, links a herramienta relacionada.
- Mismo patrón del sitio: GTM-NMVJZ8VL + consent, footer `Shard Btmkr + canal y sitio ShardBeats + CC BY-NC-SA 4.0`, sitemap + hreflang, schema HowTo + VideoObject.

## Non-goals
- No páginas de kits/beats (fase 2), no ajuste SEO de TRAKKCONVERTER (10 min aparte), no reggaeton.
- No rediseño del hub, solo agregar link a Tutoriales.
- No EN perfecto: EN = traducción directa del ES en esta fase.

## Anti-goals
- No romper URLs existentes (`shardbeats.github.io/*` se queda).
- No publicar videos nuevos ni cambiar Gumroad (sigue en draft).

## Constraints
- Sitio estático, sin build. Copiar patrón `web-tools/` (nav, styles, consent).
- ES+EN siempre, canonical + alternate hreflang + x-default.
- Licencia sitio CC BY-NC-SA 4.0 en footer; apps siguen GPL-3.0-only.

## Approaches
- A. Solo texto SEO: mejor ranking, no mueve canal. Descartado porque desperdicia tus videos.
- B. Solo índice de videos embebidos: mejor para YT, flojo para SEO. Descartado porque no ataca la causa (0% CTR por falta de título exacto).
- C. Híbrido elegido por ti: guía escrita SEO con tu video como base. Mismo esfuerzo, ataca sitio + YT. Vamos con C.

## Decidido (tuyo)
- Formato = guías escritas SEO con tus videos como base.

## Propuesta técnica (mi criterio, corrígeme)
- Rutas: `/tutoriales/`, `/tutoriales/en/`, `/tutoriales/fl-studio-ia/`, `/tutoriales/en/fl-studio-ia/`.
- Índice reutiliza `web-tools` cards; guía reutiliza layout `landing` hero + `youtube-nocookie` embed responsive + pasos + FAQ + CTA a tool.
- Hub `index.html` + `en/index.html`: agregar botón "Tutoriales".
- Sitemaps: root `sitemap.xml` + nuevo `tutoriales/sitemap.xml` (mirar patrón `tools/sitemap.xml`), referenciado desde `robots.txt` si aplica.
- Siguientes guías (no en este lote): `partes-de-un-beat`, `cuantizar-en-fl-studio`.

## Queda al builder
- IDs exactos de tus videos YT por guía (me los pasas o los tomo del canal con browser).
- Longitud final del texto y si el embed va arriba o a mitad.
