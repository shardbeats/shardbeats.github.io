# Tutoriales lote 4 (cierre - 4 guías) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Cerrar tutoriales sumando 4 guías restantes ES+EN (subir-beats, mezclas, lo-fi, efectos) y activarlas en índice + sitemap.

**Architecture:** HTML estático con patrón lote 1-3 ya en `main` (8 tutoriales totales al terminar): guía = hero + embed youtube-nocookie responsive + pasos + FAQ + CTA, JSON-LD HowTo + VideoObject. Índice y sitemap se extienden.

**Tech Stack:** HTML/CSS estático, youtube-nocookie embed, JSON-LD, GTM-NMVJZ8VL.

**Spec:** `docs/superpowers/specs/2026-11-24-tutoriales-lote4-design.md` (extiende specs lotes 1-3)

## Global Constraints

- Sitio estático, sin build; copiar estructura de `tutoriales/fl-studio-ia/index.html` ya en `main`.
- ES+EN siempre, canonical + alternate hreflang es/en/x-default recíprocos.
- GTM `GTM-NMVJZ8VL` + consent `sb-consent` default denied, uno por página.
- Footer ES: `Shard Btmkr (Darío García) · canal y sitio ShardBeats · La Piedad, Mich. · <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">Contenido del sitio: CC BY-NC-SA 4.0</a>`; EN: `Shard Btmkr (Dario Garcia) · ShardBeats channel & site · La Piedad, Mich. · <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">Site content: CC BY-NC-SA 4.0</a>`.
- Apps TRAKK SUITE `GPL-3.0-only` (0 MIT).
- No romper URLs existentes. UTF-8 estricto (`python -c "open(F,'rb').read().decode('utf-8')"`).
- Videos: subir `_n3HSiSYixs`, mezclas `b3hl_8Zv78Y`, lo-fi `UeLS1aLIkzM`, efectos `iOLKQU_2_k0`; embeds `https://www.youtube-nocookie.com/embed/<ID>`, thumbs `https://i.ytimg.com/vi/<ID>/hqdefault.jpg`, watch `https://www.youtube.com/watch?v=<ID>`.
- `uploadDate` VideoObject fallback `2026-11-24` reportado.

## Review Focus

- Embed bloqueado deja página sin video — se espera fallback "Ver en YouTube" / "Watch on YouTube" siempre visible.
- hreflang/canonical cruzados mal puestos causa duplicado ES/EN — se espera alternates recíprocos exactos.
- GTM o consent duplicado/ausente — se espera uno solo por página.
- Embed 16:9 se desborda a 360px — se espera responsive sin scroll-H.
- Ruta relativa mal calculada — se espera verificar cada `href` por profundidad (`tutoriales/X/` → `../../`, `tutoriales/en/X/` → `../../../` para raíz).

---

### Task 1: Guía subir-beats-a-youtube ES+EN

**Files:**
- Create: `tutoriales/subir-beats-a-youtube/index.html`
- Create: `tutoriales/en/subir-beats-a-youtube/index.html`
- Test: `grep` + `python` UTF-8

**Interfaces:**
- Consumes: patrón fl-studio-ia, video `_n3HSiSYixs`.
- Produces: `/tutoriales/subir-beats-a-youtube/` ES+EN.

- [ ] **Step 1: Write the failing check**

```bash
test -f tutoriales/subir-beats-a-youtube/index.html -a -f tutoriales/en/subir-beats-a-youtube/index.html
```

- [ ] **Step 2: Run check to verify it fails**

Run: `test -f ...; echo $?` Expected: `1`

- [ ] **Step 3: Implement ES**

Título `Cómo subir beats a YouTube rápido | ShardBeats`. 400-600 palabras: exportar WAV/stems, hacer video con TRAKKOUT (audio+artwork→MP4 1080p), subir a YT, mejorar metadata. Embed `_n3HSiSYixs` + fallback watch. FAQ 3. CTA `../../tools/trakkout/` + `../../tools/`. HowTo 5 + VideoObject. Canonical, hreflang, GTM, consent, footer ES.

- [ ] **Step 4: Implement EN**

Título `How to upload beats to YouTube fast | ShardBeats`. Traducción directa, `../../../` a raíz. Footer EN.

- [ ] **Step 5: Run checks**

Run: `youtube-nocookie.com/embed/_n3HSiSYixs` EMBED_OK, `watch?v=_n3HSiSYixs` FALLBACK_OK, HowTo+VideoObject SCHEMA_OK, python UTF8_OK ambas.
Expected: 4/4 OK.

- [ ] **Step 6: Commit**

```bash
git add tutoriales/subir-beats-a-youtube/index.html tutoriales/en/subir-beats-a-youtube/index.html
git commit -m "feat(tutoriales): guia subir-beats-a-youtube ES+EN con video _n3HSiSYixs"
```

### Task 2: Guía mezclas-home-studio ES+EN

**Files:**
- Create: `tutoriales/mezclas-home-studio/index.html`
- Create: `tutoriales/en/mezclas-home-studio/index.html`
- Test: `grep` + `python` UTF-8

**Interfaces:**
- Consumes: patrón, video `b3hl_8Zv78Y`. Produces: `/tutoriales/mezclas-home-studio/` ES+EN.

- [ ] **Step 1-2: Failing check → 1**

- [ ] **Step 3: Implement ES**

