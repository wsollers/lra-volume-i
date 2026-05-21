# =============================================================
# .latexmkrc — lra-volume-i
# =============================================================
$pdf_mode = 4;
$lualatex = 'lualatex -interaction=nonstopmode -file-line-error -synctex=1 -shell-escape %O %S';
$bibtex_use = 1;
$max_repeat = 8;
$out_dir = 'build';
$aux_dir = 'build';
$pdf_previewer = 'start %S';
$clean_ext = 'aux bbl blg fdb_latexmk fls idx ilg ind lof lot out run.xml synctex.gz toc tech.idx tech.ind tech.ilg dep.idx dep.ind dep.ilg nav snm vrb xdv';
