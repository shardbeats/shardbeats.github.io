# Mini-guías pilares B (7 recetas en /tutoriales/ + filtro) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publicar 7 pilares receta ES+EN en `/tutoriales/` con filtro por etiquetas en el índice, para captar long-tail fácil y empujar packs BeatStars + TRAKK.

**Architecture:** HTML estático sin build, plantilla de `tutoriales/fl-studio-ia/index.html` sin VideoObject (HowTo 5 + FAQPage 3). Índice con filtro client-side (data-tags + JS mínimo). Sitemap raíz extendido.

**Tech Stack:** HTML/CSS estático, youtube-nocookie solo donde ya exista (estas páginas no llevan embed), JSON-LD, GTM-NMVJZ8VL.

**Spec:** `docs/superpowers/specs/2026-11-25-miniguias-pilares-design.md`

## Global Constraints

- Sitio estático, sin build; copiar estructura de `tutoriales/fl-studio-ia/index.html` ya en `main`.
- ES+EN siempre, canonical + alternate hreflang es/en/x-default recíprocos.
- GTM `GTM-NMVJZ8VL` + consent `sb-consent` default denied, uno por página.
- Footer ES: `Shard Btmkr (Darío García) · canal y sitio ShardBeats · La Piedad, Mich. · <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">Contenido del sitio: CC BY-NC-SA 4.0</a>`; EN: `Shard Btmkr (Dario Garcia) · ShardBeats channel & site · La Piedad, Mich. · <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">Site content: CC BY-NC-SA 4.0</a>`.
- Apps TRAKK SUITE `GPL-3.0-only` (0 MIT). UTF-8 estricto (`python -c "open(F,'rb').read().decode('utf-8')"`).
- Reescritura total: sin etiquetas de fuente, sin terceros como autoridad, sin datos dudosos. Solo valores de los briefs de receta (Task 0).
- Sin VideoObject (texto-only). HowTo 5 pasos + FAQ 3 por página.
- No romper URLs existentes.

## Review Focus

- Contenido delgado (<500 palabras de prosa) — se espera 550-700 por página ES; el QA cuenta palabras.
- Canibalización con las 8 guías con video (títulos/H1 casi idénticos) — se espera keyword y ángulo de receta distintos + etiqueta `Receta` vs `Video`; el QA lista H1s y falla si hay duplicado funcional.
- `href` relativo mal calculado por profundidad — se espera `../../` (ES, `tutoriales/X/`) y `../../../` (EN, `tutoriales/en/X/`) verificados por grep.
- Filtro del índice roto sin JS o sin teclado — se espera que sin JS se vean las 15 cards y que los filtros sean `<button>`s.
- hreflang/canonical cruzados — se espera recíprocos exactos por par ES/EN.

---

### Task 0: Extraer y validar 7 fichas de receta (puerta de entrada, la hace el lead)

**Files:**
- Create: `docs/superpowers/recipes/01-progresiones.md`, `02-drums-808.md`, `03-sampling.md`, `04-mezcla.md`, `05-workflow.md`, `06-export.md`, `07-efectos.md`
- Test: validación del dueño (humano) por escrito antes de Task 1.

**Interfaces:**
- Consumes: BIBLIOTECA privada (`D:\Proyectos beatmaking\BIBLIOTECA`, fichas 19/04/CHEATs/23/11B/12E/22/11A-11F/14/05/08/10/12/17/07/21/32/01/46/48 + verificación en 06/12/15).
- Produces: 7 fichas con valores exactos verificados (voicings, BPM, %, settings) que Tasks 1-3 consumen como única fuente. Los implementadores NUNCA leen la BIBLIOTECA.

- [ ] **Step 1: Extraer 7 fichas** (lead, no subagente: requiere juicio + acceso a BIBLIOTECA). Cada ficha: keyword ES/EN, 5 pasos de receta con valores exactos, 3 FAQs, CTA exacto según mapeo aprobado (TB2 `.../sound-kits/241121`, TB3 `.../262279`, Lo-Fi Kit `.../218962`, general `https://www.beatstars.com/shardbeats/sound-kits`, TRAKK según pilar, `/landing/` gratis).
- [ ] **Step 2: Pedir validación al dueño** de las 7 fichas. Sin su OK escrito no existe Task 1.
- [ ] **Step 3: Commit** `docs: 7 fichas de receta verificadas para miniguias B`.

### Task 1: Pilares 1-2 (progresiones + drums/808) ES+EN

**Files:**
- Create: `tutoriales/progresiones-boombap-faciles/index.html`, `tutoriales/en/progresiones-boombap-faciles/index.html`
- Create: `tutoriales/drums-808-que-pegan/index.html`, `tutoriales/en/drums-808-que-pegan/index.html`
- Test: `grep` + `python` UTF-8 + conteo de palabras.

