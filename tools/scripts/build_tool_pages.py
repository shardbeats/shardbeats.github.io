#!/usr/bin/env python3
"""Generate the per-tool pages for the TRAKK SUITE site.

Run from the repository root:

    python scripts/build_tool_pages.py

It writes:
    <slug>/index.html      (Spanish)
    en/<slug>/index.html   (English)

Edit the TOOLS data below, then re-run. Generated files should not be
edited by hand unless you also update this script.
"""

import json
import os
import re
from string import Template

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://shardbeats.github.io/tools/"
SITE = "ShardBeats TRAKK SUITE"
VERSIONS_FILE = os.path.join(ROOT, "versions.json")


def load_versions():
    """Versions written by scripts/sync_versions.py, when present."""
    try:
        with open(VERSIONS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}

TOOLS = [
    {
        "slug": "trakkconverter",
        "name": "TRAKKCONVERTER",
        "version": "1.3.0",
        "repo": "https://github.com/shardbeats/TRAKKCONVERTER",
        "category": "MultimediaApplication",
        "video": {
            "id": "UAMboy8mtro",
            "title": "SP-404 MK2 TUTORIAL | Prepara tus samples en la SD rápido",
            "upload": "2026-08-16T11:20:29-07:00",
            "duration": "PT2M50S",
            "desc": "Cómo preparar tus samples en la tarjeta SD del SP-404MK2 para importarlos rápido.",
        },
        "es": {
            "title": "Convertir samples a WAV para SP-404MK2 | TRAKKCONVERTER",
            "desc": "Convierte librerías completas de samples al WAV que acepta el Roland SP-404MK2: 48 kHz, 16 bits, estéreo. Batch, drag and drop y .exe portable.",
            "tagline": "Samples al WAV del SP-404MK2",
            "lead": "Arrastra tu carpeta de drum kits y sample packs. TRAKKCONVERTER convierte en lote al formato que el SP-404MK2 acepta de verdad, conservando la estructura de carpetas.",
            "bullets": [
                ("48 kHz / 16 bits / estéreo", "Es el formato interno del SP-404MK2. Si entregas otra frecuencia, el sampler remuestrea al importar o rechaza el archivo."),
                ("No reconvierte lo ya convertido", "Los archivos con sufijo _sp.wav se saltan solos, así que una carpeta espejo nunca se procesa dos veces."),
                ("Copiar o convertir", "Si un archivo ya está en el destino se copia sin recodificar. Si está en otra frecuencia, se remuestrea."),
                ("Cualquier formato que decodifique FFmpeg", "MP3, AAC, FLAC, AIFF, OGG, M4A y WAV de entrada."),
            ],
            "steps": [
                ("Añade tu carpeta", "Arrastra los archivos o la carpeta completa a la ventana, o pulsa Add folder."),
                ("Elige la salida", "Misma carpeta que el origen, o una carpeta nueva conservando la estructura."),
                ("Revisa la vista previa", "Te dice qué se copia, qué se convierte y qué se salta antes de tocar nada."),
                ("Pulsa START", "Procesa en lote y muestra el resumen al terminar."),
            ],
            "specs": [
                ("Salida", "WAV PCM, 48 kHz, 16 bits, estéreo"),
                ("Entrada", "MP3, AAC, FLAC, AIFF, OGG, M4A, WAV"),
                ("Sistema", "Windows 10 / 11 (64 bits)"),
                ("Distribución", ".exe portable, sin instalación"),
                ("Licencia", "MIT"),
            ],
            "faq": [
                ("¿Necesito instalar FFmpeg?", "No. El .exe portable lo incluye. Solo lo necesitas si ejecutas desde el código fuente."),
                ("¿Pierdo calidad al pasar de MP3 a WAV?", "El MP3 ya perdió información y no se recupera. Lo que evitas es una segunda recodificación y consigues un archivo que el sampler acepta sin tocar."),
                ("¿Es gratis?", "Sí. Licencia MIT, sin cuenta y sin límite de uso."),
                ("¿Funciona sin internet?", "Sí. Todo el proceso ocurre en tu equipo."),
            ],
        },
        "en": {
            "title": "Convert Samples to SP-404MK2 WAV (Free) | TRAKKCONVERTER",
            "desc": "Batch-convert whole sample libraries to the WAV the Roland SP-404MK2 accepts: 48 kHz, 16-bit, stereo. Drag and drop, portable exe, offline. No account.",
            "tagline": "Samples to SP-404MK2 WAV",
            "lead": "Drop your drum kits and sample packs in. TRAKKCONVERTER batch-converts them to the format the SP-404MK2 actually accepts, keeping your folder structure.",
            "bullets": [
                ("48 kHz / 16-bit / stereo", "That is the SP-404MK2 internal format. Deliver anything else and the sampler resamples on import or rejects the file."),
                ("No re-converting", "Files with the _sp.wav suffix are skipped automatically, so a mirror folder is never processed twice."),
                ("Copy or convert", "Files already at the target are copied without re-encoding; files at another rate are resampled."),
                ("Anything FFmpeg decodes", "MP3, AAC, FLAC, AIFF, OGG, M4A and WAV on input."),
            ],
            "steps": [
                ("Add your folder", "Drag files or the whole folder into the window, or press Add folder."),
                ("Pick the output", "Same folder as the source, or a new one keeping the structure."),
                ("Check the preview", "It shows what will be copied, converted or skipped before touching anything."),
                ("Press START", "Runs the batch and shows a summary when it finishes."),
            ],
            "specs": [
                ("Output", "WAV PCM, 48 kHz, 16-bit, stereo"),
                ("Input", "MP3, AAC, FLAC, AIFF, OGG, M4A, WAV"),
                ("System", "Windows 10 / 11 (64-bit)"),
                ("Distribution", "Portable .exe, no install"),
                ("License", "MIT"),
            ],
            "faq": [
                ("Do I need FFmpeg installed?", "No. The portable .exe bundles it. You only need it if you run from source."),
                ("Do I lose quality going from MP3 to WAV?", "The MP3 already lost information and it does not come back. What you avoid is a second encode, and you get a file the sampler accepts as-is."),
                ("Is it free?", "Yes. MIT licensed, no account, no usage limit."),
                ("Does it work offline?", "Yes. Everything runs on your machine."),
            ],
        },
    },
    {
        "slug": "trakkstudio",
        "name": "TRAKKSTUDIO",
        "version": "1.0",
        "repo": "https://github.com/shardbeats/TRAKKSTUDIO",
        "category": "MultimediaApplication",
        "es": {
            "title": "Organizar, convertir y normalizar samples | TRAKKSTUDIO",
            "desc": "Tres herramientas en una ventana: organiza y renombra, convierte al WAV del SP-404MK2 y normaliza por pico. Sin pipeline forzado. Gratis y offline.",
            "tagline": "Tres herramientas en una ventana",
            "lead": "Organizar, convertir y normalizar son tres tareas distintas. TRAKKSTUDIO las pone en tres pestañas independientes, cada una con su propio START, para que uses solo la que necesitas.",
            "bullets": [
                ("Renombrado masivo con vista previa", "Prefijo, sufijo, reemplazo o nombre completo, más numeración anti-colisión. Ves el antes y el después antes de aplicar."),
                ("Conversión al SP-404MK2", "Las mismas reglas del conversor: 48 kHz, 16 bits, estéreo, y salta lo que ya está convertido."),
                ("Normalización por pico", "Cada clip a su propio nivel con ganancia lineal, sin comprimir ni limitar."),
                ("Carpetas limpias", "Sin CSV ni archivos sueltos junto a tus samples. El inventario vive en una base SQLite local."),
            ],
            "steps": [
                ("Arrastra tu drum kit", "A la columna de archivos de la izquierda."),
                ("Elige la pestaña", "Organizar para renombrar, Convertir para el SP-404MK2, Normalizar para los niveles."),
                ("Previsualiza", "Cada pestaña muestra qué va a pasar antes de escribir nada."),
                ("Pulsa START", "Solo en la pestaña que estés usando. Las demás no se ejecutan."),
            ],
            "specs": [
                ("Incluye", "Organizador + conversor SP-404 + normalizador"),
                ("Salida", "WAV PCM, 48 kHz, 16 bits, estéreo"),
                ("Sistema", "Windows 10 / 11 (64 bits)"),
                ("Distribución", "Instalador por usuario o .exe portable"),
                ("Licencia", "MIT"),
            ],
            "faq": [
                ("¿Es obligatorio usar las tres herramientas?", "No. Cada pestaña es independiente y tiene su propio botón de inicio. Puedes usar solo el renombrador, por ejemplo."),
                ("¿Dónde guarda la base de datos?", "En tu carpeta de usuario, y se regenera en cada escaneo. No contiene audio."),
                ("¿Cuánto espacio necesita?", "El instalador ronda los 210 MB porque lleva Qt y FFmpeg completos, además del espacio de las copias que generes."),
                ("¿Es gratis?", "Sí. Licencia MIT, sin cuenta y sin límite de uso."),
            ],
        },
        "en": {
            "title": "Organize, convert and normalize samples | TRAKKSTUDIO",
            "desc": "Three tools in one window: organize and bulk-rename, convert to SP-404MK2 WAV and peak-normalize. No forced pipeline. Free, portable and offline.",
            "tagline": "Three tools in one window",
            "lead": "Organizing, converting and normalizing are three different jobs. TRAKKSTUDIO puts them in three independent tabs, each with its own START, so you only run what you need.",
            "bullets": [
                ("Bulk rename with preview", "Prefix, suffix, replace or full name, plus anti-collision numbering. You see before and after before applying."),
                ("SP-404MK2 conversion", "Same rules as the converter: 48 kHz, 16-bit, stereo, skipping what is already converted."),
                ("Peak normalization", "Every clip to its own level with linear gain, no compression and no limiting."),
                ("Clean folders", "No CSVs or sidecar files next to your samples. The inventory lives in a local SQLite database."),
            ],
            "steps": [
                ("Drop your drum kit", "Into the file column on the left."),
                ("Pick a tab", "Organize to rename, Convert for the SP-404MK2, Normalize for levels."),
                ("Preview", "Each tab shows what will happen before anything is written."),
                ("Press START", "Only the tab you are on runs. The others stay idle."),
            ],
            "specs": [
                ("Includes", "Organizer + SP-404 converter + normalizer"),
                ("Output", "WAV PCM, 48 kHz, 16-bit, stereo"),
                ("System", "Windows 10 / 11 (64-bit)"),
                ("Distribution", "Per-user installer or portable .exe"),
                ("License", "MIT"),
            ],
            "faq": [
                ("Do I have to use all three tools?", "No. Each tab is independent and has its own start button, so you can use just the renamer for instance."),
                ("Where is the database stored?", "In your user folder, and it is rebuilt on every scan. It contains no audio."),
                ("How much disk space does it need?", "The installer is around 210 MB because it bundles Qt and FFmpeg, plus whatever room the copies you generate need."),
                ("Is it free?", "Yes. MIT licensed, no account, no usage limit."),
            ],
        },
    },
    {
        "slug": "trakknormalizer",
        "name": "TRAKKNORMALIZER",
        "version": "1.1.0",
        "repo": "https://github.com/shardbeats/TRAKKNORMALIZER",
        "category": "MultimediaApplication",
        "es": {
            "title": "Normalizar beats y samples por pico | TRAKKNORMALIZER",
            "desc": "Normaliza cada clip a su propio pico con ganancia lineal, sin comprimir. Batch para toda la librería, conservando frecuencia y profundidad. Gratis.",
            "tagline": "Normalización por pico, clip por clip",
            "lead": "Un kick a -18 dB junto a otro a -3 dB rompen el balance de tu beat. TRAKKNORMALIZER mide cada archivo y le aplica solo la ganancia que necesita, en lugar de subirlo todo lo mismo.",
            "bullets": [
                ("Por clip, no por lote", "Un normalizador convencional sube todo por igual y hace recortar lo que ya estaba alto."),
                ("Solo ganancia lineal", "Sin compresión ni limitador: los transitorios de tus samples no cambian."),
                ("Conserva el original", "Frecuencia y profundidad intactas. Los procesados llevan sufijo _N y no se reprocesan."),
                ("Recrea la estructura", "Reproduce las carpetas de origen en la salida, para no perder el orden de la librería."),
            ],
            "steps": [
                ("Arrastra archivos o carpetas", "O usa Add folder para añadir una librería completa."),
                ("Elige el objetivo", "Por defecto -1.0 dB, con 0.5 dB de tolerancia para saltar lo que ya está en rango."),
                ("Decide la salida", "Misma carpeta que el origen o una carpeta de salida, con la estructura recreada."),
                ("Pulsa START", "Procesa en paralelo y muestra el progreso por archivo."),
            ],
            "specs": [
                ("Objetivo por defecto", "-1.0 dB (tolerancia 0.5 dB)"),
                ("Formatos", "WAV, MP3, FLAC, AIFF, OGG, M4A"),
                ("Procesado", "Ganancia lineal, sin compresión"),
                ("Sistema", "Windows"),
                ("Licencia", "MIT"),
            ],
            "faq": [
                ("¿En qué se diferencia de un normalizador normal?", "Un normalizador convencional aplica la misma ganancia a todo. Este mide cada archivo y le aplica la suya, así el resultado queda parejo."),
                ("¿Cambia el sonido de mis samples?", "No hay compresión ni limitación, solo ganancia. La forma de onda se conserva, escalada."),
                ("¿Va a reprocesar archivos ya normalizados?", "No. Los archivos con sufijo _N se saltan en las siguientes pasadas."),
                ("¿Es gratis?", "Sí. Licencia MIT, sin cuenta y sin límite de uso."),
            ],
        },
        "en": {
            "title": "Peak-normalize Beats and Samples | TRAKKNORMALIZER",
            "desc": "Normalize every clip to its own peak with linear gain, no compression. Batch the whole library keeping sample rate and bit depth. Fully offline.",
            "tagline": "Per-clip peak normalization",
            "lead": "A kick at -18 dB next to one at -3 dB wrecks the balance of a beat. TRAKKNORMALIZER measures each file and applies only the gain it needs, instead of pushing everything up by the same amount.",
            "bullets": [
                ("Per clip, not per batch", "A conventional normalizer raises everything equally and makes the already-loud clips clip."),
                ("Linear gain only", "No compression, no limiting: your samples' transients stay intact."),
                ("Keeps the original", "Sample rate and bit depth untouched. Processed files get an _N suffix and are never reprocessed."),
                ("Recreates the structure", "Mirrors the source folders in the output so your library order survives."),
            ],
            "steps": [
                ("Drag files or folders", "Or use Add folder to pull in a whole library."),
                ("Set the target", "-1.0 dB by default, with 0.5 dB tolerance to skip clips already in range."),
                ("Choose the output", "Same folder as the source, or an output folder with the structure recreated."),
                ("Press START", "Runs in parallel and shows per-file progress."),
            ],
            "specs": [
                ("Default target", "-1.0 dB (0.5 dB tolerance)"),
                ("Formats", "WAV, MP3, FLAC, AIFF, OGG, M4A"),
                ("Processing", "Linear gain, no compression"),
                ("System", "Windows"),
                ("License", "MIT"),
            ],
            "faq": [
                ("How is this different from a normal normalizer?", "A conventional normalizer applies the same gain to everything. This one measures each file and applies its own, so the result comes out even."),
                ("Does it change the sound of my samples?", "There is no compression or limiting, only gain. The waveform is preserved, scaled."),
                ("Will it reprocess files I already normalized?", "No. Files with the _N suffix are skipped on later runs."),
                ("Is it free?", "Yes. MIT licensed, no account, no usage limit."),
            ],
        },
    },
    {
        "slug": "trakkname",
        "name": "TRAKKNAME",
        "version": "1.3.0",
        "repo": "https://github.com/shardbeats/TRAKKNAME",
        "android": "https://github.com/shardbeats/TRAKKNAME-IONIC",
        "category": "MultimediaApplication",
        "es": {
            "title": "Generador de títulos de beats EN/ES gratis | TRAKKNAME",
            "desc": "Genera títulos de beats por género, artista y mood, en inglés y español. Banco de palabras bilingüe, 20 moods y base de datos editable. Offline.",
            "tagline": "Generador de títulos de beats",
            "lead": "Poner nombre a un beat no debería costarte veinte minutos. TRAKKNAME combina artistas ponderados por género, vocabulario bilingüe y un eje de moods para darte un título usable al instante.",
            "bullets": [
                ("Ocho patrones de generación", "Cuatro en inglés y cuatro en español, con concordancia de adjetivos en español."),
                ("Eje de moods", "Los 20 moods habituales del type beat, con dos seleccionables a la vez y búsqueda."),
                ("Sin repeticiones", "Los artistas no se repiten dentro de una generación y hay ventana anti-duplicados en los títulos."),
                ("Base de datos editable", "Artistas, palabras, patrones e historial, con importación y exportación JSON."),
            ],
            "steps": [
                ("Elige género e idioma", "El pool de artistas y el banco de palabras cambian con cada uno."),
                ("Marca uno o dos moods", "Opcional. Vacío significa cualquiera."),
                ("Pulsa Space", "Genera al instante. Ctrl+C copia el título."),
                ("Guarda el historial", "Cada título queda con su género, idioma, mood y artistas."),
            ],
            "specs": [
                ("Idiomas", "Inglés y español"),
                ("Patrones", "8 (4 EN + 4 ES)"),
                ("Moods", "20, hasta 2 a la vez"),
                ("Sistema", "Windows y Android"),
                ("Licencia", "MIT"),
            ],
            "faq": [
                ("¿Puedo usar los títulos comercialmente?", "Sí. Son texto generado, no material con derechos, y no requieren atribución."),
                ("¿Se repiten los títulos?", "Hay una ventana anti-duplicados y los artistas no se repiten dentro de una misma generación."),
                ("¿Puedo editar las palabras y los artistas?", "Sí. La base de datos tiene CRUD completo, importación y exportación JSON, y un reinicio a los datos de fábrica."),
                ("¿Hay versión para Android?", "Sí, con el mismo motor."),
            ],
        },
        "en": {
            "title": "Beat Title Generator (EN/ES, 20 Moods) | TRAKKNAME",
            "desc": "Generate beat titles by genre, artist and mood, in English and Spanish. Bilingual word banks, 20 moods and an editable database. Fully offline.",
            "tagline": "Beat title generator",
            "lead": "Naming a beat should not cost you twenty minutes. TRAKKNAME combines genre-weighted artists, bilingual vocabulary and a mood axis to hand you a usable title instantly.",
            "bullets": [
                ("Eight generation patterns", "Four in English and four in Spanish, with Spanish adjective agreement handled."),
                ("Mood axis", "The 20 usual type-beat moods, two selectable at once, searchable."),
                ("No repeats", "Artists never repeat within one generation, and titles have a duplicate-avoidance window."),
                ("Editable database", "Artists, words, patterns and history, with JSON import and export."),
            ],
            "steps": [
                ("Pick genre and language", "The artist pool and word bank follow each one."),
                ("Tick one or two moods", "Optional. Empty means any."),
                ("Press Space", "Generates instantly. Ctrl+C copies the title."),
                ("Keep the history", "Every title is stored with its genre, language, mood and artists."),
            ],
            "specs": [
                ("Languages", "English and Spanish"),
                ("Patterns", "8 (4 EN + 4 ES)"),
                ("Moods", "20, up to 2 at a time"),
                ("System", "Windows and Android"),
                ("License", "MIT"),
            ],
            "faq": [
                ("Can I use the titles commercially?", "Yes. They are generated text, not copyrighted material, and need no attribution."),
                ("Do titles repeat?", "There is a duplicate-avoidance window, and artists do not repeat within one generation."),
                ("Can I edit the words and artists?", "Yes. The database has full CRUD, JSON import and export, and a reset to factory seed data."),
                ("Is there an Android version?", "Yes, running the same engine."),
            ],
        },
    },
    {
        "slug": "trakkout",
        "name": "TRAKKOUT",
        "version": "1.0.3",
        "repo": "https://github.com/shardbeats/TRAKKOUT",
        "category": "MultimediaApplication",
        "video": {
            "id": "_n3HSiSYixs",
            "title": "La forma más fácil de subir beats a YouTube",
            "upload": "2026-09-27T10:30:21-07:00",
            "duration": "PT5M57S",
            "desc": "Cómo subir beats a YouTube de la forma más fácil, con TRAKKOUT.",
        },
        "es": {
            "title": "Convertir un beat en video 1080p para YouTube | TRAKKOUT",
            "desc": "Convierte un beat y su artwork en un MP4 1080p listo para YouTube, con plantillas de título, descripción y tags. Súbelo a tu canal o prográmalo.",
            "tagline": "Beat + artwork a video 1080p",
            "lead": "Tu beat en audio no se ve en YouTube. TRAKKOUT arma el video con FFmpeg a partir del audio y la portada, y opcionalmente lo sube a tu canal con los metadatos ya rellenados.",
            "bullets": [
                ("1920x1080 desde tu portada", "Ajuste automático con recorte o bandas, más fondo desenfocado opcional."),
                ("Plantillas de metadatos", "Variables como título, BPM, tonalidad o enlace de compra se rellenan solas en título, descripción y tags."),
                ("Publicación programada", "Envía la fecha a YouTube y el video queda privado hasta el día elegido."),
                ("Historial local", "Cada subida queda registrada en una base SQLite con su ID de video."),
            ],
            "steps": [
                ("Elige audio y portada", "Arrastra el beat y la imagen, o usa Browse."),
                ("Rellena los metadatos", "Beat, artista, BPM, tonalidad y enlace de compra."),
                ("Genera el video", "FFmpeg arma el MP4 y lo puedes previsualizar antes de subir."),
                ("Sube o programa", "Con tu propia cuenta de Google, al canal que elijas."),
            ],
            "specs": [
                ("Salida", "MP4 1920x1080, 30 fps"),
                ("Audio", "MP3, WAV, Opus, AAC (192 kbps / 48 kHz)"),
                ("Subida", "YouTube Data API v3 con tu propio OAuth"),
                ("Sistema", "Windows 10 / 11 (64 bits)"),
                ("Licencia", "MIT"),
            ],
            "faq": [
                ("¿Necesito una cuenta en algún servicio tuyo?", "No. La subida usa tu propio proyecto de Google Cloud y tu cuenta, y el video va a tu canal."),
                ("¿Puedo usarlo solo para generar el MP4?", "Sí. Puedes generar el video y no subirlo; la parte de Google es opcional."),
                ("¿Se puede programar la publicación?", "Sí. YouTube exige que esos videos empiecen como privados, y la app lo hace sola."),
                ("¿Hay límite de subidas?", "La cuota diaria de la API de YouTube, que es de tu propio proyecto."),
            ],
        },
        "en": {
            "title": "Convert a Beat into a 1080p YouTube Video | TRAKKOUT",
            "desc": "Turn a beat and its artwork into a 1080p MP4 ready for YouTube, with title, description and tag templates. Upload to your channel or schedule it.",
            "tagline": "Beat + artwork to 1080p video",
            "lead": "Your beat as audio only does not get watched on YouTube. TRAKKOUT builds the video with FFmpeg from your audio and cover, and optionally uploads it to your channel with the metadata already filled in.",
            "bullets": [
                ("1920x1080 from your cover", "Auto-fit with crop or letterbox, plus an optional blurred background."),
                ("Metadata templates", "Variables like title, BPM, key or purchase link fill title, description and tags by themselves."),
                ("Scheduled publishing", "Sends the date to YouTube, and the video stays private until the chosen day."),
                ("Local history", "Every upload is logged in a SQLite database with its video ID."),
            ],
            "steps": [
                ("Pick audio and artwork", "Drag the beat and the image in, or use Browse."),
                ("Fill the metadata", "Beat, artist, BPM, key and purchase link."),
                ("Generate the video", "FFmpeg builds the MP4 and you can preview it before uploading."),
                ("Upload or schedule", "With your own Google account, to the channel you choose."),
            ],
            "specs": [
                ("Output", "MP4 1920x1080, 30 fps"),
                ("Audio", "MP3, WAV, Opus, AAC (192 kbps / 48 kHz)"),
                ("Upload", "YouTube Data API v3 with your own OAuth"),
                ("System", "Windows 10 / 11 (64-bit)"),
                ("License", "MIT"),
            ],
            "faq": [
                ("Do I need an account on some service of yours?", "No. Uploads use your own Google Cloud project and your account, and the video goes to your channel."),
                ("Can I use it just to generate the MP4?", "Yes. You can build the video and never upload it; the Google part is optional."),
                ("Can publishing be scheduled?", "Yes. YouTube requires those videos to start as private, and the app does that automatically."),
                ("Is there an upload limit?", "Your own project's daily YouTube API quota."),
            ],
        },
    },
    {
        "slug": "trakklicense",
        "name": "TRAKKLICENSE",
        "version": "1.0.0",
        "repo": "https://github.com/shardbeats/TRAKKLICENSE",
        "category": "BusinessApplication",
        "es": {
            "title": "Contratos de licencia de beats en PDF | TRAKKLICENSE",
            "desc": "Genera contratos de licencia de beats en PDF, en español e inglés: lease y exclusiva, con folio consecutivo y evidencia SHA256. Todo offline.",
            "tagline": "Contratos de licencia en PDF",
            "lead": "Cuando vendes un beat necesitas un contrato, no un párrafo copiado. TRAKKLICENSE rellena plantillas completas en español e inglés y las exporta a PDF con folio y evidencia.",
            "bullets": [
                ("Cuatro tiers listos", "MP3, WAV, Trackout y Unlimited como leases no exclusivos, más la exclusiva, cada uno con su plantilla."),
                ("Plantillas completas", "25 secciones: titularidad, cesión, regalías, Content ID, sincronización, plazo y terminación."),
                ("Folio y evidencia", "Cada exportación recibe un folio consecutivo que nunca se reutiliza, más SHA256 del texto y versión de plantilla."),
                ("Editable sin romper el original", "Los cambios se hacen sobre copias; el texto de fábrica se restaura cuando quieras."),
            ],
            "steps": [
                ("Elige el tier", "Lease no exclusivo o exclusiva."),
                ("Rellena la venta", "Comprador, precio, plazo, país y, si los tienes, los IPI."),
                ("Revisa la vista previa", "El contrato se actualiza mientras escribes."),
                ("Exporta a PDF", "Se guarda con folio, hash y registro en el historial."),
            ],
            "specs": [
                ("Tiers", "MP3, WAV, Trackout, Unlimited y Exclusiva"),
                ("Idiomas", "Español e inglés"),
                ("Salida", "PDF y Markdown"),
                ("Datos", "SQLite local, sin nube"),
                ("Licencia", "MIT"),
            ],
            "faq": [
                ("¿Esto es asesoría legal?", "No. Es una herramienta de autoayuda que rellena plantillas con los datos que escribes. Para una operación importante, revisa el contrato con un abogado de tu jurisdicción."),
                ("¿Puedo editar el texto del contrato?", "Sí. Los cambios se guardan sobre una copia, así el texto de fábrica sigue disponible."),
                ("¿Cómo pruebo que hubo una venta?", "Cada exportación lleva folio consecutivo y un SHA256 del texto renderizado, guardado en el historial local."),
                ("¿Se sube algo a internet?", "No. La app funciona sin conexión y no tiene binarios de terceros."),
            ],
        },
        "en": {
            "title": "Beat License Contracts as PDF (EN/ES) | TRAKKLICENSE",
            "desc": "Generate beat license contracts as PDF, in English and Spanish: lease and exclusive tiers, with sequential folios and SHA256 evidence. Fully offline.",
            "tagline": "Beat license contracts as PDF",
            "lead": "When you sell a beat you need a contract, not a paragraph you copied somewhere. TRAKKLICENSE fills full templates in English and Spanish and exports them to PDF with a folio and evidence.",
            "bullets": [
                ("Four ready tiers", "MP3, WAV, Trackout and Unlimited non-exclusive leases, plus the exclusive, each with its own template."),
                ("Complete templates", "25 sections: ownership, grant, royalties, Content ID, sync, term and termination."),
                ("Folio and evidence", "Every export gets a sequential folio that is never reused, plus a SHA256 of the text and the template version."),
                ("Editable without breaking the original", "Edits go to copies; factory text can be restored whenever you want."),
            ],
            "steps": [
                ("Pick the tier", "Non-exclusive lease or exclusive."),
                ("Fill the sale", "Buyer, price, term, country and, if you have them, the IPIs."),
                ("Check the preview", "The contract updates as you type."),
                ("Export to PDF", "Saved with folio, hash and a history record."),
            ],
            "specs": [
                ("Tiers", "MP3, WAV, Trackout, Unlimited and Exclusive"),
                ("Languages", "English and Spanish"),
                ("Output", "PDF and Markdown"),
                ("Data", "Local SQLite, no cloud"),
                ("License", "MIT"),
            ],
            "faq": [
                ("Is this legal advice?", "No. It is a self-help tool that fills templates with the values you type. For a significant deal, have a lawyer in your jurisdiction review the contract."),
                ("Can I edit the contract text?", "Yes. Edits are stored on a copy, so the factory text stays available."),
                ("How do I prove a sale happened?", "Every export carries a sequential folio and a SHA256 of the rendered text, stored in the local history."),
                ("Does anything go to the internet?", "No. The app runs offline and ships no third-party binaries."),
            ],
        },
    },
    {
        "slug": "trakkart",
        "name": "TRAKKART",
        "version": "1.4.0",
        "repo": "https://github.com/shardbeats/TRAKKART",
        "category": "MultimediaApplication",
        "es": {
            "title": "Portadas con dithering y animación, offline | TRAKKART",
            "desc": "Estudio offline de portadas: convierte cualquier imagen en artwork con dithering para singles, pósters, merch y redes. 36 motores, canvas libre, exporta el paquete. Sin internet, sin cuentas.",
            "tagline": "Portadas con dithering + animación",
            "lead": "La portada de tu beat sin salir de tu máquina: convierte cualquier imagen en artwork con dithering, anímala y exporta el paquete listo para publicar.",
            "bullets": [
                ("36 motores de dithering", "Ordenados (Bayer, blue-noise, halftone), difusión de error, Hilbert, CMYK, ASCII, bordes y constructor de motivos."),
                ("Canvas primero", "Presets de proporción o tamaño libre con encuadre cover, contain, stretch y blur."),
                ("Color a tu manera", "Paletas TRAKK (BW, SLIME, VAPOR, EMBER), biblioteca de paletas, extracción automática desde la imagen, duotono, posterize y split-tone."),
                ("FX, datamosh y partículas", "Pila de efectos reordenable, 7 sabores de mosh y cadena de partículas en loop perfecto."),
                ("Exporta el paquete", "Imagen a tamaño de lienzo + miniatura 1080p, SVG vectorial, GIF/WebP animado, MP4, metadata.json, separaciones de tinta y BMP para la pantalla del SP-404MK2."),
            ],
            "steps": [
                ("Abre tu imagen", "Archivo → Abrir, arrástrala a la ventana o pégala con Ctrl+V."),
                ("Elige el motor", "Los botones ◀ ▶ recorren los 36 motores; ajusta color, profundidad y tintas."),
                ("Anímala (opcional)", "Previsualiza en el panel VIDEO: GIF al tamaño del documento, MP4 a 1080p."),
                ("Exporta", "Exportar (Ctrl+Mayús+S) o exportación rápida (Ctrl+S). Instalador o portable, sin internet."),
            ],
            "specs": [
                ("Salida", "Imagen + thumb 1080p, SVG, GIF/WebP, MP4, metadata.json, BMP para SP-404MK2"),
                ("Sistema", "Windows 10 / 11 (64 bits)"),
                ("Distribución", "Instalador .exe y .zip portable"),
                ("Licencia", "MIT (código); FFmpeg incluido bajo GPLv3"),
            ],
            "faq": [
                ("¿Necesito internet para usarlo?", "No. Cero red, cero telemetría, cero cuentas. Todo vive en la carpeta de datos de la app."),
                ("¿Es gratis?", "Sí. El código es MIT, sin cuenta y sin límite de uso."),
                ("¿Puedo usarlo desde la terminal?", "Sí. El modo CLI procesa presets y paletas sin abrir la interfaz."),
                ("¿Qué hago si SmartScreen avisa?", "Es un aviso normal en builds sin firmar: Más información → Ejecutar de todos modos. Hay instalador y portable con SHA-256 publicados."),
            ],
        },
        "en": {
            "title": "Dithered cover art and animation, offline | TRAKKART",
            "desc": "Offline cover-art studio: turn any image into dithered artwork for singles, posters, merch and socials. 36 engines, free canvas, export the bundle. No internet, no accounts.",
            "tagline": "Dithered covers + animation",
            "lead": "Your beat artwork without leaving your machine: turn any image into dithered artwork, animate it and export a publish-ready bundle.",
            "bullets": [
                ("36 dither engines", "Ordered (Bayer, blue-noise, halftone), error diffusion, Hilbert, CMYK, ASCII, edges and motif builder."),
                ("Canvas first", "Ratio presets or free custom size with cover, contain, stretch and blur framing."),
                ("Your color", "TRAKK palettes (BW, SLIME, VAPOR, EMBER), palette library, auto-extract from source, duotone, posterize and split-tone."),
                ("FX, datamosh and particles", "Reorderable effect stack, 7 mosh flavors and a seamlessly looping particle chain."),
                ("Export the bundle", "Canvas-size image + 1080p thumb, vector SVG, animated GIF/WebP, MP4, metadata.json, ink separations and SP-404MK2 screen BMP."),
            ],
            "steps": [
                ("Open your image", "File → Open, drag it onto the window or paste with Ctrl+V."),
                ("Pick the engine", "The ◀ ▶ buttons cycle the 36 engines; tune color, depth and inks."),
                ("Animate it (optional)", "Preview in the VIDEO panel: GIF at document size, MP4 at 1080p."),
                ("Export", "Export (Ctrl+Shift+S) or quick export (Ctrl+S). Installer or portable, no internet."),
            ],
            "specs": [
                ("Output", "Image + 1080p thumb, SVG, GIF/WebP, MP4, metadata.json, SP-404MK2 BMP"),
                ("System", "Windows 10 / 11 (64-bit)"),
                ("Distribution", "Installer .exe and portable .zip"),
                ("License", "MIT (code); bundled FFmpeg under GPLv3"),
            ],
            "faq": [
                ("Do I need internet to use it?", "No. Zero network, zero telemetry, zero accounts. Everything lives in the app data folder."),
                ("Is it free?", "Yes. MIT-licensed code, no account, no usage limit."),
                ("Can I run it from the terminal?", "Yes. CLI mode processes presets and palettes without opening the UI."),
                ("What if SmartScreen warns me?", "That is normal for unsigned builds: More info → Run anyway. Installer and portable ship with published SHA-256 checksums."),
            ],
        },
    },
]