Título `Cómo mejorar tus mezclas en Home Studio | ShardBeats`. 400-600 palabras: ganancia, EQ correctivo, compresión vocal, panoramización, referencia. Embed `b3hl_8Zv78Y` + fallback. FAQ 3. CTA `../../tools/` + serie. HowTo 5 + VideoObject.

- [ ] **Step 4: Implement EN**

Título `How to improve your Home Studio mixes | ShardBeats`.

- [ ] **Step 5: Run checks**

Same 4 checks con ID `b3hl_8Zv78Y`.

- [ ] **Step 6: Commit**

`feat(tutoriales): guia mezclas-home-studio ES+EN con video b3hl_8Zv78Y`

### Task 3: Guías lo-fi + efectos FL Studio (2× guías en un commit)

**Files:**
- Create: `tutoriales/beats-lofi-drumkit/index.html`, `tutoriales/en/beats-lofi-drumkit/index.html`
- Create: `tutoriales/efectos-fl-studio/index.html`, `tutoriales/en/efectos-fl-studio/index.html`
- Test: `grep` + `python` UTF-8 para las 4

**Interfaces:**
- Consumes: patrón, videos `UeLS1aLIkzM` (lo-fi) y `iOLKQU_2_k0` (efectos). Produces: 4 rutas.

- [ ] **Step 1-2: Failing check → 1 (las 4 inexistentes)**

- [ ] **Step 3: Implement lo-fi ES+EN**

ES título `Cómo hacer beats lo-fi con drumkit gratis | ShardBeats`, EN `How to make lo-fi beats with free drumkit | ShardBeats`. Embed `UeLS1aLIkzM`. Queries `beats lo-fi`, `drumkit free`.

- [ ] **Step 4: Implement efectos ES+EN**

ES título `Efectos en FL Studio: la forma sencilla | ShardBeats`, EN `FL Studio effects the easy way | ShardBeats`. Embed `iOLKQU_2_k0`. Serie FL Studio.

- [ ] **Step 5: Run checks**

Run greps para `UeLS1aLIkzM` y `iOLKQU_2_k0` ambos ES+EN (4× EMBED/FALLBACK/SCHEMA), python UTF8_OK las 4.

- [ ] **Step 6: Commit**

```bash
git add tutoriales/beats-lofi-drumkit/index.html tutoriales/en/beats-lofi-drumkit/index.html tutoriales/efectos-fl-studio/index.html tutoriales/en/efectos-fl-studio/index.html
git commit -m "feat(tutoriales): guias lo-fi y efectos ES+EN con videos UeLS1aLIkzM+iOLKQU_2_k0"
```

### Task 4: Índice + sitemap del cierre

**Files:**
- Modify: `tutoriales/index.html`, `tutoriales/en/index.html`, `sitemap.xml`
- Test: `grep` checks

**Interfaces:**
- Consumes: 4 cards lote 3 (fl-studio-ia, partes, bass, sp-404) + 4 guías nuevas Task 1-3.
- Produces: índice 8 cards + 8 loc sitemap.

- [ ] **Step 1: Write the failing check**

```bash
grep -q "subir-beats-a-youtube" tutoriales/index.html && grep -q "efectos-fl-studio" sitemap.xml && echo WIRED || echo NOT_WIRED
```

- [ ] **Step 2: Run check → NOT_WIRED**

- [ ] **Step 3: Implement índice ES+EN**

Agregar 4 cards: subir-beats, mezclas, beats-lofi, efectos (tags `Disponible`/`Available`, hrefs relativos, teasers con keywords). Mantener 4 previas. Confirmar 8/8 con `grep -c 'href=".*/"' | wc -l`.

- [ ] **Step 4: Implement sitemap.xml**

8 bloques: 4 ES weekly 0.8 (`subir-beats-a-youtube/`, `mezclas-home-studio/`, `beats-lofi-drumkit/`, `efectos-fl-studio/`) + 4 EN monthly 0.7. Sin hreflang.

- [ ] **Step 5: Run checks**

Run: `grep -q subir-beats-a-youtube tutoriales/index.html && grep -q mezclas-home-studio tutoriales/index.html && grep -q beats-lofi-drumkit tutoriales/index.html && grep -q efectos-fl-studio tutoriales/index.html && echo IDX_ES_OK`; igual EN; `grep -c "subir-beats-a-youtube\|mezclas-home-studio\|beats-lofi-drumkit\|efectos-fl-studio" sitemap.xml` → `8`.

- [ ] **Step 6: Commit**

`feat(tutoriales): activa 4 guias restantes en indice y sitemap (cierre)`

### Task 5: QA final y push

**Files:**
- Modify: ninguno (solo verificación)
- Test: `grep` + `python` + browse visual

- [ ] **Step 1: Link integrity** `grep -rho 'href="[^"]*"' tutoriales/ index.html | sort -u` → 0 rotos.

- [ ] **Step 2: SEO/consent audit** 12 archivos (8 guías nuevas ES+EN + 4 previas re-verificadas + 2 índices): `GTM-NMVJZ8VL` + `id="consent-banner"` + `creativecommons.org/licenses/by-nc-sa` → 12/12 OK.

- [ ] **Step 3: Visual Brave** 4 guías nuevas a 360px + desktop: nav, embed 16:9 sin H-scroll, fallback+CTA.

- [ ] **Step 4: Push rama feature** (`git push -u origin <rama>`) → OK; main intacto.