**Interfaces:**
- Consumes: fichas `01-progresiones.md`, `02-drums-808.md` (Task 0); plantilla `tutoriales/fl-studio-ia/index.html`.
- Produces: 4 rutas `/tutoriales/<slug>/` ES+EN que Task 4 indexa.

- [ ] **Step 1: Write the failing check**

```bash
test -f tutoriales/progresiones-boombap-faciles/index.html -a -f tutoriales/en/progresiones-boombap-faciles/index.html -a -f tutoriales/drums-808-que-pegan/index.html -a -f tutoriales/en/drums-808-que-pegan/index.html
```

- [ ] **Step 2: Run check to verify it fails**

Run: `test -f ...; echo $?` Expected: `1`

- [ ] **Step 3: Implement progresiones ES+EN**

Keyword ES `progresiones boombap fáciles` / EN `easy boombap chord progressions`. Title patrón `<Keyword> | ShardBeats` (≤60 chars). 550-700 palabras ES (EN espejo): voicings 7+9, regla del 7, 3-4 progresiones transportables con ejemplo en Cm/C. HowTo 5 + FAQPage 3. CTA primario TB2 `https://www.beatstars.com/shardbeats/sound-kits/241121` + secundario `../../tools/trakkname/` (EN: `../../../tools/en/trakkname/`). Canonical `https://shardbeats.github.io/tutoriales/progresiones-boombap-faciles/`, hreflang recíproco, nav `← Tutoriales` a `../`.

- [ ] **Step 4: Implement drums/808 ES+EN**

Keyword ES `drums y 808 que pegan` / EN `punchy drums and 808`. 550-700 palabras: kick/snare/hats, 808 pegado al kick, slides, saturación leve, swing. CTA primario TB3 `https://www.beatstars.com/shardbeats/sound-kits/262279` + secundario Lo-Fi Kit `https://www.beatstars.com/shardbeats/sound-kits/218962`. Mismo esquema SEO/GTM/footer que Step 3.

- [ ] **Step 5: Run checks**

Run greps: `trakkname` + `241121` en progresiones (ES+EN), `262279` + `218962` en drums (ES+EN); HowTo 5 + FAQ 3 por página; `GTM-NMVJZ8VL` + `id="consent-banner"` + `creativecommons.org/licenses/by-nc-sa` en las 4; python UTF8_OK las 4; conteo prosa 550-700 (script `wc.py` como en lote 4).
Expected: todo GREEN.

- [ ] **Step 6: Commit**

```bash
git add tutoriales/progresiones-boombap-faciles tutoriales/en/progresiones-boombap-faciles tutoriales/drums-808-que-pegan tutoriales/en/drums-808-que-pegan
git commit -m "feat(tutoriales): pilares progresiones y drums-808 ES+EN"
```

### Task 2: Pilares 3-4 (sampling + mezcla) ES+EN

**Files:**
- Create: `tutoriales/sampling-chops-limpios/index.html`, `tutoriales/en/sampling-chops-limpios/index.html`
- Create: `tutoriales/mezcla-home-studio-por-familia/index.html`, `tutoriales/en/mezcla-home-studio-por-familia/index.html`
- Test: `grep` + `python` UTF-8 + conteo de palabras.

**Interfaces:**
- Consumes: fichas `03-sampling.md`, `04-mezcla.md` (Task 0); plantilla fl-studio-ia.
- Produces: 4 rutas que Task 4 indexa.

- [ ] **Step 1-2: Failing check → 1** (mismo patrón Task 1 con los 4 archivos).
- [ ] **Step 3: Implement sampling ES+EN**

Keyword ES `sampling y chops limpios` / EN `clean sampling and chops`. 550-700 palabras: elegir sample, chop por frase, time-stretch, dejar aire a la voz. CTA primario `../../tools/trakkconverter/` (EN `../../../tools/en/trakkconverter/`) + secundario `../../landing/` (EN `../../../landing/en/`).

- [ ] **Step 4: Implement mezcla ES+EN**

Keyword ES `mezcla por familia home studio` / EN `mix by instrument family home studio`. 550-700 palabras: keys/drums/guitar/strings/acentos + panning canon + tape. Slug OBLIGATORIO `mezcla-home-studio-por-familia` (distinto de la guía con video `mezclas-home-studio`). CTA primario `https://www.beatstars.com/shardbeats/sound-kits` + secundario `../../tools/`.

- [ ] **Step 5: Run checks** (mismo set que Task 1 Step 5 para estos 4 archivos).
- [ ] **Step 6: Commit** `feat(tutoriales): pilares sampling y mezcla-por-familia ES+EN`

### Task 3: Pilares 5-7 (workflow + export + efectos) ES+EN