UI = {
    "es": {
        "nav_tools": "Herramientas",
        "nav_guide": "Guía",
        "nav_kits": "Sound Kits",
        "nav_faq": "FAQ",
        "nav_github": "GitHub",
        "lang_switch": "EN",
        "crumb_home": "Inicio",
        "crumb_tools": "Herramientas",
        "download": "Descargar para Windows",
        "repo": "Ver el código",
        "android": "Versión Android",
        "screenshot_alt": "Captura de {name} funcionando",
        "what": "Qué hace",
        "how": "Cómo se usa",
        "specs": "Ficha técnica",
        "spec_version": "Versión",
        "faq_title": "Preguntas frecuentes",
        "others": "Otras herramientas de la suite",
        "others_lead": "Siete herramientas independientes. Usa solo la que necesites.",
        "all_tools": "Ver todas las herramientas",
        "free": "Gratis y open source (MIT)",
        "footer_legal": "Privacidad",
        "footer_cookies": "Cookies",
        "footer_pack": "Pack de beats gratis",
        "consent_text": "<strong>Cookies y analítica.</strong> Usamos Google Analytics para contar visitas y clics en descargas. Puedes aceptar o rechazar; con \"Rechazar\" no se guarda ninguna cookie de medición.",
        "consent_more": "Política de privacidad",
        "consent_yes": "Aceptar",
        "consent_no": "Rechazar",
        "consent_label": "Consentimiento de cookies",
        "faq_page": "Página de",
        "video_heading": "Míralo funcionando",
        "video_play": "Reproducir vídeo:",
        "video_watch": "Verlo en YouTube",
    },
    "en": {
        "nav_tools": "Tools",
        "nav_guide": "Guide",
        "nav_kits": "Sound Kits",
        "nav_faq": "FAQ",
        "nav_github": "GitHub",
        "lang_switch": "ES",
        "crumb_home": "Home",
        "crumb_tools": "Tools",
        "download": "Download for Windows",
        "repo": "View the source",
        "android": "Android version",
        "screenshot_alt": "{name} screenshot",
        "what": "What it does",
        "how": "How to use it",
        "specs": "Specifications",
        "spec_version": "Version",
        "faq_title": "Frequently asked questions",
        "others": "Other tools in the suite",
        "others_lead": "Seven independent tools. Use only the ones you need.",
        "all_tools": "See all tools",
        "free": "Free and open source (MIT)",
        "footer_legal": "Privacy",
        "footer_cookies": "Cookies",
        "footer_pack": "Free beat pack",
        "consent_text": "<strong>Cookies and analytics.</strong> We use Google Analytics to count visits and download clicks. You can accept or decline; choosing \"Decline\" stores no measurement cookie.",
        "consent_more": "Privacy policy",
        "consent_yes": "Accept",
        "consent_no": "Decline",
        "consent_label": "Cookie consent",
        "faq_page": "Page of",
        "video_heading": "See it working",
        "video_play": "Play video:",
        "video_watch": "Watch on YouTube",
    },
}

