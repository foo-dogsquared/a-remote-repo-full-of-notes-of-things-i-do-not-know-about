
config = {
    "DEFAULT_NOTE_EDITOR": "vim",
    "FIGURES_DIRECTORY_NAME": "graphics",
    "DEFAULT_LATEXMKRC_TEMPLATE": """ensure_path( 'TEXINPUTS', '../../styles//' );""",
    "DEFAULT_LATEX_SUBFILE_SOURCE_CODE": r"""\documentclass[class=memoir, crop=false, oneside, 14pt]{standalone}
\usepackage{docs-config}

% document metadata
\author{${__author__}}
\title{${__title__}}
\date{${__date__}}

\begin{document}
% Frontmatter of the class note if it's compiled standalone
\ifrootdocument
    \renewcommand{\abstractname}{Summary}
    \maketitle
    \newpage

    \frontmatter
    \chapter{Preface}

    \newpage

    \tableofcontents
    \newpage

    \listoffigures
    \newpage

    \mainmatter
\fi
% Core content (HINT: always start with chapter LaTeX tag)

\bibliographystyle{plain}
\bibliography{ref}
\end{document}
""",
"DEFAULT_LATEX_MAIN_LECTURE_IMPORT_CODE": r"\\part{{{note['title']}}}\n\\inputchilddocument{{{note['slug']}}}\n\n",
"DEFAULT_LATEX_MAIN_FILE_SOURCE_CODE": r"""\documentclass[class=memoir, crop=false, oneside, 12pt]{standalone}
\usepackage{docs-config}

% document metadata
\author{${__author__}}
\title{${__title__}}
\date{${__date__}}

\begin{document}
% Frontmatter of the class note
\renewcommand{\abstractname}{Summary}
\maketitle
\newpage

\frontmatter
${__preface__}

\tableofcontents
\newpage

\listoffigures
\newpage

\mainmatter

${__main__}

\bibliographystyle{plain}
\bibliography{ref}
\end{document}
""",
"DEFAULT_SVG_EDITOR": "inkscape",
"DEFAULT_SVG_TEMPLATE": """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="240mm"
   height="120mm"
   viewBox="0 0 240 120"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.4 (unknown)"
   sodipodi:docname="figure.svg">
  <defs
     id="defs2" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.99437388"
     inkscape:cx="284.27627"
     inkscape:cy="182.72055"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     showborder="true"
     width="200mm"
     showguides="true"
     inkscape:guide-bbox="true"
     inkscape:window-width="2520"
     inkscape:window-height="995"
     inkscape:window-x="20"
     inkscape:window-y="65"
     inkscape:window-maximized="1">
    <inkscape:grid
       type="xygrid"
       id="grid815"
       units="mm"
       spacingx="10"
       spacingy="10"
       empspacing="4"
       dotted="false" />
  </sodipodi:namedview>
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(0,-177)" />
</svg>
"""
}