**Files:**
- Create: `tutoriales/workflow-fl-studio-vintage-boombap/index.html` + EN, `tutoriales/exportar-vender-beats-packs/index.html` + EN, `tutoriales/efectos-clave-sin-comprar-nada/index.html` + EN (6 archivos).
- Test: `grep` + `python` UTF-8 + conteo de palabras.

**Interfaces:**
- Consumes: fichas `05-workflow.md`, `06-export.md`, `07-efectos.md` (Task 0).
- Produces: 6 rutas que Task 4 indexa.

- [ ] **Step 1-2: Failing check → 1** (los 6 inexistentes).
- [ ] **Step 3: Implement workflow ES+EN** — keyword ES `workflow fl studio boombap` / EN `boombap fl studio workflow`. CTA primario `../../tools/` (EN `../../../tools/en/`).
- [ ] **Step 4: Implement export + efectos ES+EN** — export keyword ES `exportar beats para vender` / EN `export beats to sell`, CTA `../../tools/trakkname/` + `../../tools/trakkconverter/`; efectos keyword ES `efectos fl studio stock` / EN `fl studio stock effects`, CTA `../../tools/`.
- [ ] **Step 5: Run checks** (set Task 1 para los 6 archivos).
- [ ] **Step 6: Commit** `feat(tutoriales): pilares workflow, export y efectos ES+EN`

### Task 4: Índice con filtro por etiquetas + sitemap

**Files:**
- Modify: `tutoriales/index.html`, `tutoriales/en/index.html`, `sitemap.xml`
- Test: `grep` checks + prueba de filtro.

**Interfaces:**
- Consumes: 7 cards nuevas (Tasks 1-3) + 8 cards con video existentes.
- Produces: índice 15 cards filtrables + 14 locs sitemap.

- [ ] **Step 1: Write the failing check**

```bash
grep -q "progresiones-boombap-faciles" tutoriales/index.html && grep -q "efectos-clave-sin-comprar-nada" sitemap.xml && echo WIRED || echo NOT_WIRED
```

- [ ] **Step 2: Run check → NOT_WIRED**
- [ ] **Step 3: Implement filtro + cards ES+EN**

Taxonomía: tipo `video`/`receta` + tema (`acordes`, `drums-808`, `sampling`, `mezcla`, `workflow`, `vender`, `efectos`). Cada card lleva `data-tags="receta acordes"` etc; las 8 con video reciben `data-tags="video <tema>"`. Selector a la derecha con `<button>`s por etiqueta + "Todo"; JS mínimo inline que filtra por `data-tags` (sin recarga); sin JS se ven las 15. 7 cards nuevas con teaser + etiqueta visible `Receta`.
- [ ] **Step 4: Implement sitemap.xml**

14 bloques: 7 ES weekly 0.8 + 7 EN monthly 0.7 (slugs de Tasks 1-3). Formato loc/changefreq/priority SIN hreflang.

- [ ] **Step 5: Run checks**

`grep -c 'data-tags="receta' tutoriales/index.html` → `7`; `grep -c 'data-tags="video' tutoriales/index.html` → `8`; igual EN; `grep -c "progresiones-boombap-faciles\|drums-808-que-pegan\|sampling-chops-limpios\|mezcla-home-studio-por-familia\|workflow-fl-studio-vintage-boombap\|exportar-vender-beats-packs\|efectos-clave-sin-comprar-nada" sitemap.xml` → `14`.

- [ ] **Step 6: Commit** `feat(tutoriales): filtro por etiquetas + 7 pilares en indice y sitemap`

### Task 5: QA final y push

**Files:** ninguno (solo verificación).
**Test:** `grep` + `python` + browse visual.

- [ ] **Step 1: Link integrity** `grep -rho 'href="[^"]*"' tutoriales/ | sort -u` → 0 rotos; 15 cards por índice.
- [ ] **Step 2: SEO/consent audit** 16 páginas (14 pilares + 2 índices): `GTM-NMVJZ8VL` + `id="consent-banner"` + `creativecommons.org/licenses/by-nc-sa` + UTF-8 → 16/16.
- [ ] **Step 3: Contenido** prosa 550-700 por página ES (EN espejo ±10%), H1s únicos (cruce contra las 8 guías con video → 0 duplicados funcionales), HowTo 5 + FAQ 3 por pilar, 0 `MIT`, 0 `VideoObject`, 0 `uploadDate` inventado.
- [ ] **Step 4: Visual Brave** 3 pilares (1 mobile 360 + desktop): filtro clicable por teclado, cards filtran sin recarga, sin H-scroll.
- [ ] **Step 5: Push rama feature** (`git push -u origin <rama>`, máx 2 intentos) — main intacto.