PAGE = Template("""<!doctype html>
<html lang="$lang">
<head>
<meta name="p:domain_verify" content="b057c8e43a06a802d24c1c27cfb07d3d"/>
<meta name="google-site-verification" content="VdLDbokxShSCLe5d8as7TuPpIL4R1LN5wWVfc7z7G2c"/>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({"gtm.start":new Date().getTime(),event:"gtm.js"});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!="dataLayer"?'&l='+l:'';j.async=true;j.src="https://www.googletagmanager.com/gtm.js?id="+i+dl;f.parentNode.insertBefore(j,f);})(window,document,"script","dataLayer","GTM-NMVJZ8VL");</script>
<!-- End Google Tag Manager -->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>$title</title>
  <meta name="description" content="$desc" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
  <meta name="theme-color" content="#151617" />
  <link rel="canonical" href="$canonical" />
  <link rel="alternate" hreflang="es" href="$alt_es" />
  <link rel="alternate" hreflang="en" href="$alt_en" />
  <link rel="alternate" hreflang="x-default" href="$alt_es" />

  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="$site" />
  <meta property="og:locale" content="$oglocale" />
  <meta property="og:url" content="$canonical" />
  <meta property="og:title" content="$title" />
  <meta property="og:description" content="$desc" />
  <meta property="og:image" content="$og_image" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="$name — $tagline" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="$title" />
  <meta name="twitter:description" content="$desc" />
  <meta name="twitter:image" content="$og_image" />

  <link rel="icon" type="image/png" sizes="64x64" href="${root_rel}favicon-64.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="${root_rel}apple-touch-icon.png" />
  <link rel="preconnect" href="https://www.googletagmanager.com" />

  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('consent', 'default', {
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied',
      analytics_storage: 'denied',
      wait_for_update: 500
    });
    gtag('set', 'url_passthrough', true);
    gtag('set', 'ads_data_redaction', true);
    try {
      if (localStorage.getItem('sb-consent') === 'granted') {
        gtag('consent', 'update', {
          ad_storage: 'granted',
          ad_user_data: 'granted',
          ad_personalization: 'granted',
          analytics_storage: 'granted'
        });
      }
    } catch (e) {}
  </script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JRJH6GRXTB"></script>
  <script>
    gtag('js', new Date());
    gtag('config', 'G-JRJH6GRXTB', { anonymize_ip: true });
  </script>

  <script type="application/ld+json">
  $schema
  </script>

  <link rel="stylesheet" href="${root_rel}styles.css" />
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NMVJZ8VL" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
  <div id="bg3d" aria-hidden="true"></div>
  <header>
  <nav aria-label="$navlabel">
    <div class="container">
      <div class="logo"><a href="$home_es" class="logo-link"><img src="${root_rel}logo-120.png" width="40" height="40" alt="Shard Beats logo" />Shard <span>Beats</span></a></div>
      <div class="nav-links">
        <a href="$home_es#tools">$nav_tools</a>
        <a href="$home_es#guia">$nav_guide</a>
        <a href="$home_es#soundkits">$nav_kits</a>
        <a href="$home_es#faq">$nav_faq</a>
        <a href="$alt_other" hreflang="$otherlang" lang="$otherlang2">$lang_switch</a>
        <a href="https://github.com/shardbeats" target="_blank" rel="noopener">$nav_github</a>
      </div>
    </div>
  </nav>
  </header>

  <main>
  <section class="section tool-hero">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="$home_es">$crumb_home</a> <span aria-hidden="true">/</span>
        <a href="$home_es#tools">$crumb_tools</a> <span aria-hidden="true">/</span>
        <span>$name</span>
      </nav>
      <div class="eyebrow">$site</div>
      <h1>$name</h1>
      <p class="tool-tagline">$tagline</p>
      <p class="lead">$lead</p>
      <div class="cta-row">
        <a class="dl-btn big" href="$download" target="_blank" rel="noopener">$download_label</a>
        <a class="repo-link" href="$repo" target="_blank" rel="noopener">$repo_label</a>
$android_link
      </div>
      <figure class="shot">
        <img src="$shot" alt="$shot_alt" width="$shot_w" height="$shot_h" loading="lazy" />
        <figcaption>$name v$version</figcaption>
      </figure>
    </div>
  </section>

  <section class="section alt">
    <div class="container prose">
      <h2>$what</h2>
      <ul class="feature-list">
$bullets
      </ul>
    </div>
  </section>

  <section class="section">
    <div class="container prose">
      <h2>$how</h2>
      <ol class="step-list">
$steps
      </ol>
    </div>
  </section>

$video_section

  <section class="section alt">
    <div class="container prose">
      <h2>$specs</h2>
      <table class="spec-table">
        <tbody>
$specs_rows
        </tbody>
      </table>
    </div>
  </section>

  <section class="section" id="faq">
    <div class="container prose">
      <h2>$faq_title</h2>
      <div class="faq">
$faq_html
      </div>
    </div>
  </section>

  <section class="section alt">
    <div class="container">
      <h2>$others</h2>
      <p class="lead">$others_lead</p>
      <div class="grid">
$others_cards
      </div>
      <p style="margin-top:24px;"><a class="dl-btn" href="$home_es#tools">$all_tools</a></p>
    </div>
  </section>
  </main>

  <footer>
    <p>Shard Btmkr - Dario Garcia - La Piedad, Mich. - <a href="https://github.com/shardbeats">github.com/shardbeats</a></p>
    <p><a href="${root_rel}privacy.html">$footer_legal</a> · <a href="#consent-banner" data-consent-reset>$footer_cookies</a> · <a href="$home_pack">$footer_pack</a> · <a href="$alt_other" hreflang="$otherlang" lang="$otherlang2">$lang_switch_full</a></p>
  </footer>

  <div id="consent-banner" class="consent" role="dialog" aria-live="polite" aria-label="$consent_label" hidden>
    <p>$consent_text <a href="${root_rel}privacy.html">$consent_more</a>.</p>
    <div class="consent-actions">
      <button class="consent-btn ghost" type="button" data-consent="denied">$consent_no</button>
      <button class="consent-btn" type="button" data-consent="granted">$consent_yes</button>
    </div>
  </div>

  <script>
    (function(){
      var banner = document.getElementById('consent-banner');
      if (banner) {
        var stored = null;
        try { stored = localStorage.getItem('sb-consent'); } catch (e) {}
        if (!stored) banner.hidden = false;

        banner.addEventListener('click', function(e){
          var btn = e.target.closest('[data-consent]');
          if (!btn) return;
          var state = btn.getAttribute('data-consent');
          try { localStorage.setItem('sb-consent', state); } catch (err) {}
          gtag('consent', 'update', {
            ad_storage: state,
            ad_user_data: state,
            ad_personalization: state,
            analytics_storage: state
          });
          banner.hidden = true;
        });

        document.querySelectorAll('[data-consent-reset]').forEach(function(el){
          el.addEventListener('click', function(e){
            e.preventDefault();
            banner.hidden = false;
          });
        });
      }
      document.querySelectorAll('.dl-btn').forEach(function(a){
        a.addEventListener('click', function(){
          gtag('event', 'download_click', { tool: '$name', link_url: a.href, language: '$lang' });
        });
      });
    })();
  </script>
$video_script
$bg_script
</body>
</html>
""")

