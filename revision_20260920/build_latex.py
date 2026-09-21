"""Generate a self-contained LaTeX source tree and compile it with XeLaTeX."""
from pathlib import Path
import argparse, subprocess, shutil, re, platform
P=Path(__file__).resolve().parent
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--output-dir',type=Path,default=P.parent/'paper'/'revised')
ap.add_argument('--font',default='Times New Roman' if platform.system()=='Windows' else 'TeX Gyre Termes')
ap.add_argument('--no-compile',action='store_true')
args=ap.parse_args();out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
if not shutil.which('pandoc'):ap.error('Install Pandoc and add it to PATH')
if not args.no_compile and not shutil.which('xelatex'):ap.error('Install XeLaTeX (TeX Live or MiKTeX) and add it to PATH')
(out/'figures').mkdir(exist_ok=True)
md=(P/'Paper3_Revised.md').read_text(encoding='utf-8')
parts=md.split('\n\n',2);title=parts[0].lstrip('# ') + ': '+parts[1].strip();md=parts[2]
for image in re.findall(r'\]\(analysis/([^)]*)\)',md):
    shutil.copy2(P/'analysis'/image,out/'figures'/image)
md=md.replace('](analysis/','](figures/')
# Preserve hand-numbered section headings and figure captions consistently with Word.
md=re.sub(r'^### \d+\.\d+\s+', '### ',md,flags=re.M)
md=re.sub(r'^## \d+\s+', '## ',md,flags=re.M)
md=re.sub(r'^(#{2,3}) ',lambda m:m.group(1)[1:]+' ',md,flags=re.M)
md=re.sub(r'^# (Abstract|Keywords|Data availability|Relationship to related manuscripts|References)$',r'# \1 {.unnumbered}',md,flags=re.M)
md=re.sub(r'^Table \d+  (.+)$',r'Table: \1',md,flags=re.M)
md=re.sub(r'(?<![<(])(https?://[^\s<>]+)',r'<\1>',md)
(out/'manuscript.md').write_text(md,encoding='utf-8')
header=r'''\usepackage{float}
\usepackage{xurl}
\usepackage{placeins}
\usepackage{caption}
\captionsetup{font=small,labelfont=bf}
\floatplacement{figure}{H}
\setlength{\emergencystretch}{3em}
\AtBeginEnvironment{longtable}{\small}
'''
(out/'header.tex').write_text(header,encoding='utf-8')
cmd=['pandoc','manuscript.md','--standalone','--to=latex','--top-level-division=section','--number-sections','--resource-path=.',
     '--metadata',f'title={title}','--metadata','date=','-V','documentclass=article','-V','fontsize=11pt','-V','papersize=a4','-V','geometry:margin=2.3cm',
     '-V',f'mainfont={args.font}','-V','colorlinks=true','-V','linkcolor=black','-V','urlcolor=blue','--include-in-header=header.tex','-o','Paper3_Revised.tex']
subprocess.run(cmd,cwd=out,check=True)
if not args.no_compile:
    for _ in range(2):
        result=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','Paper3_Revised.tex'],cwd=out,capture_output=True,text=True,encoding='utf-8',errors='replace')
        (out/'build_console.txt').write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
        if result.returncode:raise RuntimeError(f'XeLaTeX failed; see {out / "build_console.txt"}')
print(f'LaTeX output: {out}')