BG_SCRIPT = """  <script>
    (function(){
      var el = document.getElementById('bg3d');
      if (!el) return;
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      var conn = navigator.connection;
      if (conn && conn.saveData) return;

      var COLORS = ['#6ab7ff', '#2f6bff'];
      var GLYPHS = ['\\u266A', '\\u266B'];
      var canvas = document.createElement('canvas');
      var ctx = canvas.getContext('2d');
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var W = 0, H = 0, notes = [], frame = 0;

      function makeSprite(glyph, color) {
        var s = document.createElement('canvas');
        s.width = s.height = 64;
        var g = s.getContext('2d');
        g.font = 'bold 46px "Segoe UI Symbol","Apple Symbols",serif';
        g.textAlign = 'center';
        g.textBaseline = 'middle';
        g.shadowColor = color;
        g.shadowBlur = 12;
        g.fillStyle = color;
        g.fillText(glyph, 32, 34);
        return s;
      }

      var sprites = [makeSprite(GLYPHS[0], COLORS[0]), makeSprite(GLYPHS[1], COLORS[1])];

      function build() {
        var count = W < 700 ? 70 : 150;
        notes = [];
        for (var i = 0; i < count; i++) {
          notes.push({
            s: i % 2,
            x: Math.random() * W,
            y: Math.random() * H,
            size: 14 + Math.random() * 26,
            sway: 0.4 + Math.random() * 1.2,
            phase: Math.random() * Math.PI * 2,
            speed: 0.08 + Math.random() * 0.22,
            alpha: 0.14 + Math.random() * 0.45
          });
        }
      }

      function resize() {
        W = window.innerWidth; H = window.innerHeight;
        canvas.width = Math.floor(W * dpr);
        canvas.height = Math.floor(H * dpr);
        canvas.style.width = W + 'px';
        canvas.style.height = H + 'px';
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        build();
      }

      function draw() {
        ctx.clearRect(0, 0, W, H);
        for (var i = 0; i < notes.length; i++) {
          var n = notes[i];
          n.y -= n.speed;
          if (n.y < -40) { n.y = H + 40; n.x = Math.random() * W; }
          var x = n.x + Math.sin(n.y * 0.01 + n.phase) * 14 * n.sway;
          ctx.globalAlpha = n.alpha;
          ctx.drawImage(sprites[n.s], x - n.size / 2, n.y - n.size / 2, n.size, n.size);
        }
        ctx.globalAlpha = 1;
        frame = requestAnimationFrame(draw);
      }
      function start() { if (!frame) frame = requestAnimationFrame(draw); }
      function stop() { if (frame) { cancelAnimationFrame(frame); frame = 0; } }

      el.appendChild(canvas);
      resize();
      window.addEventListener('resize', function(){ clearTimeout(resize._t); resize._t = setTimeout(resize, 150); });
      document.addEventListener('visibilitychange', function(){ document.hidden ? stop() : start(); });
      start();
    })();
  </script>"""


VIDEO_SCRIPT = """  <script>
    (function(){
      document.querySelectorAll('.video-facade').forEach(function(btn){
        btn.addEventListener('click', function(){
          var wrap = btn.closest('.video-embed');
          var id = wrap && wrap.getAttribute('data-video-id');
          if (!id) return;
          var frame = document.createElement('iframe');
          frame.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
          frame.title = btn.getAttribute('aria-label') || 'YouTube';
          frame.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
          frame.allowFullscreen = true;
          wrap.innerHTML = '';
          wrap.appendChild(frame);
        });
      });
    })();
  </script>"""


def img_size(path):
    try:
        with open(path, 'rb') as f:
            head = f.read(32)
        if head[:8] != b'\x89PNG\r\n\x1a\n':
            return (1200, 630)
        w = int.from_bytes(head[16:20], 'big')
        h = int.from_bytes(head[20:24], 'big')
        return (w, h)
    except OSError:
        return (1200, 630)


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;'))


def build(tool, lang):
    other = 'en' if lang == 'es' else 'es'
    ui = UI[lang]
    t = tool[lang]

    if lang == 'es':
        root_rel = '../'
        home_es = '../'
        alt_other = '../en/' + tool['slug'] + '/'
    else:
        root_rel = '../../'
        home_es = '../../'
        alt_other = '../../' + tool['slug'] + '/'

    home_pack = 'https://shardbeats.github.io/landing/' + ('' if lang == 'es' else 'en/')
    canonical = BASE_URL + ('' if lang == 'es' else 'en/') + tool['slug'] + '/'
    alt_es = BASE_URL + tool['slug'] + '/'
    alt_en = BASE_URL + 'en/' + tool['slug'] + '/'
    og_image = BASE_URL + 'assets/og-' + tool['slug'] + '.png'
    shot_rel = root_rel + 'assets/shot-' + tool['slug'] + '.png'
    shot_w, shot_h = img_size(os.path.join(ROOT, 'assets', 'shot-' + tool['slug'] + '.png'))
    if os.path.exists(os.path.join(ROOT, 'assets', 'shot-' + tool['slug'] + '.jpg')):
        shot_rel = root_rel + 'assets/shot-' + tool['slug'] + '.jpg'

    bullets = '\n'.join(
        '        <li><strong>%s</strong>%s</li>' % (esc(h), ' ' + esc(p))
        for h, p in t['bullets']
    )

    steps = '\n'.join(
        '        <li><strong>%s</strong> %s</li>' % (esc(h), esc(p))
        for h, p in t['steps']
    )

    specs_rows = '\n'.join(
        '          <tr><th scope="row">%s</th><td>%s</td></tr>' % (esc(k), esc(v))
        for k, v in [('Version', tool['version'])] + t['specs']
    )

    faq_html = '\n'.join(
        '        <details><summary>%s</summary><p>%s</p></details>' % (esc(q), esc(a))
        for q, a in t['faq']
    )

    others = [o for o in TOOLS if o['slug'] != tool['slug']]
    cards = []
    for o in others:
        href = '../' + o['slug'] + '/'
        cards.append(
            '        <div class="card">\n'
            '          <h3><a href="%s">%s</a></h3>\n'
            '          <p>%s</p>\n'
            '        </div>' % (href, esc(o['name']), esc(o[lang]['tagline']))
        )

    android_link = ''
    if tool.get('android'):
        android_link = ('        <a class="repo-link" href="%s" target="_blank" rel="noopener">%s</a>'
                        % (tool['android'], ui['android']))

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareApplication",
                "name": tool['name'],
                "description": t['desc'],
                "applicationCategory": tool['category'],
                "operatingSystem": "Windows 10, Windows 11" + (", Android" if tool.get('android') else ""),
                "softwareVersion": tool['version'],
                "downloadUrl": tool['repo'] + '/releases/latest',
                "installUrl": tool['repo'] + '/releases/latest',
                "softwareHelp": canonical,
                "license": "https://opensource.org/licenses/MIT",
                "isAccessibleForFree": True,
                "image": BASE_URL + 'assets/shot-' + tool['slug'] + '.png',
                "screenshot": BASE_URL + 'assets/shot-' + tool['slug'] + '.png',
                "inLanguage": lang,
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                "author": {"@type": "Organization", "name": "ShardBeats",
                           "url": BASE_URL},
                "isPartOf": {"@type": "WebSite", "name": SITE, "url": BASE_URL},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": ui["crumb_home"],
                     "item": BASE_URL + ('' if lang == 'es' else 'en/')},
                    {"@type": "ListItem", "position": 2, "name": ui["crumb_tools"],
                     "item": BASE_URL + ('' if lang == 'es' else 'en/') + '#tools'},
                    {"@type": "ListItem", "position": 3, "name": tool["name"],
                     "item": canonical},
                ],
            },
        ],
    }

    if tool.get('video'):
        vid = tool['video']
        schema["@graph"].append({
            "@type": "VideoObject",
            "name": vid['title'],
            "description": vid['desc'],
            "thumbnailUrl": BASE_URL + 'assets/video-' + tool['slug'] + '.jpg',
            "uploadDate": vid['upload'],
            "duration": vid['duration'],
            "embedUrl": 'https://www.youtube-nocookie.com/embed/' + vid['id'],
            "contentUrl": 'https://www.youtube.com/watch?v=' + vid['id'],
            "inLanguage": "es",
            "publisher": {
                "@type": "Organization",
                "name": "ShardBeats",
                "url": BASE_URL,
            },
        })

    video_section = ''
    video_script = ''
    if tool.get('video'):
        vid = tool['video']
        label = ui['video_play'] + ' ' + vid['title']
        video_section = '\n'.join([
            '  <section class="section" id="video">',
            '    <div class="container prose">',
            '      <h2>' + esc(ui['video_heading']) + '</h2>',
            '      <div class="video-embed" data-video-id="' + vid['id'] + '">',
            '        <button type="button" class="video-facade" aria-label="' + esc(label) + '">',
            '          <img src="' + root_rel + 'assets/video-' + tool['slug'] + '.jpg"'
            ' alt="" width="1280" height="720" loading="lazy" />',
            '          <span class="video-badge" aria-hidden="true"></span>',
            '        </button>',
            '      </div>',
            '      <p class="video-caption">' + esc(vid['title'])
            + ' · <a href="https://www.youtube.com/watch?v=' + vid['id']
            + '" target="_blank" rel="noopener">' + esc(ui['video_watch']) + '</a></p>',
            '    </div>',
            '  </section>',
        ])
        video_script = VIDEO_SCRIPT

    import json
    html = PAGE.substitute(
        lang=lang,
        title=esc(t['title']),
        desc=esc(t['desc']),
        canonical=canonical,
        alt_es=alt_es,
        alt_en=alt_en,
        alt_other=alt_other,
        otherlang=other,
        otherlang2=other,
        site=SITE,
        name=tool['name'],
        version=tool['version'],
        tagline=esc(t['tagline']),
        lead=esc(t['lead']),
        root_rel=root_rel,
        home_es=home_es,
        home_pack=home_pack,
        og_image=og_image,
        oglocale='es_ES' if lang == 'es' else 'en_US',
        shot=shot_rel,
        shot_alt=esc(ui['screenshot_alt'].format(name=tool['name'])),
        shot_w=shot_w,
        shot_h=shot_h,
        download=tool['repo'] + '/releases/latest',
        download_label=ui['download'],
        repo=tool['repo'],
        repo_label=ui['repo'],
        android_link=android_link,
        bullets=bullets,
        steps=steps,
        specs_rows=specs_rows,
        faq_html=faq_html,
        others_cards='\n'.join(cards),
        schema=json.dumps(schema, ensure_ascii=False, indent=2),
        bg_script=BG_SCRIPT,
        video_section=video_section,
        video_script=video_script,
        lang_switch_full='English' if lang == 'es' else 'Español',
        navlabel='Principal' if lang == 'es' else 'Main',
        **{k: v for k, v in ui.items() if k not in ('screenshot_alt', 'download', 'repo')},
    )
    return html


def main():
    versions = load_versions()
    written = 0
    for tool in TOOLS:
        tool = dict(tool)
        tool["version"] = versions.get(tool["slug"], tool["version"])
        for lang in ('es', 'en'):
            if lang == 'es':
                out_dir = os.path.join(ROOT, tool['slug'])
            else:
                out_dir = os.path.join(ROOT, 'en', tool['slug'])
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, 'index.html')
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(build(tool, lang))
            written += 1
            t = tool[lang]
            print('%-44s title=%d desc=%d' % (os.path.relpath(path, ROOT), len(t['title']), len(t['desc'])))
    print('written: %d' % written)


if __name__ == '__main__':
    main()
