%global shortname texlive
%global source_date 20210325
%global source_name texlive-%{source_date}-source
%{!?_texdir: %global _texdir %{_datadir}/%{shortname}}
%{!?_texmf_var: %global _texmf_var %{_var}/lib/texmf}

%global etc_fmtutil_cnf %{_sysconfdir}/texlive/web2c/fmtutil.cnf
%global usr_fmtutil_cnf %{_texdir}/texmf-dist/web2c/fmtutil.cnf
%global fmtutil_cnf_d %{_texdir}/fmtutil.cnf.d

# don't export private perl modules
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((LatexIndent.*|PDF::Reuse.*|Pedigree.*|TeXLive.*|Tk::path_tre)\\)

# We do not want exec perms changing.
%global __brp_mangle_shebangs_exclude ^$

# We have a circular dep on latex due to xindy
%bcond_with bootstrap

Name: %{shortname}-base
Version: %{source_date}
Release: 32%{?dist}
Epoch: 9
Summary: TeX formatting system
# The only files in the base package are directories, cache, and license texts
# So we'll just list the license texts. This is also a bit of a lie, since most of these license texts do not apply to themselves.
License: ASL 2.0 and Artistic 2.0 and BSD and GFDL and GPL+ and GPLv2 and GPLv3 and Knuth and LGPLv2+ and LGPLv3+ and LPPL and OFL and Public Domain
URL: http://tug.org/texlive/
Source0: https://ctan.math.illinois.edu/systems/texlive/Source/%{source_name}.tar.xz
Source1: macros.texlive
Source2: http://tug.ctan.org/systems/texlive/tlnet/tlpkg/texlive.tlpdb
Source3: texlive-licenses.tar.xz
Source4: generate-fmtutilcnf
# These noarch components are packed wrong upstream (do not unpack into texmf-dist)
Source5: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cyrillic.tar.xz
Source6: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cyrillic.doc.tar.xz
Source7: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/glyphlist.tar.xz
Source8: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex.tar.xz
Source9: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex.doc.tar.xz
Source10: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lyluatex.tar.xz
Source11: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lyluatex.doc.tar.xz
Source12: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oberdiek.tar.xz
Source13: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/oberdiek.doc.tar.xz
Source14: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-en.doc.tar.xz
# These are the noarch components for the built binaries.
Source15: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/a2ping.doc.tar.xz
Source16: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/a2ping.tar.xz
Source17: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/accfonts.doc.tar.xz
Source18: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/accfonts.tar.xz
Source19: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adhocfilelist.doc.tar.xz
Source20: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/adhocfilelist.tar.xz
Source21: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/afm2pl.tar.xz
Source22: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aleph.doc.tar.xz
Source23: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/aleph.tar.xz
Source24: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amstex.doc.tar.xz
Source25: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/amstex.tar.xz
Source26: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arara.doc.tar.xz
Source27: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/arara.tar.xz
Source28: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/attachfile2.doc.tar.xz
Source29: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/attachfile2.tar.xz
Source30: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/authorindex.doc.tar.xz
Source31: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/authorindex.tar.xz
Source32: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/autosp.doc.tar.xz
Source33: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/axodraw2.doc.tar.xz
Source34: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/axodraw2.tar.xz
Source35: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bib2gls.doc.tar.xz
Source36: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bib2gls.tar.xz
Source37: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibexport.doc.tar.xz
Source38: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibexport.tar.xz
Source39: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibtex8.doc.tar.xz
Source40: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibtex8.tar.xz
Source41: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibtex.doc.tar.xz
Source42: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibtex.tar.xz
Source43: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bibtexu.doc.tar.xz
Source44: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bundledoc.doc.tar.xz
Source45: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bundledoc.tar.xz
Source46: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cachepic.doc.tar.xz
Source47: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cachepic.tar.xz
Source48: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/checkcites.doc.tar.xz
Source49: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/checkcites.tar.xz
Source50: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/checklistings.doc.tar.xz
Source51: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/checklistings.tar.xz
Source52: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chklref.doc.tar.xz
Source53: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chklref.tar.xz
Source54: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chktex.doc.tar.xz
Source55: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chktex.tar.xz
Source56: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk-gs-integrate.doc.tar.xz
Source57: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk-gs-integrate.tar.xz
Source58: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjkutils.tar.xz
Source59: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/clojure-pamphlet.doc.tar.xz
Source60: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/clojure-pamphlet.tar.xz
Source61: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cluttex.doc.tar.xz
Source62: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cluttex.tar.xz
Source63: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context.doc.tar.xz
Source64: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/context.tar.xz
Source65: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/convbkmk.doc.tar.xz
Source66: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/convbkmk.tar.xz
Source67: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crossrefware.doc.tar.xz
Source68: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/crossrefware.tar.xz
Source69: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cslatex.tar.xz
Source70: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/csplain.tar.xz
Source71: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctanbib.doc.tar.xz
Source72: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctanbib.tar.xz
Source73: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctanify.doc.tar.xz
Source74: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctanify.tar.xz
Source75: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctan-o-mat.doc.tar.xz
Source76: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctan-o-mat.tar.xz
Source77: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctanupload.doc.tar.xz
Source78: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctanupload.tar.xz
Source79: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ctie.doc.tar.xz
Source80: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cweb.doc.tar.xz
Source81: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cweb.tar.xz
Source82: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cyrillic-bin.doc.tar.xz
Source83: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cyrillic-bin.tar.xz
Source84: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/de-macro.doc.tar.xz
Source85: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/de-macro.tar.xz
Source86: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/detex.doc.tar.xz
Source87: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/detex.tar.xz
Source88: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/diadia.doc.tar.xz
Source89: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/diadia.tar.xz
Source90: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dosepsbin.doc.tar.xz
Source91: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dosepsbin.tar.xz
Source92: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dtl.doc.tar.xz
Source93: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dtl.tar.xz
Source94: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dtxgen.doc.tar.xz
Source95: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dtxgen.tar.xz
Source96: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvi2tty.doc.tar.xz
Source97: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvi2tty.tar.xz
Source98: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dviasm.doc.tar.xz
Source99: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dviasm.tar.xz
Source100: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvicopy.doc.tar.xz
Source101: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvicopy.tar.xz
Source102: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvidvi.doc.tar.xz
Source103: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvidvi.tar.xz
Source104: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dviinfox.doc.tar.xz
Source105: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dviinfox.tar.xz
Source106: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dviljk.doc.tar.xz
Source107: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dviljk.tar.xz
Source108: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dviout-util.doc.tar.xz
Source109: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvipdfmx.doc.tar.xz
Source110: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvipdfmx.tar.xz
Source111: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvipng.doc.tar.xz
Source112: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvipng.tar.xz
Source113: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvipos.doc.tar.xz
Source114: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvipos.tar.xz
Source115: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvips.doc.tar.xz
Source116: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvips.tar.xz
Source117: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvisvgm.doc.tar.xz
Source118: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/dvisvgm.tar.xz
Source119: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebong.doc.tar.xz
Source120: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ebong.tar.xz
Source121: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eplain.doc.tar.xz
Source122: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/eplain.tar.xz
Source123: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epspdf.doc.tar.xz
Source124: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epspdf.tar.xz
Source125: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epstopdf.doc.tar.xz
Source126: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epstopdf.tar.xz
Source127: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/exceltex.doc.tar.xz
Source128: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/exceltex.tar.xz
Source129: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fig4latex.doc.tar.xz
Source130: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fig4latex.tar.xz
Source131: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/findhyph.doc.tar.xz
Source132: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/findhyph.tar.xz
Source133: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontinst.doc.tar.xz
Source134: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontinst.tar.xz
Source135: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontools.doc.tar.xz
Source136: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontools.tar.xz
Source137: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fontware.doc.tar.xz
Source138: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fragmaster.doc.tar.xz
Source139: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fragmaster.tar.xz
Source140: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/getmap.doc.tar.xz
Source141: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/getmap.tar.xz
Source142: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/glossaries.doc.tar.xz
Source143: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/glossaries.tar.xz
Source144: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gregoriotex.doc.tar.xz
Source145: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gregoriotex.tar.xz
Source146: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gsftopk.doc.tar.xz
Source147: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/gsftopk.tar.xz
Source148: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/installfont.doc.tar.xz
Source149: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/installfont.tar.xz
Source150: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jadetex.doc.tar.xz
Source151: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jadetex.tar.xz
Source152: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jfmutil.doc.tar.xz
Source153: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/jfmutil.tar.xz
Source154: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ketcindy.doc.tar.xz
Source155: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ketcindy.tar.xz
Source156: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-utils.doc.tar.xz
Source157: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kotex-utils.tar.xz
Source158: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kpathsea.doc.tar.xz
Source159: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/kpathsea.tar.xz
Source160: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3build.tar.xz
Source161: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/l3build.doc.tar.xz
Source162: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lacheck.doc.tar.xz
Source163: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2man.doc.tar.xz
Source164: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2man.tar.xz
Source165: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2nemeth.doc.tar.xz
Source166: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex2nemeth.tar.xz
Source167: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexdiff.doc.tar.xz
Source168: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexdiff.tar.xz
Source169: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexfileversion.doc.tar.xz
Source170: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexfileversion.tar.xz
Source171: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-git-log.doc.tar.xz
Source172: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-git-log.tar.xz
Source173: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexindent.doc.tar.xz
Source174: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexindent.tar.xz
Source175: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexpand.doc.tar.xz
Source176: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latexpand.tar.xz
Source177: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-papersize.doc.tar.xz
Source178: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/latex-papersize.tar.xz
Source179: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lcdftypetools.doc.tar.xz
Source180: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lilyglyphs.doc.tar.xz
Source181: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lilyglyphs.tar.xz
Source182: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/listbib.doc.tar.xz
Source183: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/listbib.tar.xz
Source184: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/listings-ext.doc.tar.xz
Source185: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/listings-ext.tar.xz
Source186: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lollipop.doc.tar.xz
Source187: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lollipop.tar.xz
Source188: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltxfileinfo.doc.tar.xz
Source189: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltxfileinfo.tar.xz
Source190: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltximg.doc.tar.xz
Source191: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ltximg.tar.xz
Source192: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaotfload.doc.tar.xz
Source193: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luaotfload.tar.xz
Source194: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luahbtex.doc.tar.xz
Source195: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luahbtex.tar.xz
Source196: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatex.doc.tar.xz
Source197: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatex.tar.xz
Source198: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lwarp.doc.tar.xz
Source199: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lwarp.tar.xz
Source200: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/make4ht.doc.tar.xz
Source201: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/make4ht.tar.xz
Source202: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/makedtx.doc.tar.xz
Source203: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/makedtx.tar.xz
Source204: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/makeindex.doc.tar.xz
Source205: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/makeindex.tar.xz
Source206: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/match_parens.doc.tar.xz
Source207: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/match_parens.tar.xz
Source208: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathspic.doc.tar.xz
Source209: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mathspic.tar.xz
Source210: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metafont.doc.tar.xz
Source211: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metafont.tar.xz
Source212: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metapost.doc.tar.xz
Source213: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/metapost.tar.xz
Source214: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mex.doc.tar.xz
Source215: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mex.tar.xz
Source216: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mf2pt1.doc.tar.xz
Source217: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mf2pt1.tar.xz
Source218: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mflua.tar.xz
Source219: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfware.doc.tar.xz
Source220: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mfware.tar.xz
Source221: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mkgrkindex.doc.tar.xz
Source222: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mkgrkindex.tar.xz
Source223: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mkjobtexmf.doc.tar.xz
Source224: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mkjobtexmf.tar.xz
Source225: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mkpic.doc.tar.xz
Source226: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mkpic.tar.xz
Source227: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mltex.doc.tar.xz
Source228: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mltex.tar.xz
Source229: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mptopdf.doc.tar.xz
Source230: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/mptopdf.tar.xz
Source231: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/m-tx.doc.tar.xz
Source232: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/m-tx.tar.xz
Source233: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multibibliography.doc.tar.xz
Source234: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multibibliography.tar.xz
Source235: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixtex.doc.tar.xz
Source236: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixtex.tar.xz
Source237: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixtnt.doc.tar.xz
Source238: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/musixtnt.tar.xz
Source239: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/omegaware.doc.tar.xz
Source240: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/patgen.doc.tar.xz
Source241: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/patgen.tar.xz
Source242: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pax.doc.tar.xz
Source243: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pax.tar.xz
Source244: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfbook2.doc.tar.xz
Source245: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfbook2.tar.xz
Source246: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcrop.doc.tar.xz
Source247: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcrop.tar.xz
Source248: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfjam.doc.tar.xz
Source249: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfjam.tar.xz
Source250: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdflatexpicscale.doc.tar.xz
Source251: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdflatexpicscale.tar.xz
Source252: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftex.doc.tar.xz
Source253: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftex.tar.xz
Source254: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftex-quiet.doc.tar.xz
Source255: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdftex-quiet.tar.xz
Source256: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfxup.doc.tar.xz
Source257: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfxup.tar.xz
Source258: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pedigree-perl.doc.tar.xz
Source259: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pedigree-perl.tar.xz
Source260: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/perltex.doc.tar.xz
Source261: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/perltex.tar.xz
Source262: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/petri-nets.doc.tar.xz
Source263: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/petri-nets.tar.xz
Source264: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pfarrei.doc.tar.xz
Source265: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pfarrei.tar.xz
Source266: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pkfix.doc.tar.xz
Source267: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pkfix-helper.doc.tar.xz
Source268: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pkfix-helper.tar.xz
Source269: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pkfix.tar.xz
Source270: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmxchords.doc.tar.xz
Source271: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmxchords.tar.xz
Source272: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmx.doc.tar.xz
Source273: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pmx.tar.xz
Source274: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ps2eps.doc.tar.xz
Source275: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ps2eps.tar.xz
Source276: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ps2pk.doc.tar.xz
Source277: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ps2pk.tar.xz
Source278: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst2pdf.doc.tar.xz
Source279: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst2pdf.tar.xz
Source280: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-pdf.doc.tar.xz
Source281: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pst-pdf.tar.xz
Source282: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psutils.doc.tar.xz
Source283: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/psutils.tar.xz
Source284: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex2pdf.doc.tar.xz
Source285: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex2pdf.tar.xz
Source286: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex.doc.tar.xz
Source287: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-fontmaps.doc.tar.xz
Source288: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-fontmaps.tar.xz
Source289: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex.tar.xz
Source290: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/purifyeps.doc.tar.xz
Source291: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/purifyeps.tar.xz
Source292: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pygmentex.doc.tar.xz
Source293: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pygmentex.tar.xz
Source294: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pythontex.doc.tar.xz
Source295: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pythontex.tar.xz
Source296: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rubik.doc.tar.xz
Source297: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/rubik.tar.xz
Source298: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seetexk.doc.tar.xz
Source299: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/seetexk.tar.xz
Source300: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/splitindex.doc.tar.xz
Source301: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/splitindex.tar.xz
Source302: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/srcredact.doc.tar.xz
Source303: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/srcredact.tar.xz
Source304: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sty2dtx.doc.tar.xz
Source305: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sty2dtx.tar.xz
Source306: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/svn-multi.doc.tar.xz
Source307: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/svn-multi.tar.xz
Source308: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/synctex.doc.tar.xz
Source309: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/synctex.tar.xz
Source310: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex4ebook.doc.tar.xz
Source311: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex4ebook.tar.xz
Source312: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex4ht.doc.tar.xz
Source313: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex4ht.tar.xz
Source314: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texcount.doc.tar.xz
Source315: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texcount.tar.xz
Source316: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdef.doc.tar.xz
Source317: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdef.tar.xz
Source318: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdiff.doc.tar.xz
Source319: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdiff.tar.xz
Source320: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdirflatten.doc.tar.xz
Source321: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdirflatten.tar.xz
Source322: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdoc.doc.tar.xz
Source323: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex.doc.tar.xz
Source324: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdoc.tar.xz
Source325: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdoctk.tar.xz
Source326: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texdoctk.doc.tar.xz
Source327: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texfot.doc.tar.xz
Source328: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texfot.tar.xz
Source329: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive.infra.doc.tar.xz
Source330: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive.infra.tar.xz
Source331: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texliveonfly.doc.tar.xz
Source332: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texliveonfly.tar.xz
Source333: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-scripts.doc.tar.xz
Source334: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-scripts.tar.xz
Source335: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-scripts-extra.doc.tar.xz
Source336: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-scripts-extra.tar.xz
Source337: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texloganalyser.doc.tar.xz
Source338: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texloganalyser.tar.xz
Source339: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texosquery.doc.tar.xz
Source340: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texosquery.tar.xz
Source341: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texplate.doc.tar.xz
Source342: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texplate.tar.xz
Source343: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texsis.doc.tar.xz
Source344: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texsis.tar.xz
Source345: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex.tar.xz
Source346: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texware.doc.tar.xz
Source347: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texware.tar.xz
Source348: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thumbpdf.doc.tar.xz
Source349: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/thumbpdf.tar.xz
Source350: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tie.doc.tar.xz
Source351: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tie.tar.xz
Source352: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tpic2pdftex.doc.tar.xz
Source353: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tpic2pdftex.tar.xz
Source354: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ttfutils.doc.tar.xz
Source355: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ttfutils.tar.xz
Source356: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typeoutfileinfo.doc.tar.xz
Source357: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/typeoutfileinfo.tar.xz
Source358: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ulqda.doc.tar.xz
Source359: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ulqda.tar.xz
Source360: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uplatex.doc.tar.xz
Source361: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uptex.doc.tar.xz
Source362: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/urlbst.doc.tar.xz
Source363: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/urlbst.tar.xz
Source364: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/velthuis.doc.tar.xz
Source365: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/velthuis.tar.xz
Source366: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vlna.doc.tar.xz
Source367: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vpe.doc.tar.xz
Source368: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/vpe.tar.xz
Source369: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/web.doc.tar.xz
Source370: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/web.tar.xz
Source371: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/webquiz.doc.tar.xz
Source372: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/webquiz.tar.xz
Source373: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wordcount.doc.tar.xz
Source374: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/wordcount.tar.xz
Source375: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xdvi.doc.tar.xz
Source376: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xdvi.tar.xz
Source377: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex.doc.tar.xz
Source378: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xetex.tar.xz
Source379: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xindex.doc.tar.xz
Source380: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xindex.tar.xz
%if ! 0%{?eln}
Source381: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xindy.doc.tar.xz
Source382: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xindy.tar.xz
%endif
Source383: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xmltex.doc.tar.xz
Source384: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xmltex.tar.xz
Source385: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpdfopen.doc.tar.xz
Source386: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yplan.doc.tar.xz
Source387: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/yplan.tar.xz
Source388: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/optex.tar.xz
Source389: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/optex.doc.tar.xz
# 2021
Source390: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/albatross.tar.xz
Source391: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/albatross.doc.tar.xz
Source392: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/git-latexdiff.tar.xz
Source393: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/git-latexdiff.doc.tar.xz
Source394: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyperxmp.tar.xz
Source395: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyperxmp.doc.tar.xz
Source396: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/light-latex-make.tar.xz
Source397: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/light-latex-make.doc.tar.xz
Source398: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spix.tar.xz
Source399: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/spix.doc.tar.xz
Source400: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikztosvg.tar.xz
Source401: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tikztosvg.doc.tar.xz
Source402: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xml2pmx.tar.xz
Source403: https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xml2pmx.doc.tar.xz

Patch1: tl-kpfix.patch
Patch2: tl-format.patch
Patch5: texlive-2016-kpathsea-texlive-path.patch
# fixes from arch and upstream texlive
Patch7: texlive-20210325-new-poppler.patch
# fix texmf.cnf so that it finds texinfo bits in Fedora
Patch8: texlive-20210325-texinfo-path-fix.patch
# These tests only fail on 32 bit arches with gcc8
Patch11: texlive-20200327-disable-more-failing-tests.patch
# Another test which fails on 32 bit arches (in F30+)
# probably because of stricter malloc checks in glibc.
# https://bugzilla.redhat.com/show_bug.cgi?id=1631847
# Filed issue upstream, no resolution yet.
Patch15: texlive-base-20180414-disable-omegafonts-check-test.patch
# fix annocheck issue detected by rpmdiff
Patch17: texlive-20180414-annocheck.patch
Patch18: texlive-20210325-poppler-0.73.patch
# Fix libgs detection in configure/configure.ac in dvisvgm
Patch20: texlive-20190410-dvisvgm-fix-libgs-detection.patch
# Since we need to include tlmgr.pl for texconfig
# lets try to keep people from shooting themselves with it
Patch21: texlive-20190410-tlmgr-ignore-warning.patch
Patch23: texlive-20210325-poppler-0.84.patch
# Fixes for poppler 0.90 (f33+)
Patch29: texlive-20200327-poppler-0.90.patch
# Fix pdflatex run out of memory
Patch30: texlive-base-20200327-out-of-memory.patch
# Fix configure to properly detect poppler
Patch31: texlive-base-20210325-configure-poppler-xpdf-fix.patch

# Can't do this because it causes everything else to be noarch
# BuildArch: noarch
BuildRequires: make
BuildRequires: gcc gcc-c++
BuildRequires: xz libXaw-devel libXi-devel ncurses-devel bison flex file perl(Digest::MD5) texinfo gcc-c++
BuildRequires: gd-devel
BuildRequires: teckit-devel >= 2.5.7
BuildRequires: freetype-devel libpng-devel t1lib-devel zlib-devel poppler-devel t1utils
BuildRequires: zziplib-devel libicu-devel cairo-devel harfbuzz-devel perl-generators pixman-devel graphite2-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires: libgs-devel
%else
BuildRequires: ghostscript-devel
%endif
BuildRequires: libpaper-devel potrace-devel autoconf automake libtool
BuildRequires: gmp-devel mpfr-devel
# This is really for macros.
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if %{without bootstrap}
# This is for xindy
%if ! 0%{?eln}
BuildRequires: clisp-devel
BuildRequires: texlive-cyrillic, texlive-latex, texlive-metafont, texlive-cm-super, texlive-ec
%endif
%endif
# This is temporary to fix build while missing kpathsea dep is active
BuildRequires: texlive-texlive-scripts
# This is needed for a test
BuildRequires: texlive-amsfonts

# Cleanup Provides/Obsoletes
# texlive-cjk-gs-integrate (depackaged 2018-03-09)
Provides: texlive-cjk-gs-integrate = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cjk-gs-integrate <= 7:20170520
Provides: tex-cjk-gs-integrate = %{epoch}:%{source_date}-%{release}
Obsoletes: tex-cjk-gs-integrate <= 7:20170520
Provides: texlive-cjk-gs-integrate-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-cjk-gs-integrate-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cjk-gs-integrate-bin <= 7:20170520
Obsoletes: tex-cjk-gs-integrate-bin <= 7:20170520
Provides: texlive-cjk-gs-integrate-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cjk-gs-integrate-doc <= 7:20170520

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n %{shortname}-a2ping
Provides: tex-a2ping = %{epoch}:%{source_date}-%{release}
Provides: texlive-a2ping-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-a2ping-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-a2ping-bin < 7:20170520
License: GPL+
Summary: Advanced PS, PDF, EPS converter
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-a2ping
a2ping is a Perl script command line utility written for Unix
that converts many raster image and vector graphics formats to
EPS or PDF and other page description formats. Accepted input
file formats are: PS (PostScript), EPS, PDF, PNG, JPEG, TIFF,
PNM, BMP, GIF, LBM, XPM, PCX, TGA. Accepted output formats are:
EPS, PCL5, PDF, PDF1, PBM, PGM, PPM, PS, markedEPS, markedPS,
PNG, XWD, BMP, TIFF, JPEG, GIF, XPM. a2ping delegates the low-
level work to Ghostscript (GS), pdftops and sam2p. a2ping fixes
many glitches during the EPS to EPS conversion, so its output
is often more compatible and better embeddable than its input.

%package -n %{shortname}-accfonts
Provides: tex-accfonts = %{epoch}:%{source_date}-%{release}
Provides: texlive-accfonts-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-accfonts-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-accfonts-bin < 7:20170520
Provides: tex-accfonts-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-accfonts-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-accfonts-doc < 7:20170520
License: GPL+
Summary: Utilities to derive new fonts from existing ones
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(CSX.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(ISO-Latin1.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(ISO-Latin2.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(IndUni_Omega.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(Norman.def) = %{epoch}:%{source_date}-%{release}
BuildArch: noarch

%description -n %{shortname}-accfonts
The accfonts package contains three utilities to permit easy
manipulation of fonts, in particular the creation of unusual
accented characters. Mkt1font works on Adobe Type 1 fonts,
vpl2vpl works on TeX virtual fonts and vpl2ovp transforms a TeX
font to an Omega one. All three programs read in a font (either
the font itself or a property list), together with a simple
definition file containing lines such as '128 z acute'; they
then write out a new version of the font with the requested new
characters in the numerical slots specified. Great care is
taken over the positioning of accents, and over the provision
of kerning information for new characters; mkt1font also
generates suitable "hints" to enhance quality at small sizes or
poor resolutions. The programs are written in Perl.

%package -n %{shortname}-adhocfilelist
Provides: tex-adhocfilelist = %{epoch}:%{source_date}-%{release}
Provides: texlive-adhocfilelist-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-adhocfilelist-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-adhocfilelist-bin < 7:20170520
Provides: tex-adhocfilelist-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-adhocfilelist-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-adhocfilelist-doc < 7:20170520
License: LPPL
Summary: '\listfiles' entries from the command line
Requires: texlive-base
Requires: texlive-kpathsea
# shell
BuildArch: noarch

%description -n %{shortname}-adhocfilelist
The package provides a Unix shell script to display a list of
LaTeX \Provides...-command contexts on screen. Provision is
made for controlling the searches that the package does. The
package was developed on a Unix-like system, using (among other
things) the gnu variant of the find command.

%package -n %{shortname}-afm2pl
Provides: tex-afm2pl = %{epoch}:%{source_date}-%{release}
Provides: texlive-afm2pl-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-afm2pl-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-afm2pl-bin < 7:20170520
License: LPPL
Summary: afm2pl package
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(afm2pl-ot1.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(afm2pl-ot1ital.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(afm2pl-ot1tt.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(afm2pl-texnanlc.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(afm2pl-texnanuc.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(makesc8y.tex) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-afm2pl
afm2pl package.

%package -n %{shortname}-albatross
Summary: Find fonts that contain a given glyph
License: BSD
Requires: texlive-base texlive-kpathsea

%description -n %{shortname}-albatross
This is a command line tool for finding fonts that contain a
given (Unicode) glyph. It relies on Fontconfig.

%package -n %{shortname}-aleph
Provides: tex-aleph = %{epoch}:%{source_date}-%{release}
Provides: texlive-aleph-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-aleph-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-aleph-bin < 7:20170520
Provides: tex-aleph-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-aleph-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-aleph-doc < 7:20170520
Summary: Extended TeX
Requires: texlive-base
Requires: texlive-kpathsea
Requires(post,postun): coreutils
Requires: texlive-latex
Requires: texlive-plain
Requires: texlive-lambda
Requires: texlive-cm
Requires: texlive-hyphen-base
Requires: texlive-knuth-lib
Requires: texlive-antomega
Requires: texlive-latex-fonts
Requires: texlive-omega
Requires: texlive-l3kernel

%description -n %{shortname}-aleph
An development of omega, using most of the extensions of TeX
itself developed for e-TeX.

%package -n %{shortname}-amstex
Provides: tex-amstex = %{epoch}:%{source_date}-%{release}
Provides: texlive-amstex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-amstex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-amstex-bin < 7:20170520
Provides: tex-amstex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-amstex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-amstex-doc < 7:20170520
License: LPPL
Summary: American Mathematical Society plain TeX macros
Requires: texlive-base
Requires: texlive-kpathsea
Requires(post,postun): coreutils
Requires: texlive-tex
Requires: texlive-amsfonts
Requires: texlive-cm
Requires: texlive-hyphen-base
Requires: texlive-knuth-lib
Requires: texlive-plain
Provides: tex(amsppt.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(amsppt1.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(amstex.bug) = %{epoch}:%{source_date}-%{release}
Provides: tex(amstex.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(amstex.ini) = %{epoch}:%{source_date}-%{release}
# symlinks only
BuildArch: noarch

%description -n %{shortname}-amstex
AMSTeX is a TeX macro package, originally written by Michael
Spivak for the American Mathematical Society (AMS) during 1983-
1985 and is described in the book 'The Joy of TeX'. It is based
on Plain TeX, and provides many features for producing more
professional-looking maths formulas with less burden on
authors. More recently, the focus of attention has switched to
amslatex, but AMSTeX remains as a working system.

%package -n %{shortname}-arara
Provides: tex-arara = %{epoch}:%{source_date}-%{release}
Provides: texlive-arara-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-arara-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-arara-bin < 7:20170520
Provides: tex-arara-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-arara-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-arara-doc < 7:20170520
License: BSD
Summary: Automation of LaTeX compilation
Requires: texlive-base
Requires: texlive-kpathsea
Provides: bundled(slf4j) = 1.6.4
Provides: bundled(apache-commons-collections) = 3.2.1
Provides: bundled(apache-commons-exec) = 1.1
Provides: bundled(apache-commons-lang3) = 3.1
Provides: bundled(apache-commons-cli) = 1.2
Provides: bundled(mvel2) = 2.0.19
Provides: bundled(snakeyaml) = 1.11
Provides: bundled(logback) = 1.0.1
# shell
BuildArch: noarch

%description -n %{shortname}-arara
Arara is comparable with other well-known compilation tools
like latexmk and rubber. The key difference is that that arara
determines its actions from metadata in the source code, rather
than relying on indirect resources, such as log file analysis.

%package -n %{shortname}-attachfile2
Provides: tex-attachfile2 = %{epoch}:%{source_date}-%{release}
Provides: tex-attachfile2-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-attachfile2-bin = %{epoch}:%{source_date}-%{release}
License: LPPL
Summary: Attach files into PDF
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(attachfile2.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-attachfile2
This package can be used to attach files to a PDF document. It
is a further development of Scott Pakin's package attachfile
for pdfTeX. Apart from bug fixes, this package adds support for
dvips, some new options, and gets and writes meta information
data about the attached files.

%package -n %{shortname}-authorindex
Provides: tex-authorindex = %{epoch}:%{source_date}-%{release}
Provides: texlive-authorindex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-authorindex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-authorindex-bin < 7:20170520
Provides: tex-authorindex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-authorindex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-authorindex-doc < 7:20170520
License: LPPL
Summary: Index citations by author names
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(authorindex.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-authorindex
This package allows the user to create an index of all authors
cited in a LaTeX document. Each author entry in the index
contains the pages where these citations occur. Alternatively,
the package can list the labels of the citations that appear in
the references rather than the text pages. The package relies
on BibTeX being used to handle citations. Additionally, it
requires Perl (version 5 or higher).

%package -n %{shortname}-autosp
Provides: tex-autosp = %{epoch}:%{source_date}-%{release}
Provides: texlive-autosp-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-autosp-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-autosp-bin < 7:20170520
Provides: tex-autosp-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-autosp-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-autosp-doc < 7:20170520
License: GPLv2
Summary: A Preprocessor that generates note-spacing commands for MusiXTeX scores
Requires: texlive-base

%description -n %{shortname}-autosp
This program simplifies the creation of MusiXTeX scores by
converting (non-standard) commands of the form \anotes ... \en
into one or more conventional note-spacing commands, as
determined by the note values themselves, with \sk spacing
commands inserted as necessary. The coding for an entire
measure can be entered one part at a time, without concern for
note-spacing changes within the part or spacing requirements of
other parts. For example, \anotes\qa J\qa K&\ca l\qa m\ca n\en
generates \Notes\qa J\sk\qa K\sk&\ca l\qa m\sk\ca n\en .

%package -n %{shortname}-axodraw2
Provides: tex-axodraw2 = %{epoch}:%{source_date}-%{release}
Provides: texlive-axodraw2-bin = %{epoch}:%{source_date}-%{release}
License: GPLv3
Summary: Feynman diagrams in a LaTeX document
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(axodraw2.sty) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-axodraw2
This package defines macros for drawing Feynman graphs in LaTeX
documents. It is an important update of the axodraw package,
but since it is not completely backwards compatible, we have
given the style file a changed name. Many new features have
been added, with new types of line, and much more flexibility
in their properties. In addition, it is now possible to use
axodraw2 with pdfLaTeX, as well as with the LaTeX-dvips method.
However with pdfLaTeX (and also LuaLaTeX and XeLaTeX), an
external program, axohelp, is used to perform the geometrical
calculations needed for the pdf code inserted in the output
file. The processing involves a run of pdfLaTeX, a run of
axohelp, and then another run of pdfLaTeX.

%package -n %{shortname}-bib2gls
Provides: tex-bib2gls = %{epoch}:%{source_date}-%{release}
Provides: texlive-bib2gls-bin = %{epoch}:%{source_date}-%{release}
License: GPLv3+
Summary: Convert .bib files to glossaries-extra.sty resource files
Requires: texlive-base
# Java and shell
BuildArch: noarch

%description -n %{shortname}-bib2gls
This Java command line application may be used to extract
glossary information stored in a .bib file and convert it into
glossary entry definition commands. This application should be
used with glossaries-extra.sty's 'record' package option. It
performs two functions in one: selects entries according to
records found in the .aux file (similar to bibtex),
hierarchically sorts entries and collates location lists
(similar to makeindex or xindy). The glossary entries can then
be managed in a system such as JabRef, and only the entries
that are actually required will be defined, reducing the
resources required by TeX. The supplementary application
convertgls2bib can be used to convert existing .tex files
containing definitions (\newglossaryentry etc.) to the .bib
format required by bib2gls.

%package -n %{shortname}-bibexport
Provides: tex-bibexport = %{epoch}:%{source_date}-%{release}
Provides: texlive-bibexport-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-bibexport-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-bibexport-bin < 7:20170520
Provides: tex-bibexport-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-bibexport-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-bibexport-doc < 7:20170520
License: LPPL 1.3
Summary: Extract a BibTeX file based on a .aux file
Requires: texlive-base
Requires: texlive-kpathsea
BuildArch: noarch

%description -n %{shortname}-bibexport
A Bourne shell script that uses BibTeX to extract bibliography
entries that are \cite'd in a document. It can also expand a
BibTeX file, expanding the abbreviations (other than the built-
in ones like month names) and followig the cross-references.

%package -n %{shortname}-bibtex
Provides: tex-bibtex = %{epoch}:%{source_date}-%{release}
Provides: texlive-bibtex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-bibtex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-bibtex-bin < 7:20170520
Provides: tex-bibtex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-bibtex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-bibtex-doc < 7:20170520
License: Knuth
Summary: Process bibliographies for LaTeX, etc
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(apalike.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(apalike.tex) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-bibtex
BibTeX allows the user to store his citation data in generic
form, while printing citations in a document in the form
specified by a BibTeX style, to be specified in the document
itself (one often needs a LaTeX citation-style package, such as
natbib as well). BibTeX itself is an ASCII-only program; there
is, however, a version that copes with 8-bit character sets.
However, BibTeX's facilities rapidly run out as one moves away
from simple ASCII (for example, in the various national sorting
rules for languages expressed in different parts of ISO-8859 --
the "ISO Latin" series). For more flexibility, the user is
urged to consider using biber with biblatex to typeset its
output. In fact, it is best to avoid BibTeX in favour of biber
and biblatex, if at all possible.

%package -n %{shortname}-bibtexu
Provides: tex-bibtexu = %{epoch}:%{source_date}-%{release}
Provides: texlive-bibtexu-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-bibtexu-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-bibtexu-bin < 7:20170520
Provides: tex-bibtexu-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-bibtexu-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-bibtexu-doc < 7:20170520
License: LPPL
Summary: bibtexu package
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-bibtexu
bibtexu package.

%package -n %{shortname}-bibtex8
Provides: tex-bibtex8 = %{epoch}:%{source_date}-%{release}
Provides: texlive-bibtex8-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-bibtex8-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-bibtex8-bin < 7:20170520
Provides: tex-bibtex8-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-bibtex8-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-bibtex8-doc < 7:20170520
License: GPL+
Summary: A fully 8-bit adaptation of BibTeX 0.99
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-bibtex8
An enhanced, portable C version of BibTeX. Enhanced by
conversion to "big" (32-bit) capacity, addition of run-time
selectable capacity and 8-bit support extensions. National
character set and sorting order are controlled by an external
configuration file. Various examples are included.

%package -n %{shortname}-bundledoc
Provides: tex-bundledoc = %{epoch}:%{source_date}-%{release}
Provides: texlive-bundledoc-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-bundledoc-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-bundledoc-bin < 7:20170520
Provides: tex-bundledoc-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-bundledoc-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-bundledoc-doc < 7:20170520
License: LPPL
Summary: Bundle together all the files needed to build a LaTeX document
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(miktex.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(texlive-unix-arlatex.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(texlive-unix.cfg) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-bundledoc
The bundledoc package is a post-processor for the snapshot
package that bundles together all the classes, packages and
files needed to build a given LaTeX document. It reads the .dep
file that snapshot produces, finds each of the files mentioned
therein, and archives them into a single .tar.gz (or .zip, or
whatever) file, suitable for moving across systems,
transmitting to a colleague, etc. A script, arlatex, provides
an alternative "archiving" mechanism, creating a single LaTeX
file that contains all of the ancillary files of a LaTeX
document, together with the document itself, using the
filecontents* environment.

%package -n %{shortname}-cachepic
Provides: tex-cachepic = %{epoch}:%{source_date}-%{release}
Provides: texlive-cachepic-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-cachepic-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cachepic-bin < 7:20170520
Provides: tex-cachepic-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-cachepic-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cachepic-doc < 7:20170520
License: LPPL 1.3
Summary: Convert document fragments into graphics
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(graphicx.sty)
Requires: tex(verbatim.sty)
Provides: tex(cachepic.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(prcachepic.def) = %{epoch}:%{source_date}-%{release}
# lua
BuildArch: noarch

%description -n %{shortname}-cachepic
The bundle simplifies and automates conversion of document
fragments into external EPS or PDF files. The bundle consists
of two parts: a LaTeX package that implements a document level
interface, and a command line tool (written in lua) that
generates the external graphics.

%package -n %{shortname}-checkcites
Provides: tex-checkcites = %{epoch}:%{source_date}-%{release}
Provides: texlive-checkcites-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-checkcites-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-checkcites-bin < 7:20170520
Provides: tex-checkcites-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-checkcites-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-checkcites-doc < 7:20170520
License: LPPL 1.3
Summary: Check citation commands in a document
Requires: texlive-base
Requires: texlive-kpathsea
# lua script
BuildArch: noarch

%description -n %{shortname}-checkcites
The package provides a lua script written for the sole purpose
of detecting undefined and unused references from LaTeX
auxiliary or bibliography files.

%package -n %{shortname}-checklistings
Provides: tex-checklistings = %{epoch}:%{source_date}-%{release}
Provides: texlive-checklistings-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-checklistings-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-checklistings-bin < 7:20170520
Provides: tex-checklistings-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-checklistings-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-checklistings-doc < 7:20170520
License: LPPL 1.2
Summary: Pass verbatim contents through a compiler and reincorporate the resulting output
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(keyval.sty)
Requires: tex(kvoptions.sty)
Requires: tex(fancyvrb.sty)
Requires: tex(color.sty)
Requires: tex(listings.sty)
Provides: tex(checklistings.sty) = %{epoch}:%{source_date}-%{release}
# shell script
BuildArch: noarch

%description -n %{shortname}-checklistings
This package augments the fancyvrb and listings packages to
allow the source code they contain to be checked by an external
tool (like a compiler). The external tool's messages can be
automatically reincorporated into the original document. The
package does not focus on a specific programming language, but
it is designed to work well with languages and compilers in the
ML family.

%package -n %{shortname}-chklref
Provides: tex-chklref = %{epoch}:%{source_date}-%{release}
License: GPLv3
Summary: Check for problems with labels in LaTeX
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(chklref.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-chklref
It is quite common that after modifying a TeX file, many unused
labels remain in it. The purpose of chklref is to automatically
find these useless labels. It also looks for "non starred"
mathematical environments with no labels and advises the user
to use a starred version instead.

%package -n %{shortname}-chktex
Provides: tex-chktex = %{epoch}:%{source_date}-%{release}
Provides: texlive-chktex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-chktex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-chktex-bin < 7:20170520
Provides: tex-chktex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-chktex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-chktex-doc < 7:20170520
License: GPL+
Summary: Check for errors in LaTeX documents
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-chktex
The program reports typographic and other errors in LaTeX
documents. Filters are also provided for checking the LaTeX
parts of CWEB documents.

%if 0
%package -n %{shortname}-cjk-gs-integrate
Provides: tex-cjk-gs-integrate = %{epoch}:%{source_date}-%{release}
Provides: texlive-cjk-gs-integrate-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-cjk-gs-integrate-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cjk-gs-integrate-bin < 7:20170520
Provides: tex-cjk-gs-integrate-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-cjk-gs-integrate-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cjk-gs-integrate-doc < 7:20170520
License: GPLv3+
Summary: Tools to integrate CJK fonts into Ghostscript
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-cjk-gs-integrate
This script searches a list of directories for CJK fonts, and
makes them available to an installed GhostScript. In the
simplest case with sufficient privileges, a run without
arguments should effect in a complete setup of GhostScript.
%endif

%package -n %{shortname}-cjkutils
Provides: tex-cjkutils = %{epoch}:%{source_date}-%{release}
Provides: texlive-cjkutils-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-cjkutils-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cjkutils-bin < 7:20170520
License: LPPL
Summary: cjkutils package
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(b5ka12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(b5kr12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(b5so12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(c1so12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(c2so12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(c3so12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(c4so12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(c5so12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(c6so12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(c7so12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(csso12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(gsfs14.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(j2so12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(jsso12.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(ksso17.cfg) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-cjkutils
cjkutils package.

%package -n %{shortname}-clojure-pamphlet
Provides: tex-clojure-pamphlet = %{epoch}:%{source_date}-%{release}
Provides: texlive-clojure-pamphlet-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-clojure-pamphlet-bin = %{epoch}:%{source_date}-%{release}
License: GPLv3+
Summary: A simple literate programming tool based on clojure's pamphlet system
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(clojure-pamphlet.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-clojure-pamphlet
The Clojure pamphlet system is a system based on the Clojure
literate system. In the Clojure's pamphlet system you have your
main LaTeX file, which can be compiled regularly. This file
contains documentation and source code (just like in other
forms of literate programming). These code snippets are wrapped
in the chunk environment, hence they can be recognized by the
tangler in order to extract them. Chunks can be included inside
each other by the getchunk command (which will be typesetted
accordingly). Finally, the LaTeX file will be run through the
tangler to get the desired chunk of code.

%package -n %{shortname}-cluttex
Provides: tex-cluttex = %{epoch}:%{source_date}-%{release}
Provides: texlive-cluttex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-cluttex-bin = %{epoch}:%{source_date}-%{release}
License: GPLv3
Summary: An automation tool for running LaTeX
Requires: texlive-base
Requires: texlive-kpathsea
# lua
BuildArch: noarch

%description -n %{shortname}-cluttex
This is another tool for the automation of LaTeX document
processing, like latexmk or arara. The main feature of this
tool is that it does not clutter your working directory with
.aux or .log or other auxiliary files. It has of course the
usual features of automation tools: It automatically re-runs
(La)TeX for cross-references. MakeIndex, BibTeX, Biber, or
makeglossaries will be executed if a corresponding option is
set. Furthermore, cluttex can watch input files for changes
(using an external program).

%package -n %{shortname}-context
Provides: tex-context = %{epoch}:%{source_date}-%{release}
Provides: texlive-context-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-context-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-context-bin < 7:20170520
Provides: tex-context-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-context-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-context-doc < 7:20170520
License: GPL+ or LPPL
Summary: The ConTeXt macro package
Requires: texlive-base
Requires: texlive-kpathsea
# for /usr/bin/realpath
Requires: coreutils
Requires(post,postun): coreutils
Requires: texlive-metapost
%if %{without bootstrap}
Requires: texlive-pdftex
Requires: texlive-xetex
%endif
Requires: texlive-luatex
Requires: texlive-lm
Requires: texlive-lm-math
Requires: texlive-amsfonts
Requires: texlive-manfnt-font
Requires: texlive-mflogo-font
Requires: texlive-stmaryrd
Requires: texlive-mptopdf
Requires: ruby
Requires: tex(pstricks.sty)
Requires: tex(pst-plot.sty)
Provides: tex(notepad++.ini) = %{epoch}:%{source_date}-%{release}
Provides: tex(texworks-setup.ini) = %{epoch}:%{source_date}-%{release}
Provides: tex(tools.ini) = %{epoch}:%{source_date}-%{release}
Provides: tex(TeXworks.ini) = %{epoch}:%{source_date}-%{release}
Provides: tex(scite-context-readme.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(type-buy.dat) = %{epoch}:%{source_date}-%{release}
Provides: tex(type-fsf.dat) = %{epoch}:%{source_date}-%{release}
Provides: tex(type-ghz.dat) = %{epoch}:%{source_date}-%{release}
Provides: tex(type-tmf.dat) = %{epoch}:%{source_date}-%{release}
Provides: tex(contnav.afm) = %{epoch}:%{source_date}-%{release}
Provides: tex(cmin.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(cmit.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(cmitt.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(cmrm.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(cmsc.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(cmtt.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(ec-2004.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-8r.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(teff-trinite.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(contnav.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(8r-base.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(ec-base.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(ec-os-public-lm.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(mkiv-base.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(mkiv-px.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(mkiv-tx.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-adobe-euro.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-ams-base.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-ams-cmr.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-ams-euler.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-base.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-context-symbol.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-dummy.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-empty.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-micropress-informal.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-public-csr.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-public-lm.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-public-plr.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-public-vnr.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-vogel-symbol.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-wasy.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-youngryu-px.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(original-youngryu-tx.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(qx-base.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(qx-os-public-lm.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(t5-base.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(t5-os-public-lm.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(texnansi-base.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(texnansi-os-public-lm.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(tlig.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(contnav.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(contnav.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(bidi-symbols.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(demo-symbols.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(export-example.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-cweb.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-datastrc.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-educat.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-format.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-layout.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-narrowtt.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-newmat.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-pictex.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-streams.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-subsub.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(metatex.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-arrange.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-combine.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-common.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-copy.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-ideas.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-listing.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-markdown.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-precache.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-select.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-sql.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-timing.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtx-context-xml.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-abr-01.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-abr-02.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-abr-03.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-abr-04.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-cdr-01.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-faq-00.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-faq-01.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-faq-02.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-faq-03.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-mag-01.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-00.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-01.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-02.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-03.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-04.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-05.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-06.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-07.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-08.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-09.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-10.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-11.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-12.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-13.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-14.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-15.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-16.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-18.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-19.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-22.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-23.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-26.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-27.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-50.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-61.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-62.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-63.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-64.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-66.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-67.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-68.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-93.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-pre-96.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(s-ptj-01.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(status-mkiv.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(supp-mis.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(supp-mpe.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(supp-pdf.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(x-dir-01.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(bibl-ams.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(bibl-apa-de.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(bibl-apa-fr.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(bibl-apa-it.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(bibl-apa.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(bibl-aps.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(bibl-num-fr.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(bibl-num.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(bibl-ssa.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mag-0000.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(setup-qr.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(aesop-de.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(bryson.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cervantes-es.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(darwin.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(davis.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(dawkins.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(demo-mps.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(demo-tex.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(demo-xml.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(douglas.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(hawking.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(khatt-ar.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(khatt-en.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(knuth.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(linden.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lorem.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(materie.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(montgomery.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(quevedo-es.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(reich.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(sample.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(samples.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(thuan.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(tufte.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(ward.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(weisman.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(zapf.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(context-test.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatex-basics.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatex-fonts.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatex-languages.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatex-math.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatex-mplib.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatex-plain.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatex-preprocessor-test.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatex-preprocessor.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatex-swiglib-test.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatex-swiglib.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatex-test.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-ch-de.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-ch-en.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-ch-nl.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-ch-de.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-ch-en.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-ch-nl.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(m-pictex.sty) = %{epoch}:%{source_date}-%{release}
# shell and lua
BuildArch: noarch

%description -n %{shortname}-context
A full featured, parameter driven macro package, which fully
supports advanced interactive documents. See the ConTeXt garden
for a wealth of support information.

%package -n %{shortname}-context-doc
Requires: texlive-context
Provides: tex-context-doc = %{epoch}:%{source_date}-%{release}
Summary: Documentation for context
License: GPL+ or LPPL

%description -n %{shortname}-context-doc
Documentation for context.

%package -n %{shortname}-convbkmk
Provides: tex-convbkmk = %{epoch}:%{source_date}-%{release}
Provides: texlive-convbkmk-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-convbkmk-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-convbkmk-bin < 7:20170520
Provides: tex-convbkmk-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-convbkmk-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-convbkmk-doc < 7:20170520
License: MIT
Summary: Correct platex/uplatex bookmarks in PDF created with hyperref
Requires: texlive-base
Requires: texlive-kpathsea
Requires: ruby
# ruby script
BuildArch: noarch

%description -n %{shortname}-convbkmk
The package provides a small Ruby script that corrects
bookmarks in PDF files created by platex/uplatex, using
hyperref.

%package -n %{shortname}-crossrefware
Provides: tex-crossrefware = %{epoch}:%{source_date}-%{release}
Provides: texlive-crossrefware-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-crossrefware-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-crossrefware-bin < 7:20170520
Provides: tex-crossrefware-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-crossrefware-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-crossrefware-doc < 7:20170520
License: GPL+
Summary: Scripts for working with crossref.org
# Just perl.
BuildArch: noarch

%description -n %{shortname}-crossrefware
This bundle contains the following scripts: bibdoiadd.pl: add
DOI numbers to papers in a given bib file, bibzbladd.pl: add
Zbl numbers to papers in a given bib file, ltx2crossrefxml.pl:
a tool for the creation of XML files for submitting to the
parent site

%package -n %{shortname}-cslatex
Provides: tex-cslatex = %{epoch}:%{source_date}-%{release}
Provides: texlive-cslatex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-cslatex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cslatex-bin < 7:20170520
License: GPL+
Summary: LaTeX support for Czech/Slovak typesetting
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-latex
Requires: texlive-cm
Requires: texlive-csplain
Requires: texlive-hyphen-base
Requires: texlive-latex-fonts
Requires: texlive-tex-ini-files
Requires(post,postun): coreutils
Requires: tex(czech.ldf)
Requires: tex(slovak.ldf)
Provides: tex(czech.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(fonttext.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(hyphen.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2cmdh.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2cmfib.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2cmfr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2cmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2cmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2cmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2cmvtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2enc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2lcmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2lcmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(slovak.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(cspsfont.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2pag.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2pbk.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2pcr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2phv.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2phvn.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2pnc.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2ppl.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2ptm.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2pzc.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(nhelvet.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ntimes.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(xl2pag.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(xl2pbk.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(xl2pcr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(xl2phv.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(xl2phvn.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(xl2pnc.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(xl2ppl.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(xl2ptm.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(xl2pzc.fd) = %{epoch}:%{source_date}-%{release}
# symlinks
BuildArch: noarch

%description -n %{shortname}-cslatex
LaTeX support for Czech/Slovak typesetting

%package -n %{shortname}-csplain
Provides: tex-csplain = %{epoch}:%{source_date}-%{release}
Provides: texlive-csplain-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-csplain-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-csplain-bin < 7:20170520
License: GPLv2+
Summary: Plain TeX multilanguage support
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-tex
Requires: texlive-cm
Requires(post,postun): coreutils
Requires: texlive-cs
Requires: texlive-hyphen-base
Requires: texlive-plain
Requires: texlive-enctex
Requires: texlive-tex-ini-files
Requires: texlive-luatex
Requires: texlive-luatex85
Provides: tex(csenc-k.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(csenc-p.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(csenc-u.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(csenc-w.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(csfonts.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(csfontsm.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(czhyphen.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(extcode.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(fonttabs.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(il2code.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(plaina4.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(skhyphen.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1code.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1enc-u.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(ucode.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(uni-lcuc.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(ams-math.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cavantga.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cbookman.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(chars-8z.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(chelvet.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cncent.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cpalatin.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-adventor.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-all.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-antt.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-arev.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-bera.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-bonum.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-charter.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-cursor.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-heros.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-pagella.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-polta.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-schola.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cs-termes.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(ctimes.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(cyrchars.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(dcfonts.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(ecfonts.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(exchars.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lmfonts.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luafonts.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(ntx-math.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(tx-math.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(unifam.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(opmac-bib-iso690.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(opmac-bib-simple.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(opmac-bib.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(opmac-xetex.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(opmac.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfuni.tex) = %{epoch}:%{source_date}-%{release}
# symlinks
BuildArch: noarch

%description -n %{shortname}-csplain
CSplain is a small extension of basic Plain TeX macros, the
formats csplain and pdfcsplain can be generated. It supports:
hyphenation of words for 50+ languages, simple and powerfull
font loading system (various sizes of fonts), tex, pdftex,
xetex and luatex engines, math fonts simply loaded with full
amstex-like features, three internal encodings (IL2 for
Czech/Slovak languages, T1 for many languages with latin
alphabet and Unicode in new TeX engines), natural UTF-8 input
in pdfTeX using encTeX without any active characters, Czech and
Slovak special typesetting features. An important part of the
package is OPmac, which implements most of LaTeX's features
(sectioning, font selection, color, hyper reference and urls,
bibliography, index, toc, tables,etc.) by Plain TeX macros. The
OPmac macros can generate and bibliography without any external
program.

%package -n %{shortname}-ctan-o-mat
Provides: tex-ctan-o-mat = %{epoch}:%{source_date}-%{release}
Provides: texlive-ctan-o-mat-bin = %{epoch}:%{source_date}-%{release}
License: BSD
Summary: Upload or validate a package for CTAN
Requires: texlive-base
Requires: texlive-kpathsea
Requires: perl-interpreter
#perl
BuildArch: noarch

%description -n %{shortname}-ctan-o-mat
This program can be used to automate the upload of a package to
CTAN. The description of the package is contained in a
configuration file. The provided information is validated in
any case. If the validation succeeds and not only the
validation is requested, then the provided archive file will be
placed in the incoming area of the CTAN for further processing
by the CTAN team. In any case any finding during the validation
is reported at the end of the processing. Note that the
validation is the default and an official submission has to be
requested by an appropriate command line option. ctan-o-mat
requires an Internet connection to the CTAN server. Even the
validation retrieves the known attributes and the basic
constraints from the server.

%package -n %{shortname}-ctanbib
Provides: tex-ctanbib = %{epoch}:%{source_date}-%{release}
Provides: texlive-ctanbib-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-ctanbib-bin = %{epoch}:%{source_date}-%{release}
License: LPPL
Summary: Export ctan entries to bib format
Requires: texlive-base
Requires: texlive-kpathsea
#lua
BuildArch: noarch

%description -n %{shortname}-ctanbib
This script can generate BibTeX records for LaTeX packages hosted on CTAN.

%package -n %{shortname}-ctanify
Provides: tex-ctanify = %{epoch}:%{source_date}-%{release}
Provides: texlive-ctanify-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-ctanify-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ctanify-bin < 7:20170520
Provides: tex-ctanify-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-ctanify-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ctanify-doc < 7:20170520
License: LPPL 1.3
Summary: Prepare a package for upload to CTAN
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-ctanify
Given a list of filenames, ctanify creates a tarball (a .tar.gz
file) with the files laid out in CTAN's preferred structure.
The tarball additionally contains a ZIP (.zip) file with copies
of all files laid out in the standard TeX Directory Structure
(TDS), which may be used by those intending to install the
package, or by those who need to incorporate it in a
distribution. (The TDS ZIP file will be installed in the CTAN
install/ tree.)

%package -n %{shortname}-ctanupload
Provides: tex-ctanupload = %{epoch}:%{source_date}-%{release}
Provides: texlive-ctanupload-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-ctanupload-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ctanupload-bin < 7:20170520
Provides: tex-ctanupload-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-ctanupload-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ctanupload-doc < 7:20170520
License: GPLv3+
Summary: Support for users uploading to CTAN
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-ctanupload
The package provides a Perl script that allows the uploads of a
contribution to CTAN from the command line. The aim is to
simplify the release process for LaTeX package authors.

%package -n %{shortname}-ctie
Provides: tex-ctie = %{epoch}:%{source_date}-%{release}
Provides: texlive-ctie-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-ctie-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ctie-bin < 7:20170520
License: GPL+
Summary: C version of tie (merging Web change files)
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-ctie
This is a version of tie converted for use with cweb.

%package -n %{shortname}-cweb
Provides: tex-cweb = %{epoch}:%{source_date}-%{release}
Provides: texlive-cweb-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-cweb-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cweb-bin < 7:20170520
Provides: tex-cweb-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-cweb-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cweb-doc < 7:20170520
License: Knuth
Summary: A Web system in C
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(cwebmac.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfXcwebmac.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfcwebmac.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfdcwebmac.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdffcwebmac.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdficwebmac.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfwebmac.tex) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-cweb
The Cweb system is a system for Structured Software
Documentation (also known as Literate Programming) in the
programming language C.

%package -n %{shortname}-cyrillic
Provides: tex-cyrillic = %{epoch}:%{source_date}-%{release}
Provides: texlive-cyrillic-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-cyrillic-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cyrillic-bin < 7:20170520
Provides: tex-cyrillic-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-cyrillic-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cyrillic-doc < 7:20170520
Provides: texlive-cyrillic-bin-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-cyrillic-bin-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-cyrillic-bin-bin < 7:20170520
License: LPPL 1.3
Summary: Support for Cyrillic fonts in LaTeX
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(fontenc.sty)
Provides: tex(cp1251.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp855.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp866.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp866av.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp866mav.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp866nav.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp866tat.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(ctt.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(dbk.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(iso88595.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(isoir111.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(koi8-r.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(koi8-ru.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(koi8-u.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcy.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcyccr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcycmbr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcycmdh.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcycmfib.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcycmfr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcycmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcycmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcycmtl.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcycmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcycmvtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcydefs.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcyenc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcylcmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(lcylcmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(maccyr.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(macukr.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(mik.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(mls.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(mnk.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(mos.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(ncc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2ccr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2cmbr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2cmdh.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2cmfib.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2cmfr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2cmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2cmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2cmtl.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2cmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2cmvtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2enc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2lcmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2lcmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2wlcyr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2wlcyss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2wncyr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot2wncyss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(pt154.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(pt254.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2accr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2acmbr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2acmdh.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2acmfib.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2acmfr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2acmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2acmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2acmtl.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2acmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2acmvtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2aenc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2alcmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2alcmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2bccr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2bcmbr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2bcmdh.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2bcmfib.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2bcmfr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2bcmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2bcmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2bcmtl.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2bcmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2bcmvtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2benc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2blcmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2blcmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2cccr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2ccmbr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2ccmdh.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2ccmfib.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2ccmfr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2ccmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2ccmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2ccmtl.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2ccmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2ccmvtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2cenc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2clcmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t2clcmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2ccr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2cmbr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2cmdh.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2cmfib.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2cmfr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2cmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2cmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2cmtl.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2cmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2cmvtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2enc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2lcmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(x2lcmtt.fd) = %{epoch}:%{source_date}-%{release}
# shell
BuildArch: noarch

%description -n %{shortname}-cyrillic
This bundle of macros files provides macro support (including
font encoding macros) for the use of Cyrillic characters in
fonts encoded under the T2* and X2 encodings. These encodings
cover (between them) pretty much every language that is written
in a Cyrillic alphabet.

%package -n %{shortname}-de-macro
Provides: tex-de-macro = %{epoch}:%{source_date}-%{release}
Provides: texlive-de-macro-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-de-macro-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-de-macro-bin < 7:20170520
Provides: tex-de-macro-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-de-macro-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-de-macro-doc < 7:20170520
License: AFL
Summary: Expand private macros in a document
Requires: texlive-base
Requires: texlive-kpathsea
# python
BuildArch: noarch

%description -n %{shortname}-de-macro
De-macro is a Python script that helps authors who like to use
private LaTeX macros (for example, as abbreviations). A
technical editor or a cooperating author may balk at such a
manuscript; you can avoid manuscript rejection misery by
running de-macro on it. De-macro will expand macros defined in
\(re)newcommand or \(re)newenvironment commands, within the
document, or in the document's "private" package file.

%package -n %{shortname}-detex
Provides: tex-detex = %{epoch}:%{source_date}-%{release}
Provides: texlive-detex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-detex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-detex-bin < 7:20170520
License: NCSA
Summary: Strip TeX from a source file
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-detex
Detex is a program to remove TeX constructs from a text file.
It recognizes the \input command. The program assumes it is
dealing with LaTeX input if it sees the string \begin{document}
in the text. In this case, it also recognizes the \include and
\includeonly commands.

%package -n %{shortname}-diadia
Provides: tex-diadia = %{epoch}:%{source_date}-%{release}
Provides: texlive-diadia-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-diadia-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-diadia-bin < 7:20170520
Provides: tex-diadia-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-diadia-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-diadia-doc < 7:20170520
License: LPPL
Summary: Package to keep a diabetes diary
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(xkeyval.sty)
Requires: tex(pgfplots.sty)
Requires: tex(pgfplotstable.sty)
Requires: tex(pgfcalendar.sty)
Requires: tex(tabularx.sty)
Requires: tex(booktabs.sty)
Requires: tex(colortbl.sty)
Requires: tex(ifthen.sty)
Requires: tex(calc.sty)
Requires: tex(translations.sty)
Requires: tex(amsmath.sty)
Requires: tex(tcolorbox.sty)
Requires: tex(environ.sty)
Requires: tex(multicol.sty)
Requires: tex(amssymb.sty)
Provides: tex(diadia.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(diadia.sty) = %{epoch}:%{source_date}-%{release}
# lua
BuildArch: noarch

%description -n %{shortname}-diadia
The diadia package allows you to keep a diabetes diary.
Usually, this means keeping record of certain medical values
like blood sugar, blood pressure, pulse or weight. It might
also include other medical, pharmaceutical or nutritional data
(HbA1c, insulin doses, carbohydrate units). The diadia package
supports all of this plus more - simply by adding more columns
to the data file! It is able to evaluate the data file and
typesets formatted tables and derived plots. Furthermore, it
supports medication charts and info boxes. Supported languages:
English, German. Feel free to provide other translation files!

%package -n %{shortname}-dosepsbin
Provides: tex-dosepsbin = %{epoch}:%{source_date}-%{release}
Provides: texlive-dosepsbin-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dosepsbin-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dosepsbin-bin < 7:20170520
Provides: tex-dosepsbin-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-dosepsbin-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dosepsbin-doc < 7:20170520
License: GPLv2 or Artistic
Summary: Deal with DOS binary EPS files
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-dosepsbin
A Encapsulated PostScript (EPS) file may given in a special
binary format to support the inclusion of a thumbnail. This
file format, commonly known as DOS EPS format starts with a
binary header that contains the positions of the possible
sections: Postscript (PS); Windows Metafile Format (WMF); and
Tag Image File Format (TIFF). The PS section must be present
and either the WMF file or the TIFF file should be given. The
package provides a Perl program that will extract any of the
sections of such a file, in particular providing a 'text'-form
EPS file for use with (La)TeX.

%package -n %{shortname}-dtl
Provides: tex-dtl = %{epoch}:%{source_date}-%{release}
Provides: texlive-dtl-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dtl-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dtl-bin < 7:20170520
License: Public Domain
Summary: Tools to dis-assemble and re-assemble DVI files
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-dtl
DTL (DVI Text Language) is a means of expressing the content of
a DVI file, which is readily readable by humans. The DTL bundle
contains an assembler dt2dv (which produces DVI files from DTL
files) and a disassembler dv2dt (which produces DTL files from
DVI files). The DTL bundle was developed so as to avoid some
infelicities of dvitype (among other pressing reasons).

%package -n %{shortname}-dtxgen
Provides: tex-dtxgen = %{epoch}:%{source_date}-%{release}
Provides: texlive-dtxgen-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dtxgen-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dtxgen-bin < 7:20170520
Provides: tex-dtxgen-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-dtxgen-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dtxgen-doc < 7:20170520
License: GPL+
Summary: Creates a template for a self-extracting .dtx file
Requires: texlive-base
Requires: texlive-kpathsea
# bash
BuildArch: noarch

%description -n %{shortname}-dtxgen
The bash script dtxgen creates a template for a self-extracting
.dtx file. It is useful for those who plan to create a new
Documented LaTeX Source (.dtx) file.

%package -n %{shortname}-dvi2tty
Provides: tex-dvi2tty = %{epoch}:%{source_date}-%{release}
Provides: texlive-dvi2tty-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dvi2tty-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dvi2tty-bin < 7:20170520
License: GPL+
Summary: Produce ASCII from DVI
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-dvi2tty
A DVI driver to produce an ASCII representation of the
document. The original version was written in Pascal, and the
present author translated the program to C.

%package -n %{shortname}-dviasm
Provides: tex-dviasm = %{epoch}:%{source_date}-%{release}
Provides: texlive-dviasm-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dviasm-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dviasm-bin < 7:20170520
Provides: tex-dviasm-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-dviasm-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dviasm-doc < 7:20170520
License: GPLv3+
Summary: A utility for editing DVI files
Requires: texlive-base
Requires: texlive-kpathsea
# python
BuildArch: noarch

%description -n %{shortname}-dviasm
A Python script to support changing or creating DVI files via
disassembling into text, editing, and then reassembling into
binary format. It supports advanced features such as adding a
preprint number or watermarks.

%package -n %{shortname}-dvicopy
Provides: tex-dvicopy = %{epoch}:%{source_date}-%{release}
Provides: texlive-dvicopy-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dvicopy-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dvicopy-bin < 7:20170520
License: GPL+
Summary: Copy DVI files, flattening VFs
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-dvicopy
DVICOPY is a utility program that allows one to take a DVI file
that references composite fonts (VF) and convert it into a DVI
file that does not contain such references. It also serves as a
basis for writing DVI drivers (much like DVItype).

%package -n %{shortname}-dvidvi
Provides: tex-dvidvi = %{epoch}:%{source_date}-%{release}
Provides: texlive-dvidvi-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dvidvi-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dvidvi-bin < 7:20170520
License: Copyright only
Summary: Convert one DVI file into another
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-dvidvi
The output DVI file's contents are specified by page selection
commands; series of pages and page number ranges may be
specified, as well as inclusions and exclusions.

%package -n %{shortname}-dviinfox
Provides: tex-dviinfox = %{epoch}:%{source_date}-%{release}
Provides: texlive-dviinfox-bin = %{epoch}:%{source_date}-%{release}
License: MIT
Summary: Perl script to print DVI meta information
# perl
BuildArch: noarch
Requires: texlive-base
Requires: texlive-kpathsea
Requires: perl-interpreter

%description -n %{shortname}-dviinfox
The package provides a perl script which prints information
about a DVI file. It also supports XeTeX XDV format.

%package -n %{shortname}-dviljk
Provides: tex-dviljk = %{epoch}:%{source_date}-%{release}
Provides: texlive-dviljk-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dviljk-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dviljk-bin < 7:20170520
License: GPL+
Summary: DVI to Laserjet output
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-dviljk
A dvi driver for the LaserJet printers, using kpathsea
recursive file searching.

%package -n %{shortname}-dviout-util
Provides: tex-dviout-util = %{epoch}:%{source_date}-%{release}
Provides: texlive-dviout-util-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dviout-util-bin = %{epoch}:%{source_date}-%{release}
License: MIT
Summary: DVI output utilities
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-dviout-util
This is a partial repackaging of elements of the DVIOUT package
by Toshio OSHIMA, Yoshiki OTOBE, and Kazunori ASAYAMA.
Here we don't include the main DVI previewer, but just want small utility
programs.

%package -n %{shortname}-dvipdfmx
Provides: tex-dvipdfmx = %{epoch}:%{source_date}-%{release}
Provides: texlive-dvipdfmx-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dvipdfmx-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dvipdfmx-bin < 7:20170520
Provides: tex-dvipdfmx-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-dvipdfmx-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dvipdfmx-doc < 7:20170520
Provides: dvipdfmx = %{epoch}:%{source_date}-%{release}
Provides: dvipdfm = %{epoch}:%{source_date}-%{release}
License: GPL+
Summary: An extended version of dvipdfm
Requires: texlive-base
Requires: texlive-glyphlist
Requires: texlive-kpathsea
Requires: texlive-xetex
Provides: tex(dvipdfmx.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(cid-x.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(ckx.map) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-dvipdfmx
Dvipdfmx (formerly dvipdfm-cjk) is a development of dvipdfm
created to support multi-byte character encodings and large
character sets for East Asian languages. Dvipdfmx, if "called"
with the name dvipdfm, operates in a "dvipdfm compatibility"
mode, so that users of the both packages need only keep one
executable. A secondary design goal is to support as many "PDF"
features as does pdfTeX. There being no documentation as such,
users are advised to consult the documentation of dvipdfm (as
well, of course, as the package Readme.

%package -n %{shortname}-dvipng
Provides: tex-dvipng = %{epoch}:%{source_date}-%{release}
Provides: texlive-dvipng-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dvipng-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dvipng-bin < 7:20170520
Provides: tex-dvipng-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-dvipng-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dvipng-doc < 7:20170520
Provides: dvipng = %{epoch}:%{source_date}-%{release}
License: LGPLv2+
Summary: A fast DVI to PNG/GIF converter
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-dvipng
This program makes PNG and/or GIF graphics from DVI files as
obtained from TeX and its relatives. Its benefits include:
Speed. It offers very fast rendering of DVI as bitmap files,
which makes it suitable for generating large amounts of images
on-the-fly, as needed in preview-latex, WeBWorK and others; It
does not read the postamble, so it can be started before TeX
finishes. There is a --follow switch that makes dvipng wait at
end-of-file for further output, unless it finds the POST marker
that indicates the end of the DVI; Interactive query of
options. dvipng can read options interactively through stdin,
and all options are usable. It is even possible to change the
input file through this interface. Support for PK, VF,
PostScript Type1, and TrueType fonts, colour specials, and
inclusion of PostScript, PNG, JPEG or GIF images.

%package -n %{shortname}-dvipos
Provides: tex-dvipos = %{epoch}:%{source_date}-%{release}
Provides: texlive-dvipos-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dvipos-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dvipos-bin < 7:20170520
License: LPPL
Summary: dvipos package
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-dvipos
dvipos package.

%package -n %{shortname}-dvips
Provides: tetex-dvips = %{epoch}:%{source_date}-%{release}
Provides: tex-dvips = %{epoch}:%{source_date}-%{release}
Provides: texlive-dvips-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dvips-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dvips-bin < 7:20170520
Provides: tex-dvips-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-dvips-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dvips-doc < 7:20170520
License: GPL+
Summary: A DVI to PostScript driver
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(canonex.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(cx.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(deskjet.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(dfaxhigh.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvired.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(epson.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(ibmvga.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(ljfour.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(qms.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(toshiba.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(6w.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(7t.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(8a.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(8r.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(ad.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(ansinew.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(asex.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(asexp.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(dc.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvips.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(ec.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(extex.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(funky.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(odvips.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-cs-uni.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-ec-uni.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-l7x-uni.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-qx-uni.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-rm-uni.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-t2a-uni.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-t2b-uni.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-t2c-uni.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-t5-uni.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-texnansi-uni.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(q-ts1-uni.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(qx.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(stormex.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(tex256.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(texmext.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(texmital.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(texmsym.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(texnansx.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(blackdvi.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(blackdvi.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(colordvi.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(colordvi.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(rotate.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(rotate.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvips) = %{epoch}:%{source_date}-%{release}
Requires: texlive-latex-fonts

%description -n %{shortname}-dvips
This package has been withdrawn from CTAN, and bundled into the
distributions' package sets. The current sources of dvips may
be found in the distribution of dvipsk which forms part of the
TeX Live sources.

%package -n %{shortname}-dvisvgm
Provides: tex-dvisvgm = %{epoch}:%{source_date}-%{release}
Provides: texlive-dvisvgm-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-dvisvgm-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-dvisvgm-bin < 7:20170520
License: GPL+
Summary: Convert DVI files to Scalable Vector Graphics format (SVG)
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-dvisvgm
Dvisvgm is a command line utility that converts TeX DVI files
to the XML-based Scalable Vector Graphics (SVG) format. It
provides full font support including virtual fonts, font maps,
and sub-fonts. If necessary, dvisvgm vectorizes Metafont's
bitmap output in order to always create lossless scalable
output. The embedded SVG fonts can optionally be replaced with
graphics paths so that applications that don't support SVG
fonts are enabled to render the graphics properly. Besides many
other features, dvisvgm also supports color, emTeX, tpic, PDF
mapfile and PostScript specials.

%package -n %{shortname}-ebong
Provides: tex-ebong = %{epoch}:%{source_date}-%{release}
Provides: texlive-ebong-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-ebong-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ebong-bin < 7:20170520
Provides: tex-ebong-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-ebong-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ebong-doc < 7:20170520
License: Public Domain
Summary: Utility for writing Bengali in Rapid Roman Format
Requires: texlive-base
Requires: texlive-kpathsea
# python
BuildArch: noarch

%description -n %{shortname}-ebong
A tool (preprocessor) for writing your pRaa-ne-r ka-thaa in the
bengali langauage. It allows one to write the text in Rapid
Roman Bangla and convert it to the bangtex format by a python
program. All LaTeX markups are preserved in the target file.

%package -n %{shortname}-eplain
Provides: tex-eplain = %{epoch}:%{source_date}-%{release}
Provides: texlive-eplain-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-eplain-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-eplain-bin < 7:20170520
Provides: tex-eplain-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-eplain-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-eplain-doc < 7:20170520
License: GPLv2+
Summary: Extended plain TeX macros
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-pdftex
Requires: texlive-babel
Requires: texlive-cm
Requires: texlive-hyphen-base
Requires: texlive-latex-fonts
Requires: texlive-l3backend
Requires: texlive-l3kernel
Requires: texlive-l3packages
Requires: texlive-tex-ini-files
Requires: texlive-unicode-data
Requires: texlive-dehyph
Requires: texlive-hyph-utf8
Requires: texlive-knuth-lib
Requires(post,postun): coreutils
Provides: tex(arrow.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(btxmac.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(eplain.tex) = %{epoch}:%{source_date}-%{release}
# No actual binaries in here
BuildArch: noarch

%description -n %{shortname}-eplain
An extended version of the plain TeX format, adding support for
bibliographies, tables of contents, enumerated lists, verbatim
input of files, numbered equations, tables, two-column output,
footnotes, hyperlinks in PDF output and commutative diagrams.
Eplain can also load some of the more useful LaTeX packages,
notably graphics, graphicx (an extended of version of
graphics), color, autopict (a package instance of the LaTeX
picture code), psfrag, and url.

%package -n %{shortname}-epspdf
Provides: tex-epspdf = %{epoch}:%{source_date}-%{release}
Provides: texlive-epspdf-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-epspdf-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-epspdf-bin < 7:20170520
Provides: tex-epspdf-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-epspdf-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-epspdf-doc < 7:20170520
License: GPL+
Summary: Converter for PostScript, EPS and PDF
Requires: texlive-base
Requires: texlive-kpathsea
# tcl and lua
BuildArch: noarch

%description -n %{shortname}-epspdf
Epspdftk.tcl is a GUI ps/eps/pdf converter. Epspdf.tlu, its
command-line backend, can be used by itself. Options include
grayscaling, cropping margins and single-page selection. Some
conversion options are made possible by converting in multiple
steps.

%package -n %{shortname}-epstopdf
Provides: tex-epstopdf = %{epoch}:%{source_date}-%{release}
Provides: texlive-epstopdf-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-epstopdf-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-epstopdf-bin < 7:20170520
Provides: tex-epstopdf-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-epstopdf-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-epstopdf-doc < 7:20170520
License: BSD
Summary: Convert EPS to 'encapsulated' PDF using Ghostscript
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-epstopdf
Epstopdf is a Perl script that converts an EPS file to an
'encapsulated' PDF file (a single page file whose media box is
the same as the original EPS's bounding box). The resulting
file suitable for inclusion by PDFTeX as an image. The script
is adapted to run both on Windows and on Unix-alike systems.
The script makes use of Ghostscript for the actual conversion
to PDF. It assumes Ghostscript version 6.51 or later, and (by
default) suppresses its automatic rotation of pages where most
of the text is not horizontal. LaTeX users may make use of the
epstopdf package, which will run the epstopdf script "on the
fly", thus giving the illusion that PDFLaTeX is accepting EPS
graphic files.

%package -n %{shortname}-exceltex
Provides: tex-exceltex = %{epoch}:%{source_date}-%{release}
Provides: texlive-exceltex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-exceltex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-exceltex-bin < 7:20170520
Provides: tex-exceltex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-exceltex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-exceltex-doc < 7:20170520
License: GPL+
Summary: Get data from Excel files into LaTeX
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(ulem.sty)
Requires: tex(color.sty)
Provides: tex(exceltex.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-exceltex
Exceltex is a LaTeX package combined with a helper program
written in Perl. It provides an easy to use yet powerfull and
flexible way to get data from Spreadsheets into LaTeX. In
contrast to other solutions, exceltex does not seek to make the
creation of tables in LaTeX easier, but to get data from
Spreadsheets into LaTeX as easily as possible. The Excel (TM)
file format only acts as an interface between the spreadsheet
application and exceltex beacause it is easily accessible (via
the Spreadsheet::ParseExcel Perl module) and because most
spreadsheet applications are able to read and write Excel
files.

%package -n %{shortname}-fig4latex
Provides: tex-fig4latex = %{epoch}:%{source_date}-%{release}
Provides: texlive-fig4latex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-fig4latex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-fig4latex-bin < 7:20170520
Provides: tex-fig4latex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-fig4latex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-fig4latex-doc < 7:20170520
License: GPLv3+
Summary: Management of figures for large LaTeX documents
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-fig4latex
Fig4LaTeX simplifies management of the figures in a large LaTeX
document. Fig4LaTeX is appropriate for projects that include
figures with graphics created by XFig -- in particular,
graphics which use the combined PS/LaTeX (or PDF/LaTeX) export
method. An example document (with its output) is provided.

%package -n %{shortname}-findhyph
Provides: tex-findhyph = %{epoch}:%{source_date}-%{release}
Provides: texlive-findhyph-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-findhyph-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-findhyph-bin < 7:20170520
Provides: tex-findhyph-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-findhyph-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-findhyph-doc < 7:20170520
License: GPL+
Summary: Find hyphenated words in a document
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-findhyph
Findhyph is a Perl script that will analyse the log file from
running your document with \tracingparagraphs=1 set. The output
contains enough context to enable you to find the hyphenated
word that's being referenced.

%package -n %{shortname}-fontinst
Provides: tex-fontinst = %{epoch}:%{source_date}-%{release}
Provides: texlive-fontinst-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-fontinst-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-fontinst-bin < 7:20170520
Provides: tex-fontinst-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-fontinst-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-fontinst-doc < 7:20170520
License: LPPL
Summary: Help with installing fonts for TeX and LaTeX
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(color.sty)
Requires: tex(amstext.sty)
Provides: tex(bbox.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(cfntinst.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(fontinst.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(finstmsc.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(fontinst.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(multislot.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(xfntinst.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(csc2x.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(csckrn2x.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(osf2x.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(fontdoc.sty) = %{epoch}:%{source_date}-%{release}
# shell
BuildArch: noarch

%description -n %{shortname}-fontinst
TeX macros for converting Adobe Font Metric files to TeX metric
and virtual font format. Fontinst helps mainly with the number
crunching and shovelling parts of font installation. This means
in practice that it creates a number of files which give the
TeX metrics (and related information) for a font family that
(La)TeX needs to do any typesetting in these fonts. Fontinst
furthermore makes it easy to create fonts containing glyphs
from more than one base font, taking advantage of (e.g.)
"expert" font sets. Fontinst cannot examine files to see if
they contain any useful information, nor automatically search
for files or work with binary file formats; those tasks must
normally be done manually or with the help of some other tool,
such as the pltotf and vptovf programs.

%package -n %{shortname}-fontools
Provides: tex-fontools = %{epoch}:%{source_date}-%{release}
Provides: texlive-fontools-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-fontools-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-fontools-bin < 7:20170520
Provides: tex-fontools-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-fontools-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-fontools-doc < 7:20170520
License: GPLv2+
Summary: Tools to simplify using fonts (especially TT/OTF ones)
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(fontools_ly1.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(fontools_ot1.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(fontools_t1.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(fontools_ts1.enc) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-fontools
This package provides a few tools to ease using fonts
(especially Truetype/Opentype ones) with Latex and fontinst:
afm2afm - reencode .afm files; designed to replace fontinst's
\reencodefont for big .afm files; autoinst - simplify the use
of the LCDF TypeTools by creating a command file for otftotfm,
plus .fd and .sty files; and ot2kpx - extract all kerning pairs
from an OpenType font.

%package -n %{shortname}-fontware
Provides: tex-fontware = %{epoch}:%{source_date}-%{release}
Provides: texlive-fontware-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-fontware-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-fontware-bin < 7:20170520
License: LPPL
Summary: fontware package
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-fontware
fontware package.

%package -n %{shortname}-fragmaster
Provides: tex-fragmaster = %{epoch}:%{source_date}-%{release}
Provides: texlive-fragmaster-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-fragmaster-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-fragmaster-bin < 7:20170520
Provides: tex-fragmaster-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-fragmaster-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-fragmaster-doc < 7:20170520
License: GPL+
Summary: Using psfrag with PDFLaTeX
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-fragmaster
Fragmaster enables you to use psfrag with PDFLaTeX. It takes
EPS files and psfrag substitution definition files, and
produces PDF and EPS files with the substitutions included.

%package -n %{shortname}-getmap
Provides: tex-getmap = %{epoch}:%{source_date}-%{release}
Provides: texlive-getmap-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-getmap-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-getmap-bin < 7:20170520
Provides: tex-getmap-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-getmap-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-getmap-doc < 7:20170520
License: LPPL
Summary: Download OpenStreetMap maps for use in documents
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(xkeyval.sty)
Requires: tex(stringenc.sty)
Requires: tex(ifthen.sty)
Provides: tex(getmap.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(getmap.sty) = %{epoch}:%{source_date}-%{release}
# lua and shell
BuildArch: noarch

%description -n %{shortname}-getmap
The package provides a simple interface to OpenStreetMap, and
to Google Maps "map images". In the simplest case, it is
sufficient to specify the address you need (if you don't, the
package will use its own default). The package loads the map
image using an external lua script (invoked via \write 18:
LaTeX must be running with \write 18 enabled). The ("external")
lua script may be used from the command line; a bash version is
provided.

%package -n %{shortname}-git-latexdiff
Summary: Call latexdiff on two Git revisions of a file
License: BSD
Requires: texlive-base texlive-kpathsea
Requires: git, texlive-latexdiff

%description -n %{shortname}-git-latexdiff
git-latexdiff is a tool to graphically visualize differences
between different versions of a LaTeX file. Technically, it is
a wrapper around git and latexdiff.

%package -n %{shortname}-glossaries
Provides: tex-glossaries = %{epoch}:%{source_date}-%{release}
Provides: texlive-glossaries-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-glossaries-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-glossaries-bin < 7:20170520
Provides: tex-glossaries-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-glossaries-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-glossaries-doc < 7:20170520
License: LPPL 1.3
Summary: Create glossaries and lists of acronyms
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(tracklang.sty)
Requires: tex(ifthen.sty)
Requires: tex(xkeyval.sty)
Requires: tex(mfirstuc.sty)
Requires: tex(textcase.sty)
Requires: tex(xfor.sty)
Requires: tex(datatool-base.sty)
Requires: tex(amsgen.sty)
Requires: tex(etoolbox.sty)
Requires: tex(glossary-super.sty)
Requires: tex(glossary-tree.sty)
Requires: tex(translator.sty)
Requires: tex(accsupp.sty)
Requires: tex(longtable.sty)
Requires: tex(array.sty)
Requires: tex(multicol.sty)
Requires: tex(supertabular.sty)
Provides: tex(glossaries-babel.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossaries-compatible-207.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossaries-compatible-307.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossaries-polyglossia.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossaries-prefix.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossaries.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossaries-accsupp.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossary-hypernav.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossary-inline.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossary-list.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossary-long.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossary-longragged.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossary-mcols.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossary-super.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossary-superragged.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(glossary-tree.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-acronym-desc.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-acronym.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-acronyms-lang.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-brief.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-childnoname.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-cite.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-images.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-long.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-multipar.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-parent.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-symbols.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(example-glossaries-url.tex) = %{epoch}:%{source_date}-%{release}
# perl and lua
BuildArch: noarch

%description -n %{shortname}-glossaries
The glossaries package supports acronyms and multiple
glossaries, and has provision for operation in several
languages (using the facilities of either babel or
polyglossia). New entries are defined to have a name and
description (and optionally an associated symbol). Support for
multiple languages is offered, and plural forms of terms may be
specified. An additional package, glossaries-accsupp, can make
use of the accsupp package mechanisms for accessibility support
for PDF files containing glossaries. The user may define new
glossary styles, and preambles and postambles can be specified.
There is provision for loading a database of terms, but only
terms used in the text will be added to the relevant glossary.
The package uses an indexing program to provide the actual
glossary; either makeindex or xindy may serve this purpose, and
a Perl script is provided to serve as interface. The package
distribution also provides the mfirstuc package, for changing
the first letter of a word to upper case. The package
supersedes the author's glossary package (which is now
obsolete), and a conversion tool is provided.

%package -n %{shortname}-glyphlist
Provides: tex-glyphlist = %{epoch}:%{source_date}-%{release}
License: LPPL
Summary: glyphlist package
BuildArch: noarch
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-glyphlist
glyphlist package.

%package -n %{shortname}-gregoriotex
Provides: tex-gregoriotex = %{epoch}:%{source_date}-%{release}
Provides: texlive-gregoriotex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-gregoriotex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-gregoriotex-bin < 7:20170520
Provides: tex-gregoriotex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-gregoriotex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-gregoriotex-doc < 7:20170520
License: GPLv3
Summary: Engraving Gregorian Chant scores
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(gregoriosyms.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(gregoriotex.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(gregoriotex-signs.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(gregoriotex-syllable.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(gregoriotex.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(gregoriotex-main.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(gsp-default.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(gregoriotex-nabc.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(gregoriotex-symbols.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(gregoriotex-chars.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(gregoriotex-spaces.tex) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-gregoriotex
Gregorio is a software application for engraving Gregorian
Chant scores on a computer. Gregorio's main job is to convert a
gabc file (simple text representation of a score) into a
GregorioTeX file, which makes TeX able to create a PDF of your
score.

%package -n %{shortname}-gsftopk
Provides: tex-gsftopk = %{epoch}:%{source_date}-%{release}
Provides: texlive-gsftopk-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-gsftopk-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-gsftopk-bin < 7:20170520
License: GPL+
Summary: Convert "ghostscript fonts" to PK files
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(psfonts.map)

%description -n %{shortname}-gsftopk
Designed for use with xdvi and dvips this utility converts
Adobe Type 1 fonts to PK bitmap format. It should not
ordinarily be much used nowadays, since both its target
applications are now capable of dealing with Type 1 fonts,
direct.

%package -n %{shortname}-hyperxmp
Summary: Embed XMP metadata within a LaTeX document
License: LPPL 1.3
Requires: texlive-base texlive-kpathsea
Requires: tex(atenddvi.sty)
Requires: tex(kvoptions.sty)
Requires: tex(pdfescape.sty)
Requires: tex(stringenc.sty)
Requires: tex(intcalc.sty)
Requires: tex(ifxetex.sty)
Provides: tex(hyperxmp.sty) = %{epoch}:%{source_date}-%{release}
Provides: texlive-hyperxmp-doc = %{epoch}:%{source_date}-%{release}
Provides: tex-hyperxmp-doc = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-hyperxmp
XMP (eXtensible Metadata Platform) is a mechanism proposed by
Adobe for embedding document metadata within the document
itself. The metadata is designed to be easy to extract, even by
programs that are oblivious to the document's file format. Most
of Adobe's applications store XMP metadata when saving files.
Now, with the hyperxmp package, it is trivial for LaTeX
document authors to store XMP metadata in their documents as
well. The package integrates seamlessly with hyperref and
requires virtually no modifications to documents that already
exploit hyperref's mechanisms for specifying PDF metadata. The
current version of hyperxmp can embed the following metadata as
XMP: title, authors, primary author's title or position,
metadata writer, subject/summary, keywords, copyright, license
URL, document base URL, document identifier and instance
identifier, language, source file name, PDF generating tool,
PDF version, and contact telephone number/postal address/email
address/URL. Hyperxmp currently embeds XMP only within PDF
documents; it is compatible with pdfLaTeX, XeLaTeX,
LaTeX+dvipdfm, and LaTeX+dvips+ps2pdf.

%package -n %{shortname}-installfont
Provides: tex-installfont = %{epoch}:%{source_date}-%{release}
Provides: texlive-installfont-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-installfont-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-installfont-bin < 7:20170520
Provides: tex-installfont-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-installfont-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-installfont-doc < 7:20170520
License: LPPL
Summary: A bash script for installing a LaTeX font family
Requires: texlive-base
Requires: texlive-kpathsea
# shell
BuildArch: noarch

%description -n %{shortname}-installfont
With this script you can install a LaTeX font family
(PostScript Type 1, TrueType and OpenType formats are
supported). Font series from light to ultra bold, and (faked)
small caps and (faked) slanted shapes are supported, but not
expert fonts. The script will rename the fonts automatically
(optional) or will otherwise expect the *.afm files and the
font files (in PostScript Type1 format) named in the Karl Berry
scheme (e.g. 5bbr8a.pfb). After running the script, you should
have a working font installation in your local TeX tree.

%package -n %{shortname}-jadetex
Provides: tex-jadetex = %{epoch}:%{source_date}-%{release}
Provides: texlive-jadetex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-jadetex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-jadetex-bin < 7:20170520
Provides: tex-jadetex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-jadetex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-jadetex-doc < 7:20170520
Provides: jadetex = %{epoch}:%{source_date}-%{release}
License: MIT
Summary: Macros supporting Jade DSSSL output
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-latex
Requires: texlive-passivetex
Requires: texlive-pdftex
Requires: texlive-tex
Requires: texlive-amsfonts
Requires: texlive-atbegshi
Requires: texlive-atveryend
Requires: texlive-auxhook
Requires: texlive-babel
Requires: texlive-bigintcalc
Requires: texlive-bitset
Requires: texlive-cm
Requires: texlive-colortbl
Requires: texlive-cyrillic
Requires: texlive-dehyph
Requires: texlive-ec
Requires: texlive-etexcmds
Requires: texlive-fancyhdr
Requires: texlive-graphics
Requires: texlive-graphics-cfg
Requires: texlive-graphics-def
Requires: texlive-hycolor
Requires: texlive-hyperref
Requires: texlive-hyph-utf8
Requires: texlive-iftex
Requires: texlive-infwarerr
Requires: texlive-intcalc
Requires: texlive-kvdefinekeys
Requires: texlive-kvoptions
Requires: texlive-kvsetkeys
Requires: texlive-l3kernel
Requires: texlive-latex-fonts
Requires: texlive-latexconfig
Requires: texlive-letltxmacro
Requires: texlive-ltxcmds
Requires: texlive-marvosym
Requires: texlive-pdfescape
Requires: texlive-pdftexcmds
Requires: texlive-psnfss
Requires: texlive-rerunfilecheck
Requires: texlive-stmaryrd
Requires: texlive-symbol
Requires: texlive-tex-ini-files
Requires: texlive-tipa
Requires: texlive-tools
Requires: texlive-ulem
Requires: texlive-uniquecounter
Requires: texlive-unicode-data
Requires: texlive-url
Requires: texlive-wasysym
Requires: texlive-zapfding
Requires(post,postun): coreutils
Provides: tex(dsssl.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(uentities.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ut1omlgc.fd) = %{epoch}:%{source_date}-%{release}
# no binaries
BuildArch: noarch

%description -n %{shortname}-jadetex
Macro package on top of LaTeX to typeset TeX output of the Jade
DSSSL implementation.

%package -n %{shortname}-jfmutil
Provides: tex-jfmutil = %{epoch}:%{source_date}-%{release}
Provides: texlive-jfmutil-bin = %{epoch}:%{source_date}-%{release}
License: MIT
Summary: Utility to process pTeX-extended TFM and VF
# perl
BuildArch: noarch
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-jfmutil
This program provides functionality to process data files (JFM
and VF) that form logical fonts used in (u)pTeX. The functions
currently available include: The mutual conversion between
Japanese virtual fonts (pairs of VF and JFM) and files in the
"ZVP format", which is an original text format representing
data in virtual fonts. This function can be seen as a
counterpart to the vftovp/vptovf programs. The mutual
conversion between VF files alone and files in the "ZVP0
format", which is a subset of the ZVP format.

%package -n %{shortname}-ketcindy
Provides: tex-ketcindy = %{epoch}:%{source_date}-%{release}
Provides: tex-ketcindy-bin = %{epoch}:%{source_date}-%{release}
License: GPLv3+
Summary: Macros for graphic generation and Cinderella plugin
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(ketlayer.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ketlayer2e.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ketmedia.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ketpic.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ketpic2e.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ketslide.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ketslide2.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-ketcindy
KETpic is a macro package designed for computer algebra systems
(CAS) to generate LaTeX source codes for high-quality
mathematical artwork. KETcindy is a plugin for Cinderella that
allows to generate graphics using KETpic. The generated code
can be included in any LaTeX document.

%package -n %{shortname}-kotex-utils
Provides: tex-kotex-utils = %{epoch}:%{source_date}-%{release}
Provides: texlive-kotex-utils-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-kotex-utils-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-kotex-utils-bin < 7:20170520
Provides: tex-kotex-utils-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-kotex-utils-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-kotex-utils-doc < 7:20170520
License: LPPL
Summary: Utility scripts and support files for typesetting Korean
Requires: texlive-base
Requires: texlive-kotex-utf
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-kotex-utils
The bundle provides scripts and support files for index
generation in Korean language typesetting. The files belong to
the ko.TeX bundle.

%package -n %{shortname}-kpathsea
License: LGPLv2+
Summary: Path searching library for TeX-related files
Provides: kpathsea = %{epoch}:%{source_date}-%{release}
Obsoletes: kpathsea < %{source_date}
Provides: tex-kpathsea = %{epoch}:%{source_date}-%{release}
Provides: texlive-kpathsea-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-kpathsea-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-kpathsea-bin < 7:20170520
Provides: tex-kpathsea-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-kpathsea-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-kpathsea-doc < 7:20170520
Requires: coreutils, grep
Requires: texlive-base
# We absolutely need this to go in first, since the trigger needs it
Requires(post): texlive-texlive-scripts = %{epoch}:%{source_date}-%{release}
Provides: tex(fmtutil.cnf) = %{epoch}:%{source_date}-%{release}
Provides: tex(mktex.cnf) = %{epoch}:%{source_date}-%{release}
Provides: tex(texmf.cnf) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-kpathsea
Kpathsea is a library and utility programs which provide path
searching facilities for TeX file types, including the self-
locating feature required for movable installations, layered on
top of a general search mechanism.

%package -n %{shortname}-l3build
Provides: tex-l3build = %{epoch}:%{source_date}-%{release}
Provides: texlive-l3build-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-l3build-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-l3build-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-l3build-doc < 7:20180414
License: LPPL
Summary: A testing and building system for (La)TeX
Provides: tex(regression-test.tex) = %{epoch}:%{source_date}-%{release}
Requires: texlive-base
Requires: texlive-kpathsea
# lua
BuildArch: noarch

%description -n %{shortname}-l3build
The build system supports testing and building LaTeX3 code, on
Linux, Mac OS X and Windows systems. The package offers: A unit
testing system for (La)TeX code (whether kernel code or
contributed packages); A system for typesetting package
documentation; and An automated process for creating CTAN
releases.

%package -n %{shortname}-lacheck
Provides: tex-lacheck = %{epoch}:%{source_date}-%{release}
Provides: texlive-lacheck-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-lacheck-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-lacheck-bin < 7:20170520
License: GPL+
Summary: LaTeX checker
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-lacheck
Lacheck is a tool for finding common mistakes in LaTeX
documents. The distribution includes sources, and executables
for OS/2 and Win32 environments.

%package -n %{shortname}-latex
Provides: tex-latex = %{epoch}:%{source_date}-%{release}
Provides: tetex-latex = %{epoch}:%{source_date}-%{release}
Provides: texlive-latex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-latex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latex-bin < 7:20170520
Provides: texlive-latex-bin-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-latex-bin-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latex-bin-bin < 7:20170520
Provides: tex-latex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-latex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latex-doc < 7:20170520
License: LPPL 1.3
Summary: A TeX macro package that defines LaTeX
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-luatex
Requires: texlive-pdftex
Requires: texlive-latexconfig
Requires: texlive-latex-fonts
# As a result of changes in textcomp, it requests TS1 fonts for some things
# most notably, \textbullet. Since people probably want a working itemize
# even on rather minimal installs, we add an explicit Requires on texlive-cm-super
# here. (bz1867927)
Requires: texlive-cm-super
Requires(post,postun): coreutils
Requires: tex(multicol.sty)
Requires: tex(url.sty)
Requires: tex(hyperref.sty)
Provides: tex(alltt.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ansinew.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(applemac.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(article.cls) = %{epoch}:%{source_date}-%{release}
Provides: tex(article.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ascii.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(bezier.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(bk10.clo) = %{epoch}:%{source_date}-%{release}
Provides: tex(bk11.clo) = %{epoch}:%{source_date}-%{release}
Provides: tex(bk12.clo) = %{epoch}:%{source_date}-%{release}
Provides: tex(book.cls) = %{epoch}:%{source_date}-%{release}
Provides: tex(book.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp1250.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp1252.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp1257.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp437.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp437de.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp850.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp852.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp858.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(cp865.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(decmulti.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(doc.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(docstrip.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(exscale.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(fix-cm.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(fixltx2e.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(flafter.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(fleqn.clo) = %{epoch}:%{source_date}-%{release}
Provides: tex(fleqn.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(fltrace.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(fontenc.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(fontmath.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(fonttext.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(graphpap.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(idx.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(ifthen.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(inputenc.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(lablst.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(latex209.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(latexbug.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(latexrelease.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(latexsym.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(latin1.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(latin10.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(latin2.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(latin3.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(latin4.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(latin5.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(latin9.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(leqno.clo) = %{epoch}:%{source_date}-%{release}
Provides: tex(leqno.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(letter.cls) = %{epoch}:%{source_date}-%{release}
Provides: tex(letter.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(lppl.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(ltnews.cls) = %{epoch}:%{source_date}-%{release}
Provides: tex(ltxcheck.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(ltxdoc.cls) = %{epoch}:%{source_date}-%{release}
Provides: tex(ltxguide.cls) = %{epoch}:%{source_date}-%{release}
Provides: tex(macce.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(makeidx.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(minimal.cls) = %{epoch}:%{source_date}-%{release}
Provides: tex(newlfont.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(next.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(nfssfont.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(oldlfont.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(omlcmm.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(omlcmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(omlenc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(omllcmm.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(omscmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(omscmsy.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(omsenc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(omslcmsy.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(omxcmex.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(omxlcmex.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(openbib.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot1cmdh.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot1cmfib.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot1cmfr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot1cmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot1cmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot1cmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot1cmvtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot1enc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot1lcmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot1lcmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ot4enc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(preload.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(proc.cls) = %{epoch}:%{source_date}-%{release}
Provides: tex(proc.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(report.cls) = %{epoch}:%{source_date}-%{release}
Provides: tex(report.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(sample2e.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(sfonts.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(shortvrb.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(showidx.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(size10.clo) = %{epoch}:%{source_date}-%{release}
Provides: tex(size11.clo) = %{epoch}:%{source_date}-%{release}
Provides: tex(size12.clo) = %{epoch}:%{source_date}-%{release}
Provides: tex(slides.cls) = %{epoch}:%{source_date}-%{release}
Provides: tex(slides.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(slides.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(small2e.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(source2e.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(syntonly.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1cmdh.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1cmfib.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1cmfr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1cmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1cmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1cmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1cmvtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1enc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1enc.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1lcmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(t1lcmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(testpage.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(texsys.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(textcomp.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(tracefnt.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ts1cmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ts1cmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ts1cmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ts1cmvtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ts1enc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(tuenc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(tulmdh.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(tulmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(tulmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(tulmssq.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(tulmssq.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(tulmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(tulmvtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ucmr.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ucmss.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ucmtt.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ulasy.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(ullasy.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(utf8-test.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(utf8.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(utf8test.tex) = %{epoch}:%{source_date}-%{release}
Provides: texlive-texmf-latex = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texmf-latex < %{source_date}
# symlinks
BuildArch: noarch

%description -n %{shortname}-latex
LaTeX is a widely-used macro package for TeX, providing many
basic document formating commands extended by a wide range of
packages. It is a development of Leslie Lamport's LaTeX 2.09,
and superseded the older system in June 1994. The basic
distribution is catalogued separately, at latex-base; apart
from a large set of contributed packages and third-party
documentation (elsewhere on the archive), the distribution
includes: - a bunch of required packages, which LaTeX authors
are "entitled to assume" will be present on any system running
LaTeX; and - a minimal set of documentation detailing
differences from the 'old' version of LaTeX in the areas of
user commands, font selection and control, class and package
writing, font encodings, configuration options and modification
of LaTeX.

%package -n %{shortname}-latex-git-log
Provides: tex-latex-git-log = %{epoch}:%{source_date}-%{release}
Provides: texlive-latex-git-log-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-latex-git-log-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latex-git-log-bin < 7:20170520
Provides: tex-latex-git-log-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-latex-git-log-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latex-git-log-doc < 7:20170520
License: GPLv3+
Summary: Typeset git log information
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-latex-git-log
The program is run within a git repository, and outputs the
entire version history, as a LaTeX table. That output will
typically be redirected to a file; the author recommends
typesetting in landscape orientation.

%package -n %{shortname}-latex-papersize
Provides: tex-latex-papersize = %{epoch}:%{source_date}-%{release}
Provides: texlive-latex-papersize-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-latex-papersize-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latex-papersize-bin < 7:20170520
Provides: tex-latex-papersize-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-latex-papersize-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latex-papersize-doc < 7:20170520
License: ASL 2.0
Summary: Calculate LaTeX settings for any font and paper size
Requires: texlive-base
Requires: texlive-kpathsea
# python
BuildArch: noarch

%description -n %{shortname}-latex-papersize
The package is a Python script, whose typical use is when
preparing printed material for users with low vision. The most
effective way of doing this is to print on (notional) small
paper, and then to magnify the result; the script calculates
the settings for various font and paper sizes. More details are
to be read in the script itself.

%package -n %{shortname}-latex2man
Provides: tex-latex2man = %{epoch}:%{source_date}-%{release}
Provides: texlive-latex2man-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-latex2man-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latex2man-bin < 7:20170520
Provides: tex-latex2man-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-latex2man-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latex2man-doc < 7:20170520
License: LPPL
Summary: Translate LaTeX-based manual pages into Unix man format
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(fancyheadings.sty)
Requires: tex(fancyhdr.sty)
Provides: tex(latex2man.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(latex2man.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-latex2man
A tool to translate UNIX manual pages written with LaTeX into a
man-page format understood by the Unix man(1) command.
Alternatively HTML or TexInfo code can be produced. Output of
parts of the text may be supressed using the conditional text
feature.

%package -n %{shortname}-latex2nemeth
Provides: tex-latex2nemeth = %{epoch}:%{source_date}-%{release}
Provides: texlive-latex2nemeth-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-latex2nemeth-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latex2nemeth-bin < 7:20170520
Provides: tex-latex2nemeth-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-latex2nemeth-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latex2nemeth-doc < 7:20170520
License: GPLv3
Summary: Convert LaTeX source to Braille with math in Nemeth
Requires: texlive-base
Requires: texlive-kpathsea
# shell
BuildArch: noarch

%description -n %{shortname}-latex2nemeth
After many failed attempts to transcribe real math notes and
books to Braille/Nemeth in order to deal with a real situation
(blind student in Math Dept.), we decided to develop a new
program that follows a direct, from LaTeX to Braille/Nemeth,
approach. Other attempts (such as tex4ht) failed because they
all needed an extra step to go from xml to Braille, and this
step (say, with liblouis) produced incomprehensible output
(liblouis focuses in Office apps). Our main target was the
Greek language which is only Braille level 1, but English at
level 1 is supported as well. Simple pictures in PSTricks are
also supported in order to produce tactile graphics with
specialized equipment. Note that embossing will need
LibreOffice and odt2braille as this project does not deal with
embossers' drivers.

%package -n %{shortname}-latexdiff
Provides: tex-latexdiff = %{epoch}:%{source_date}-%{release}
Provides: texlive-latexdiff-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-latexdiff-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latexdiff-bin < 7:20170520
Provides: tex-latexdiff-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-latexdiff-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latexdiff-doc < 7:20170520
License: GPLv3+
Summary: Determine and mark up significant differences between LaTeX files
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-latexdiff
Latexdiff is a Perl script for visual mark up and revision of
significant differences between two LaTeX files. Various
options are available for visual markup using standard LaTeX
packages such as color. Changes not directly affecting visible
text, for example in formatting commands, are still marked in
the LaTeX source. A rudimentary revision facilility is provided
by another Perl script, latexrevise, which accepts or rejects
all changes. Manual editing of the difference file can be used
to override this default behaviour and accept or reject
selected changes only.

%package -n %{shortname}-latexfileversion
Provides: tex-latexfileversion = %{epoch}:%{source_date}-%{release}
Provides: texlive-latexfileversion-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-latexfileversion-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latexfileversion-bin < 7:20170520
Provides: tex-latexfileversion-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-latexfileversion-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latexfileversion-doc < 7:20170520
License: LPPL
Summary: Prints the version and date of a LaTeX class or style file
Requires: texlive-base
Requires: texlive-kpathsea
# shell
BuildArch: noarch

%description -n %{shortname}-latexfileversion
This simple shell script prints the version and date of a LaTeX
class or style file. Syntax: latexfileversion <file> This
programme handles style files (extension .sty), class files
(extension .cls), and other TeX input files. The file extension
must be given.

%package -n %{shortname}-latexindent
Provides: tex-latexindent = %{epoch}:%{source_date}-%{release}
Provides: texlive-latexindent-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-latexindent-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latexindent-bin < 7:20170520
Provides: tex-latexindent-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-latexindent-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latexindent-doc < 7:20170520
License: GPLv3+
Summary: Indent a LaTeX document, highlighting the programming structure
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-latexindent
The Perl script processes a LaTeX file, indenting parts so as to
highlight the structure for the reader.

%package -n %{shortname}-latexpand
Provides: tex-latexpand = %{epoch}:%{source_date}-%{release}
Provides: texlive-latexpand-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-latexpand-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latexpand-bin < 7:20170520
Provides: tex-latexpand-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-latexpand-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-latexpand-doc < 7:20170520
License: BSD
Summary: Expand \input and \include in a LaTeX document
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-latexpand
Latexpand is a Perl script that simply replaces \input and
\include commands with the content of the file input/included.
The script does not deal with \includeonly commands.

%package -n %{shortname}-lcdftypetools
Provides: tex-lcdftypetools = %{epoch}:%{source_date}-%{release}
# This is a mistake in the texlive package. Will be fixed in next major TL update.
Provides: lcdf-typetools = %{epoch}:%{source_date}-%{release}
Provides: texlive-lcdftypetools-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-lcdftypetools-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-lcdftypetools-bin < 7:20170520
License: GPL+
Summary: A bundle of outline font manipulation tools
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-glyphlist

%description -n %{shortname}-lcdftypetools
This bundle of tools comprises: Cfftot1, which translates a
Compact Font Format (CFF) font, or a PostScript-flavored
OpenType font, into PostScript Type 1 format. It correctly
handles subroutines and hints; Mmafm and mmpfb, which create
instances of multiple-master fonts (mmafm and mmpfb were
previously distributed in their own package, mminstance);
Otfinfo, which reports information about OpenType fonts, such
as the features they support and the contents of their 'size'
optical size features; Otftotfm, which creates TeX font metrics
and encodings that correspond to a PostScript-flavored OpenType
font. It will interpret glyph positionings, substitutions, and
ligatures as far as it is able. You can say which OpenType
features should be activated; T1dotlessj, creates a Type 1 font
whose only character is a dotless j matching the input font's
design; T1lint, which checks a Type 1 font for correctness;
T1reencode, which replaces a font's internal encoding with one
you specify; and T1testpage, which creates a PostScript proof
for a Type 1 font.

%package -n %{shortname}-lib
Summary: Shared libraries for TeX-related files
Provides: texlive-kpathsea-lib = %{epoch}:%{source_date}-%{release}
# We have to straight up lie about this to ensure the upgrade.
Provides: texlive-kpathsea-lib(%{__isa}) = 6:2016
Obsoletes: texlive-kpathsea-lib < 2015
Provides: bundled(lua) = 5.2.4

%description -n %{shortname}-lib
TeX specific shared libraries.

%package -n %{shortname}-lib-devel
Summary: Development files for TeX specific shared libraries
Requires: %{shortname}-lib%{?_isa}
Provides: texlive-kpathsea-lib-devel = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-kpathsea-lib-devel < 2015

%description -n %{shortname}-lib-devel
Development files for TeX specific shared libraries.

%package -n %{shortname}-lilyglyphs
Provides: tex-lilyglyphs = %{epoch}:%{source_date}-%{release}
Provides: texlive-lilyglyphs-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-lilyglyphs-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-lilyglyphs-bin < 7:20170520
Provides: tex-lilyglyphs-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-lilyglyphs-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-lilyglyphs-doc < 7:20170520
License: LPPL 1.3
Summary: Access lilypond fragments and glyphs, in LaTeX
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(keyval.sty)
Requires: tex(pgf.sty)
Requires: tex(adjustbox.sty)
Provides: tex(emmentaler-11.otf) = %{epoch}:%{source_date}-%{release}
Provides: tex(emmentaler-13.otf) = %{epoch}:%{source_date}-%{release}
Provides: tex(emmentaler-14.otf) = %{epoch}:%{source_date}-%{release}
Provides: tex(emmentaler-16.otf) = %{epoch}:%{source_date}-%{release}
Provides: tex(emmentaler-18.otf) = %{epoch}:%{source_date}-%{release}
Provides: tex(emmentaler-20.otf) = %{epoch}:%{source_date}-%{release}
Provides: tex(emmentaler-23.otf) = %{epoch}:%{source_date}-%{release}
Provides: tex(emmentaler-26.otf) = %{epoch}:%{source_date}-%{release}
Provides: tex(emmentaler-brace.otf) = %{epoch}:%{source_date}-%{release}
Provides: tex(lilyglyphs.sty) = %{epoch}:%{source_date}-%{release}
# python
BuildArch: noarch

%description -n %{shortname}-lilyglyphs
The package provides the means to include arbitrary elements of
Lilypond notation, including symbols from Lilypond's Emmentaler
font, in a LaTeX document. The package uses OpenType fonts, and
as a result must be compiled with LuaLaTeX or XeLaTeX.

%package -n %{shortname}-listbib
Provides: tex-listbib = %{epoch}:%{source_date}-%{release}
Provides: texlive-listbib-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-listbib-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-listbib-bin < 7:20170520
Provides: tex-listbib-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-listbib-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-listbib-doc < 7:20170520
License: GPL+
Summary: Lists contents of BibTeX files
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(listbib.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(listbib.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(listbib.tex) = %{epoch}:%{source_date}-%{release}
# shell
BuildArch: noarch

%description -n %{shortname}-listbib
Generates listings of bibliographic data bases in BibTeX format
-- for example for archival purposes. Included is a listbib.bst
which is better suited for this purpose than the standard
styles.

%package -n %{shortname}-listings-ext
Provides: tex-listings-ext = %{epoch}:%{source_date}-%{release}
Provides: texlive-listings-ext-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-listings-ext-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-listings-ext-bin < 7:20170520
Provides: tex-listings-ext-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-listings-ext-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-listings-ext-doc < 7:20170520
License: LPPL 1.2
Summary: Automated input of source
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(listings.sty)
Requires: tex(xkeyval.sty)
Provides: tex(listings-ext.sty) = %{epoch}:%{source_date}-%{release}
# shell
BuildArch: noarch

%description -n %{shortname}-listings-ext
The package provides a means of marking a source, so that
samples of it may be included in a document (by means of the
listings package) in a stable fashion, regardless of any change
to the source. The markup in the source text defines tags for
blocks of source. These tags are processed by a shell script to
make a steering file that is used by the package when LaTeX is
being run.

%package -n %{shortname}-light-latex-make
Summary: llmk: A build tool for LaTeX documents
License: MIT
Requires: texlive-base texlive-kpathsea

%description -n %{shortname}-light-latex-make
This program is yet another build tool specific for LaTeX
documents. Its aim is to provide a simple way to specify a
workflow of processing LaTeX documents and encourage people to
always explicitly show the right workflow for each document.
The main features of the executable llmk are all about the
above purpose. First, you can describe the workflows either in
an external file llmk.toml or in a LaTeX document source in the
form of magic comments. Further, multiple magic comment formats
can be used. Second, it is fully cross-platform. The only
requirement of the program is the texlua command; llmk provides
a uniform way to describe the workflows available for nearly
all TeX environments. Third, it behaves exactly the same in any
environment. At this point, llmk intentionally does not provide
any method for user configuration. Therefore one can guarantee
that for a LaTeX document with an llmk setup, the process of
typesetting the document will be reproduced in any TeX
environment with the program.

%package -n %{shortname}-lollipop
Provides: tex-lollipop = %{epoch}:%{source_date}-%{release}
Provides: texlive-lollipop-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-lollipop-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-lollipop-bin < 7:20170520
Provides: tex-lollipop-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-lollipop-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-lollipop-doc < 7:20170520
License: GPLv3+
Summary: TeX made easy
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-cm
Requires: texlive-hyphen-base
Requires: texlive-tex
Requires(post,postun): coreutils
Provides: tex(lollipop-define.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lollipop-document.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lollipop-float.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lollipop-fontdefs.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lollipop-fonts.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lollipop-heading.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lollipop-lists.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lollipop-output.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lollipop-plain.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lollipop-text.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lollipop-tools.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(lollipop.tex) = %{epoch}:%{source_date}-%{release}
# no actual binaries here
BuildArch: noarch

%description -n %{shortname}-lollipop
Lollipop is "TeX made easy" -- it is a macro package that
functions as a toolbox for writing TeX macros. Its main aim is
to make macro writing so easy that implementing a fully new
layout in TeX would become a matter of less than an hour for an
average document. The aim is that such a task could be
accomplished by someone with only a very basic training in TeX
programming. Thus, Lollipop aims to make structured text
formatting available in environments where typical users would
switch to WYSIWYG packages for the freedom that such a
mechanism offers. In addition, development of support for
Lollipop documents written in RTL languages (such as Persian)
is underway.

%package -n %{shortname}-ltxfileinfo
Provides: tex-ltxfileinfo = %{epoch}:%{source_date}-%{release}
Provides: texlive-ltxfileinfo-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-ltxfileinfo-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ltxfileinfo-bin < 7:20170520
Provides: tex-ltxfileinfo-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-ltxfileinfo-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ltxfileinfo-doc < 7:20170520
License: GPL+
Summary: Print version information for a LaTeX file
Requires: texlive-base
Requires: texlive-kpathsea
# shell
BuildArch: noarch

%description -n %{shortname}-ltxfileinfo
ltxfileinfo displays version information for LaTeX files. If no
path information is given, the file is searched using
kpsewhich. As an extra, for developers, the script will (use
the --star or --color options) check the valididity of the
\Provides... statements in the files. The script uses code from
Uwe Luck's readprov.sty.

%package -n %{shortname}-ltximg
Provides: tex-ltximg = %{epoch}:%{source_date}-%{release}
Provides: texlive-ltximg-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-ltximg-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ltximg-bin < 7:20170520
Provides: tex-ltximg-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-ltximg-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ltximg-doc < 7:20170520
License: GPLv2+
Summary: Split LaTeX files to sanitise a conversion process
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-ltximg
The package provides a Perl script that extracts all TikZ and
PStricks environments for separate processing to produce images
(in eps, pdf, png or jpg format) for use by a converter or the
preview bundle.

%package -n %{shortname}-luaotfload
Provides: tex-luaotfload = %{epoch}:%{source_date}-%{release}
Provides: texlive-luaotfload-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-luaotfload-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-luaotfload-bin < 7:20170520
Provides: tex-luaotfload-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-luaotfload-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-luaotfload-doc < 7:20170520
License: GPLv2+
Summary: OpenType 'loader' for Plain TeX and LaTeX
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-lualibs
Requires: texlive-lua-alt-getopt
Requires: tex(luatexbase.sty)
Provides: tex(luaotfload-blacklist.cnf) = %{epoch}:%{source_date}-%{release}
Provides: tex(luaotfload.sty) = %{epoch}:%{source_date}-%{release}
# lua
BuildArch: noarch

%description -n %{shortname}-luaotfload
The package adopts the TrueType/OpenType Font loader code
provided in ConTeXt, and adapts it to use in Plain TeX and
LaTeX. It works under LuaLaTeX only.

%package -n %{shortname}-luahbtex
Provides: tex-luahbtex = %{epoch}:%{source_date}-%{release}
Provides: texlive-luahbtex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-luahbtex-bin = %{epoch}:%{source_date}-%{release}
License: GPLv2+
Summary: LuaTeX with HarfBuzz library for glyph shaping
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-luatex
Requires: texlive-cm
Requires: texlive-etex
Requires: texlive-hyphen-base
Requires: texlive-knuth-lib
Requires: texlive-plain
Requires: texlive-tex-ini-files
Requires: texlive-unicode-data
Requires: texlive-hyph-utf8

%description -n %{shortname}-luahbtex
LuaTeX with HarfBuzz library for glyph shaping.

%package -n %{shortname}-luajittex
Provides: tex-luajittex = %{epoch}:%{source_date}-%{release}
Provides: tex-luajittex-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-luajittex-bin = %{epoch}:%{source_date}-%{release}
License: GPLv2+
Summary: LuaTeX with just-in-time (jit) compiler, with and without HarfBuzz
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-luatex
Requires: texlive-cm
Requires: texlive-etex
Requires: texlive-hyphen-base
Requires: texlive-knuth-lib
Requires: texlive-plain
Requires: texlive-tex-ini-files
Requires: texlive-unicode-data
Requires: texlive-hyph-utf8

%description -n %{shortname}-luajittex
LuaTeX with just-in-time (jit) compiler, with and without HarfBuzz.

%package -n %{shortname}-luatex
Provides: tex-luatex = %{epoch}:%{source_date}-%{release}
Provides: texlive-luatex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-luatex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-luatex-bin < 7:20170520
Provides: tex-luatex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-luatex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-luatex-doc < 7:20170520
License: GPLv2+
Summary: The LuaTeX engine
Requires: texlive-base
Requires: texlive-kpathsea
Requires(post,postun): coreutils
Requires: texlive-cm
Requires: texlive-etex
Requires: texlive-hyphen-base
Requires: texlive-knuth-lib
Requires: texlive-plain
Requires: texlive-tex-ini-files
Requires: texlive-unicode-data
Requires: texlive-hyph-utf8
Requires: tex(luatex.def)
Provides: tex(luatex-unicode-letters.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(luatexiniconfig.tex) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-luatex
LuaTeX is an extended version of pdfTeX using Lua as an
embedded scripting language. The LuaTeX project's main
objective is to provide an open and configurable variant of TeX
while at the same time offering downward compatibility. LuaTeX
uses Unicode (as UTF-8) as its default input encoding, and is
able to use modern (OpenType) fonts (for both text and
mathematics). It should be noted that LuaTeX is still under
development; its specification has been declared stable, but
absolute stability may not in practice be assumed. 

%package -n %{shortname}-lwarp
Provides: tex-lwarp = %{epoch}:%{source_date}-%{release}
Provides: texlive-lwarp-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-lwarp-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-lwarp-bin < 7:20170520
Provides: tex-lwarp-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-lwarp-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-lwarp-doc < 7:20170520
License: LPPL
Summary: Converts LaTeX to HTML
Requires: texlive-base
Requires: texlive-kpathsea
# lua
BuildArch: noarch

%description -n %{shortname}-lwarp
The package causes LaTeX to directly produce HTML5 output,
using external utility programs only for the final conversion
of text and images. Math may be represented by SVG files or
MathJax. Documents may be produced by LaTeX, LuaLaTeX, or
XeLaTeX. A texlua script removes the need for system utilities
such as make and gawk, and also supports xindy and latexmk.
Configuration is automatic at the first manual compile. Print
and HTML versions of each document may coexist, each with its
own set of auxiliary files. Support files are self-generated on
request. Assistance is provided for HTML import into EPUB
conversion software and word processors.

%package -n %{shortname}-lyluatex
Summary: Commands to include lilypond scores within a (Lua)LaTeX document
Version: svn51252
License: MIT
Requires: texlive-base texlive-kpathsea
Provides: tex(lyluatex.lua) = %{epoch}:%{source_date}-%{release}
Provides: tex(lyluatex.sty) = %{epoch}:%{source_date}-%{release}
# lua
BuildArch: noarch
Requires: tex(currfile.sty)
Requires: tex(environ.sty)
Requires: tex(graphicx.sty)
Requires: tex(luaotfload.sty)
Requires: tex(luatexbase.sty)
Requires: tex(metalogo.sty)
Requires: tex(minibox.sty)
Requires: tex(pdfpages.sty)
Requires: tex(xkeyval.sty)

%description -n %{shortname}-lyluatex
This package provides macros for the inclusion of LilyPond
scores within LuaLaTeX. It calls LilyPond to compile scores,
then includes the produced files.

%package -n %{shortname}-make4ht
Provides: tex-make4ht = %{epoch}:%{source_date}-%{release}
Provides: texlive-make4ht-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-make4ht-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-make4ht-bin < 7:20170520
Provides: tex-make4ht-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-make4ht-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-make4ht-doc < 7:20170520
License: LPPL 1.3
Summary: A build system for tex4ht
Requires: texlive-base
Requires: texlive-kpathsea
# lua
BuildArch: noarch

%description -n %{shortname}-make4ht
make4ht is a simple build system for tex4ht. It is both
executable, which simplifies tex4ht execution, and a library
which can be used to create customized conversion programs.

%package -n %{shortname}-makedtx
Provides: tex-makedtx = %{epoch}:%{source_date}-%{release}
Provides: texlive-makedtx-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-makedtx-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-makedtx-bin < 7:20170520
Provides: tex-makedtx-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-makedtx-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-makedtx-doc < 7:20170520
License: LPPL
Summary: Perl script to help generate dtx and ins files
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(creatdtx.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-makedtx
The makedtx bundle is provided to help LaTeX2e developers to
write the code and documentation in separate files, and then
combine them into a single .dtx file for distribution. It
automatically generates the character table, and also writes
the associated installation (.ins) script.

%package -n %{shortname}-makeindex
Provides: tex-makeindex = %{epoch}:%{source_date}-%{release}
Provides: texlive-makeindex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-makeindex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-makeindex-bin < 7:20170520
Provides: tex-makeindex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-makeindex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-makeindex-doc < 7:20170520
License: MakeIndex
Summary: Provides sorted index from unsorted raw data
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-makeindex
Provides: tex(idxmac.tex) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-makeindex
MakeIndex is a computer program which provides a sorted index
from unsorted raw data. MakeIndex can process raw data output
by various programs, however, it is generally used with LaTeX
and troff.

%package -n %{shortname}-match_parens
Provides: tex-match_parens = %{epoch}:%{source_date}-%{release}
Provides: texlive-match_parens-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-match_parens-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-match_parens-bin < 7:20170520
Provides: tex-match_parens-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-match_parens-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-match_parens-doc < 7:20170520
License: GPL+
Summary: Find mismatches of parentheses, braces, (angle) brackets, in texts
Requires: texlive-base
Requires: texlive-kpathsea
Requires: ruby
# ruby
BuildArch: noarch

%description -n %{shortname}-match_parens
Mismatches of parentheses, braces, (angle) brackets, especially
in TeX sources which may be rich in those, may be difficult to
trace. This little script helps you by writing your text to
standard output, after adding a left margin to your text, which
will normally be almost empty, but will clearly show any
mismatches.

%package -n %{shortname}-mathspic
Provides: tex-mathspic = %{epoch}:%{source_date}-%{release}
Provides: texlive-mathspic-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-mathspic-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mathspic-bin < 7:20170520
Provides: tex-mathspic-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-mathspic-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mathspic-doc < 7:20170520
License: LPPL
Summary: A Perl filter program for use with PiCTeX
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(prepictex.tex)
Requires: tex(pictexwd.tex)
Requires: tex(postpictex.tex)
Provides: tex(mathspic.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-mathspic
MathsPIC(Perl) is a development of the earlier MathsPIC(DOS)
program, now implemented as a Perl script, being much more
portable than the earlier program. MathsPIC parses a plain text
input file and generates a plain text output-file containing
commands for drawing a diagram. Version 1.0 produces output
containing PiCTeX and (La)TeX commands, which may then be
processed by plain TeX or LaTeX in the usual way. MathsPIC also
outputs a comprehensive log-file. MathsPIC facilitates creating
figures using PiCTeX by providing an environment for
manipulating named points and also allows the use of variables
and maths (advance, multiply, and divide)--in short--it takes
the pain out of PiCTeX.

%package -n %{shortname}-metafont
Provides: tex-metafont = %{epoch}:%{source_date}-%{release}
Provides: texlive-metafont-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-metafont-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-metafont-bin < 7:20170520
License: Knuth
Summary: A system for specifying fonts
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-modes
Requires(post,postun): coreutils
Provides: tex(mf.mf) = %{epoch}:%{source_date}-%{release}
Provides: tex(plain.mf) = %{epoch}:%{source_date}-%{release}
Provides: tex(cmmf.ini) = %{epoch}:%{source_date}-%{release}
Provides: tex(mf.ini) = %{epoch}:%{source_date}-%{release}
Provides: tex(mode2dpi.mf) = %{epoch}:%{source_date}-%{release}
Provides: tex(mode2dpixy.mf) = %{epoch}:%{source_date}-%{release}
Provides: tex(modename.mf) = %{epoch}:%{source_date}-%{release}
Provides: tex(modes.mf) = %{epoch}:%{source_date}-%{release}
Provides: tex(ps2mfbas.mf) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-metafont
The program takes a semi-algorithmic specification of a font,
and produces a bitmap font (whose properties are defined by a
set of parameters of the target device), and a set metrics for
use by TeX. The bitmap output may be converted into a format
directly usable by a device driver, etc., by the tools provided
in the parallel mfware distribution.

%package -n %{shortname}-metapost
Provides: tex-metapost = %{epoch}:%{source_date}-%{release}
Provides: texlive-metapost-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-metapost-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-metapost-bin < 7:20170520
Provides: tex-metapost-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-metapost-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-metapost-doc < 7:20170520
License: LGPLv2+
Summary: A development of Metafont for creating graphics
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(freeeuro.afm) = %{epoch}:%{source_date}-%{release}
Provides: tex(psyrgo.afm) = %{epoch}:%{source_date}-%{release}
Provides: tex(zpzdr-reversed.afm) = %{epoch}:%{source_date}-%{release}
Provides: tex(groff.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(troff-updmap.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(troff.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(freeeuro.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pagd8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pagdo8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pagk8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pagko8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pbkd8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pbkdi8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pbkl8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pbkli8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pcrb8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pcrbo8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pcrr8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pcrro8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(phvb8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(phvb8gn.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(phvbo8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(phvbo8gn.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(phvr8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(phvr8gn.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(phvro8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(phvro8gn.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pncb8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pncbi8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pncr8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pncri8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pplb8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pplbi8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pplr8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pplri8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(psyrgo.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(ptmb8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(ptmbi8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(ptmr8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(ptmri8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(pzcmi8g.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(zpzdr-reversed.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(freeeuro.pfa) = %{epoch}:%{source_date}-%{release}
Provides: tex(mfplain.ini) = %{epoch}:%{source_date}-%{release}
Provides: tex(trfonts.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(mproof.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mpsproof.tex) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-metapost
MetaPost uses a language based on that of Metafont to produce
precise technical illustrations. Its output is scalable
PostScript or SVG, rather than the bitmaps Metafont creates.

%package -n %{shortname}-mex
Provides: tex-mex = %{epoch}:%{source_date}-%{release}
Provides: texlive-mex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-mex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mex-bin < 7:20170520
Provides: tex-mex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-mex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mex-doc < 7:20170520
License: Public Domain
Summary: Polish formats for TeX
Requires: texlive-base
Requires: texlive-enctex
Requires: texlive-hyph-utf8
Requires: texlive-hyphen-base
Requires: texlive-hyphen-polish
Requires: texlive-knuth-lib
Requires: texlive-kpathsea
Requires: texlive-pdftex
Requires: texlive-pl
Requires: texlive-plain
Requires: texlive-tex
Requires: texlive-tex-ini-files
Requires: texlive-utf8mex
Requires(post,postun): coreutils
Provides: tex(lamex.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mex.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mex1.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mex2.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mexconf.tex) = %{epoch}:%{source_date}-%{release}
# just symlinks
BuildArch: noarch

%description -n %{shortname}-mex
MeX is an adaptation of Plain TeX (MeX) and LaTeX209 (LaMeX)
formats to the Polish language and to Polish printing customs.
It contains a complete set of Metafont sources of Polish fonts,
hyphenation rules for the Polish language and sources of
formats.

%package -n %{shortname}-mflua
Provides: tex-mflua = %{epoch}:%{source_date}-%{release}
Provides: texlive-mflua-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-mflua-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mflua-bin < 7:20170520
License: GPL+
Summary: A METAFONT compliant program with a Lua interpreter embedded
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-mflua
A METAFONT compliant program with a Lua interpreter embedded.

%package -n %{shortname}-mfware
Provides: tex-mfware = %{epoch}:%{source_date}-%{release}
Provides: texlive-mfware-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-mfware-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mfware-bin < 7:20170520
License: Knuth
Summary: Supporting tools for use with Metafont
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-mfware
A collection of programs (as web source) for processing the
output of Metafont.

%package -n %{shortname}-mf2pt1
Provides: tex-mf2pt1 = %{epoch}:%{source_date}-%{release}
Provides: texlive-mf2pt1-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-mf2pt1-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mf2pt1-bin < 7:20170520
Provides: tex-mf2pt1-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-mf2pt1-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mf2pt1-doc < 7:20170520
License: LPPL
Summary: Produce PostScript Type 1 fonts from Metafont source
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-mf2pt1
mf2pt1 facilitates producing PostScript Type 1 fonts from a
Metafont source file. It is not, as the name may imply, an
automatic converter of arbitrary Metafont fonts to Type 1
format. mf2pt1 imposes a number of restrictions on the Metafont
input. If these restrictions are met, mf2pt1 will produce valid
Type 1 output with more accurate control points than can be
reverse-engineered by TeXtrace, mftrace, and other programs
which convert bitmaps to outline fonts.

%package -n %{shortname}-mkgrkindex
Provides: tex-mkgrkindex = %{epoch}:%{source_date}-%{release}
Provides: texlive-mkgrkindex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-mkgrkindex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mkgrkindex-bin < 7:20170520
Provides: tex-mkgrkindex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-mkgrkindex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mkgrkindex-doc < 7:20170520
License: LPPL
Summary: Makeindex working with Greek
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-mkgrkindex
Makeindex is resolutely stuck with Latin-based alphabets, so
will not deal with Greek indexes, unaided. This package
provides a Perl script that will transmute the index of a Greek
document in such a way that makeindex will sort the entries
according to the rules of the Greek alphabet.

%package -n %{shortname}-mkjobtexmf
Provides: tex-mkjobtexmf = %{epoch}:%{source_date}-%{release}
Provides: texlive-mkjobtexmf-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-mkjobtexmf-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mkjobtexmf-bin < 7:20170520
Provides: tex-mkjobtexmf-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-mkjobtexmf-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mkjobtexmf-doc < 7:20170520
License: GPLv2 or Artistic
Summary: Generate a texmf tree for a particular job
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-mkjobtexmf
The package provides a Perl script, which runs a program and
tries to find the names of file used. Two methods are
available, option -recorder of (Web2C) TeX and the program
strace. Then it generates a directory with a texmf tree. It
checks the found files and tries sort them in this texmf tree.
The script may be used for archiving purposes or to speed up
later TeX runs.

%package -n %{shortname}-mkpic
Provides: tex-mkpic = %{epoch}:%{source_date}-%{release}
Provides: texlive-mkpic-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-mkpic-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mkpic-bin < 7:20170520
Provides: tex-mkpic-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-mkpic-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mkpic-doc < 7:20170520
License: GPL+
Summary: Perl interface to mfpic
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-mkpic
mkpic provides an easy interface for making small pictures with
mfpic. To this end you create an input file consisting of
commands, one per line, with space separated parameters (or you
modify the DATA section of the mkpic script, which is used if
you run it without an input file). For an extensive description
see the file mkpicdoc.pdf, which is part of the distribution.

%package -n %{shortname}-mltex
Provides: tex-mltex = %{epoch}:%{source_date}-%{release}
Provides: texlive-mltex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-mltex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mltex-bin < 7:20170520
Provides: tex-mltex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-mltex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mltex-doc < 7:20170520
License: Knuth
Summary: The MLTeX system
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-latex
Requires: texlive-pdftex
Requires: texlive-cm
Requires: texlive-hyphen-base
Requires: texlive-babel
Requires: texlive-dehyph
Requires: texlive-hyph-utf8
Requires: texlive-l3kernel
Requires: texlive-latexconfig
Requires: texlive-latex-fonts
Requires: texlive-unicode-data
Requires: texlive-knuth-lib
Requires: texlive-plain
Requires(post,postun): coreutils
Provides: tex(lo1enc.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(mlltxchg.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(mltex.sty) = %{epoch}:%{source_date}-%{release}
# symlinks
BuildArch: noarch

%description -n %{shortname}-mltex
MLTeX is a modification of TeX version >=3.0 that allows the
hyphenation of words with accented letters using ordinary
Computer Modern (CM) fonts. The system is distributed as a TeX
change file.

%package -n %{shortname}-mptopdf
Provides: tex-mptopdf = %{epoch}:%{source_date}-%{release}
Provides: texlive-mptopdf-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-mptopdf-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mptopdf-bin < 7:20170520
Provides: tex-mptopdf-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-mptopdf-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-mptopdf-doc < 7:20170520
License: LPPL
Summary: mpost to PDF, native MetaPost graphics inclusion
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-plain
Requires(post,postun): coreutils
Provides: tex(mptopdf.tex) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-mptopdf
The mptopdf script does standalone conversion from mpost to
PDF, using the supp-* and syst-* files.  They also allow native
MetaPost graphics inclusion in LaTeX (via pdftex.def) and
ConTeXt.  They can be used independently of the rest of
ConTeXt, yet are maintained as part of it.  So in TeX Live we
pull them out to this separate package for the benefit of LaTeX
users who do not install the rest of ConTeXt.  This can be
found on CTAN in macros/pdftex/graphics.

%package -n %{shortname}-multibibliography
Provides: tex-multibibliography = %{epoch}:%{source_date}-%{release}
Provides: texlive-multibibliography-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-multibibliography-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-multibibliography-bin < 7:20170520
Provides: tex-multibibliography-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-multibibliography-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-multibibliography-doc < 7:20170520
License: LPPL 1.3
Summary: Multiple versions of a bibliography, with different sort orders
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(multibibliography.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-multibibliography
Conventional standards for bibliography styles impose a forced
choice between index and name/year citations, and corresponding
references. The package avoids this choice, by providing
alphabetic, sequenced, and even chronological orderings of
references. Inline citations, that integrate these
heterogeneous styles, are also supported (and work with other
bibliography packages).

%package -n %{shortname}-musixtex
Provides: tex-musixtex = %{epoch}:%{source_date}-%{release}
Provides: texlive-musixtex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-musixtex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-musixtex-bin < 7:20170520
Provides: tex-musixtex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-musixtex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-musixtex-doc < 7:20170520
License: GPLv2+
Summary: Sophisticated music typesetting
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(musixadd.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixadf.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixbar.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixbbm.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixblx.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixbm.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixcho.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixcpt.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixcrd.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixdat.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixdbr.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixdia.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixec.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixeng.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixesf.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixevo.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixext.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixfll.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixgre.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixgui.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixhor.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixhou.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixhv.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixinv.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixlit.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixlyr.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixmad.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixper.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixplt.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixpoi.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixppff.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixps.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixref.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixslu.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixsqr.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixste.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixstf.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixstr.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixsty.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixtex.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixtmr.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixtri.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixcpt.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixcrd.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixfll.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixltx.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(musixtex.sty) = %{epoch}:%{source_date}-%{release}
# lua
BuildArch: noarch

%description -n %{shortname}-musixtex
MusiXTeX provides a set of macros, based on the earlier
MusicTeX, for typesetting music with TeX. To produce optimal
spacing, MusixTeX is a three-pass system: etex, musixflx, and
etex again. (Musixflx is a lua script that is provided in the
bundle.) The three-pass process, optionally followed by
processing for printed output, is automated by the musixtex
wrapper script. The package uses its own specialised fonts,
which must be available on the system for musixtex to run. This
version of MusixTeX builds upon work by Andreas Egler, whose
own version is no longer being developed. The MusiXTeX macros
are universally acknowledged to be challenging to use directly:
the pmx preprocessor compiles a simpler input language to
MusixTeX macros.

%package -n %{shortname}-musixtnt
Provides: tex-musixtnt = %{epoch}:%{source_date}-%{release}
Provides: texlive-musixtnt-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-musixtnt-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-musixtnt-bin < 7:20170520
Provides: tex-musixtnt-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-musixtnt-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-musixtnt-doc < 7:20170520
License: GPLv2+
Summary: A MusiXTeX extension library that enables transformations of the effect of notes commands
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-musixtex
Provides: tex(musixtnt.tex) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-musixtnt
The package includes an archive containing a MusiXTeX extension
library musixtnt, and documentation for a program:
msxlint. musixtnt.tex provides a macro \TransformNotes that
enables transformations of the effect of notes commands such
as \notes. In general, the effect of
\TransformNotes{input}{output} is that notes commands in the
source will expect their arguments to match the input pattern,
but the notes will be typeset according to the output pattern.
An example is extracting single-instrument parts from a multi-
instrument score. msxlint detects incorrectly formatted notes
lines in a MusiXTeX source file. This should be used before
using \TransformNotes.

%package -n %{shortname}-m-tx
Provides: tex-m-tx = %{epoch}:%{source_date}-%{release}
Provides: texlive-m-tx-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-m-tx-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-m-tx-bin < 7:20170520
Provides: tex-m-tx-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-m-tx-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-m-tx-doc < 7:20170520
License: GPL+
Summary: A preprocessor for pmx
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(mtx.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(mtxlatex.sty) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-m-tx
M-Tx is a preprocessor to pmx, which is itself a preprocessor
to musixtex, a music typesetting system. The prime motivation
to the development of M-Tx was to provide lyrics for music to
be typeset. In fact, pmx now provides a lyrics interface, but M-
Tx continues in use by those who prefer its language.

%package -n %{shortname}-oberdiek
Provides: tex-oberdiek = %{epoch}:%{source_date}-%{release}
Provides: tex-oberdiek-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-oberdiek-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-oberdiek-doc < 7:20170520
License: LPPL
Summary: A bundle of packages submitted by Heiko Oberdiek
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-auxhook
Requires: texlive-grfext
Requires: texlive-grffile
Requires: texlive-iftex
Requires: texlive-kvoptions
Requires: texlive-infwarerr
Requires: texlive-pdftexcmds
# To complete the bundle
Requires: tex(ifluatex.sty)
Requires: tex(intcalc.sty)
Requires: tex(ifpdf.sty)
Requires: tex(etexcmds.sty)
Requires: tex(kvoptions.sty)
Requires: tex(ifxetex.sty)
Requires: tex(etex.sty)
Requires: tex(color.sty)
Requires: tex(keyval.sty)
Requires: tex(soul.sty)
Requires: tex(remreset.sty)
Requires: tex(makematch.sty)
Requires: tex(zref-lastpage.sty)
Requires: tex(hyperref.sty)
Requires: tex(fp-basic.sty)
Requires: tex(fp-snap.sty)
Requires: tex(graphics.sty)
Requires: tex(amsmath.sty)
Requires: tex(grfext.sty)
Requires: tex(hypdoc.sty)
Requires: tex(array.sty)
Requires: tex(fontspec.sty)
Requires: tex(unicode-math.sty)
Requires: tex(doc.sty)
Requires: tex(calc.sty)
Requires: tex(thumbpdf.sty)
Requires: tex(inputenc.sty)
Requires: tex(listings.sty)
Requires: tex(tikz.sty)
Requires: tex(everyshi.sty)
Requires: tex(parallel.sty)
Requires: tex(parcolumns.sty)
Requires: tex(lscape.sty)
Requires: tex(index.sty)
Requires: tex(zref-pagelayout.sty)
Provides: tex(aliascnt.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(bmpsize-base.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(bmpsize-dvipdfm.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(bmpsize-dvipdfmx.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(bmpsize-dvips.def) = %{epoch}:%{source_date}-%{release}
Provides: tex(bmpsize.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(bmpsize-test.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(centernot.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(chemarr.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(classlist.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(colonequals.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvipscol.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(engord.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(enparen.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(eolgrab.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(fibnum.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(flags.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(holtxdoc.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(hopatch.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(hypbmsec.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(hypcap.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(hypdestopt.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(hypdoc.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(hypgotoe.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(hyphsubst.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(ifdraft.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(iflang.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(pagegrid.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(pagesel.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfcolfoot.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfcolparallel.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfcolparcolumns.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfcol.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfcrypt.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfrender.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(protecteddef.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(resizegather.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(rotchiffre.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(scrindex.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(setouterhbox.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(settobox.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(stackrel.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(stampinclude.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(tabularht.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(tabularkv.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(telprint.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(thepdfnumber.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(twoopt.sty) = %{epoch}:%{source_date}-%{release}
BuildArch: noarch

%description -n %{shortname}-oberdiek
The bundle comprises packages to provide: aliascnt: 'alias
counters'; bmpsize: get bitmap size and resolution data;
centernot: a horizontally-centred \not symbol; chemarr:
extensible chemists' reaction arrows; classlist: record
information about document class(es) used; colonequals: poor
man's mathematical relation symbols; dvipscol: dvips colour
stack management; engord: define counter-printing operations
producing English ordinals; eolgrab: collect arguments
delimited by end of line; flags: setting and clearing flags in
bit fields and converting the bit field into a decimal number;
holtxdoc: extra documentation macros; hopatch: safely apply
package patches; hypbmsec: bookmarks in sectioning commands;
hypcap: anjusting anchors of captions; hypdestopt: optimising
hyperref's pdfTeX driver destinations; hypdoc: hyper-references
in the LaTeX standard doc package; hypgotoe: experimental
package for links to embedded files; hyphsubst: substitute
hyphenation patterns; ifdraft: switch for option draft; iflang:
provides expandable checks for the current language; pagegrid:
prints a page grid in the background; pagesel: select pages of
a document for output; pdfcolfoot: using pdfTeX's color stack
for footnotes; pdfcol: macros for setting and maintaining new
color stacks; pdfcolparallel: fixes colour problems in package
parallel; pdfcolparcolumns: fixes colour problems in package
parcolumns; pdfcrypt: setting PDF encryption; pdfrender:
control PDF rendering modes; protecteddef: define a command
that protected against expansion; resizegather: automatically
resize overly large equations; rotchiffre: performs simple
rotation cyphers; scrindex: redefines environment 'theindex' of
package 'index', if a class from KOMA-Script is loaded;
setouterhbox: set \hbox in outer horizontal mode; settobox:
getting box sizes; soul and adds some support for UTF-8;
stackrel: extensions of the \stackrel command; stampinclude:
selects the files for \include by inspecting the timestamp of
the .aux file(s); tabularht: tabulars with height
specification; tabularkv: key value interface for tabular
parameters; telprint: print German telephone numbers;
thepdfnumber: canonical numbers for use in PDF files and
elsewhere; twoopt: commands with two optional arguments; Each
of the packages is represented by two files, a .dtx (documented
source) and a PDF file; the .ins file necessary for
installation is extracted by running the .dtx file with Plain
TeX.

%package -n %{shortname}-omegaware
Provides: tex-omegaware = %{epoch}:%{source_date}-%{release}
Provides: texlive-omegaware-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-omegaware-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-omegaware-bin < 7:20170520
Provides: tex-omegaware-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-omegaware-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-omegaware-doc < 7:20170520
License: LPPL
Summary: Omegaware package
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-omegaware
Omegaware package.

%package -n %{shortname}-optex
License: Public Domain
Summary: LuaTeX format based on Plain TeX and OPmac
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-amsfonts
Requires: texlive-cm
Requires: texlive-ec
Requires: texlive-hyphen-base
Requires: texlive-lm
Requires: texlive-luatex
Requires: texlive-rsfs

%description -n %{shortname}-optex
OpTeX is a LuaTeX format based on Plain TeX macros with power
from OPmac (fonts selection system, colors, external graphics,
references, hyperlinks, ...) with unicode fonts.

%package -n %{shortname}-patgen
Provides: tex-patgen = %{epoch}:%{source_date}-%{release}
Provides: texlive-patgen-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-patgen-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-patgen-bin < 7:20170520
License: Knuth
Summary: Generate hyphenation patterns
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-patgen
This is the last version of the program distributed by Knuth;
it advertises itself as a pattern generator for "the algorithm
used in TeX", but, of course, the patterns used in modern
distributions are Unicode-based.

%package -n %{shortname}-pax
Provides: tex-pax = %{epoch}:%{source_date}-%{release}
Provides: texlive-pax-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-pax-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pax-bin < 7:20170520
Provides: tex-pax-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pax-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pax-doc < 7:20170520
License: GPLv2+
Summary: Extract and reinsert PDF annotations with pdfTeX
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(ifpdf.sty)
Requires: tex(graphicx.sty)
Requires: tex(ltxcmds.sty)
Requires: tex(kvsetkeys.sty)
Requires: tex(kvoptions.sty)
Requires: tex(auxhook.sty)
Requires: tex(etexcmds.sty)
Provides: tex(pax.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-pax
If PDF files are included using pdfTeX, PDF annotations are
stripped. The pax project offers a solution without altering
pdfTeX. A Java program (pax.jar) parses the PDF file that will
later be included. The program then writes the data of the
annotations into a file that can be read by TeX. The LaTeX
package pax extends the graphics package to support the scheme:
if a PDF file is included, the package looks for the file with
the annotation data, reads them and puts the annotations in the
right place.

%package -n %{shortname}-pdfbook2
Provides: tex-pdfbook2 = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdfbook2-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-pdfbook2-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdfbook2-bin < 7:20170520
Provides: tex-pdfbook2-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdfbook2-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdfbook2-doc < 7:20170520
License: GPLv3+
Summary: Create booklets from PDF files
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-pdfcrop
Requires: texlive-pdfjam
# python
BuildArch: noarch

%description -n %{shortname}-pdfbook2
This python program creates print-ready PDF files from some
input PDF files for booklet printing. The resulting files need
to be printed in landscape/long edge double sided printing. The
default paper format depends on the locale and is chosen by
pdfjam. It can be chosen using the --paper option. Before the
pdf is composed, the input file is cropped to the relevant area
in order to discard unnecessary white spaces. In this process,
all pages are cropped to the same dimensions. Extra margins can
be defined at the edges of the booklet and in the middle where
the binding occurs. The output is written to INPUT-book.pdf.
Existing files will be overwritten. All input files are
processed seperately.

%package -n %{shortname}-pdfcrop
Provides: tex-pdfcrop = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdfcrop-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-pdfcrop-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdfcrop-bin < 7:20170520
Provides: tex-pdfcrop-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdfcrop-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdfcrop-doc < 7:20170520
License: LPPL
Summary: Crop PDF graphics
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-pdfcrop
A Perl script that can either trim pages of any whitespace
border, or trim them of a fixed border.

%package -n %{shortname}-pdfjam 
Provides: tex-pdfjam = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdfjam-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-pdfjam-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdfjam-bin < 7:20170520
Provides: tex-pdfjam-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdfjam-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdfjam-doc < 7:20170520
License: GPLv2+
Summary: Shell scripts interfacing to pdfpages
Requires: texlive-base
Requires: texlive-collection-latex
Requires: texlive-kpathsea
Requires: texlive-latex
Requires: tex(pdfpages.sty)
# shell
BuildArch: noarch

%description -n %{shortname}-pdfjam
This is a collection of shell scripts which provide an
interface to the pdfpages LaTeX package. They do such jobs as
selecting pages, concatenating files, doing n-up formatting,
and so on.

%package -n %{shortname}-pdflatexpicscale
Provides: tex-pdflatexpicscale = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdflatexpicscale-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-pdflatexpicscale-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdflatexpicscale-bin < 7:20170520
Provides: tex-pdflatexpicscale-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdflatexpicscale-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdflatexpicscale-doc < 7:20170520
License: LPPL
Summary: Support software for downscaling graphics to be included by pdfLaTeX
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-pdflatexpicscale
The package provides a script to scale pictures down to a
target resolution before creating a PDF document with pdfLaTeX.

%package -n %{shortname}-pdftex
Provides: tex-pdftex = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdftex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-pdftex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdftex-bin < 7:20170520
Provides: tex-pdftex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdftex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdftex-doc < 7:20170520
License: GPL+
Summary: A TeX extension for direct creation of PDF
Requires: texlive-base
Requires: texlive-kpathsea
Requires(post,postun): coreutils
Requires: tex-graphics-def
Requires: texlive-cm
Requires: texlive-dehyph
Requires: texlive-etex
Requires: texlive-hyph-utf8
Requires: texlive-hyphen-base
Requires: texlive-knuth-lib
Requires: texlive-plain
Requires: tex-tex-ini-files
Provides: tex(dummy-space.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(dummy-space.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dummy-space.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdftex-dvi.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(glyphtounicode.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pdfcolor.tex) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-pdftex
An extension of TeX which can be configured to directly
generate PDF documents instead of DVI. All current free TeX
distributions including TeX live, MacTeX and MiKTeX include
pdfTeX (Plain TeX) and pdfLaTeX (LaTeX). ConTeXt was designed
around use of pdfTeX (though it is now migrating towards
LuaTeX).

%package -n %{shortname}-pdftex-quiet
Provides: tex-pdftex-quiet = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdftex-quiet-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-pdftex-quiet-bin = %{epoch}:%{source_date}-%{release}
License: GPLv3
Summary: Bash utility to reduce the output of the pdftex command
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-pdftex
#bash
BuildArch: noarch

%description -n %{shortname}-pdftex-quiet
This is a tool in BASH serving to reduce the output of `pdftex` command and see
only relevant errors in red bold font to fight them ASAP.

%package -n %{shortname}-pdftosrc
Provides: tex-pdftosrc = %{epoch}:%{source_date}-%{release}
Provides: tex-pdftosrc-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdftosrc-bin = %{epoch}:%{source_date}-%{release}
License: GPLv2+
Summary: Extract source file or stream from PDF file
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-pdftosrc
Extracts an embedded source file, or extracts and uncompresses
a PDF stream given by object number. Developed as part of the
pdfTeX source tree.

%package -n %{shortname}-pdfxup
Provides: tex-pdfxup = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdfxup-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-pdfxup-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdfxup-bin < 7:20170520
Provides: tex-pdfxup-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pdfxup-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pdfxup-doc < 7:20170520
License: LPPL
Summary: Create n-up PDF pages with minimal margins
Requires: texlive-base
Requires: texlive-kpathsea
# shell
BuildArch: noarch

%description -n %{shortname}-pdfxup
pdfxup is a unix/linux shell script that creates a PDF document
where each page is obtained by combining several pages of a PDF
file given as output.

%package -n %{shortname}-pedigree-perl
Provides: tex-pedigree-perl = %{epoch}:%{source_date}-%{release}
Provides: texlive-pedigree-perl-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-pedigree-perl-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pedigree-perl-bin < 7:20170520
Provides: tex-pedigree-perl-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pedigree-perl-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pedigree-perl-doc < 7:20170520
License: GPLv2+
Summary: Generate TeX pedigree files from CSV files
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-pedigree-perl
This program generates TeX commands to typeset pedigrees --
either TeX fragments or full LaTeX files, to be processed by
the authors' pst-pdgr package. The program has support for
multilanguage pedigrees (at the present moment the English and
Russian languages are supported).

%package -n %{shortname}-perltex
Provides: tex-perltex = %{epoch}:%{source_date}-%{release}
Provides: texlive-perltex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-perltex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-perltex-bin < 7:20170520
Provides: tex-perltex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-perltex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-perltex-doc < 7:20170520
License: LPPL
Summary: Define LaTeX macros in terms of Perl code
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(perltex.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-perltex
PerlTeX is a combination Perl script (perltex.pl) and LaTeX2e
package (perltex.sty) that, together, give the user the ability
to define LaTeX macros in terms of Perl code. Once defined, a
Perl macro becomes indistinguishable from any other LaTeX
macro. PerlTeX thereby combines LaTeX's typesetting power with
Perl's programmability. PerlTeX will make use of persistent
named pipes, and thereby run more efficiently, on operating
systems that offer them (mostly Unix-like systems). Also
provided is a switch to generate a PerlTeX-free, document-
specific, noperltex.sty that is useful when distributing a
document to places where PerlTeX is not available.

%package -n %{shortname}-petri-nets
Provides: tex-petri-nets = %{epoch}:%{source_date}-%{release}
Provides: texlive-petri-nets-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-petri-nets-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-petri-nets-bin < 7:20170520
Provides: tex-petri-nets-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-petri-nets-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-petri-nets-doc < 7:20170520
License: GPL+
Summary: A set of TeX/LaTeX packages for drawing Petri nets
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(pndraw.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(pndraw.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pnets.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(pnets.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pntext.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(pntext.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pnversion.tex) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-petri-nets
Petri-nets offers a set of TeX/LaTeX packages about Petri nets
and related models. Three packages are available: the first
allows the user to draw Petri-nets in PostScript documents; the
second defines macros related to PBC, M-nets and B(PN) models;
and a third that combines the other two.

%package -n %{shortname}-pfarrei
Provides: tex-pfarrei = %{epoch}:%{source_date}-%{release}
Provides: texlive-pfarrei-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-pfarrei-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pfarrei-bin < 7:20170520
Provides: tex-pfarrei-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pfarrei-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pfarrei-doc < 7:20170520
License: LPPL 1.3
Summary: LaTeX support of pastors' and priests' work
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(ifpdf.sty)
Requires: tex(pdfpages.sty)
Requires: tex(keyval.sty)
Provides: tex(a5toa4.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(pfarrei.sty) = %{epoch}:%{source_date}-%{release}
# lua
BuildArch: noarch

%description -n %{shortname}-pfarrei
In "Die TeXnische Komodie" (issue 1/2013) Christian Justen
described his use of LaTeX in his work as priest (similar
requirements may be encountered in the work of pastors and
other ministers of religion). One point was to arrange A5 pages
onto A4 landscape paper, either side-by-side or as a booklet.
Justen made two bash scripts for this job; the package provides
one texlua script for both requirements.

%package -n %{shortname}-pkfix
Provides: tex-pkfix = %{epoch}:%{source_date}-%{release}
Provides: tex-pkfix-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-pkfix-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pkfix-bin < 7:20170520
Provides: tex-pkfix-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pkfix-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pkfix-doc < 7:20170520
License: LPPL 1.3
Summary: Replace pk fonts in PostScript with Type 1 fonts
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-pkfix
The perl script pkfix looks for DVIPSBitmapFont comments in
PostScript files, generated by 'not too old' dvips, and
replaces them by type 1 versions of the fonts, if possible.

%package -n %{shortname}-pkfix-helper
Provides: tex-pkfix-helper = %{epoch}:%{source_date}-%{release}
Provides: tex-pkfix-helper-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-pkfix-helper-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pkfix-helper-bin < 7:20170520
Provides: tex-pkfix-helper-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pkfix-helper-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pkfix-helper-doc < 7:20170520
License: LPPL
Summary: Make PostScript files accessible to pkfix
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-pkfix-helper
Pkfix is a useful utility for replacing resolution-dependent
bitmapped fonts in a dvips-produced PostScript file with the
corresponding resolution-independent vector fonts.
Unfortunately, pkfix needs to parse certain PostScript comments
that appear only in files produced by dvips versions later than
5.58 (ca. 1996); it fails to work on PostScript files produced
by older versions of dvips. Pkfix-helper is a program that
attempts to insert newer-dvips comments into an older-dvips
PostScript file, thereby making the file suitable for
processing by pkfix. pkfix-helper can sometimes process
documents fully autonomously but does require the user to
verify and, if needed, correct its decisions.

%package -n %{shortname}-pmx
Provides: tex-pmx = %{epoch}:%{source_date}-%{release}
Provides: tex-pmx-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-pmx-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pmx-bin < 7:20170520
Provides: tex-pmx-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pmx-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pmx-doc < 7:20170520
License: GPLv2+
Summary: Preprocessor for MusiXTeX
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(pmx.tex) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-pmx
PMX is a preprocessor for MusiXTeX. It builds the TeX input
file from a file in a much simpler language, making most of the
layout decisions by itself. An auxiliary program makes single-
player parts from a multi-player score. For proof-listening,
PMX can make a MIDI file of your score. The present version
requires at least version 1.15 of MusiXTeX, running on an e-tex-
enhanced TeX system.

%package -n %{shortname}-pmxchords
Provides: tex-pmxchords = %{epoch}:%{source_date}-%{release}
Provides: tex-pmxchords-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-pmxchords-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pmxchords-bin < 7:20170520
Provides: tex-pmxchords-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pmxchords-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pmxchords-doc < 7:20170520
License: GPLv2+
Summary: Produce chord information to go with pmx output
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(chords.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(chordsCZ.tex) = %{epoch}:%{source_date}-%{release}
# lua
BuildArch: noarch

%description -n %{shortname}-pmxchords
The bundle supplements pmx, providing the means of typesetting
chords above the notes of a score. The bundle contains: macros
for typing the chords; a Lua script to transpose chord macros
to the required key signature; and support scripts for common
requirements.

%package -n %{shortname}-psutils
Provides: tex-psutils = %{epoch}:%{source_date}-%{release}
Provides: tex-psutils-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-psutils-bin = %{epoch}:%{source_date}-%{release}
License: psutils
Summary: The TeXLive fork of the PS Utilities
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-psutils
Utilities for manipulating PostScript documents.
Page selection and rearrangement are supported, including arrangement into
signatures for booklet printing, and page merging for n-up printing.

This package contains a fork of the psutils binaries adjusted for TexLive.
All of the standard binaries have been namespaced with a "tl-" prefix.

%package -n %{shortname}-pst2pdf
Provides: tex-pst2pdf = %{epoch}:%{source_date}-%{release}
Provides: tex-pst2pdf-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-pst2pdf-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pst2pdf-bin < 7:20170520
Provides: tex-pst2pdf-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pst2pdf-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pst2pdf-doc < 7:20170520
License: GPLv2+
Summary: A script to compile pstricks documents via pdftex
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-pst2pdf
The script extracts the preamble of the document and runs all
\begin{postscript}...\end{postscript}
\begin{pspicture}...\end{pspicture} and
\pspicture...\endpspicture separately through LaTeX with the
same preamble as the original document; thus it creates EPS,
PNG and PDF files of these snippets. In a final PDFLaTeX run
the script replaces the environments with \includegraphics to
include the processed snippets.

%package -n %{shortname}-pst-pdf
Provides: tex-pst-pdf = %{epoch}:%{source_date}-%{release}
Provides: tex-pst-pdf-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-pst-pdf-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pst-pdf-bin < 7:20170520
Provides: tex-pst-pdf-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pst-pdf-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pst-pdf-doc < 7:20170520
License: LPPL
Summary: Make PDF versions of graphics by processing between runs
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(graphicx.sty)
Requires: tex(pstricks.sty)
Requires: tex(environ.sty)
Provides: tex(pst-pdf.sty) = %{epoch}:%{source_date}-%{release}
# shell
BuildArch: noarch

%description -n %{shortname}-pst-pdf
The package pst-pdf simplifies the use of graphics from
PSTricks and other PostScript code in PDF documents. As in
building a bibliography with BibTEX, additional external
programmes are invoked. In this case they are used to create a
PDF file (\PDFcontainer) that will contain all the graphics
material. In the final document these contents will be inserted
instead of the original PostScript code. The package works with
pstricks and requires a recent version of the preview package.

%package -n %{shortname}-ps2eps
Provides: tex-ps2eps = %{epoch}:%{source_date}-%{release}
License: GPL+
Summary: Produce Encapsulated PostScript from PostScript
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-ps2eps
Produce Encapsulated PostScript Files (EPS/EPSF) from a
one-page PostScript document, or any PostScript document. A
correct Bounding Box is calculated for the EPS files and some
PostScript command sequences that can produce erroneous
results on printers are filtered. The input is cropped to
include just the image contained in the PostScript file. The
EPS files can then be included into TeX documents. Other
programs like ps2epsi (a script distributed with ghostscript)
don't always calculate the correct bounding box (because the
values are put on the PostScript stack which may get corrupted
by bad PostScript code) or they round it off, resulting in
clipping the image. Therefore ps2eps uses a resolution of 144
dpi to get the correct bounding box. Included in the distribution
is the bbox program, an application to produce Bounding Box values
for rawppm or rawpbm format files.

%package -n %{shortname}-ps2pk
Provides: tex-ps2pk = %{epoch}:%{source_date}-%{release}
Provides: tex-ps2pk-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-ps2pk-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ps2pk-bin < 7:20170520
Provides: texlive-ps2pkm = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ps2pkm < 7:20170520
Provides: texlive-ps2pkm-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ps2pkm-bin < 7:20170520
License: MIT
Summary: Generate a PK font from an Adobe Type 1 font
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-ps2pk
Generates a PK file from an Adobe Type 1 font. PK fonts are (or
used to be) valuable in enabling previewers to view documents
generated that use Type 1 fonts. The program makes use of code
donated to the X consortium by IBM.

%package -n %{shortname}-ptex
Provides: tex-ptex = %{epoch}:%{source_date}-%{release}
Provides: tex-ptex-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-ptex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ptex-bin < 7:20170520
Provides: tex-ptex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-ptex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ptex-doc < 7:20170520
Provides: texlive-platex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-platex-bin < 7:20170520
License: BSD
Summary: A TeX system for publishing in Japanese
Requires: texlive-adobemapping
Requires: texlive-base
Requires: texlive-cm
Requires: texlive-etex
Requires: texlive-hyphen-base
Requires: texlive-hyph-utf8
Requires: texlive-ipaex
Requires: texlive-japanese-otf
Requires: texlive-knuth-lib
Requires: texlive-kpathsea
Requires: texlive-latex
Requires: texlive-plain
Requires: texlive-ptex-base
Requires: texlive-ptex-fonts
Requires: texlive-tex
Requires: tex(oldlfont.sty)
Requires: tex(shortvrb.sty)
Requires(post,postun): coreutils
Provides: tex(morisawa.map) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-ptex
PTeX adds features related to vertical writing, and deals with
other problems in typesetting Japanese. A set of additions to a
TEXMF tree, for use with PTeX, may be found in package PTeX-
texmf. PTeX is distributed as WEB change files.

%package -n %{shortname}-ptex-fontmaps
Provides: tex-ptex-fontmaps = %{epoch}:%{source_date}-%{release}
Provides: tex-ptex-fontmaps = %{epoch}:%{source_date}-%{release}
Provides: texlive-ptex-fontmaps-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ptex-fontmaps-bin < 7:20170520
Provides: tex-ptex-fontmaps-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-ptex-fontmaps-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ptex-fontmaps-doc < 7:20170520
Provides: tex-jfontmaps = %{epoch}:%{source_date}-%{release}
Provides: texlive-jfontmaps = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-jfontmaps <= 6:svn40613
Provides: tex-jfontmaps-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-jfontmaps-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-jfontmaps-bin <= 6:svn29848.0
Provides: tex-jfontmaps-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-jfontmaps-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-jfontmaps-doc <= 6:svn40613
License: GPLv3
Summary: Font maps and configuration tools for Japanese/Chinese/Korean fonts with (u)ptex
Requires: texlive-arphic-ttf
Requires: texlive-baekmuk
Requires: texlive-base
Requires: texlive-ipaex
Requires: texlive-kpathsea
# shell and perl
BuildArch: noarch

%description -n %{shortname}-ptex-fontmaps
This package provides font maps and setup tools for Japanese,
Korean, Traditional Chinese, and Simplified Chinese. It is the
successor of the jfontmaps package. The files in this package
contain font maps for dvipdfmx to make various
Japanese/Chinese/Korean fonts available for (u)ptex and related
programs and formats.

%package -n %{shortname}-ptex2pdf
Provides: tex-ptex2pdf = %{epoch}:%{source_date}-%{release}
Provides: tex-ptex2pdf-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-ptex2pdf-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ptex2pdf-bin < 7:20170520
Provides: tex-ptex2pdf-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-ptex2pdf-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ptex2pdf-doc < 7:20170520
License: GPLv2+
Summary: Convert Japanese TeX documents to PDF
Requires: texlive-base
Requires: texlive-kpathsea
# lua
BuildArch: noarch

%description -n %{shortname}-ptex2pdf
The Lua script provides system-independent support of Japanese
typesetting engines in TeXworks. As TeXworks typesetting setup
does not allow for multistep processing, this script runs one
of the ptex-based programs (ptex, uptex, eptex, platex,
uplatex) followed by dvipdfmx.

%package -n %{shortname}-purifyeps
Provides: tex-purifyeps = %{epoch}:%{source_date}-%{release}
Provides: tex-purifyeps-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-purifyeps-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-purifyeps-bin < 7:20170520
Provides: tex-purifyeps-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-purifyeps-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-purifyeps-doc < 7:20170520
License: LPPL
Summary: Make EPS work with both LaTeX/dvips and pdfLaTeX
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-purifyeps
While pdfLaTeX has a number of nice features, its primary
shortcoming relative to standard LaTeX+dvips is that it is
unable to read ordinary Encapsulated PostScript (EPS) files,
the most common graphics format in the LaTeX world. Purifyeps
converts EPS files into a 'purified' form that can be read by
both LaTeX+dvips and pdfLaTeX. The trick is that the standard
LaTeX2e graphics packages can parse MetaPost-produced EPS
directly. Hence, purifyeps need only convert an arbitrary EPS
file into the same stylized format that MetaPost outputs.

%package -n %{shortname}-pygmentex
Provides: tex-pygmentex = %{epoch}:%{source_date}-%{release}
Provides: tex-pygmentex-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-pygmentex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pygmentex-bin < 7:20170520
Provides: tex-pygmentex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pygmentex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pythontex-doc < 7:20170520
License: LPPL 1.3
Summary: Use Pygments to format code listings in documents
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(fancyvrb.sty)
Requires: tex(color.sty)
Requires: tex(ifthen.sty)
Requires: tex(caption.sty)
Requires: tex(pgfkeys.sty)
Requires: tex(efbox.sty)
Requires: tex(mdframed.sty)
Requires: tex(fvextra.sty)
Provides: tex(pygmentex.sty) = %{epoch}:%{source_date}-%{release}
# python
BuildArch: noarch

%description -n %{shortname}-pygmentex
PygmenTeX is a Python-based LaTeX package that can be used for
typesetting code listings in a LaTeX document using Pygments.
Pygments is a generic syntax highlighter for general use in all
kinds of software such as forum systems, wikis or other
applications that need to prettify source code.

%package -n %{shortname}-pythontex
Provides: tex-pythontex = %{epoch}:%{source_date}-%{release}
Provides: tex-pythontex-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-pythontex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pythontex-bin < 7:20170520
Provides: tex-pythontex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-pythontex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-pythontex-doc < 7:20170520
License: LPPL 1.3
Summary: Run Python from within a document, typesetting the results
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(fancyvrb.sty)
Requires: tex(etex.sty)
Requires: tex(etoolbox.sty)
Requires: tex(xstring.sty)
Requires: tex(pgfopts.sty)
Requires: tex(newfloat.sty)
Requires: tex(currfile.sty)
Requires: tex(xcolor.sty)
Requires: tex(upquote.sty)
Provides: tex(pythontex.sty) = %{epoch}:%{source_date}-%{release}
# python
BuildArch: noarch

%description -n %{shortname}-pythontex
The package allows you to enter Python code within a LaTeX
document, execute the code, and access its output in the
original document. Python code is only executed when it has
been modified, or when it meets user-specified criteria. Code
may be divided into user-defined sessions, which automatically
run in parallel. Errors and warnings are synchronized with the
LaTeX document, so that they refer to the document's line
numbers. External dependencies can be tracked, so that code is
re-executed when the data it depends on is modified. PythonTeX
also provides syntax highlighting for code in LaTeX documents
via the Pygments syntax highlighter. The package provides a
depythontex utility, that creates a copy of the document in
which all Python code has been replaced by its output. This is
useful for journal submissions, sharing documents, and
conversion to other formats.

%package -n %{shortname}-rubik
Provides: tex-rubik = %{epoch}:%{source_date}-%{release}
Provides: tex-rubik-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-rubik-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-rubik-bin < 7:20170520
Provides: tex-rubik-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-rubik-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-rubik-doc < 7:20170520
License: LPPL 1.3
Summary: Document Rubik cube configurations and rotation sequences
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(tikz.sty)
Requires: tex(fancyvrb.sty)
Provides: tex(rubikcube.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(rubikrotation.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-rubik
The bundle provides two packages: rubikcube provides commands
for typesetting Rubik cubes and their transformations; and
rubikrotation which can process a sequence of Rubik rotation
moves, with the help of a Perl package executed via \write18
(shell escape) commands.

%package -n %{shortname}-seetexk
Provides: tex-seetexk = %{epoch}:%{source_date}-%{release}
Provides: tex-seetexk-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-seetexk-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-seetexk-bin < 7:20170520
License: MIT
Summary: Utilities for manipulating DVI files
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-seetexk
The collection comprises: dvibook, which will rearrange the
pages of a DVI file into 'signatures' as used when printing a
book; dviconcat, for concatenating pages of DVI file(s);
dviselect, which will select pages from one DVI file to create
a new DVI file; dvitodvi, which will rearrange the pages of a
DVI file to create a new file; and libtex, a library for
manipulating the files, from the old SeeTeX project. The
utilities are provided as C source with Imakefiles, and an MS-
DOS version of dvibook is also provided.

%package -n %{shortname}-spix
Summary: Yet another TeX compilation tool: simple, human readable, no option, no magic
License: GPLv3+
Requires: texlive-base texlive-kpathsea

%description -n %{shortname}-spix
SpiX offers a way to store information about the compilation
process for a tex file inside the tex file itself. Just write
the commands as comments in the tex files, and SpiX will
extract and run those commands. Everything is stored in the tex
file (so that you are not missing some piece of information
that is located somewhere else), in a human-readable format (no
need to know SpiX to understand it).

%package -n %{shortname}-splitindex
Provides: tex-splitindex = %{epoch}:%{source_date}-%{release}
Provides: tex-splitindex-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-splitindex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-splitindex-bin < 7:20170520
Provides: tex-splitindex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-splitindex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-splitindex-doc < 7:20170520
License: LPPL
Summary: Unlimited number of indexes
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(splitindex.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(splitidx.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-splitindex
SplitIndex consists of a LaTeX package, splitidx, and a small
program, splitindex. The package may be used to produce one
index or several indexes. Without splitindex (for example,
using the index package), the number of indexes is limited by
the number of TeX's output streams. But using the program you
may use even more than 16 indexes: splitidx outputs only a
single file \jobname.idx and the program splits that file into
several raw index files and calls your favorite index processor
for each of the files.

%package -n %{shortname}-srcredact
Provides: tex-srcredact = %{epoch}:%{source_date}-%{release}
Provides: tex-srcredact-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-srcredact-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-srcredact-bin < 7:20170520
Provides: tex-srcredact-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-srcredact-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-srcredact-doc < 7:20170520
License: GPLv2+
Summary: A tool for redacting sources
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-srcredact
This package provides a tool to keep a master source,
consisting of different "chunks" intended for different
audiences. The tool allows to extract the versions intended for
different audiences and to incorporate the changes made in any
of these versions into the master document. This work was
commissioned by the Consumer Financial Protection Bureau,
United States Treasury.

%package -n %{shortname}-sty2dtx
Provides: tex-sty2dtx = %{epoch}:%{source_date}-%{release}
Provides: tex-sty2dtx-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-sty2dtx-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-sty2dtx-bin < 7:20170520
Provides: tex-sty2dtx-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-sty2dtx-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-sty2dtx-doc < 7:20170520
License: GPLv3+
Summary: Create a .dtx file from a .sty file
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-sty2dtx
The package provides a Perl script that converts a .sty file
(LaTeX package) to .dtx format (documented LaTeX source), by
surrounding macro definitions with macro and macrocode
environments. The macro name is automatically inserted as an
argument to the macro environemnt. Code lines outside macro
definitions are wrapped only in macrocode environments. Empty
lines are removed. The script should not be thought to be fool
proof and 100% accurate but rather as a good start to the
business of making a .dtx file from an undocumented style file.
Full .dtx files are generated. A template based on the skeleton
file from 'dtxtut' is used. User level macros are added
automatically to the 'Usage' section of the .dtx file. A
corresponding .ins file can be generated as well.

%package -n %{shortname}-svn-multi
Provides: tex-svn-multi = %{epoch}:%{source_date}-%{release}
Provides: tex-svn-multi-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-svn-multi-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-svn-multi-bin < 7:20170520
Provides: tex-svn-multi-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-svn-multi-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-svn-multi-doc < 7:20170520
License: LPPL
Summary: Subversion keywords in multi-file LaTeX documents
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(kvoptions.sty)
Requires: tex(filehook.sty)
Requires: tex(currfile.sty)
Requires: tex(graphics.sty)
Requires: tex(pgf.sty)
Provides: tex(svn-multi.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(svnkw.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-svn-multi
This package lets you typeset keywords of the version control
system Subversion inside your LaTeX files anywhere you like.
Unlike the otherwise similar package svn the use of multiple
files for one LaTeX document is well supported. The package
uses the author's filehook and currfile packages. The package
interacts with an external Perl script, to retrieve information
necessary for the required output.

%package -n %{shortname}-synctex
Provides: tex-synctex = %{epoch}:%{source_date}-%{release}
Provides: tex-synctex-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-synctex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-synctex-bin < 7:20170520
License: LPPL
Summary: synctex package
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-synctex
synctex package.

%package -n %{shortname}-tex
Provides: tex-tex = %{epoch}:%{source_date}-%{release}
Provides: tex-tex-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-tex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-tex-bin < 7:20170520
License: Knuth
Summary: A sophisticated typesetting engine
Requires: texlive-base
Requires: texlive-cm
Requires: texlive-hyphen-base
Requires: texlive-knuth-lib
Requires: texlive-kpathsea
Requires: texlive-plain
Requires(post,postun): coreutils

%description -n %{shortname}-tex
TeX is a typesetting system that incorporates a macro
processor. A TeX source document specifies or incorporates a
number of macro definitions that instruct the TeX engine how to
typeset the document. The TeX engine also uses font metrics
generated by Metafont, or by any of several other mechanisms
that incorporate fonts from other sources into an environment
suitable for TeX. TeX has been, and continues, a basis and an
inspiration for several other programs, including e-TeX and
PDFTeX.

%package -n %{shortname}-tex4ebook
Provides: tex-tex4ebook = %{epoch}:%{source_date}-%{release}
Provides: tex-tex4ebook-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-tex4ebook-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-tex4ebook-bin < 7:20170520
Provides: tex-tex4ebook-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-tex4ebook-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-tex4ebook-doc < 7:20170520
License: LPPL 1.3
Summary: Convertor from LaTeX to ebook formats
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(etoolbox.sty)
Requires: tex(kvoptions.sty)
Requires: tex(graphicx.sty)
Provides: tex(tex4ebook.sty) = %{epoch}:%{source_date}-%{release}
# lua
BuildArch: noarch

%description -n %{shortname}-tex4ebook
This is a bundle of lua scripts and LaTeX packages for
conversion of LaTeX files to ebook formats such as epub, mobi
and epub3. tex4ht is used as conversion engine.

%package -n %{shortname}-tex4ht
Provides: tex-tex4ht = %{epoch}:%{source_date}-%{release}
Provides: tex-tex4ht-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-tex4ht-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-tex4ht-bin < 7:20170520
Provides: tex-tex4ht-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-tex4ht-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-tex4ht-doc < 7:20170520
License: LPPL
Summary: Convert (La)TeX to HTML/XML
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(m-tex4ht.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(tex4ht.sty) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-tex4ht
A converter from TeX and LaTeX to SGML-based formats such as
(X)HTML, MathML, OpenDocument, and DocBook, providing a
configurable (La)TeX-based authoring system for hypertext.
Tex4ht does not parse (La)TeX source (so that it avoids the
difficulties encountered by many other converters, arising from
the irregularity of (La)TeX syntax). Instead, Tex4ht uses
(La)TeX itself (with an extra macro package) to produce a non-
standard DVI file that it can then process. This technique
allows TeX4ht to approach the robustness characteristic of
restricted-syntax systems such as hyperlatex and gellmu.

%package -n %{shortname}-texcount
Provides: tex-texcount = %{epoch}:%{source_date}-%{release}
Provides: tex-texcount-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texcount-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texcount-bin < 7:20170520
Provides: tex-texcount-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texcount-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texcount-doc < 7:20170520
License: LPPL
Summary: Count words in a LaTeX document
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-texcount
TeXcount is a Perl script that counts words in the text of
LaTeX files. It has rules for handling most of the common
macros, and can provide colour-coded output showing which parts
of the text have been counted. The package script is available
as a Web service via its home page.

%package -n %{shortname}-texdef
Provides: tex-texdef = %{epoch}:%{source_date}-%{release}
Provides: tex-texdef-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texdef-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texdef-bin < 7:20170520
Provides: tex-texdef-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texdef-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texdef-doc < 7:20170520
License: GPLv3+
Summary: Display the definitions of TeX commands
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-texdef
The (Perl) script displays the definition of (La)TeX command
sequences/macros. Various options allow the selection of the
used class and package files and other things which can have
influence on the definition (before/after the preamble, inside
an environment, ...). The script creates a temporary TeX file
which is then compiled using (La)TeX to find the '\meaning' of
the command sequence. The result is formatted and presented to
the user. Length or number command sequences (dimensions,
\char..., count registers, ...) are recognized and the
contained value is also shown (using \the). Special definitions
like protected macros are also recognized and the underlying
macros are shown as well. The script will show plain TeX
definitions by default. LaTeX and ConTeXt are supported,
including flavours (pdf(la)tex, lua(la)tex, xe(la)tex, ...).
The flavour can be selected using an command line option or
over the script name: latexdef will use LaTeX as default, etc.

%package -n %{shortname}-texdiff
Provides: tex-texdiff = %{epoch}:%{source_date}-%{release}
Provides: tex-texdiff-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texdiff-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texdiff-bin < 7:20170520
Provides: tex-texdiff-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texdiff-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texdiff-doc < 7:20170520
License: GPL+ or Artistic
Summary: Compares two (La)TeX documents to create a merged version showing changes
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-texdiff
Texdiff compares two (La)TeX documents to create a merged version showing
changes, similar to that of 'Change Tracking' in some word processors.

%package -n %{shortname}-texdirflatten
Provides: tex-texdirflatten = %{epoch}:%{source_date}-%{release}
Provides: tex-texdirflatten-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texdirflatten-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texdirflatten-bin < 7:20170520
License: GPL+ or Artistic
Summary: Collect files related to a LaTeX job in a single directory
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-texdirflatten
The Perl script parses a LaTeX file recursively, scanning all
child files, and collects details of any included and other
data files. These component files, are then all put into a
single directory (thus "flattening" the document's directory
tree).

%package -n %{shortname}-texdoc
Provides: tex-texdoc = %{epoch}:%{source_date}-%{release}
Provides: tex-texdoc-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texdoc-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texdoc-bin < 7:20170520
Provides: tex-texdoc-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texdoc-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texdoc-doc < 7:20170520
License: GPL+
Summary: Documentation access for TeX distributions
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(texdoc.cnf) = %{epoch}:%{source_date}-%{release}
# lua and perl
BuildArch: noarch

%description -n %{shortname}-texdoc
TeXdoc is an application for easy access to the package
documentation of a TeX distributions (i.e., .dvi, .pdf or .ps
files on the $TEXDOCS tree). It is distributed with TeX-Live
and a derivative is distributed with miktex.

%package -n %{shortname}-texdoctk
Provides: tex-texdoctk = %{epoch}:%{source_date}-%{release}
Provides: tex-texdoctk-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-texdoctk-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texdoctk-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texdoctk-doc = %{epoch}:%{source_date}-%{release}
License: GPL+
Summary: Easy access to package documentation
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(texdoctk.dat) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-texdoctk
A Perl/Tk-based GUI for easy access to package documentation
for TeX on Unix platforms; the databases it uses are based on
the texmf/doc subtrees of teTeX, but database files for local
configurations with modified/extended directories can be
derived from them. Note that texdoctk is not a viewer itself,
but an interface for finding documentation files and opening
them with the appropriate viewer; so it relies on appropriate
programs to be installed on the system. However, the choice of
these programs can be configured by the sysadmin or user. Now
only distributed as part of TeX Live, which includes a Windows
executable.

%package -n %{shortname}-texfot
Provides: tex-texfot = %{epoch}:%{source_date}-%{release}
Provides: tex-texfot-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texfot-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texfot-bin < 7:20170520
Provides: tex-texfot-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texfot-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texfot-doc < 7:20170520
License: Public Domain
Summary: Filter clutter from the output of a TeX run
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-texfot
The package provides a small Perl script to filter the online
output from a TeX run, attempting to show only those messages
which probably deserve some change in the source. The TeX
invocation itself need not change.

%package -n %{shortname}-texliveonfly
Provides: tex-texliveonfly = %{epoch}:%{source_date}-%{release}
Provides: tex-texliveonfly-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texliveonfly-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texliveonfly-bin < 7:20170520
Provides: tex-texliveonfly-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texliveonfly-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texliveonfly-doc < 7:20170520
License: GPLv3+
Summary: On-the-fly download of missing TeX live packages
Requires: texlive-base
Requires: texlive-kpathsea
# python
BuildArch: noarch

%description -n %{shortname}-texliveonfly
The package provides a script that performs 'on the fly'
downloads of missing packages, while a document is being
compiled. (This feature is already available in the MikTeX
distribution for Windows machines.) To use the script, replace
your (LaTeX) compilation command with texliveonfly.py file.tex
(default options are --engine=lualatex and --arguments="-
synctex=1 -interaction=nonstopmode", which may all be changed).
The script is designed to work on Linux distributions.

%package -n %{shortname}-texlive-en
Provides: tex-texlive-en = %{epoch}:%{source_date}-%{release}
Provides: tex-texlive-en-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texlive-en-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texlive-en-doc < 7:20170520
License: LPPL
Summary: TeX Live manual (English)
Requires: texlive-base
Requires: texlive-kpathsea
BuildArch: noarch

%description -n %{shortname}-texlive-en
TeX Live manual (English).

%package -n %{shortname}-texlive-scripts
Provides: tex-texlive-scripts = %{epoch}:%{source_date}-%{release}
Provides: texlive-texlive-scripts-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texlive-scripts-bin < 7:20170520
License: LPPL
Summary: TeX Live infrastructure programs
Requires: texlive-base
Requires: texlive-kpathsea = %{epoch}:%{source_date}-%{release}
Requires: texlive-texlive.infra
Provides: texlive-tetex = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-tetex < 7:20200327
# perl
BuildArch: noarch

%description -n %{shortname}-texlive-scripts
Includes install-tl, tl-portable, rungs, etc.; not needed for
tlmgr to run but still ours.  Not included in tlcritical.

%package -n %{shortname}-texlive-scripts-extra
Provides: tex-texlive-scripts-extra = %{epoch}:%{source_date}-%{release}
Provides: texlive-texlive-scripts-extra-bin = %{epoch}:%{source_date}-%{release}
License: GPL+ and LPPL and Public Domain
Summary: TeX Live scripts
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-texlive.infra
Obsoletes: texlive-texconfig < 7:20200327
Obsoletes: texlive-pstools < 7:20200327
Obsoletes: texlive-pdftools < 7:20200327
# perl and shell
BuildArch: noarch

%description -n %{shortname}-texlive-scripts-extra
Miscellaneous scripts maintained as part of TeX Live, but not important for
the infrastructure. Thus, this is not part of scheme-infraonly or tlcritical,
just a normal package.

%package -n %{shortname}-texlive.infra
Provides: tex-texlive.infra = %{epoch}:%{source_date}-%{release}
Provides: tex-texlive.infra-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texlive.infra-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texlive.infra-bin < 7:20170520
Provides: tex-texlive.infra-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texlive.infra-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texlive.infra-doc < 7:20170520
License: LPPL
Summary: Basic TeX Live infrastructure
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(fmtutil-hdr.cnf) = %{epoch}:%{source_date}-%{release}
Provides: tex(updmap-hdr.cfg) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-texlive.infra
This package contains the files needed to get the TeX Live
tools (notably tlmgr) running: perl modules, xz binaries, plus
(sometimes) tar and wget.  These files end up in the standalone
install packages, and in the tlcritical repository.

%package -n %{shortname}-texloganalyser
Provides: tex-texloganalyser = %{epoch}:%{source_date}-%{release}
Provides: tex-texloganalyser-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texloganalyser-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texloganalyser-bin < 7:20170520
Provides: tex-texloganalyser-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texloganalyser-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texloganalyser-doc < 7:20170520
License: BSD
Summary: Analyse TeX logs
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-texloganalyser
The perl script allows the user to extract (and display)
elements of the log file.

%package -n %{shortname}-texosquery
Provides: tex-texosquery = %{epoch}:%{source_date}-%{release}
Provides: tex-texosquery-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texosquery-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texosquery-bin < 7:20170520
Provides: tex-texosquery-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texosquery-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texosquery-doc < 7:20170520
License: LPPL
Summary: Cross-platform Java application to query OS information
Requires: texlive-base
Requires: texlive-kpathsea
Requires: java-headless
# shell
BuildArch: noarch

%description -n %{shortname}-texosquery
This package provides a cross-platform Java application to
query OS information designed for use in TeX's shell escape
mechanism. The application can query the following: locale and
codeset current working directory user home directory temporary
directory OS name, arch and version Current date and time in
PDF format (for TeX formats that don't provide
\pdfcreationdate) Date-time stamp of a file in PDF format (for
TeX formats that don't provide \pdffilemoddate) Size of a file
in bytes (for TeX formats that don't provide \pdffilesize)
Contents of a directory (captured as a list) Directory contents
filtered by regular expression (captured as a list) URI of a
file Canonical path of a file All paths use a forward slash as
directory divider so results can be used, for example, in
commands like \includegraphics. There are files provided for
easy access in TeX documents: texosquery.tex: generic TeX code
texosquery.sty: LaTeX package This provides commands to run
texosquery using TeX's shell escape mechanism and capture the
result in a control sequence. The category code of most of
TeX's default special characters (and some other potentially
problematic characters) is temporarily changed to 12 while
reading the result.

%package -n %{shortname}-texplate
Provides: tex-texplate = %{epoch}:%{source_date}-%{release}
Provides: tex-texplate-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texplate-bin = %{epoch}:%{source_date}-%{release}
License: BSD
Summary: A tool for creating document structures based on templates
Requires: texlive-base
Requires: texlive-kpathsea
# So much java
BuildArch: noarch

%description -n %{shortname}-texplate
TeXplate is a tool for creating document structures based on
templates. The application name is a word play on TeX and
template, so the purpose seems quite obvious: we want to
provide an easy and straightforward framework for reducing the
typical code boilerplate when writing TeX documents. Also note
that one can easily extrapolate the use beyond articles and
theses: the application is powerful enough to generate any
text-based structure, given that a corresponding template
exists.

%package -n %{shortname}-texsis
Provides: tex-texsis = %{epoch}:%{source_date}-%{release}
Provides: tex-texsis-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texsis-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texsis-bin < 7:20170520
Provides: tex-texsis-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-texsis-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texsis-doc < 7:20170520
License: LPPL
Summary: Plain TeX macros for Physicists
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-pdftex
Requires: texlive-tex
Requires: texlive-cm
Requires: texlive-hyphen-base
Requires: texlive-knuth-lib
Requires: texlive-plain
Requires(post,postun): coreutils
Provides: tex(TXSconts.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSdcol.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSenvmt.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSeqns.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSfigs.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSfmts.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSfonts.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXShead.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSinit.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSletr.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSmacs.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSmemo.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSprns.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSrefs.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSruled.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSsects.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSsite.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXSsymb.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXStags.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(TXStitle.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(texsis.tex) = %{epoch}:%{source_date}-%{release}
# symlinks only
BuildArch: noarch

%description -n %{shortname}-texsis
TeXsis is a TeX macro package which provides useful features
for typesetting research papers and related documents. For
example, it includes support specifically for: Automatic
numbering of equations, figures, tables and references;
Simplified control of type sizes, line spacing, footnotes,
running headlines and footlines, and tables of contents,
figures and tables; Specialized document formats for research
papers, preprints and ``e-prints,'' conference proceedings,
theses, books, referee reports, letters, and memoranda;
Simplified means of constructing an index for a book or thesis;
Easy to use double column formatting; Specialized environments
for lists, theorems and proofs, centered or non-justified text,
and listing computer code; Specialized macros for easily
constructing ruled tables. TeXsis was originally developed for
physicists, but others may also find it useful. It is
completely compatible with Plain TeX.

%package -n %{shortname}-texware
Provides: tex-texware = %{epoch}:%{source_date}-%{release}
Provides: tex-texware-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-texware-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-texware-bin < 7:20170520
License: Knuth
Summary: Utility programs for use with TeX
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-texware
Basic utitility programs, comprising: - dvitype, which converts
a TeX output (DVI) file to a plain text file (see also the DVI
Text Language suite); - pooltype, which converts a TeX-suite
program's "pool" (string) file into human-readable form; and -
tftopl and pltotf, which convert TeX Font Metric (TFM) file to
human readable Property List (PL) files and vice versa.

%package -n %{shortname}-thumbpdf
Provides: tex-thumbpdf = %{epoch}:%{source_date}-%{release}
Provides: tex-thumbpdf-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-thumbpdf-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-thumbpdf-bin < 7:20170520
Provides: tex-thumbpdf-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-thumbpdf-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-thumbpdf-doc < 7:20170520
License: LPPL
Summary: Thumbnails for pdfTeX and dvips/ps2pdf
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(ifluatex.sty)
Requires: ghostscript
Provides: tex(thumbpdf.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(thumbpdf.tex) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-thumbpdf
A Perl script that provides support for thumbnails in pdfTeX
and dvips/ps2pdf. The script uses ghostscript to generate the
thumbnails which get represented in a TeX readable file that is
read by the package thumbpdf.sty to automatically include the
thumbnails. This arrangement works with both plain TeX and
LaTeX.

%package -n %{shortname}-tie
Provides: tex-tie = %{epoch}:%{source_date}-%{release}
Provides: tex-tie-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-tie-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-tie-bin < 7:20170520
License: Latex2e
Summary: Allow multiple web change files
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-tie
Tie was originally developed to allow web programmers to apply
more than one change file to their source. The program may also
be used to create a new version of a .web file that
incorporates existing changes.

%package -n %{shortname}-tikztosvg
Summary: A utility for rendering TikZ diagrams to SVG
License: GPLv3
Requires: texlive-base texlive-kpathsea

%description -n %{shortname}-tikztosvg
This package provides a shell script that calls XeTeX and
pdf2svg to convert TikZ environments to SVG files.

%package -n %{shortname}-tpic2pdftex
Provides: tex-tpic2pdftex = %{epoch}:%{source_date}-%{release}
Provides: tex-tpic2pdftex-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-tpic2pdftex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-tpic2pdftex-bin < 7:20170520
Provides: tex-tpic2pdftex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-tpic2pdftex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-tpic2pdftex-doc < 7:20170520
License: GPL+
Summary: Use tpic commands in PDFTeX
Requires: texlive-base
Requires: texlive-kpathsea
# awk
BuildArch: noarch

%description -n %{shortname}-tpic2pdftex
The AWK script converts pic language, embedded inline
(delimited by .PS and .PE markers), to \pdfliteral commands.

%package -n %{shortname}-ttfutils
Provides: tex-ttfutils = %{epoch}:%{source_date}-%{release}
Provides: tex-ttfutils-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-ttfutils-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ttfutils-bin < 7:20170520
Provides: tex-ttfutils-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-ttfutils-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ttfutils-doc < 7:20170520
License: LPPL
Summary: Linux TrueType utilities
Requires: texlive-base
Requires: texlive-kpathsea
Provides: tex(T1-WGL4.enc) = %{epoch}:%{source_date}-%{release}
Provides: tex(ttf2pk.cfg) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-ttfutils
Linux TrueType utilities.

%package -n %{shortname}-typeoutfileinfo
Provides: tex-typeoutfileinfo = %{epoch}:%{source_date}-%{release}
Provides: tex-typeoutfileinfo-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-typeoutfileinfo-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-typeoutfileinfo-bin < 7:20170520
Provides: tex-typeoutfileinfo-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-typeoutfileinfo-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-typeoutfileinfo-doc < 7:20170520
License: LPPL 1.3
Summary: Display class/package/file information
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(readprov.sty)
# shell
BuildArch: noarch

%description -n %{shortname}-typeoutfileinfo
The package provides a minimalist shell script, for Unix
systems, that displays the information content in a
\ProvidesFile, \ProvidesPackage or \ProvidesClass command in a
LaTeX source file. The package requires that the readprov
package is available.

%package -n %{shortname}-ulqda
Provides: tex-ulqda = %{epoch}:%{source_date}-%{release}
Provides: tex-ulqda-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-ulqda-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ulqda-bin < 7:20170520
Provides: tex-ulqda-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-ulqda-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-ulqda-doc < 7:20170520
License: LPPL
Summary: Support of Qualitative Data Analysis
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(multicol.sty)
Requires: tex(tikz.sty)
Requires: tex(dot2texi.sty)
Requires: tex(soul.sty)
Provides: tex(ulqda.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-ulqda
The package is for use in Qualitative Data Analysis research.
It supports the integration of Qualitative Data Analysis (QDA)
research tasks, specifically for Grounded Theory, into the
LaTeX work flow. It assists in the analysis of textual data
such as interview transcripts and field notes by providing the
LaTeX user with macros which are used to markup textual
information -- for example, in-depth interviews.

%package -n %{shortname}-uptex
Provides: tex-uptex = %{epoch}:%{source_date}-%{release}
Provides: tex-uptex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-uptex-doc = %{epoch}:%{source_date}-%{release}
Provides: tex-uplatex = %{epoch}:%{source_date}-%{release}
Provides: tex-uplatex-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-uplatex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-uptex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-uptex-bin < 7:20170520
Provides: texlive-uplatex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-uplatex-bin < 7:20170520
Provides: texlive-uplatex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-uplatex-doc < 7:20170520
Provides: texlive-uptex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-uptex-doc < 7:20170520
License: BSD
Summary: Binaries for uptex
Requires: texlive-base
Requires: texlive-convbkmk
Requires: texlive-etex
Requires: texlive-hyphen-base
Requires: texlive-hyph-utf8
Requires: texlive-ipaex
Requires: texlive-japanese-otf
Requires: texlive-knuth-lib
Requires: texlive-kpathsea
Requires: texlive-plain
Requires: texlive-ptex-base
Requires: texlive-uptex-base
Requires: texlive-uptex-fonts

%description -n %{shortname}-uptex
upTeX is an extension of pTeX, using UTF-8 input and producing UTF-8 
output. It was originally designed to improve support for Japanese, 
but is also useful for documents in Chinese and Korean. It can 
process Chinese simplified, Chinese traditional, Japanese, and Korean
simultaneously, and can also produce original LaTeX with \inputenc{utf8}
and Babel (Latin/Cyrillic/Greek etc.) by switching its \kcatcode
tables.

%package -n %{shortname}-urlbst
Provides: tex-urlbst = %{epoch}:%{source_date}-%{release}
Provides: tex-urlbst-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-urlbst-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-urlbst-bin < 7:20170520
Provides: tex-urlbst-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-urlbst-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-urlbst-doc < 7:20170520
License: GPL+
Summary: Web support for BibTeX
Requires: texlive-base
Requires: texlive-kpathsea
# perl
BuildArch: noarch

%description -n %{shortname}-urlbst
Supports a new BibTeX 'webpage' entry type and 'url',
'lastchecked', and 'eprint' and 'DOI' fields. The Perl script
urlbst can be used to add this support to an arbitrary .bst
file which has a reasonably conventional structure. The result
is meant to be robust rather than pretty.

%package -n %{shortname}-velthuis
Provides: tex-velthuis = %{epoch}:%{source_date}-%{release}
Provides: tex-velthuis-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-velthuis-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-velthuis-bin < 7:20170520
Provides: tex-velthuis-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-velthuis-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-velthuis-doc < 7:20170520
Provides: texlive-devnag = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-devnag < 7:20170520
Provides: texlive-devnag-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-devnag-bin < 7:20170520
License: GPL+
Summary: Typeset Devanagari
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex-xetex-devanagari
Requires: tex(hindicaptions.sty)
Requires: tex(cite.sty)
Requires: tex(ifxetex.sty)
Provides: tex(dvng.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnb10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnb8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnb9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbb10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbb8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbb9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbbi10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbbi8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbbi9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbi10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbi8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbi9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnc10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnc8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnc9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncb10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncb8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncb9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncbi10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncbi8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncbi9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnci10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnci8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnci9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvng10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvng8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvng9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngb10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngb8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngb9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngbi10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngbi8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngbi9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngi10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngi8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngi9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnn10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnn8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnn9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnb10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnb8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnb9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnbi10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnbi8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnbi9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnni10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnni8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnni9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpb10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpb8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpb9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpc10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpc8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpc9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpn10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpn8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpn9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpnn10.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpnn8.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpnn9.tfm) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnb10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnb8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnb9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbb10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbb8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbb9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbbi10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbbi8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbbi9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbi10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbi8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnbi9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnc10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnc8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnc9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncb10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncb8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncb9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncbi10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncbi8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvncbi9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnci10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnci8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnci9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvng10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvng8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvng9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngb10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngb8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngb9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngbi10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngbi8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngbi9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngi10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngi8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngi9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnn10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnn8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnn9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnb10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnb8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnb9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnbi10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnbi8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnnbi9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnni10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnni8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvnni9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpb10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpb8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpb9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpc10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpc8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpc9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpn10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpn8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpn9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpnn10.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpnn8.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvpnn9.pfb) = %{epoch}:%{source_date}-%{release}
Provides: tex(hindi.ldf) = %{epoch}:%{source_date}-%{release}
Provides: tex(hindi.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(dev.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(dev209.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(devanagari.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(dvngcite.sty) = %{epoch}:%{source_date}-%{release}
Provides: tex(udn.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(udnb.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(udnc.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(udnn.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(udnp.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(udnpb.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(udnpc.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(udnpn.fd) = %{epoch}:%{source_date}-%{release}
Provides: tex(dnmacs.tex) = %{epoch}:%{source_date}-%{release}
Provides: tex(hindicaptions.sty) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-velthuis
Frans Velthuis' preprocessor for Devanagari text, and fonts and
macros to use when typesetting the processed text. The macros
provide features that support Sanskrit, Hindi, Marathi, Nepali,
and other languages typically printed in the Devanagari script.
The package provides fonts, in both Metafont and Type 1
formats. Users of modern TeX distributions may care to try the
XeTeX based package, which is far preferable for users who can
type Unicode text.

%package -n %{shortname}-vlna
Provides: tex-vlna = %{epoch}:%{source_date}-%{release}
Provides: tex-vlna-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-vlna-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-vlna-bin < 7:20170520
Provides: tex-vlna-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-vlna-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-vlna-doc < 7:20170520
License: LPPL
Summary: Adds tilde after each non-syllabic preposition
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-vlna
There exists a special Czech and Slovak typographical rule:
you cannot leave the non-syllabic preposition on the end of one
line and continue writting text on next line. For example, you
cannot write down the text "v lese" (in a forest) like
"v<new-line>lese". The program vlna adds the asciitilde between
such preposition and the next word and removes the space(s) in
this place.  It means, the program converts "v lese" to
"v~lese". You can use this program as a preporcessor before
TeXing. Moreower, you can set another sequence to store instead
asciitilte (see the -x option).

%package -n %{shortname}-vpe
Provides: tex-vpe = %{epoch}:%{source_date}-%{release}
Provides: tex-vpe-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-vpe-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-vpe-bin < 7:20170520
Provides: tex-vpe-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-vpe-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-vpe-doc < 7:20170520
License: LPPL
Summary: Source specials for PDF output
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(keyval.sty)
Requires: tex(color.sty)
Requires: tex(pifont.sty)
Provides: tex(vpe.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-vpe
VPE is a system to make the equivalent of "source special"
marks in a PDF file. Clicking on a mark will activate an
editor, pointing at the source line that produced the text that
was marked. The system comprises a perl file (vpe.pl) and a
LaTeX package (vpe.sty); it will work with PDF files generated
via LaTeX/dvips, pdfTeX (version 0.14 or better), and
LaTeX/VTeX. Using the LaTeX/dvips or pdfLaTeX routes, the
(pdf)TeX processor should be run with shell escapes enabled.

%package -n %{shortname}-web
Provides: tex-web = %{epoch}:%{source_date}-%{release}
Provides: tex-web-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-web-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-web-bin < 7:20170520
License: Knuth
Summary: Original web programs tangle and weave
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-web
The system processes 'web' files in two ways: firstly to
rearrange them to produce compilable code (using the program
tangle), and secondly to produce a TeX source (using the
program weave) that may be typeset for comfortable reading.

%package -n %{shortname}-webquiz
Provides: tex-webquiz = %{epoch}:%{source_date}-%{release}
Provides: tex-webquiz-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-webquiz-bin = %{epoch}:%{source_date}-%{release}
License: GPLv3+
Summary: A LaTeX package for writing online quizzes
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-tex4ht
Requires: texlive-make4ht
Requires: tex(tikz.sty)
Requires: tex(pstricks.sty)
Requires: texlive-dvisvgm
Requires: ghostscript
Requires: python3
# python3
BuildArch: noarch

%description -n %{shortname}-webquiz
WebQuiz makes it possible to use LaTeX to write interactive online quizzes.
The quizzes are first written in LaTeX and then converted into HTML using
WebQuiz, which is written in python. The conversion from LaTeX to HTML is
done behind the scenes using TeX4ht. The idea is that you should be able to
produce nice online quizzes using WebQuiz and basic knowledge of LaTeX.

%package -n %{shortname}-wordcount
Provides: tex-wordcount = %{epoch}:%{source_date}-%{release}
Provides: texlive-wordcount-bin = %{epoch}:%{source_date}-%{release}
Provides: tex-wordcount-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-wordcount-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-wordcount-doc < 7:20180414
Provides: tex(wordcount.tex) = %{epoch}:%{source_date}-%{release}
License: LPPL
Summary: Estimate the number of words in a LaTeX document
Requires: texlive-base
Requires: texlive-kpathsea
# shell
BuildArch: noarch

%description -n %{shortname}-wordcount
The package provides a relatively easy way of estimating the
number of words in a LaTeX document that does not require
dvitty or other DVI converters. It does however require
something like Unix grep -c that can search a file for a
particular string and report the number of matching lines. An
accompanying shell script wordcount.sh contains more
information in its comments.

%package -n %{shortname}-xdvi
License: MIT
Summary: A DVI previewer for the X Window System
Provides: tex-xdvi = %{epoch}:%{source_date}-%{release}
Provides: tex-xdvi-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-xdvi-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-xdvi-bin < 7:20170520
Provides: xdvi = %{epoch}:%{source_date}-%{release}
Provides: xdvik = %{epoch}:%{source_date}-%{release}
Requires: texlive-kpathsea
Requires: texlive-base

%description -n %{shortname}-xdvi
The canonical previewer for use on Unix and other X-windows
based systems.

%package -n %{shortname}-xetex
Provides: tex-xetex = %{epoch}:%{source_date}-%{release}
Provides: tex-xetex-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-xetex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-xetex-bin < 7:20170520
Provides: tex-xetex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-xetex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-xetex-doc < 7:20170520
License: MIT
Summary: Unicode and OpenType-enabled TeX engine
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-xetexconfig
Requires: texlive-latex
Requires: texlive-dvipdfmx
Requires: texlive-cm
Requires: texlive-hyphen-base
Requires: texlive-tex-ini-files
Requires: texlive-unicode-data
Requires: texlive-etex
Requires: texlive-plain
Requires: texlive-babel
Requires: texlive-l3kernel
Requires: texlive-latex-fonts
Requires: texlive-lm
Requires: teckit
Requires(post,postun): coreutils
Requires: tex(xetex.def)
Provides: tex(qx-unicode.map) = %{epoch}:%{source_date}-%{release}
Provides: tex(tex-text.map) = %{epoch}:%{source_date}-%{release}

%description -n %{shortname}-xetex
XeTeX is an extension of TeX that integrates TeX's typesetting capabilities
with (a) the Unicode text encoding standard (supporting most of the world’s
scripts) and (b) modern font technologies (TrueType and OpenType) and text
layout services (AAT, OpenType layout, SIL Graphite) provided by the host
operating system and available libraries.

With XeTeX, the advanced typographic features provided by OpenType fonts become
available for all TeX users, as well as support for complex non-roman scripts.
XeTeX also eliminates the complex task of managing a TeX font installation.
XeTeX is now part of the standard TeX distribution TeXLive and works well with
TeX macro packages like LaTeX and ConTeXt.

%package -n %{shortname}-xindex
Provides: tex-xindex = %{epoch}:%{source_date}-%{release}
Provides: tex-xindex-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-xindex-bin = %{epoch}:%{source_date}-%{release}
License: LPPL 1.3
Summary: Unicode compatible index program for LaTeX
Requires: lua >= 5.3
Requires: texlive-base
Requires: texlive-kpathsea
Requires: texlive-luatex
Provides: tex(xindex.lua) = %{epoch}:%{source_date}-%{release}
Provides: tex(xindex.sty) = %{epoch}:%{source_date}-%{release}
# lua
BuildArch: noarch

%description -n %{shortname}-xindex
Unicode compatible index program for LaTeX.

%if ! 0%{?eln}
%package -n %{shortname}-xindy
Provides: tex-xindy = %{epoch}:%{source_date}-%{release}
%if %{without bootstrap}
Provides: tex-xindy-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-xindy-bin = %{epoch}:%{source_date}-%{release}
%endif
Provides: tex-xindy-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-xindy-bin <= 6:svn41316
Provides: tex-xindy-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-xindy-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-xindy-doc <= 6:svn41316
License: GPLv2+
Summary: A general-purpose index processor
# There are some arch specific binaries in here.
# BuildArch: noarch
Requires: texlive-base
Requires: texlive-kpathsea
Requires: clisp

%description -n %{shortname}-xindy
Xindy was deceloped after an impasse had been encountered in
the attempt to complete internationalisation of makeindex.
Xindy can be used to process indexes for documents marked up
using (La)TeX, Nroff family and SGML-based languages. Xindy is
highly configurable, both in markup terms and in terms of the
collating order of the text being processed.
%endif

%package -n %{shortname}-xml2pmx
Summary: Convert MusicXML to PMX and MusiXTeX
License: GPLv3+
Requires: texlive-base texlive-kpathsea

%description -n %{shortname}-xml2pmx
This program translates MusicXML files to input suitable for
PMX and MusiXTeX processing. This package supports Windows,
MacOS and Linux systems.

%package -n %{shortname}-xmltex
Provides: tex-xmltex = %{epoch}:%{source_date}-%{release}
Provides: tex-xmltex-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-xmltex-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-xmltex-bin < 7:20170520
Provides: tex-xmltex-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-xmltex-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-xmltex-doc < 7:20170520
Provides: xmltex = %{epoch}:%{source_date}-%{release}
License: LPPL
Summary: Support for parsing XML documents
Requires: texlive-base
Requires: texlive-kpathsea-bin, tex-kpathsea
Requires: texlive-latex
Requires: texlive-pdftex
Requires: texlive-tex
Requires: texlive-xmltexconfig
Requires: texlive-babel
Requires: texlive-cm
Requires: texlive-hyphen-base
Requires: texlive-latex-fonts
Requires: texlive-l3backend
Requires: texlive-l3kernel
Requires: texlive-l3packages
Requires: texlive-tex-ini-files
Requires: texlive-unicode-data
Requires: texlive-dehyph
Requires: texlive-hyph-utf8
Requires: texlive-latexconfig
Provides: tex(xmltex.cfg) = %{epoch}:%{source_date}-%{release}
Provides: tex(xmltex.tex) = %{epoch}:%{source_date}-%{release}
# symlinks
BuildArch: noarch

%description -n %{shortname}-xmltex
The package provides an implementation of a parser for
documents matching the XML 1.0 and XML Namespace
Recommendations. In addition to parsing commands are provided
to attatch TeX typesetting instructions to the various markup
elemenets as they are encounted. Sample files for typesetting a
subset of TEI, MathML, are included. Element and Attribute
names, as well as character data, may use any characters
allowed in XML, using UTF-8 or a suitable 8-bit encoding.

%package -n %{shortname}-xpdfopen
Provides: tex-xpdfopen = %{epoch}:%{source_date}-%{release}
Provides: tex-xpdfopen-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-xpdfopen-bin = %{epoch}:%{source_date}-%{release}
License: Public Domain
Summary: Commands to control PDF readers, under X11
Requires: texlive-base
Requires: texlive-kpathsea

%description -n %{shortname}-xpdfopen
The command-line programs pdfopen and pdfclose allow you to
control the X Window System version of Adobe's Acrobat Reader
from the command line or from within a (shell) script. The
programs work with Acrobat Reader 5, 7, 8 and 9 for Linux, xpdf
and evince. This version derives from one written by Fabrice
Popineau for Microsoft operating systems.

%package -n %{shortname}-yplan
Provides: tex-yplan = %{epoch}:%{source_date}-%{release}
Provides: tex-yplan-bin = %{epoch}:%{source_date}-%{release}
Provides: texlive-yplan-bin = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-yplan-bin < 7:20170520
Provides: tex-yplan-doc = %{epoch}:%{source_date}-%{release}
Provides: texlive-yplan-doc = %{epoch}:%{source_date}-%{release}
Obsoletes: texlive-yplan-doc < 7:20170520
License: LPPL
Summary: Daily planner type calendar
Requires: texlive-base
Requires: texlive-kpathsea
Requires: tex(ifthen.sty)
Provides: tex(yplan.sty) = %{epoch}:%{source_date}-%{release}
# perl
BuildArch: noarch

%description -n %{shortname}-yplan
Prints two six-monthly vertical-type daily planner (i.e.,
months along the top, days downwards), with each 6-month period
fitting onto a single A4 (or US letter) sheet. The package
offers support for English, French, German, Spanish and
Portuguese. The previous scheme of annual updates has now been
abandoned, in favour of a Perl script yplan that generates a
year's planner automatically. (The last manually-generated
LaTeX file remains on the archive.)

%prep
%setup -q -c -T
xz -dc %{SOURCE0} | tar x
[ -e %{source_name} ] && mv %{source_name} source
%patch1 -p0
%patch2 -p1 -b .format
%patch5 -p0
%if 0%{?fedora} || 0%{?rhel} >= 8
%patch7 -p1 -b .newpoppler
%endif
%patch8 -p1 -b .texinfo-fix
%patch11 -p1 -b .dt
%patch15 -p1 -b .disabletest
%patch17 -p1 -b .annocheck
%if 0%{?fedora} || 0%{?rhel} >= 8
%patch18 -p1 -b .poppler-0.73
%endif
%patch20 -p1 -b .fix-libgs-detection
%if 0%{?fedora} || 0%{?rhel} >= 8
%patch23 -p1 -b .poppler-0.84
%endif
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%patch29 -p1 -b .poppler090
%endif
%patch30 -p1 -b .out_of_memory
%patch31 -p1 -b .poppler-xpdf-fix

# Setup copies of the licenses
for l in `unxz -c %{SOURCE3} | tar t`; do
ln -s %{_texdir}/licenses/$l $l
done

# Value here is "16" not "15" because we have a source0 at index 1.
# Source15 at index 16 is our first "normal" noarch source file.
# Also, this macro has to be here, not at the top, or it will not evaluate properly. :P
%global mysources %{lua: for index,value in ipairs(sources) do if index >= 16 then print(value.." ") end end}

%build
%define _lto_cflags %{nil}

%if %{without bootstrap} && ! 0%{?eln}
cat /usr/share/texlive/kpathsea.log || :
# DEBUG
# Okay. Lets look at things.
# 1. /usr/share/texlive/texmf-dist/web2c/fmtutil.cnf should exist and be valid.
ls -l /usr/share/texlive/texmf-dist/web2c/fmtutil.cnf || :
# cat /usr/share/texlive/texmf-dist/web2c/fmtutil.cnf

# Check for ls-R files
ls -l /usr/share/texlive/texmf-config/ls-R || :
ls -l /usr/share/texlive/texmf-dist/ls-R || :
ls -l /usr/share/texlive/texmf-local/ls-R || :
ls -l /usr/share/texlive/texmf-var/ls-R || :

# 2. kpsewhich -all fmtutil.cnf
# We should see /usr/share/texlive/texmf-dist/web2c/fmtutil.cnf
kpsewhich -version || :

kpsewhich --debug -1 -all fmtutil.cnf || :

# 3. fmtutil-sys --all
# This should recreate all format files, may not be able to do that here (non-root)
fmtutil-sys --all || :

# 4. mktexfmt latex should succeed
mktexfmt latex || :

# Make texlive generate latex.fmt, so that multiple threads do not race to
# make it during the xindy build.
cat > dummy.tex << EOF
\documentclass{article}
\begin{document}
This is a document.
\end{document}
EOF
latex dummy.tex
rm -f dummy.*
%endif

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Werror=format-security"
export CXXFLAGS="$RPM_OPT_FLAGS -std=c++11 -fno-strict-aliasing -Werror=format-security"
cd source
PREF=`pwd`/inst
mkdir -p work
%global _configure ../configure
cd work
%configure \
--prefix=$PREF --datadir=$PREF --libdir=$PREF/lib --includedir=$PREF/include --datarootdir=$PREF/share --mandir=$PREF/share/man \
--infodir=$PREF/share/info --exec_prefix=$PREF --bindir=$PREF/bin --with-system-zlib --with-system-libpng --with-system-xpdf \
--with-system-gd --with-system-t1lib --with-system-teckit --with-system-freetype2 --with-system-poppler --with-system-zziplib \
--with-system-cairo --with-system-icu --with-system-harfbuzz --with-system-graphite2 --with-system-libgs --with-system-pixman \
--with-system-libpaper --with-system-potrace --with-pic --with-xdvi-x-toolkit=xaw --with-system-mpfr --with-system-gmp \
--enable-shared --enable-compiler-warnings=max --without-cxx-runtime-hack \
--disable-native-texlive-build --disable-t1utils --enable-psutils --disable-biber --disable-ptexenc --disable-largefile \
%ifarch %{power64} s390 s390x
--disable-luajittex --disable-mfluajit --disable-luajithbtex --disable-mfluajit-nowin \
%endif
%if %{without bootstrap} && ! 0%{?eln}
--enable-xindy \
%else
--disable-xindy \
%endif
--disable-xindy-docs --disable-xindy-rules \
--disable-rpath

# disable rpath
for i in `find . -name libtool`; do
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' $i
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' $i
done

%make_build world STRIPPROG=/bin/true STRIP=/bin/true

%install
# make directories
mkdir -p %{buildroot}%{_texdir}/texmf-config/web2c
mkdir -p %{buildroot}%{_texmf_var}

# make symlinks
pushd %{buildroot}%{_texdir}/texmf-config/web2c
ln -s ../../texmf-dist/web2c/updmap.cfg updmap.cfg
popd

# make compatibility symlink
pushd %{buildroot}%{_datadir}
mkdir -p texlive/texmf-local/texmf-compat
ln -s texlive/texmf-local/texmf-compat texmf
popd

# make opentype fontdir symlinks
# NOTE: fontawesome, stix, oldstandard are a conflict, so we just add Requires for the 
# corresponding system font packages for them.
# NOTE: We might have to handle this differently if there are lots of conflicts later.
# DO NOT MAKE A SYMLINK FOR public/ebgaramond
# The EB Garamond upstream font decided to map some historical flags (i.e., flags 
# obsolete for centuries) to the Unicode flag emoji code points.
# Since most other fonts do not include the relevant code points, Fontconfig decides to 
# pick up the EB Garamond flags through the fallback font mechanism for almost all 
# fonts on the system, including DejaVu Sans, Liberation Sans, etc.
mkdir -p %{buildroot}%{_datadir}/fonts
pushd %{buildroot}%{_datadir}/fonts
for i in public/lilyglyphs ; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
popd

# install binaries
mkdir -p %{buildroot}%{_bindir}
rm -f source/inst/bin/man
cp -a source/inst/bin/* %{buildroot}%{_bindir}

# install libs
mkdir -p %{buildroot}%{_libdir}
cp -d source/inst/lib/*.so* %{buildroot}%{_libdir}
cp -a source/inst/lib/pkgconfig %{buildroot}%{_libdir}

# install includes
mkdir -p %{buildroot}%{_includedir}
cp -r source/inst/include/* %{buildroot}%{_includedir}

# install shared files
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texdir}
pushd source/inst/share
cp -a info %{buildroot}%{_datadir}/
cp -a man %{buildroot}%{_datadir}/
cp -a texmf-dist %{buildroot}%{_texdir}/
popd

# relocate binaries to %%{_bindir} and fix relative symlinks
pushd %{buildroot}%{_bindir}
for i in `find . -type l`; do
if [ "`readlink $i | grep '..' | wc -l`" == "1" ]; then
l=`readlink $i | sed s,.*texmf,/usr/share/texlive/texmf,`
rm -f $i
ln -s $l $i
fi
done
popd

# install noarch bits
pushd %{buildroot}%{_texdir}
echo %{mysources}
for noarchsrc in %{mysources}; do
  xz -dc $noarchsrc | tar x
done
popd
# Do the weird noarch bits
pushd  %{buildroot}%{_texdir}/texmf-dist
xz -dc %{SOURCE5} | tar x
xz -dc %{SOURCE6} | tar x
xz -dc %{SOURCE7} | tar x
xz -dc %{SOURCE8} | tar x
xz -dc %{SOURCE9} | tar x
xz -dc %{SOURCE10} | tar x
xz -dc %{SOURCE11} | tar x
xz -dc %{SOURCE12} | tar x
xz -dc %{SOURCE13} | tar x
xz -dc %{SOURCE14} | tar x
popd

# We want the texmf.cnf we patched, not the vanilla one from the kpathsea.tar.xz
cp -a source/texk/kpathsea/texmf.cnf %{buildroot}%{_texdir}/texmf-dist/web2c/texmf.cnf

# Apply fixes
# We do it here because this is the first time we have the complete tree.
# bz1384067
sed -i 's|\\sc |\\scshape |g' %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/base/acm.bst
sed -i 's|\\sc |\\scshape |g' %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/base/siam.bst

# Patches to component tarballs
pushd %{buildroot}%{_texdir}/texmf-dist

# neuter tlmgr a bit
patch -p1 < %{_sourcedir}/texlive-20190410-tlmgr-ignore-warning.patch
popd

# config files in /etc symlinked
mkdir -p %{buildroot}%{_sysconfdir}/texlive/web2c
mkdir -p %{buildroot}%{_sysconfdir}/texlive/dvips/config
mkdir -p %{buildroot}%{_sysconfdir}/texlive/tex/generic/config

for i in mktex.cnf texmf.cnf updmap.cfg; do
        mv %{buildroot}%{_texdir}/texmf-dist/web2c/$i %{buildroot}%{_sysconfdir}/texlive/web2c/
        ln -s %{_sysconfdir}/texlive/web2c/$i %{buildroot}%{_texdir}/texmf-dist/web2c/$i
done

# configure texmf-local - make it visible to kpathsea
sed -i -e 's|^TEXMFLOCAL.*|TEXMFLOCAL = $TEXMFROOT/texmf-local//|' %{buildroot}%{_sysconfdir}/texlive/web2c/texmf.cnf

mv %{buildroot}%{_texdir}/texmf-dist/dvips/config/config.ps %{buildroot}%{_sysconfdir}/texlive/dvips/config/
ln -s %{_sysconfdir}/texlive/dvips/config/config.ps %{buildroot}%{_texdir}/texmf-dist/dvips/config/config.ps

# Move the stock fmtutil.cnf under /etc and make sure everything is commented out
mv %{buildroot}%{usr_fmtutil_cnf} %{buildroot}%{etc_fmtutil_cnf}
sed -i '/^[a-z].*$/s/^/\#\!\ /' %{buildroot}%{_sysconfdir}/texlive/web2c/fmtutil.cnf

# Split the stock texmf.cnf file:
# * Look for lines like "# from foo:" and use those as the names of the files
#   we generate.
# * Take the text starting at "# from foo:" and ending just before the next
#   line containing just '#' (or EOF).
# * remove '#!'
# * Add a single line containing '#' to the beginning
# * Stuff that into a file named "foo" in %%_texdir/fmtutil.cnf.d
#
# This is a bit fragile as the precise format of the stock fmtutil.cnf file
# could change.
# The leading '#' and the "# from foo:" line are added to the output only to
# match the existing format of the file, just in case some tool cares.
mkdir %{buildroot}%{_texdir}/fmtutil.cnf.d
for i in $(grep '^# from .*:$' %{buildroot}%{etc_fmtutil_cnf}|sed 's/^# from //; s/:$//'); do
    echo "#" > %{buildroot}%{fmtutil_cnf_d}/$i
    sed -n "s/^#! //; /^# from $i:\$/,/^#\$/{/^#\$/!p}" %{buildroot}%{etc_fmtutil_cnf} >> %{buildroot}%{fmtutil_cnf_d}/$i
done

# Install the fmtutil.cnf generation script
install -D -p -m 755 -t %{buildroot}%{_sbindir} %{SOURCE4}

# create macro file for building texlive
mkdir -p %{buildroot}%{_rpmmacrodir}
cp -a %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.texlive

# install texlive.tlpdb
cp %{SOURCE2} %{buildroot}%{_texdir}
# make a symlink so texdoc is happy
pushd %{buildroot}%{_texdir}/tlpkg
ln -s ../texlive.tlpdb .
popd

# install licenses
mkdir -p %{buildroot}%{_texdir}/licenses
pushd %{buildroot}%{_texdir}/licenses
xz -dc %{SOURCE3} | tar x
popd

# nuke useless tlmgr packaging stuff and doc droppings
rm -f %{buildroot}/%{_texdir}/install-tl
rm -rf %{buildroot}%{_texdir}/tlpkg/gpg/
rm -rf %{buildroot}%{_texdir}/tlpkg/tltcl/
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
# texconfig needs tlmgr.pl
# We're only including what it needs, no more.
# rm -f %{buildroot}%{_texdir}/texmf-dist/doc/man/man1/tlmgr.1
# rm -f %{buildroot}%{_texdir}/texmf-dist/scripts/texlive/tlmgr.pl
# rm -f %{buildroot}%{_bindir}/tlmgr
# rm -f %{buildroot}%{_texdir}/tlpkg/installer/config.guess
rm -f %{buildroot}%{_texdir}/texmf-dist/scripts/texlive/tlmgr.pl.orig
rm -f %{buildroot}%{_texdir}/texmf-dist/scripts/texlive/tl-errmess.vbs
rm -f %{buildroot}%{_texdir}/texmf-dist/scripts/texlive/tlmgrgui.pl
rm -f %{buildroot}%{_texdir}/texmf-dist/scripts/texlive/uninstall-win32.pl
rm -f %{buildroot}%{_texdir}/texmf-dist/scripts/texlive/uninstq.vbs
rm -f %{buildroot}%{_texdir}/texmf-dist/scripts/tlcockpit/tlcockpit.sh
rm -f %{buildroot}%{_texdir}/texmf-dist/scripts/tlshell/tlshell.tcl
rm -f %{buildroot}%{_texdir}/tlpkg/installer/COPYING.MinGW-runtime.txt
rm -f %{buildroot}%{_texdir}/tlpkg/installer/ctan-mirrors.pl
rm -f %{buildroot}%{_texdir}/tlpkg/installer/install-menu-extl.pl
rm -f %{buildroot}%{_texdir}/tlpkg/installer/install-menu-perltk.pl
rm -f %{buildroot}%{_texdir}/tlpkg/installer/install-menu-text.pl
rm -f %{buildroot}%{_texdir}/tlpkg/installer/install-menu-wizard.pl
rm -f %{buildroot}%{_texdir}/tlpkg/installer/install-tl-gui.tcl
rm -f %{buildroot}%{_texdir}/tlpkg/installer/texlive.png
rm -f %{buildroot}%{_bindir}/tlcockpit
rm -f %{buildroot}%{_bindir}/tlshell
rm -rf %{buildroot}%{_datadir}/info/dir
rm -rf %{buildroot}%{_texdir}/readme-txt.dir/README.*
rm -rf %{buildroot}%{_texdir}/texmf-dist/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf-dist/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf-dist/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf-dist/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf-dist/doc/info/dir
# nuke unwanted ptexenc devel files
rm -rf %{buildroot}%{_includedir}/ptexenc
# nuke context windows files
rm -f %{buildroot}/%{_texdir}/texmf-dist/scripts/context/stubs/mswin/*
rm -f %{buildroot}/%{_texdir}/texmf-dist/scripts/context/stubs/win64/*
rm -f %{buildroot}/%{_texdir}/texmf-dist/scripts/context/stubs/source/*

# Make this perl module show up in @INC
mkdir -p %{buildroot}%{_datadir}/perl5
ln -s %{_texdir}/tlpkg/TeXLive %{buildroot}%{_datadir}/perl5/TeXLive

# not sure why this is here
rm -rf %{buildroot}%{_texdir}/texmf-dist/source/fonts/zhmetrics/ttfonts.map

pushd %{buildroot}%{_texdir}
# ALWAYS NUKE THIS IF IT IS HERE.
rm -rf texmf-var
# AND NOW WE MAKE THE SYMLINK.
ln -s %{_texmf_var} texmf-var
popd

# sync built/distro binaries
pushd %{buildroot}%{_bindir}
[ ! -e mfplain ] && ln -s mpost mfplain
[ ! -e texlua ] && ln -s luatex texlua
[ ! -e texluac ] && ln -s luatex texluac

# remove latexmk
# This lives in the "latexmk" package in Fedora.
rm -f latexmk
rm -rf %{buildroot}%{_texdir}/texmf-dist/scripts/latexmk
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man/man1/latexmk.*

# Fix symlinks for helper scripts
rm -f bibexport.sh
ln -s /usr/share/texlive/texmf-dist/scripts/bibexport/bibexport.sh bibexport.sh
rm -f texmfstart
ln -s /usr/share/texlive/texmf-dist/scripts/context/ruby/texmfstart.rb texmfstart
rm -rf mktexmf
ln -s /usr/share/texlive/texmf-dist/scripts/texlive/mktexmf mktexmf
rm -rf mkjobtexmf
ln -s /usr/share/texlive/texmf-dist/scripts/mkjobtexmf/mkjobtexmf.pl mkjobtexmf

# fix context
rm -f context
cat > context << EOF
#!/bin/sh
export TEXMF=/usr/share/texlive/texmf-dist;
export TEXMFCNF=/usr/share/texlive/texmf-dist/web2c;
export TEXMFCACHE=\$(realpath \$HOME/.cache/texlive);
%{_bindir}/mtxrun --script context "\$@"
EOF
chmod 0755 context
popd

# Move docs
mkdir -p %{buildroot}%{_datadir}/
mkdir -p %{buildroot}%{_infodir}/
cp -R %{buildroot}%{_texdir}/texmf-dist/doc/man %{buildroot}%{_datadir}/
find %{buildroot}%{_texdir}/texmf-dist/doc/man -type f | xargs rm -f
mv %{buildroot}%{_texdir}/texmf-dist/doc/info/* %{buildroot}%{_infodir}/

# Remove cjk-gs-integrate files
# Yes, we probably should remove the source, but there is a possibility that we will
# re-add this subpackage at some point.
rm -rf %{buildroot}%{_bindir}/cjk-gs-integrate
rm -rf %{buildroot}%{_texdir}/texmf-dist/scripts/cjk-gs-integrate
rm -rf %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cjk-gs-integrate
rm -rf %{buildroot}%{_texdir}/texmf-dist/fonts/misc/cjk-gs-integrate

# Fix pkgconfig files
for file in $(find %{buildroot}%{_libdir}/pkgconfig/ -type f -name '*.pc')
do sed -i 's|%{_builddir}/%{name}-%{source_date}/source/inst|/usr|g' $file
   sed -i 's|/usr/lib|%{_libdir}|g' $file
done

# Python fixup
# Change shebang in all relevant files in this directory and all subdirectories
# See `man find` for how the `-exec command {} +` syntax works
pushd %{buildroot}
find -type f -exec sed -i '1s|^#!/usr/bin/python$|#!%{__python3}|' {} +
find -type f -exec sed -i '1s|^#!/usr/bin/env python$|#!%{__python3}|' {} +
sed -i '1s|^#!/usr/bin/python |#!%{__python3} |' ./%{_texdir}/texmf-dist/scripts/de-macro/de-macro

# Get rid of the python2 variant bits from pythontex (we need them to generate the py3 bits, but not in the package)
rm -rf ./%{_texdir}/texmf-dist/scripts/pythontex/pythontex2.py
rm -rf ./%{_texdir}/texmf-dist/scripts/pythontex/depythontex2.py
popd

# One dir to own
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/context/third

# TeXLive has a fork of psutils
# we namespace those binaries to avoid conflicts with the upstream psutils
pushd %{buildroot}%{_bindir}
for i in epsffit extractres includeres psbook psjoin psnup psresize psselect pstops
do mv $i tl-$i
done
popd
# we also rename the manpages
pushd %{buildroot}%{_mandir}/man1/
for i in epsffit extractres includeres psbook psjoin psnup psresize psselect pstops psutils
do mv $i.1 tl-$i.1
done
popd
# and move the config file
mkdir -p %{buildroot}%{_sysconfdir}/texlive/psutils
mv %{buildroot}%{_texdir}/texmf-dist/psutils/paper.cfg %{buildroot}%{_sysconfdir}/texlive/psutils/paper.cfg
ln -s %{_sysconfdir}/texlive/psutils/paper.cfg %{buildroot}%{_texdir}/texmf-dist/psutils/paper.cfg

# SCRIPTLETS

%pretrans -p <lua>
path = "/usr/share/texmf"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

%pre
rm -rf %{_texdir}/texmf-var
rm -rf %{_texmf_var}/*
:

%posttrans
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%transfiletriggerin -n %{shortname}-context -- %{_texdir}
export TEXMFLOCAL=/usr/share/texlive/texmf-local
%{_bindir}/mtxrun --generate &> /dev/null || :

%transfiletriggerin -n %{shortname}-kpathsea -- %{_texdir}
# Commented lines are DEBUG mode
# touch /usr/share/texlive/kpathsea.log
# /usr/share/texlive/texmf-dist/scripts/texlive/mktexlsr --version 2>&1 | tee -a /usr/share/texlive/kpathsea.log || :
# /usr/share/texlive/texmf-dist/scripts/texlive/mktexlsr --verbose 2>&1 | tee -a /usr/share/texlive/kpathsea.log || :
# /usr/bin/sh -x %{_bindir}/texhash 2>&1 | tee -a /usr/share/texlive/kpathsea.log || :
/usr/share/texlive/texmf-dist/scripts/texlive/mktexlsr 2> /dev/null || :
export TEXMF=/usr/share/texlive/texmf-dist
export TEXMFCNF=/usr/share/texlive/texmf-dist/web2c
export TEXMFCACHE=/var/lib/texmf
# %{_bindir}/fmtutil-sys --all 2>&1 | tee -a /usr/share/texlive/kpathsea.log || :
%{_bindir}/fmtutil-sys --all &> /dev/null || :

%transfiletriggerpostun -n %{shortname}-kpathsea -- %{_texdir}
/usr/share/texlive/texmf-dist/scripts/texlive/mktexlsr 2> /dev/null || :

%transfiletriggerin -n %{shortname}-kpathsea -- %{_texdir}/texmf-dist/fonts/map/dvips/
list=`grep "\.map" | sort -n | uniq`
while read -r line; do
        [ -z "$line" ] && continue
        shortfile=`basename "$line"`
        if `echo $shortfile | grep -Eq 'allrunes.map|arabtex.map|arss.map|artm.map|bbold.map|cbgreek-full.map|ccpl.map|cmextra.map|cmll.map|cm.map|cm-super-t1.map|cm-super-t2a.map|cm-super-t2b.map|cm-super-t2c.map|cm-super-ts1.map|cm-super-x2.map|cmtext-bsr-interpolated.map|cyrillic.map|dvng.map|esint.map|ethiop.map|eurosym.map|hfbright.map|iby.map|latxfont.map|lxfonts.map|manfnt.map|mflogo.map|mongolian.map|musix.map|pigpen.map|plother.map|pltext.map|rsfs.map|semaf.map|stmaryrd.map|symbols.map|tipa.map|trajan.map|vnrother.map|vnrtext.map|wasy.map|xypic.map|yhmath.map'`; then
                %{_bindir}/updmap-sys --nomkmap --enable MixedMap=$shortfile >/dev/null 2>&1 || :
        else
                %{_bindir}/updmap-sys --nomkmap --enable Map=$shortfile >/dev/null 2>&1 || :
        fi
done <<< "$list"
%{_bindir}/updmap-sys --quiet --nomkmap >/dev/null || :

%transfiletriggerpostun -n %{shortname}-kpathsea -- %{_texdir}/texmf-dist/fonts/map/dvips/
list=`grep "\.map" | sort -n | uniq`
while read -r line; do
        [ -z "$line" ] && continue
        shortfile=`basename "$line"`
        if `echo $shortfile | grep -Eq 'allrunes.map|arabtex.map|arss.map|artm.map|bbold.map|cbgreek-full.map|ccpl.map|cmextra.map|cmll.map|cm.map|cm-super-t1.map|cm-super-t2a.map|cm-super-t2b.map|cm-super-t2c.map|cm-super-ts1.map|cm-super-x2.map|cmtext-bsr-interpolated.map|cyrillic.map|dvng.map|esint.map|ethiop.map|eurosym.map|hfbright.map|iby.map|latxfont.map|lxfonts.map|manfnt.map|mflogo.map|mongolian.map|musix.map|pigpen.map|plother.map|pltext.map|rsfs.map|semaf.map|stmaryrd.map|symbols.map|tipa.map|trajan.map|vnrother.map|vnrtext.map|wasy.map|xypic.map|yhmath.map'`; then
                %{_bindir}/updmap-sys --nomkmap --disable MixedMap=$shortfile >/dev/null 2>&1 || :
        else
                %{_bindir}/updmap-sys --nomkmap --disable Map=$shortfile >/dev/null 2>&1 || :
        fi
done <<< "$list"
%{_bindir}/updmap-sys --quiet --nomkmap >/dev/null || :

%transfiletriggerin -n %{shortname}-kpathsea -P 2000000 -- %{_texdir}/fmtutil.cnf.d/
%{_sbindir}/generate-fmtutilcnf %{_texdir}

%transfiletriggerpostun -n %{shortname}-kpathsea -P 2000000 -- %{_texdir}/fmtutil.cnf.d/
%{_sbindir}/generate-fmtutilcnf %{_texdir}

%files
%{_texdir}/licenses/
%{_texdir}/texlive.tlpdb
%{_texdir}/tlpkg/texlive.tlpdb
%{_rpmmacrodir}/macros.texlive
# Mostly we own directories.
%dir %{_sysconfdir}/%{shortname}
%dir %{_sysconfdir}/%{shortname}/dvips
%dir %{_sysconfdir}/%{shortname}/dvips/config
%dir %{_sysconfdir}/%{shortname}/tex
%dir %{_sysconfdir}/%{shortname}/tex/generic
%dir %{_sysconfdir}/%{shortname}/tex/generic/config
%dir %{_sysconfdir}/%{shortname}/web2c
%dir %{_texdir}
%dir %{_texdir}/texmf-dist
%dir %{_texdir}/texmf-dist/bibtex/
%dir %{_texdir}/texmf-dist/bibtex/csf
%dir %{_texdir}/texmf-dist/bibtex/csf/base
%dir %{_texdir}/texmf-dist/doc
%dir %{_texdir}/texmf-dist/doc/info
%dir %{_texdir}/texmf-dist/doc/man
%dir %{_texdir}/texmf-dist/doc/man/man1
%dir %{_texdir}/texmf-dist/doc/man/man5
%dir %{_texdir}/texmf-dist/dvips
%dir %{_texdir}/texmf-dist/dvips/config
%dir %{_texdir}/texmf-dist/fonts
%dir %{_texdir}/texmf-dist/fonts/cmap
%dir %{_texdir}/texmf-dist/fonts/enc
%dir %{_texdir}/texmf-dist/fonts/enc/dvips
%dir %{_texdir}/texmf-dist/fonts/map
%dir %{_texdir}/texmf-dist/fonts/map/dvips
%dir %{_texdir}/texmf-dist/fonts/map/glyphlist
%dir %{_texdir}/texmf-dist/fonts/sfd
%dir %{_texdir}/texmf-dist/scripts
%dir %{_texdir}/texmf-dist/scripts/texlive
%dir %{_texdir}/texmf-dist/source
%dir %{_texdir}/texmf-dist/source/fonts
%dir %{_texdir}/texmf-dist/source/fonts/zhmetrics
%dir %{_texdir}/texmf-dist/tex
%dir %{_texdir}/texmf-dist/tex/generic
%dir %{_texdir}/texmf-dist/tex/generic/bibtex
%dir %{_texdir}/texmf-dist/tex/generic/config
%dir %{_texdir}/texmf-dist/tex/latex
%dir %{_texdir}/texmf-dist/tex/lualatex
%dir %{_texdir}/texmf-dist/tex/luatex
%dir %{_texdir}/texmf-dist/tex/xelatex
%dir %{_texdir}/texmf-dist/web2c
%dir %{_texmf_var}
%{_texdir}/texmf-var
%{_texdir}/texmf-local/
%{_datadir}/texmf
%ghost %{_datadir}/texmf.rpmmoved

%files -n %{shortname}-a2ping
%license gpl.txt
%{_bindir}/a2ping
%{_texdir}/texmf-dist/scripts/a2ping/
%{_mandir}/man1/a2ping.1*
%doc %{_texdir}/texmf-dist/doc/support/a2ping/

%files -n %{shortname}-accfonts
%license gpl.txt
%{_bindir}/mkt1font
%{_bindir}/vpl2ovp
%{_bindir}/vpl2vpl
%{_texdir}/texmf-dist/scripts/accfonts/
%{_texdir}/texmf-dist/tex/latex/accfonts/
%doc %{_texdir}/texmf-dist/doc/fonts/accfonts/

%files -n %{shortname}-adhocfilelist
%license lppl1.txt
%{_bindir}/adhocfilelist
%{_texdir}/texmf-dist/scripts/adhocfilelist/
%{_texdir}/texmf-dist/tex/support/adhocfilelist/
%doc %{_texdir}/texmf-dist/doc/support/adhocfilelist/

%files -n %{shortname}-afm2pl
%license lppl1.txt
%{_bindir}/afm2pl
%{_mandir}/man1/afm2pl.1*
%{_texdir}/texmf-dist/fonts/enc/dvips/afm2pl/
%{_texdir}/texmf-dist/fonts/lig/afm2pl/
%{_texdir}/texmf-dist/tex/fontinst/afm2pl/

%files -n %{shortname}-albatross
%license bsd.txt
%{_bindir}/albatross
%{_mandir}/man1/albatross.*
%doc %{_texdir}/texmf-dist/doc/support/albatross
%{_texdir}/texmf-dist/scripts/albatross

%files -n %{shortname}-aleph
%license gpl.txt
%{_bindir}/aleph
# symlink to aleph, not created in 2021
# %%{_bindir}/lamed
%{_mandir}/man1/aleph.1*
%{_mandir}/man1/lamed.1*
%{fmtutil_cnf_d}/aleph
%doc %{_texdir}/texmf-dist/doc/aleph/

%files -n %{shortname}-amstex
%license lppl1.txt
%{_bindir}/amstex
%{_mandir}/man1/amstex.1*
%{_texdir}/texmf-dist/tex/amstex/base/
%{_texdir}/texmf-dist/tex/amstex/config/
%{fmtutil_cnf_d}/amstex
%doc %{_texdir}/texmf-dist/doc/amstex/base/

%files -n %{shortname}-arara
%license bsd.txt
%{_bindir}/arara
%{_mandir}/man1/arara.*
%{_texdir}/texmf-dist/scripts/arara/
%doc %{_texdir}/texmf-dist/doc/support/arara/

%files -n %{shortname}-attachfile2
%license lppl1.3.txt
%{_bindir}/pdfatfi
%{_mandir}/man1/pdfatfi.1*
%{_texdir}/texmf-dist/scripts/attachfile2/
%{_texdir}/texmf-dist/tex/latex/attachfile2/
%doc %{_texdir}/texmf-dist/doc/latex/attachfile2/

%files -n %{shortname}-authorindex
%license lppl1.txt
%{_bindir}/authorindex
%{_texdir}/texmf-dist/scripts/authorindex/
%{_texdir}/texmf-dist/tex/latex/authorindex/
%doc %{_texdir}/texmf-dist/doc/latex/authorindex/

%files -n %{shortname}-autosp
%license gpl2.txt
%{_bindir}/autosp
%{_bindir}/tex2aspc
%{_mandir}/man1/autosp.1*
%{_mandir}/man1/tex2aspc.1*
%doc %{_texdir}/texmf-dist/doc/generic/autosp/

%files -n %{shortname}-axodraw2
%license gpl3.txt
%{_bindir}/axohelp
%{_mandir}/man1/axohelp.1*
%{_texdir}/texmf-dist/tex/latex/axodraw2/
%doc %{_texdir}/texmf-dist/doc/latex/axodraw2/

%files -n %{shortname}-bib2gls
%license gpl3.txt
%{_bindir}/bib2gls
%{_bindir}/convertgls2bib
%{_texdir}/texmf-dist/scripts/bib2gls/
%doc %{_texdir}/texmf-dist/doc/support/bib2gls/

%files -n %{shortname}-bibexport
%license lppl1.3.txt
%{_bindir}/bibexport
%{_bindir}/bibexport.sh
%{_texdir}/texmf-dist/bibtex/bst/bibexport/
%{_texdir}/texmf-dist/scripts/bibexport/
%doc %{_texdir}/texmf-dist/doc/bibtex/bibexport/

%files -n %{shortname}-bibtex
%license knuth.txt
%{_bindir}/bibtex
%{_mandir}/man1/bibtex.1*
%{_texdir}/texmf-dist/bibtex/bib/base/xampl.bib
%{_texdir}/texmf-dist/bibtex/bst/base/abbrv.bst
%{_texdir}/texmf-dist/bibtex/bst/base/acm.bst
%{_texdir}/texmf-dist/bibtex/bst/base/alpha.bst
%{_texdir}/texmf-dist/bibtex/bst/base/apalike.bst
%{_texdir}/texmf-dist/bibtex/bst/base/ieeetr.bst
%{_texdir}/texmf-dist/bibtex/bst/base/plain.bst
%{_texdir}/texmf-dist/bibtex/bst/base/siam.bst
%{_texdir}/texmf-dist/bibtex/bst/base/unsrt.bst
%doc %{_texdir}/texmf-dist/doc/bibtex/base/README
%doc %{_texdir}/texmf-dist/doc/bibtex/base/btxbst.doc
%doc %{_texdir}/texmf-dist/doc/bibtex/base/btxdoc.bib
%doc %{_texdir}/texmf-dist/doc/bibtex/base/btxdoc.pdf
%doc %{_texdir}/texmf-dist/doc/bibtex/base/btxdoc.tex
%doc %{_texdir}/texmf-dist/doc/bibtex/base/btxhak.pdf
%doc %{_texdir}/texmf-dist/doc/bibtex/base/btxhak.tex
%{_texdir}/texmf-dist/tex/generic/bibtex/apalike.sty
%{_texdir}/texmf-dist/tex/generic/bibtex/apalike.tex

%files -n %{shortname}-bibtexu
%license lppl1.txt
%{_bindir}/bibtexu
%doc %{_texdir}/texmf-dist/doc/bibtexu/
%{_mandir}/man1/bibtexu.1*

%files -n %{shortname}-bibtex8
%license gpl.txt
%{_bindir}/bibtex8
%{_texdir}/texmf-dist/bibtex/csf/base/88591lat.csf
%{_texdir}/texmf-dist/bibtex/csf/base/88591sca.csf
%{_texdir}/texmf-dist/bibtex/csf/base/README.TEXLIVE
%{_texdir}/texmf-dist/bibtex/csf/base/ascii.csf
%{_texdir}/texmf-dist/bibtex/csf/base/cp437lat.csf
%{_texdir}/texmf-dist/bibtex/csf/base/cp850lat.csf
%{_texdir}/texmf-dist/bibtex/csf/base/cp850sca.csf
%{_texdir}/texmf-dist/bibtex/csf/base/cp866rus.csf
%{_texdir}/texmf-dist/bibtex/csf/base/csfile.txt
%{_texdir}/texmf-dist/bibtex/csf/polish-csf/88592pl.csf
%{_texdir}/texmf-dist/bibtex/csf/polish-csf/cp1250pl.csf
%{_texdir}/texmf-dist/bibtex/csf/polish-csf/cp852pl.csf
%{_texdir}/texmf-dist/bibtex/csf/polish-csf/iso8859-7.csf
%doc %{_texdir}/texmf-dist/doc/bibtex8/
%{_mandir}/man1/bibtex8.1*

%files -n %{shortname}-bundledoc
%license lppl1.txt
%{_bindir}/arlatex
%{_bindir}/bundledoc
%{_mandir}/man1/arlatex.1*
%{_mandir}/man1/bundledoc.1*
%{_texdir}/texmf-dist/scripts/bundledoc/
%{_texdir}/texmf-dist/tex/latex/bundledoc/
%doc %{_texdir}/texmf-dist/doc/support/bundledoc/

%files -n %{shortname}-cachepic
%license lppl1.3.txt
%{_bindir}/cachepic
%{_texdir}/texmf-dist/scripts/cachepic/
%{_texdir}/texmf-dist/tex/latex/cachepic/
%doc %{_texdir}/texmf-dist/doc/latex/cachepic/

%files -n %{shortname}-checkcites
%license lppl1.3.txt
%{_bindir}/checkcites
%{_texdir}/texmf-dist/scripts/checkcites/
%doc %{_texdir}/texmf-dist/doc/support/checkcites/

%files -n %{shortname}-checklistings
%license lppl1.2.txt
%{_bindir}/checklistings
%{_texdir}/texmf-dist/scripts/checklistings/
%{_texdir}/texmf-dist/tex/latex/checklistings/
%doc %{_texdir}/texmf-dist/doc/latex/checklistings/

%files -n %{shortname}-chklref
%license gpl3.txt
%{_bindir}/chklref
%{_mandir}/man1/chklref.1*
%{_texdir}/texmf-dist/scripts/chklref/
%{_texdir}/texmf-dist/tex/latex/chklref/
%doc %{_texdir}/texmf-dist/doc/support/chklref/

%files -n %{shortname}-chktex
%license gpl.txt
%{_bindir}/chktex
%{_bindir}/chkweb
%{_bindir}/deweb
%{_mandir}/man1/chktex.1*
%{_mandir}/man1/chkweb.1*
%{_mandir}/man1/deweb.1*
%{_texdir}/texmf-dist/chktex/
%{_texdir}/texmf-dist/scripts/chktex/
%doc %{_texdir}/texmf-dist/doc/chktex/

%if 0
%files -n %{shortname}-cjk-gs-integrate
%license gpl3.txt
%{_bindir}/cjk-gs-integrate
%{_texdir}/texmf-dist/scripts/cjk-gs-integrate/
%{_texdir}/texmf-dist/fonts/misc/cjk-gs-integrate/
%doc %{_texdir}/texmf-dist/doc/fonts/cjk-gs-integrate/
%endif

%files -n %{shortname}-cjkutils
%license lppl1.txt
%{_bindir}/bg5+latex
%{_bindir}/bg5+pdflatex
%{_bindir}/bg5conv
%{_bindir}/bg5latex
%{_bindir}/bg5pdflatex
%{_bindir}/cef5conv
%{_bindir}/cef5latex
%{_bindir}/cef5pdflatex
%{_bindir}/cefconv
%{_bindir}/ceflatex
%{_bindir}/cefpdflatex
%{_bindir}/cefsconv
%{_bindir}/cefslatex
%{_bindir}/cefspdflatex
%{_bindir}/extconv
%{_bindir}/gbklatex
%{_bindir}/gbkpdflatex
%{_bindir}/hbf2gf
%{_bindir}/sjisconv
%{_bindir}/sjislatex
%{_bindir}/sjispdflatex
%{_mandir}/man1/bg5conv.1*
%{_mandir}/man1/cef5conv.1*
%{_mandir}/man1/cefconv.1*
%{_mandir}/man1/cefsconv.1*
%{_mandir}/man1/extconv.1*
%{_mandir}/man1/hbf2gf.1*
%{_mandir}/man1/sjisconv.1*
%{_texdir}/texmf-dist/hbf2gf/

%files -n %{shortname}-clojure-pamphlet
%license gpl3.txt
%{_bindir}/pamphletangler
%{_texdir}/texmf-dist/scripts/clojure-pamphlet/
%{_texdir}/texmf-dist/tex/latex/clojure-pamphlet/
%doc %{_texdir}/texmf-dist/doc/support/clojure-pamphlet/

%files -n %{shortname}-cluttex
%license gpl3.txt
%{_bindir}/cllualatex
%{_bindir}/cluttex
%{_bindir}/clxelatex
%{_texdir}/texmf-dist/scripts/cluttex/
%doc %{_texdir}/texmf-dist/doc/support/cluttex/

%files -n %{shortname}-context
%{_bindir}/context
%{_bindir}/contextjit
%{_bindir}/luatools
%{_bindir}/mtxrun
%{_bindir}/mtxrunjit
%{_bindir}/texexec
%{_bindir}/texmfstart
%{_mandir}/man1/context.1*
%{_mandir}/man1/luatools.1*
%{_mandir}/man1/mtx-babel.1*
%{_mandir}/man1/mtx-base.1*
%{_mandir}/man1/mtx-bibtex.1*
%{_mandir}/man1/mtx-cache.1*
%{_mandir}/man1/mtx-chars.1*
%{_mandir}/man1/mtx-check.1*
%{_mandir}/man1/mtx-colors.1*
%{_mandir}/man1/mtx-context.1*
%{_mandir}/man1/mtx-dvi.1*
%{_mandir}/man1/mtx-epub.1*
%{_mandir}/man1/mtx-evohome.1*
%{_mandir}/man1/mtx-fcd.1*
%{_mandir}/man1/mtx-flac.1*
%{_mandir}/man1/mtx-fonts.1*
%{_mandir}/man1/mtx-grep.1*
%{_mandir}/man1/mtx-interface.1*
%{_mandir}/man1/mtx-metapost.1*
# %%{_mandir}/man1/mtx-metatex.1*
%{_mandir}/man1/mtx-modules.1*
%{_mandir}/man1/mtx-package.1*
%{_mandir}/man1/mtx-patterns.1*
%{_mandir}/man1/mtx-pdf.1*
%{_mandir}/man1/mtx-plain.1*
%{_mandir}/man1/mtx-profile.1*
%{_mandir}/man1/mtx-rsync.1*
%{_mandir}/man1/mtx-scite.1*
%{_mandir}/man1/mtx-server.1*
%{_mandir}/man1/mtx-texworks.1*
%{_mandir}/man1/mtx-timing.1*
%{_mandir}/man1/mtx-tools.1*
%{_mandir}/man1/mtx-unicode.1*
%{_mandir}/man1/mtx-unzip.1*
%{_mandir}/man1/mtx-update.1*
%{_mandir}/man1/mtx-vscode.1*
%{_mandir}/man1/mtx-watch.1*
%{_mandir}/man1/mtx-youless.1*
%{_mandir}/man1/mtxrun.1*
%{_mandir}/man1/texexec.1*
%{_mandir}/man1/texmfstart.1*
%{_texdir}/texmf-dist/bibtex/bst/context/
%{_texdir}/texmf-dist/context/
%{_texdir}/texmf-dist/fonts/afm/hoekwater/context/contnav.afm
%{_texdir}/texmf-dist/fonts/cid/fontforge/Adobe-CNS1-4.cidmap
%{_texdir}/texmf-dist/fonts/cid/fontforge/Adobe-GB1-4.cidmap
%{_texdir}/texmf-dist/fonts/cid/fontforge/Adobe-Identity-0.cidmap
%{_texdir}/texmf-dist/fonts/cid/fontforge/Adobe-Japan1-5.cidmap
%{_texdir}/texmf-dist/fonts/cid/fontforge/Adobe-Japan1-6.cidmap
%{_texdir}/texmf-dist/fonts/cid/fontforge/Adobe-Japan2-0.cidmap
%{_texdir}/texmf-dist/fonts/cid/fontforge/Adobe-Korea1-2.cidmap
%{_texdir}/texmf-dist/fonts/enc/dvips/context/
# %%{_texdir}/texmf-dist/fonts/fea/context/
%{_texdir}/texmf-dist/fonts/map/dvips/context/
%{_texdir}/texmf-dist/fonts/map/luatex/context/
%{_texdir}/texmf-dist/fonts/map/pdftex/context/
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/context/
%{_texdir}/texmf-dist/fonts/tfm/hoekwater/context/
%{_texdir}/texmf-dist/fonts/type1/hoekwater/context/
%{_texdir}/texmf-dist/metapost/context/
%exclude %{_texdir}/texmf-dist/scripts/context/perl/mptopdf.pl
%{_texdir}/texmf-dist/scripts/context/
%{_texdir}/texmf-dist/tex/context/
%exclude %{_texdir}/texmf-dist/tex/generic/context/mptopdf
%{_texdir}/texmf-dist/tex/generic/context/
%{_texdir}/texmf-dist/tex/latex/context/
%{fmtutil_cnf_d}/context

%files -n %{shortname}-context-doc
%doc %{_texdir}/texmf-dist/doc/context/

%files -n %{shortname}-convbkmk
%{_bindir}/convbkmk
%{_texdir}/texmf-dist/scripts/convbkmk/
%doc %{_texdir}/texmf-dist/doc/support/convbkmk/

%files -n %{shortname}-crossrefware
%license gpl.txt
%{_bindir}/bbl2bib
%{_bindir}/bibdoiadd
%{_bindir}/bibmradd
%{_bindir}/biburl2doi
%{_bindir}/bibzbladd
%{_bindir}/ltx2crossrefxml
%{_mandir}/man1/bbl2bib.1*
%{_mandir}/man1/bibdoiadd.1*
%{_mandir}/man1/bibmradd.1*
%{_mandir}/man1/biburl2doi.1*
%{_mandir}/man1/bibzbladd.1*
%{_mandir}/man1/ltx2crossrefxml.1*
%{_texdir}/texmf-dist/scripts/crossrefware/
%{_texdir}/texmf-dist/tex/latex/crossrefware/
%doc %{_texdir}/texmf-dist/doc/support/crossrefware/

%files -n %{shortname}-cslatex
%license gpl.txt
%{_bindir}/cslatex
%{_bindir}/pdfcslatex
%{_texdir}/texmf-dist/tex/cslatex/
%{fmtutil_cnf_d}/cslatex

%files -n %{shortname}-csplain
%{_bindir}/csplain
%{_bindir}/pdfcsplain
%{_texdir}/texmf-dist/tex/csplain/
%{fmtutil_cnf_d}/csplain

%files -n %{shortname}-ctan-o-mat
%license bsd.txt
%{_bindir}/ctan-o-mat
%{_mandir}/man1/ctan-o-mat.1*
%{_texdir}/texmf-dist/scripts/ctan-o-mat/
%doc %{_texdir}/texmf-dist/doc/support/ctan-o-mat/

%files -n %{shortname}-ctanbib
%license lppl1.3.txt
%{_bindir}/ctanbib
%{_mandir}/man1/ctanbib.1*
%{_texdir}/texmf-dist/scripts/ctanbib/
%doc %{_texdir}/texmf-dist/doc/support/ctanbib/

%files -n %{shortname}-ctanify
%license lppl1.3.txt
%{_bindir}/ctanify
%{_mandir}/man1/ctanify.1*
%{_texdir}/texmf-dist/scripts/ctanify/
%doc %{_texdir}/texmf-dist/doc/latex/ctanify/

%files -n %{shortname}-ctanupload
%license gpl3.txt
%{_bindir}/ctanupload
%{_texdir}/texmf-dist/scripts/ctanupload/
%doc %{_texdir}/texmf-dist/doc/support/ctanupload/

%files -n %{shortname}-ctie
%license gpl.txt
%{_bindir}/ctie
%{_mandir}/man1/ctie.1*

%files -n %{shortname}-cweb
%license knuth.txt
%{_bindir}/ctangle
%{_bindir}/ctwill
%{_bindir}/ctwill-refsort
%{_bindir}/ctwill-twinx
%{_bindir}/cweave
%{_mandir}/man1/ctangle.1*
%{_mandir}/man1/ctwill.1*
%{_mandir}/man1/ctwill-refsort.1*
%{_mandir}/man1/ctwill-twinx.1*
%{_mandir}/man1/cweave.1*
%{_mandir}/man1/cweb.1*
%{_texdir}/texmf-dist/tex/plain/cweb/
%doc %{_texdir}/texmf-dist/doc/plain/cweb/

%files -n %{shortname}-cyrillic
%license lppl1.3.txt
%{_bindir}/rubibtex
%{_bindir}/rumakeindex
%{_mandir}/man1/rubibtex.1*
%{_mandir}/man1/rumakeindex.1*
%{_texdir}/texmf-dist/tex/latex/cyrillic/
%{_texdir}/texmf-dist/scripts/texlive-extra/rubibtex.sh
%{_texdir}/texmf-dist/scripts/texlive-extra/rumakeindex.sh
%doc %{_texdir}/texmf-dist/doc/latex/cyrillic/

%files -n %{shortname}-de-macro
%{_bindir}/de-macro
%{_texdir}/texmf-dist/scripts/de-macro/
%doc %{_texdir}/texmf-dist/doc/support/de-macro/

%files -n %{shortname}-detex
%{_bindir}/detex
%{_mandir}/man1/detex.1*

%files -n %{shortname}-diadia
%license lppl1.txt
%{_bindir}/diadia
%{_texdir}/texmf-dist/scripts/diadia/
%{_texdir}/texmf-dist/tex/latex/diadia/
%doc %{_texdir}/texmf-dist/doc/latex/diadia/

%files -n %{shortname}-dosepsbin
%{_bindir}/dosepsbin
%{_mandir}/man1/dosepsbin.1*
%{_texdir}/texmf-dist/scripts/dosepsbin/
%doc %{_texdir}/texmf-dist/doc/support/dosepsbin/

%files -n %{shortname}-dtl
%license pd.txt
%{_bindir}/dt2dv
%{_bindir}/dv2dt
%{_mandir}/man1/dt2dv.1*
%{_mandir}/man1/dv2dt.1*

%files -n %{shortname}-dtxgen
%license gpl.txt
%{_bindir}/dtxgen
%{_texdir}/texmf-dist/scripts/dtxgen/
%doc %{_texdir}/texmf-dist/doc/support/dtxgen/

%files -n %{shortname}-dvi2tty
%license gpl.txt
%{_bindir}/disdvi
%{_bindir}/dvi2tty
%{_mandir}/man1/disdvi.1*
%{_mandir}/man1/dvi2tty.1*

%files -n %{shortname}-dviasm
%license gpl3.txt
%{_bindir}/dviasm
%{_mandir}/man1/dviasm.1*
%{_texdir}/texmf-dist/scripts/dviasm/
%doc %{_texdir}/texmf-dist/doc/latex/dviasm/

%files -n %{shortname}-dvicopy
%license gpl.txt
%{_bindir}/dvicopy
%{_mandir}/man1/dvicopy.1*

%files -n %{shortname}-dvidvi
%{_bindir}/dvidvi
%{_mandir}/man1/dvidvi.1*

%files -n %{shortname}-dviinfox
%{_bindir}/dviinfox
%{_texdir}/texmf-dist/scripts/dviinfox/
%doc %{_texdir}/texmf-dist/doc/latex/dviinfox/

%files -n %{shortname}-dviljk
%license gpl.txt
%{_bindir}/dvihp
%{_bindir}/dvilj
%{_bindir}/dvilj2p
%{_bindir}/dvilj4
%{_bindir}/dvilj4l
%{_bindir}/dvilj6
%{_mandir}/man1/dvihp.1*
%{_mandir}/man1/dvilj.1*
%{_mandir}/man1/dvilj2p.1*
%{_mandir}/man1/dvilj4.1*
%{_mandir}/man1/dvilj4l.1*
%{_mandir}/man1/dvilj6.1*

%files -n %{shortname}-dviout-util
%{_bindir}/chkdvifont
%{_bindir}/dvispc
%{_mandir}/man1/chkdvifont.1*
%{_mandir}/man1/dvispc.1*

%files -n %{shortname}-dvipdfmx
%license gpl.txt
%{_bindir}/dvipdfm
%{_bindir}/dvipdfmx
%{_bindir}/dvipdft
%{_bindir}/ebb
%{_bindir}/extractbb
%{_mandir}/man1/dvipdfm.1*
%{_mandir}/man1/dvipdfmx.1*
%{_mandir}/man1/dvipdft.1*
%{_mandir}/man1/ebb.1*
%{_mandir}/man1/extractbb.1*
%{_mandir}/man1/xdvipdfmx.1*
%{_texdir}/texmf-dist/dvipdfmx/
%{_texdir}/texmf-dist/fonts/cmap/dvipdfmx/
%{_texdir}/texmf-dist/fonts/map/dvipdfmx/
%exclude %{_texdir}/texmf-dist/fonts/map/dvipdfmx/ptex-fontmaps/
%{_texdir}/tlpkg/tlpostcode/dvipdfmx.pl
%doc %{_texdir}/texmf-dist/doc/dvipdfm/
%doc %{_texdir}/texmf-dist/doc/dvipdfmx/

%files -n %{shortname}-dvipng
%license lgpl2.1.txt
%{_bindir}/dvigif
%{_bindir}/dvipng
%{_mandir}/man1/dvigif.1*
%{_mandir}/man1/dvipng.1*
%{_infodir}/dvipng.info*
%doc %{_texdir}/texmf-dist/doc/dvipng/

%files -n %{shortname}-dvipos
%license lppl1.txt
%{_bindir}/dvipos
%{_mandir}/man1/dvipos.1*

%files -n %{shortname}-dvips
%license gpl.txt
%{_bindir}/afm2tfm
%{_bindir}/dvips
%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/dvips.1*
%{_infodir}/dvips.info*
%{_texdir}/texmf-dist/dvips/base/
%{_texdir}/texmf-dist/dvips/config/alt-rule.pro
%{_texdir}/texmf-dist/dvips/config/canonex.cfg
%{_texdir}/texmf-dist/dvips/config/config.bakoma
%{_texdir}/texmf-dist/dvips/config/config.canonex
%{_texdir}/texmf-dist/dvips/config/config.cx
%{_texdir}/texmf-dist/dvips/config/config.deskjet
%{_texdir}/texmf-dist/dvips/config/config.dvired
%{_texdir}/texmf-dist/dvips/config/config.epson
%{_texdir}/texmf-dist/dvips/config/config.ibmvga
%{_texdir}/texmf-dist/dvips/config/config.ljfour
%{_texdir}/texmf-dist/dvips/config/config.luc
%{_texdir}/texmf-dist/dvips/config/config.mbn
%{_texdir}/texmf-dist/dvips/config/config.mga
%{_texdir}/texmf-dist/dvips/config/config.mirrorprint
%{_texdir}/texmf-dist/dvips/config/config.ot2
%config(noreplace) %{_sysconfdir}/texlive/dvips/config/config.ps
%{_texdir}/texmf-dist/dvips/config/config.ps
%{_texdir}/texmf-dist/dvips/config/config.qms
%{_texdir}/texmf-dist/dvips/config/config.toshiba
%{_texdir}/texmf-dist/dvips/config/config.unms
%{_texdir}/texmf-dist/dvips/config/config.xyp
%{_texdir}/texmf-dist/dvips/config/cx.cfg
%{_texdir}/texmf-dist/dvips/config/deskjet.cfg
%{_texdir}/texmf-dist/dvips/config/dfaxhigh.cfg
%{_texdir}/texmf-dist/dvips/config/dvired.cfg
%{_texdir}/texmf-dist/dvips/config/epson.cfg
%{_texdir}/texmf-dist/dvips/config/ibmvga.cfg
%{_texdir}/texmf-dist/dvips/config/ljfour.cfg
%{_texdir}/texmf-dist/dvips/config/qms.cfg
%{_texdir}/texmf-dist/dvips/config/toshiba.cfg
%{_texdir}/texmf-dist/fonts/enc/dvips/base/
%{_texdir}/texmf-dist/fonts/map/dvips/
%{_texdir}/texmf-dist/tex/generic/dvips/
%doc %{_texdir}/texmf-dist/doc/dvips/

%files -n %{shortname}-dvisvgm
%license gpl.txt
%{_bindir}/dvisvgm
%{_mandir}/man1/dvisvgm.1*

%files -n %{shortname}-ebong
%license pd.txt
%{_bindir}/ebong
%{_texdir}/texmf-dist/scripts/ebong/
%doc %{_texdir}/texmf-dist/doc/latex/ebong/

%files -n %{shortname}-eplain
%license gpl2.txt
%{_bindir}/eplain
%{_mandir}/man1/eplain.1*
%{_infodir}/eplain.info*
%{_texdir}/texmf-dist/tex/eplain/
%{fmtutil_cnf_d}/eplain
%doc %{_texdir}/texmf-dist/doc/eplain/

%files -n %{shortname}-epspdf
%license gpl.txt
%{_bindir}/epspdf
%{_bindir}/epspdftk
%{_infodir}/epspdf.info*
%{_texdir}/texmf-dist/scripts/epspdf/
%doc %{_texdir}/texmf-dist/doc/support/epspdf/

%files -n %{shortname}-epstopdf
%{_bindir}/epstopdf
%{_bindir}/repstopdf
%{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/repstopdf.1*
%{_texdir}/texmf-dist/scripts/epstopdf/
%doc %{_texdir}/texmf-dist/doc/support/epstopdf/

%files -n %{shortname}-exceltex
%license gpl.txt
%{_bindir}/exceltex
%{_texdir}/texmf-dist/scripts/exceltex/
%{_texdir}/texmf-dist/tex/latex/exceltex/
%doc %{_texdir}/texmf-dist/doc/latex/exceltex/

%files -n %{shortname}-fig4latex
%license gpl3.txt
%{_bindir}/fig4latex
%{_texdir}/texmf-dist/scripts/fig4latex/
%doc %{_texdir}/texmf-dist/doc/support/fig4latex/

%files -n %{shortname}-findhyph
%license gpl.txt
%{_bindir}/findhyph
%{_mandir}/man1/findhyph.1*
%{_texdir}/texmf-dist/scripts/findhyph/
%doc %{_texdir}/texmf-dist/doc/support/findhyph/

%files -n %{shortname}-fontinst
%license lppl1.txt
%{_bindir}/fontinst
%{_mandir}/man1/fontinst.1*
%{_texdir}/texmf-dist/scripts/texlive-extra/fontinst.sh
%{_texdir}/texmf-dist/tex/fontinst/
%{_texdir}/texmf-dist/tex/latex/fontinst/
%doc %{_texdir}/texmf-dist/doc/fonts/fontinst/

%files -n %{shortname}-fontools
%license gpl2.txt
%{_bindir}/afm2afm
%{_bindir}/autoinst
%{_bindir}/ot2kpx
%{_mandir}/man1/afm2afm.1*
%{_mandir}/man1/autoinst.1*
%{_mandir}/man1/ot2kpx.1*
%{_texdir}/texmf-dist/fonts/enc/dvips/fontools/
%{_texdir}/texmf-dist/scripts/fontools/
%doc %{_texdir}/texmf-dist/doc/support/fontools/

%files -n %{shortname}-fontware
%license lppl1.txt
%{_bindir}/pltotf
%{_bindir}/tftopl
%{_bindir}/vftovp
%{_bindir}/vptovf
%{_mandir}/man1/pltotf.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/vftovp.1*
%{_mandir}/man1/vptovf.1*

%files -n %{shortname}-fragmaster
%license gpl.txt
%{_bindir}/fragmaster
%{_texdir}/texmf-dist/scripts/fragmaster/
%doc %{_texdir}/texmf-dist/doc/support/fragmaster/

%files -n %{shortname}-getmap
%license lppl1.txt
%{_bindir}/getmapdl
%{_texdir}/texmf-dist/scripts/getmap/
%{_texdir}/texmf-dist/tex/latex/getmap/
%doc %{_texdir}/texmf-dist/doc/latex/getmap/

%files -n %{shortname}-git-latexdiff
%{_bindir}/git-latexdiff
%{_mandir}/man1/git-latexdiff.*
%doc %{_texdir}/texmf-dist/doc/support/git-latexdiff
%{_texdir}/texmf-dist/scripts/git-latexdiff

%files -n %{shortname}-glossaries
%license lppl1.3.txt
%{_bindir}/makeglossaries
%{_bindir}/makeglossaries-lite
%{_mandir}/man1/makeglossaries.1*
%{_mandir}/man1/makeglossaries-lite.1*
%{_texdir}/texmf-dist/scripts/glossaries/
%{_texdir}/texmf-dist/tex/latex/glossaries/
%doc %{_texdir}/texmf-dist/doc/latex/glossaries/

%files -n %{shortname}-glyphlist
%{_texdir}/texmf-dist/fonts/map/glyphlist/

%files -n %{shortname}-gregoriotex
%license gpl3.txt
%{_bindir}/gregorio
%{_texdir}/texmf-dist/scripts/gregoriotex/
%{_texdir}/texmf-dist/tex/lualatex/gregoriotex/
%{_texdir}/texmf-dist/tex/luatex/gregoriotex/
%{_texdir}/texmf-dist/fonts/source/gregoriotex/
%{_texdir}/texmf-dist/fonts/truetype/public/gregoriotex/
%doc %{_texdir}/texmf-dist/doc/luatex/gregoriotex/

%files -n %{shortname}-gsftopk
%license gpl.txt
%{_bindir}/gsftopk
%{_mandir}/man1/gsftopk.1*
%{_texdir}/texmf-dist/dvips/gsftopk/

%files -n %{shortname}-hyperxmp
%license lppl1.3c.txt
%{_bindir}/hyperxmp-add-bytecount
%{_mandir}/man1/hyperxmp*
%doc %{_texdir}/texmf-dist/doc/latex/hyperxmp
%{_texdir}/texmf-dist/scripts/hyperxmp
%{_texdir}/texmf-dist/tex/latex/hyperxmp

%files -n %{shortname}-installfont
%license lppl1.txt
%{_bindir}/installfont-tl
%{_texdir}/texmf-dist/scripts/installfont/
%doc %{_texdir}/texmf-dist/doc/support/installfont/

%files -n %{shortname}-jadetex
%{_bindir}/jadetex
%{_bindir}/pdfjadetex
%{_mandir}/man1/jadetex.1*
%{_mandir}/man1/pdfjadetex.1*
%{_texdir}/texmf-dist/tex/jadetex/
%{fmtutil_cnf_d}/jadetex
%doc %{_texdir}/texmf-dist/doc/otherformats/jadetex/

%files -n %{shortname}-jfmutil
%{_bindir}/jfmutil
%{_texdir}/texmf-dist/scripts/jfmutil/
%doc %{_texdir}/texmf-dist/doc/fonts/jfmutil/

%files -n %{shortname}-ketcindy
%license gpl3.txt
%{_bindir}/ketcindy
%{_texdir}/texmf-dist/scripts/ketcindy/
%{_texdir}/texmf-dist/tex/latex/ketcindy/
%doc %{_texdir}/texmf-dist/doc/support/ketcindy/

%files -n %{shortname}-kotex-utils
%license lppl1.txt
%{_bindir}/jamo-normalize
%{_bindir}/komkindex
%{_bindir}/ttf2kotexfont
%{_texdir}/texmf-dist/makeindex/kotex-utils/
%{_texdir}/texmf-dist/scripts/kotex-utils/
%doc %{_texdir}/texmf-dist/doc/latex/kotex-utils/

%files -n %{shortname}-kpathsea
%license lgpl2.1.txt
%{_bindir}/kpseaccess
%{_bindir}/kpsereadlink
%{_bindir}/kpsestat
%{_bindir}/kpsewhich
%{_bindir}/mkocp
%{_bindir}/mkofm
%{_bindir}/mktexfmt
%{_bindir}/texhash
%{_sbindir}/generate-fmtutilcnf
%{_mandir}/man1/kpseaccess.1*
%{_mandir}/man1/kpsereadlink.1*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsewhich.1*
%{_mandir}/man1/mkocp.1*
%{_mandir}/man1/mkofm.1*
%{_mandir}/man1/mktexfmt.1*
%{_mandir}/man1/texhash.1*
%{_mandir}/man5/fmtutil.cnf.5*
%{_infodir}/kpathsea.info*
%{_infodir}/tds.info*
%{_infodir}/web2c.info*
%{_texdir}/texmf-dist/web2c/amiga-pl.tcx
%{_texdir}/texmf-dist/web2c/cp1250cs.tcx
%{_texdir}/texmf-dist/web2c/cp1250pl.tcx
%{_texdir}/texmf-dist/web2c/cp1250t1.tcx
%{_texdir}/texmf-dist/web2c/cp227.tcx
%{_texdir}/texmf-dist/web2c/cp852-cs.tcx
%{_texdir}/texmf-dist/web2c/cp852-pl.tcx
%{_texdir}/texmf-dist/web2c/cp8bit.tcx
%{_texdir}/texmf-dist/web2c/empty.tcx
%config(noreplace) %{_sysconfdir}/texlive/web2c/fmtutil.cnf
%ghost %{_texdir}/texmf-dist/web2c/fmtutil.cnf
%{_texdir}/texmf-dist/web2c/il1-t1.tcx
%{_texdir}/texmf-dist/web2c/il2-cs.tcx
%{_texdir}/texmf-dist/web2c/il2-pl.tcx
%{_texdir}/texmf-dist/web2c/il2-t1.tcx
%{_texdir}/texmf-dist/web2c/kam-cs.tcx
%{_texdir}/texmf-dist/web2c/kam-t1.tcx
%{_texdir}/texmf-dist/web2c/macce-pl.tcx
%{_texdir}/texmf-dist/web2c/macce-t1.tcx
%{_texdir}/texmf-dist/web2c/maz-pl.tcx
%config(noreplace) %{_sysconfdir}/texlive/web2c/mktex.cnf
%{_texdir}/texmf-dist/web2c/mktex.cnf
%{_texdir}/texmf-dist/web2c/mktex.opt
%{_texdir}/texmf-dist/web2c/mktexdir
%{_texdir}/texmf-dist/web2c/mktexdir.opt
%{_texdir}/texmf-dist/web2c/mktexnam
%{_texdir}/texmf-dist/web2c/mktexnam.opt
%{_texdir}/texmf-dist/web2c/mktexupd
%{_texdir}/texmf-dist/web2c/natural.tcx
%{_texdir}/texmf-dist/web2c/tcvn-t5.tcx
%config(noreplace) %{_sysconfdir}/texlive/web2c/texmf.cnf
%{_texdir}/texmf-dist/web2c/texmf.cnf
%{_texdir}/texmf-dist/web2c/viscii-t5.tcx
%dir %{fmtutil_cnf_d}
%doc %{_texdir}/texmf-dist/doc/kpathsea/
%doc %{_texdir}/texmf-dist/doc/web2c/

%files -n %{shortname}-l3build
%license lppl1.3.txt
%{_bindir}/l3build
%{_mandir}/man1/l3build.1*
%{_texdir}/texmf-dist/scripts/l3build/
%{_texdir}/texmf-dist/tex/latex/l3build/
%doc %{_texdir}/texmf-dist/doc/latex/l3build/

%files -n %{shortname}-lacheck
%license gpl.txt
%{_bindir}/lacheck
%{_mandir}/man1/lacheck.1*

%files -n %{shortname}-latex
%license lppl1.3.txt
%{_bindir}/dvilualatex
%{_bindir}/latex
%{_bindir}/lualatex
%{_bindir}/pdflatex
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pdflatex.1*
%{_texdir}/texmf-dist/makeindex/latex/
%{_texdir}/texmf-dist/tex/latex/base/
%{fmtutil_cnf_d}/latex-bin
%doc %{_texdir}/texmf-dist/doc/latex/base/

%files -n %{shortname}-latex-git-log
%license gpl3.txt
%{_bindir}/latex-git-log
%{_mandir}/man1/latex-git-log.1*
%{_texdir}/texmf-dist/scripts/latex-git-log/
%doc %{_texdir}/texmf-dist/doc/support/latex-git-log/

%files -n %{shortname}-latex-papersize
%license apache2.txt
%{_bindir}/latex-papersize
%{_texdir}/texmf-dist/scripts/latex-papersize
%doc %{_texdir}/texmf-dist/doc/support/latex-papersize/

%files -n %{shortname}-latex2man
%license lppl1.txt
%{_bindir}/latex2man
%{_mandir}/man1/latex2man.1*
%{_infodir}/latex2man.info*
%{_texdir}/texmf-dist/scripts/latex2man/
%{_texdir}/texmf-dist/tex/latex/latex2man/
%doc %{_texdir}/texmf-dist/doc/support/latex2man/

%files -n %{shortname}-latex2nemeth
%license gpl3.txt
%{_bindir}/latex2nemeth
%{_texdir}/texmf-dist/scripts/latex2nemeth
%doc %{_texdir}/texmf-dist/doc/support/latex2nemeth

%files -n %{shortname}-latexdiff
%license gpl3.txt
%{_bindir}/latexdiff
%{_bindir}/latexdiff-vc
%{_bindir}/latexrevise
%{_mandir}/man1/latexdiff-vc.1*
%{_mandir}/man1/latexdiff.1*
%{_mandir}/man1/latexrevise.1*
%{_texdir}/texmf-dist/scripts/latexdiff/
%doc %{_texdir}/texmf-dist/doc/support/latexdiff/

%files -n %{shortname}-latexfileversion
%license lppl1.txt
%{_bindir}/latexfileversion
%{_texdir}/texmf-dist/scripts/latexfileversion/
%doc %{_texdir}/texmf-dist/doc/support/latexfileversion/

%files -n %{shortname}-latexpand
%license bsd.txt
%{_bindir}/latexpand
%{_texdir}/texmf-dist/scripts/latexpand/
%doc %{_texdir}/texmf-dist/doc/support/latexpand/

%files -n %{shortname}-latexindent
%license gpl3.txt
%{_bindir}/latexindent
%{_texdir}/texmf-dist/scripts/latexindent/
%doc %{_texdir}/texmf-dist/doc/support/latexindent/

%files -n %{shortname}-lcdftypetools
%license gpl.txt
%{_bindir}/cfftot1
%{_bindir}/mmafm
%{_bindir}/mmpfb
%{_bindir}/otfinfo
%{_bindir}/otftotfm
%{_bindir}/t1dotlessj
%{_bindir}/t1lint
%{_bindir}/t1rawafm
%{_bindir}/t1reencode
%{_bindir}/t1testpage
%{_bindir}/ttftotype42
%{_mandir}/man1/cfftot1.1*
%{_mandir}/man1/mmafm.1*
%{_mandir}/man1/mmpfb.1*
%{_mandir}/man1/otfinfo.1*
%{_mandir}/man1/otftotfm.1*
%{_mandir}/man1/t1dotlessj.1*
%{_mandir}/man1/t1lint.1*
%{_mandir}/man1/t1rawafm.1*
%{_mandir}/man1/t1reencode.1*
%{_mandir}/man1/t1testpage.1*
%{_mandir}/man1/ttftotype42.1*

%files -n %{shortname}-lib
%{_libdir}/*.so.*
%dir %{_texdir}/texmf-config
%dir %{_texdir}/texmf-config/web2c
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %{_texdir}/texmf-config/ls-R
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %{_texdir}/texmf-dist/ls-R
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %{_texdir}/texmf-local/ls-R

%files -n %{shortname}-lib-devel
%dir %{_includedir}/kpathsea
%{_includedir}/kpathsea/*
%{_includedir}/synctex/
%{_includedir}/texlua53/
%ifnarch %{power64} s390 s390x
%{_includedir}/texluajit/
%endif
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n %{shortname}-light-latex-make
%{_bindir}/llmk
%{_mandir}/man1/llmk*
%doc %{_texdir}/texmf-dist/doc/support/light-latex-make
%{_texdir}/texmf-dist/scripts/light-latex-make

%files -n %{shortname}-lilyglyphs
%license lppl1.3.txt
%{_bindir}/lily-glyph-commands
%{_bindir}/lily-image-commands
%{_bindir}/lily-rebuild-pdfs
%{_datadir}/fonts/lilyglyphs
%{_texdir}/texmf-dist/fonts/opentype/public/lilyglyphs/
%{_texdir}/texmf-dist/scripts/lilyglyphs/
%{_texdir}/texmf-dist/tex/latex/lilyglyphs/
%doc %{_texdir}/texmf-dist/doc/latex/lilyglyphs/

%files -n %{shortname}-listbib
%license gpl.txt
%{_bindir}/listbib
%{_texdir}/texmf-dist/bibtex/bst/listbib/
%{_texdir}/texmf-dist/scripts/listbib/
%{_texdir}/texmf-dist/tex/latex/listbib/
%doc %{_texdir}/texmf-dist/doc/latex/listbib/

%files -n %{shortname}-listings-ext
%license lppl1.2.txt
%{_bindir}/listings-ext.sh
%{_texdir}/texmf-dist/scripts/listings-ext/
%{_texdir}/texmf-dist/tex/latex/listings-ext/
%doc %{_texdir}/texmf-dist/doc/latex/listings-ext/

%files -n %{shortname}-lollipop
%license gpl3.txt
%{_bindir}/lollipop
%{_texdir}/texmf-dist/tex/lollipop/
%{fmtutil_cnf_d}/lollipop
%doc %{_texdir}/texmf-dist/doc/otherformats/lollipop/

%files -n %{shortname}-ltxfileinfo
%license gpl.txt
%{_bindir}/ltxfileinfo
%{_texdir}/texmf-dist/scripts/ltxfileinfo/
%doc %{_texdir}/texmf-dist/doc/support/ltxfileinfo/

%files -n %{shortname}-ltximg
%license gpl2.txt
%{_bindir}/ltximg
%{_texdir}/texmf-dist/scripts/ltximg/
%doc %{_texdir}/texmf-dist/doc/support/ltximg/

%files -n %{shortname}-luaotfload
%license gpl2.txt
%{_bindir}/luaotfload-tool
%{_mandir}/man1/luaotfload-tool.1*
%{_mandir}/man5/luaotfload.conf.5*
%{_texdir}/texmf-dist/scripts/luaotfload/
%{_texdir}/texmf-dist/tex/luatex/luaotfload/
%doc %{_texdir}/texmf-dist/doc/luatex/luaotfload/

%files -n %{shortname}-luahbtex
%license gpl2.txt
%{_bindir}/luahbtex
%{_bindir}/lualatex-dev
%{_mandir}/man1/luahbtex.1*
%{_mandir}/man1/lualatex-dev.1*
%{fmtutil_cnf_d}/luahbtex

%files -n %{shortname}-luajittex
%license gpl2.txt
%ifnarch %{power64} s390 s390x
%{_bindir}/luajittex
%{_bindir}/luajithbtex
%{_bindir}/texluajit
%{_bindir}/texluajitc
%endif
%{_mandir}/man1/luajittex.1*
%{fmtutil_cnf_d}/luajittex

%files -n %{shortname}-luatex
%license gpl2.txt
%{_bindir}/dviluatex
%{_bindir}/dvilualatex-dev
%{_bindir}/luacsplain
%{_bindir}/luatex
%{_bindir}/texlua
%{_bindir}/texluac
%{_mandir}/man1/dvilualatex-dev.1*
%{_mandir}/man1/dviluatex.1*
%{_mandir}/man1/luatex.1*
%{_mandir}/man1/texlua.1*
%{_mandir}/man1/texluac.1*
%{_texdir}/texmf-dist/tex/generic/config/luatex-unicode-letters.tex
%{_texdir}/texmf-dist/tex/generic/config/luatexiniconfig.tex
%{_texdir}/texmf-dist/web2c/texmfcnf.lua
%{fmtutil_cnf_d}/luatex
%doc %{_texdir}/texmf-dist/doc/luatex/base/

%files -n %{shortname}-lwarp
%license lppl1.3.txt
%{_bindir}/lwarpmk
%{_texdir}/texmf-dist/scripts/lwarp
%{_texdir}/texmf-dist/tex/latex/lwarp
%doc %{_texdir}/texmf-dist/doc/latex/lwarp

%files -n %{shortname}-lyluatex
%{_texdir}/texmf-dist/scripts/lyluatex/
%{_texdir}/texmf-dist/tex/luatex/lyluatex/
%doc %{_texdir}/texmf-dist/doc/support/lyluatex/

%files -n %{shortname}-make4ht
%license lppl1.3.txt
%{_bindir}/make4ht
%{_texdir}/texmf-dist/scripts/make4ht/
%doc %{_texdir}/texmf-dist/doc/support/make4ht/

%files -n %{shortname}-makedtx
%license lppl1.txt
%{_bindir}/makedtx
%{_texdir}/texmf-dist/scripts/makedtx/
%{_texdir}/texmf-dist/tex/latex/makedtx/
%doc %{_texdir}/texmf-dist/doc/support/makedtx/

%files -n %{shortname}-makeindex
%{_bindir}/makeindex
%{_bindir}/mkindex
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/mkindex.1*
%exclude %{_texdir}/texmf-dist/makeindex/latex/
%{_texdir}/texmf-dist/makeindex/
%{_texdir}/texmf-dist/tex/plain/makeindex/
%doc %{_texdir}/texmf-dist/doc/support/makeindex/

%files -n %{shortname}-match_parens
%license gpl.txt
%{_bindir}/match_parens
%{_texdir}/texmf-dist/scripts/match_parens/
%doc %{_texdir}/texmf-dist/doc/support/match_parens/

%files -n %{shortname}-mathspic
%license lppl1.txt
%{_bindir}/mathspic
%{_mandir}/man1/mathspic.1*
%{_texdir}/texmf-dist/scripts/mathspic/
%{_texdir}/texmf-dist/tex/latex/mathspic/
%doc %{_texdir}/texmf-dist/doc/latex/mathspic/

%files -n %{shortname}-metafont
%license knuth.txt
%{_bindir}/inimf
%{_bindir}/mf
%{_bindir}/mf-nowin
%{_mandir}/man1/inimf.1.*
%{_mandir}/man1/mf-nowin.1*
%{_mandir}/man1/mf.1*
%{_texdir}/texmf-dist/metafont/
%{fmtutil_cnf_d}/metafont

%files -n %{shortname}-metapost
%license lgpl2.1.txt
%{_bindir}/dvitomp
%{_bindir}/mfplain
%{_bindir}/mpost
%{_bindir}/r-mpost
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/mpost.1*
%{_texdir}/texmf-dist/fonts/afm/metapost/
%{_texdir}/texmf-dist/fonts/enc/dvips/metapost/
%{_texdir}/texmf-dist/fonts/map/dvips/metapost/
%{_texdir}/texmf-dist/fonts/tfm/metapost/
%{_texdir}/texmf-dist/fonts/type1/metapost/
%exclude %{_texdir}/texmf-dist/metapost/context/
%{_texdir}/texmf-dist/metapost/
%{_texdir}/texmf-dist/tex/generic/metapost/
%doc %{_texdir}/texmf-dist/doc/metapost/

%files -n %{shortname}-mex
%license pd.txt
%{_bindir}/mex
%{_bindir}/pdfmex
%{_bindir}/utf8mex
%{_texdir}/texmf-dist/tex/mex/
%{fmtutil_cnf_d}/mex
%doc %{_texdir}/texmf-dist/doc/mex/

%files -n %{shortname}-mflua
%license gpl2.txt
%{_bindir}/mflua
%{_bindir}/mflua-nowin
%ifnarch %{power64} s390 s390x
%{_bindir}/mfluajit
%{_bindir}/mfluajit-nowin
%endif
%{fmtutil_cnf_d}/mflua
%{_texdir}/texmf-dist/scripts/mflua/

%files -n %{shortname}-mfware
%license knuth.txt
%{_bindir}/gftodvi
%{_bindir}/gftopk
%{_bindir}/gftype
%{_bindir}/mft
%{_bindir}/pktogf
%{_bindir}/pktype
%{_mandir}/man1/gftodvi.1*
%{_mandir}/man1/gftopk.1*
%{_mandir}/man1/gftype.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/pktogf.1*
%{_mandir}/man1/pktype.1*
%{_texdir}/texmf-dist/mft/

%files -n %{shortname}-mf2pt1
%license lppl1.txt
%{_bindir}/mf2pt1
%{_infodir}/mf2pt1.info*
%{_texdir}/texmf-dist/metapost/mf2pt1/
%{_texdir}/texmf-dist/scripts/mf2pt1/
%doc %{_texdir}/texmf-dist/doc/support/mf2pt1/

%files -n %{shortname}-mkgrkindex
%{_bindir}/mkgrkindex
%{_texdir}/texmf-dist/makeindex/mkgrkindex/
%{_texdir}/texmf-dist/scripts/mkgrkindex/
%doc %{_texdir}/texmf-dist/doc/support/mkgrkindex/

%files -n %{shortname}-mkjobtexmf
%{_bindir}/mkjobtexmf
%{_mandir}/man1/mkjobtexmf.1*
%{_texdir}/texmf-dist/scripts/mkjobtexmf/
%doc %{_texdir}/texmf-dist/doc/generic/mkjobtexmf/

%files -n %{shortname}-mkpic
%license gpl.txt
%{_bindir}/mkpic
%{_texdir}/texmf-dist/scripts/mkpic/
%doc %{_texdir}/texmf-dist/doc/support/mkpic/

%files -n %{shortname}-mltex
%license knuth.txt
%{_bindir}/mllatex
%{_bindir}/mltex
%{_texdir}/texmf-dist/tex/latex/mltex/
%{_texdir}/texmf-dist/tex/mltex/
%{fmtutil_cnf_d}/mltex
%doc %{_texdir}/texmf-dist/doc/latex/mltex/

%files -n %{shortname}-mptopdf
%license lppl1.txt
%{_bindir}/mptopdf
%{_mandir}/man1/mptopdf.1*
%{_texdir}/texmf-dist/scripts/context/perl/mptopdf.pl
%{_texdir}/texmf-dist/tex/context/base/mkii/supp-mis.mkii
%{_texdir}/texmf-dist/tex/context/base/mkii/supp-mpe.mkii
%{_texdir}/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
%{_texdir}/texmf-dist/tex/context/base/mkii/syst-tex.mkii
%{_texdir}/texmf-dist/tex/generic/context/mptopdf/
%{fmtutil_cnf_d}/mptopdf
%doc %{_texdir}/texmf-dist/doc/context/scripts/mkii/mptopdf.man

%files -n %{shortname}-multibibliography
%license lppl1.3.txt
%{_bindir}/multibibliography
%{_texdir}/texmf-dist/bibtex/bst/multibibliography/
%{_texdir}/texmf-dist/scripts/multibibliography/
%{_texdir}/texmf-dist/tex/latex/multibibliography/
%doc %{_texdir}/texmf-dist/doc/latex/multibibliography/

%files -n %{shortname}-musixtex
%license gpl2.txt
%{_bindir}/musixflx
%{_bindir}/musixtex
%{_mandir}/man1/musixflx.1*
%{_mandir}/man1/musixtex.1*
%{_texdir}/texmf-dist/dvips/musixtex/
%{_texdir}/texmf-dist/scripts/musixtex/
%{_texdir}/texmf-dist/tex/generic/musixtex/
%{_texdir}/texmf-dist/tex/latex/musixtex/
%doc %{_texdir}/texmf-dist/doc/generic/musixtex/

%files -n %{shortname}-musixtnt
%license gpl2.txt
%{_bindir}/msxlint
%{_mandir}/man1/msxlint.1*
%{_texdir}/texmf-dist/tex/generic/musixtnt/
%doc %{_texdir}/texmf-dist/doc/generic/musixtnt/

%files -n %{shortname}-m-tx
%license gpl.txt
%{_bindir}/m-tx
%{_bindir}/prepmx
%{_mandir}/man1/prepmx.1*
%{_texdir}/texmf-dist/scripts/m-tx/
%{_texdir}/texmf-dist/tex/generic/m-tx/
%{_texdir}/texmf-dist/tex/latex/m-tx/
%doc %{_texdir}/texmf-dist/doc/generic/m-tx/

%files -n %{shortname}-oberdiek
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bib/oberdiek/
%{_texdir}/texmf-dist/tex/generic/oberdiek/
%{_texdir}/texmf-dist/tex/latex/oberdiek/
%doc %{_texdir}/texmf-dist/doc/latex/oberdiek/

%files -n %{shortname}-omegaware
%license lppl1.txt
%{_bindir}/odvicopy
%{_bindir}/odvitype
%{_bindir}/ofm2opl
%{_bindir}/omfonts
%{_bindir}/opl2ofm
%{_bindir}/otangle
%{_bindir}/otp2ocp
%{_bindir}/outocp
%{_bindir}/ovf2ovp
%{_bindir}/ovp2ovf
%{_bindir}/wofm2opl
%{_bindir}/wopl2ofm
%{_bindir}/wovf2ovp
%{_mandir}/man1/odvicopy.1*
%{_mandir}/man1/odvitype.1*
%{_mandir}/man1/ofm2opl.1*
%{_mandir}/man1/opl2ofm.1*
%{_mandir}/man1/otangle.1*
%{_mandir}/man1/otp2ocp.1*
%{_mandir}/man1/outocp.1*
%{_mandir}/man1/ovf2ovp.1*
%{_mandir}/man1/ovp2ovf.1*

%files -n %{shortname}-optex
%{_bindir}/optex
%{fmtutil_cnf_d}/optex
%{_mandir}/man1/optex.1*
%{_texdir}/texmf-dist/tex/optex/
%doc %{_texdir}/texmf-dist/doc/optex/

%files -n %{shortname}-patgen
%license knuth.txt
%{_bindir}/patgen
%{_mandir}/man1/patgen.1*

%files -n %{shortname}-pax
%{_bindir}/pdfannotextractor
%{_texdir}/texmf-dist/scripts/pax/
%{_texdir}/texmf-dist/tex/latex/pax/
%doc %{_texdir}/texmf-dist/doc/latex/pax/

%files -n %{shortname}-pdfbook2
%license gpl3.txt
%{_bindir}/pdfbook2
%{_mandir}/man1/pdfbook2.1*
%{_texdir}/texmf-dist/scripts/pdfbook2/
%doc %{_texdir}/texmf-dist/doc/support/pdfbook2/

%files -n %{shortname}-pdfcrop
%license lppl1.txt
%{_bindir}/pdfcrop
%{_bindir}/rpdfcrop
%{_texdir}/texmf-dist/scripts/pdfcrop/
%doc %{_texdir}/texmf-dist/doc/support/pdfcrop/

%files -n %{shortname}-pdfjam
%license gpl2.txt
%{_bindir}/pdfjam
%{_mandir}/man1/pdfjam.1*
%{_texdir}/texmf-dist/scripts/pdfjam/
%doc %{_texdir}/texmf-dist/doc/support/pdfjam/

%files -n %{shortname}-pdflatexpicscale
%license lppl.txt
%{_bindir}/pdflatexpicscale
%{_texdir}/texmf-dist/scripts/pdflatexpicscale
%doc %{_texdir}/texmf-dist/doc/support/pdflatexpicscale

%files -n %{shortname}-pdftex
%license gpl.txt
%{_bindir}/etex
%{_bindir}/latex-dev
%{_bindir}/pdfetex
%{_bindir}/pdflatex-dev
%{_bindir}/pdftex
%{_bindir}/simpdftex
%{_mandir}/man1/latex-dev.1*
%{_mandir}/man1/pdfetex.1*
%{_mandir}/man1/pdflatex-dev.1*
%{_mandir}/man1/pdftex.1*
%{_texdir}/texmf-dist/fonts/map/dvips/dummy-space/dummy-space.map
%{_texdir}/texmf-dist/fonts/tfm/public/pdftex/
%{_texdir}/texmf-dist/fonts/type1/public/pdftex/
%{_texdir}/texmf-dist/scripts/simpdftex/simpdftex
%{_texdir}/texmf-dist/tex/generic/config/pdftex-dvi.tex
%{_texdir}/texmf-dist/tex/generic/pdftex/
%{fmtutil_cnf_d}/latex-bin-dev
%{fmtutil_cnf_d}/pdftex
%doc %{_texdir}/texmf-dist/doc/pdftex/

%files -n %{shortname}-pdftex-quiet
%license gpl3.txt
%{_bindir}/pdftex-quiet
%{_texdir}/texmf-dist/scripts/pdftex-quiet/
%doc %{_texdir}/texmf-dist/doc/support/pdftex-quiet/

%files -n %{shortname}-pdftosrc
%license gpl2.txt
%{_bindir}/pdftosrc
%{_mandir}/man1/pdftosrc.1*

%files -n %{shortname}-pdfxup
%license lppl1.3.txt
%{_bindir}/pdfxup
%{_mandir}/man1/pdfxup.1*
%{_texdir}/texmf-dist/tex/latex/pdfxup/
%{_texdir}/texmf-dist/scripts/pdfxup/
%doc %{_texdir}/texmf-dist/doc/support/pdfxup/

%files -n %{shortname}-pedigree-perl
%license gpl2.txt
%{_bindir}/pedigree
%{_mandir}/man1/pedigree.1*
%{_texdir}/texmf-dist/scripts/pedigree-perl/
%doc %{_texdir}/texmf-dist/doc/support/pedigree-perl/

%files -n %{shortname}-perltex
%license lppl1.txt
%{_bindir}/perltex
%{_mandir}/man1/perltex.1*
%{_texdir}/texmf-dist/scripts/perltex/
%{_texdir}/texmf-dist/tex/latex/perltex/
%doc %{_texdir}/texmf-dist/doc/latex/perltex/

%files -n %{shortname}-petri-nets
%license gpl.txt
%{_bindir}/pn2pdf
%{_texdir}/texmf-dist/scripts/petri-nets/
%{_texdir}/texmf-dist/tex/generic/petri-nets/
%doc %{_texdir}/texmf-dist/doc/generic/petri-nets/

%files -n %{shortname}-pfarrei
%license lppl1.3.txt
%{_bindir}/a5toa4
%{_bindir}/pfarrei
%{_texdir}/texmf-dist/scripts/pfarrei/
%{_texdir}/texmf-dist/tex/latex/pfarrei/
%doc %{_texdir}/texmf-dist/doc/latex/pfarrei/

%files -n %{shortname}-pkfix
%license lppl1.3.txt
%{_bindir}/pkfix
%{_texdir}/texmf-dist/scripts/pkfix/
%doc %{_texdir}/texmf-dist/doc/support/pkfix/

%files -n %{shortname}-pkfix-helper
%license lppl1.txt
%{_bindir}/pkfix-helper
%{_mandir}/man1/pkfix-helper.1*
%{_texdir}/texmf-dist/scripts/pkfix-helper/
%doc %{_texdir}/texmf-dist/doc/support/pkfix-helper/

%files -n %{shortname}-pmx
%license gpl2.txt
%{_bindir}/pmxab
%{_bindir}/scor2prt
%{_mandir}/man1/pmxab.1*
%{_mandir}/man1/scor2prt.1*
%{_texdir}/texmf-dist/tex/generic/pmx/
%doc %{_texdir}/texmf-dist/doc/generic/pmx/

%files -n %{shortname}-pmxchords
%license gpl2.txt
%{_bindir}/pmxchords
%{_mandir}/man1/pmxchords.1*
%{_texdir}/texmf-dist/scripts/pmxchords/
%{_texdir}/texmf-dist/tex/generic/pmxchords/
%doc %{_texdir}/texmf-dist/doc/pmxchords/

%files -n %{shortname}-pst2pdf
%license gpl2.txt
%{_bindir}/pst2pdf
%{_texdir}/texmf-dist/scripts/pst2pdf/
%doc %{_texdir}/texmf-dist/doc/support/pst2pdf/

%files -n %{shortname}-pst-pdf
%license lppl1.txt
%{_bindir}/ps4pdf
%{_texdir}/texmf-dist/scripts/pst-pdf/
%{_texdir}/texmf-dist/tex/latex/pst-pdf/
%doc %{_texdir}/texmf-dist/doc/latex/pst-pdf/

%files -n %{shortname}-psutils
%{_bindir}/tl-epsffit
%{_bindir}/tl-extractres
%{_bindir}/tl-includeres
%{_bindir}/tl-psbook
%{_bindir}/tl-psjoin
%{_bindir}/tl-psnup
%{_bindir}/tl-psresize
%{_bindir}/tl-psselect
%{_bindir}/tl-pstops
%{_mandir}/man1/tl-epsffit.1*
%{_mandir}/man1/tl-extractres.1*
%{_mandir}/man1/tl-includeres.1*
%{_mandir}/man1/tl-psbook.1*
%{_mandir}/man1/tl-psjoin.1*
%{_mandir}/man1/tl-psnup.1*
%{_mandir}/man1/tl-psresize.1*
%{_mandir}/man1/tl-psselect.1*
%{_mandir}/man1/tl-pstops.1*
%{_mandir}/man1/tl-psutils.1*
%{_texdir}/texmf-dist/dvips/getafm/
%{_texdir}/texmf-dist/psutils/
%dir %{_sysconfdir}/texlive/psutils
%config(noreplace) %{_sysconfdir}/texlive/psutils/paper.cfg
%{_texdir}/texmf-dist/scripts/psutils

%files -n %{shortname}-ps2eps
%license gpl.txt
%{_bindir}/bbox
%{_bindir}/ps2eps
%{_mandir}/man1/bbox.1*
%{_mandir}/man1/ps2eps.1*
%{_texdir}/texmf-dist/scripts/ps2eps/

%files -n %{shortname}-ps2pk
%license other-free.txt
%{_bindir}/mag
%{_bindir}/pfb2pfa
%{_bindir}/pk2bm
%{_bindir}/ps2pk
%{_mandir}/man1/mag.1*
%{_mandir}/man1/pfb2pfa.1*
%{_mandir}/man1/pk2bm.1*
%{_mandir}/man1/ps2pk.1*

%files -n %{shortname}-ptex
%{_bindir}/eptex
%{_bindir}/makejvf
%{_bindir}/mendex
%{_bindir}/pbibtex
%{_bindir}/pdvitomp
%{_bindir}/pdvitype
%{_bindir}/platex
%{_bindir}/platex-dev
%{_bindir}/pmpost
%{_bindir}/ppltotf
%{_bindir}/ptex
%{_bindir}/ptftopl
%{_bindir}/r-pmpost
%{_mandir}/man1/eptex.1*
%{_mandir}/man1/makejvf.1*
%{_mandir}/man1/mendex.1*
%{_mandir}/man1/platex-dev.1*
%{_mandir}/man1/ppltotf.1*
%{_mandir}/man1/ptex.1*
%{_mandir}/man1/ptftopl.1*
%{fmtutil_cnf_d}/platex
%{fmtutil_cnf_d}/ptex

%files -n %{shortname}-ptex-fontmaps
%license gpl3.txt
%license pd.txt
%{_bindir}/kanji-config-updmap
%{_bindir}/kanji-config-updmap-sys
%{_bindir}/kanji-config-updmap-user
%{_bindir}/kanji-fontmap-creator
%{_texdir}/texmf-dist/fonts/cmap/ptex-fontmaps
%{_texdir}/texmf-dist/fonts/map/dvipdfmx/ptex-fontmaps
%{_texdir}/texmf-dist/fonts/misc/ptex-fontmaps/
%{_texdir}/texmf-dist/scripts/ptex-fontmaps
%{_texdir}/tlpkg/tlpostcode/ptex-fontmaps-tlpost.pl
%doc %{_texdir}/texmf-dist/doc/fonts/ptex-fontmaps

%files -n %{shortname}-ptex2pdf
%license gpl2.txt
%{_bindir}/ptex2pdf
%{_texdir}/texmf-dist/scripts/ptex2pdf/
%{_texdir}/tlpkg/tlpostcode/ptex2pdf-tlpost.pl
%doc %{_texdir}/texmf-dist/doc/latex/ptex2pdf/

%files -n %{shortname}-purifyeps
%license lppl1.txt
%{_bindir}/purifyeps
%{_mandir}/man1/purifyeps.1*
%{_texdir}/texmf-dist/scripts/purifyeps/
%doc %{_texdir}/texmf-dist/doc/support/purifyeps/

%files -n %{shortname}-pygmentex
%license lppl1.3.txt
%{_bindir}/pygmentex
%{_texdir}/texmf-dist/scripts/pygmentex/
%{_texdir}/texmf-dist/tex/latex/pygmentex/
%doc %{_texdir}/texmf-dist/doc/latex/pygmentex/

%files -n %{shortname}-pythontex
%license lppl1.3.txt
%{_bindir}/depythontex
%{_bindir}/pythontex
%{_texdir}/texmf-dist/scripts/pythontex/
%{_texdir}/texmf-dist/tex/latex/pythontex/
%doc %{_texdir}/texmf-dist/doc/latex/pythontex/

%files -n %{shortname}-rubik
%license lppl1.3.txt
%{_bindir}/rubikrotation
%{_mandir}/man1/rubikrotation.1*
%{_texdir}/texmf-dist/scripts/rubik/
%{_texdir}/texmf-dist/tex/latex/rubik/
%doc %{_texdir}/texmf-dist/doc/latex/rubik/

%files -n %{shortname}-seetexk
%{_bindir}/dvibook
%{_bindir}/dviconcat
%{_bindir}/dviselect
%{_bindir}/dvitodvi
%{_mandir}/man1/dvibook.1*
%{_mandir}/man1/dviconcat.1*
%{_mandir}/man1/dviselect.1*
%{_mandir}/man1/dvitodvi.1*

%files -n %{shortname}-spix
%license gpl3.txt
%{_bindir}/spix
%{_mandir}/man1/spix*
%doc %{_texdir}/texmf-dist/doc/support/spix
%{_texdir}/texmf-dist/scripts/spix

%files -n %{shortname}-splitindex
%license lppl1.txt
%{_bindir}/splitindex
%{_mandir}/man1/splitindex.1*
%{_texdir}/texmf-dist/scripts/splitindex/
%{_texdir}/texmf-dist/tex/generic/splitindex/
%{_texdir}/texmf-dist/tex/latex/splitindex/
%doc %{_texdir}/texmf-dist/doc/latex/splitindex/

%files -n %{shortname}-srcredact
%license gpl2.txt
%{_bindir}/srcredact
%{_mandir}/man1/srcredact.1*
%{_texdir}/texmf-dist/scripts/srcredact/
%doc %{_texdir}/texmf-dist/doc/support/srcredact/

%files -n %{shortname}-sty2dtx
%license gpl3.txt
%{_bindir}/sty2dtx
%{_mandir}/man1/sty2dtx.1*
%{_texdir}/texmf-dist/scripts/sty2dtx/
%doc %{_texdir}/texmf-dist/doc/support/sty2dtx/

%files -n %{shortname}-svn-multi
%license lppl1.txt
%{_bindir}/svn-multi
%{_texdir}/texmf-dist/scripts/svn-multi/
%{_texdir}/texmf-dist/tex/latex/svn-multi/
%doc %{_texdir}/texmf-dist/doc/latex/svn-multi/
%doc %{_texdir}/texmf-dist/doc/support/svn-multi/

%files -n %{shortname}-synctex
%license lppl1.txt
%{_bindir}/synctex
%{_mandir}/man1/synctex.1*
%{_mandir}/man5/synctex.5*

%files -n %{shortname}-tex
%license knuth.txt
%{_bindir}/initex
%{_bindir}/tex
%{_mandir}/man1/initex.1*
%{_mandir}/man1/tex.1*
%{fmtutil_cnf_d}/tex

%files -n %{shortname}-tex4ebook
%license lppl1.3.txt
%{_bindir}/tex4ebook
%{_texdir}/texmf-dist/scripts/tex4ebook/
%{_texdir}/texmf-dist/tex/latex/tex4ebook/
%doc %{_texdir}/texmf-dist/doc/support/tex4ebook/

%files -n %{shortname}-tex4ht
%license lppl1.txt
%{_bindir}/ht
%{_bindir}/htcontext
%{_bindir}/htlatex
%{_bindir}/htmex
%{_bindir}/httex
%{_bindir}/httexi
%{_bindir}/htxelatex
%{_bindir}/htxetex
%{_bindir}/mk4ht
%{_bindir}/t4ht
%{_bindir}/tex4ht
%{_bindir}/xhlatex
%{_texdir}/texmf-dist/scripts/tex4ht/
%{_texdir}/texmf-dist/tex/generic/tex4ht/
%{_texdir}/texmf-dist/tex4ht/
%doc %{_texdir}/texmf-dist/doc/generic/tex4ht/

%files -n %{shortname}-texcount
%license lppl1.txt
%{_bindir}/texcount
%{_texdir}/texmf-dist/scripts/texcount/
%doc %{_texdir}/texmf-dist/doc/support/texcount/

%files -n %{shortname}-texdef
%license gpl3.txt
%{_bindir}/latexdef
%{_bindir}/texdef
%{_texdir}/texmf-dist/scripts/texdef/
%doc %{_texdir}/texmf-dist/doc/support/texdef/

%files -n %{shortname}-texdiff
%license gpl.txt
%{_bindir}/texdiff
%{_texdir}/texmf-dist/scripts/texdiff
%{_mandir}/man1/texdiff.1*
%doc %{_texdir}/texmf-dist/doc/support/texdiff/

%files -n %{shortname}-texdirflatten
%{_bindir}/texdirflatten
%{_mandir}/man1/texdirflatten.1*
%{_texdir}/texmf-dist/scripts/texdirflatten/
%doc %{_texdir}/texmf-dist/doc/support/texdirflatten/

%files -n %{shortname}-texdoc
%license gpl.txt
%{_bindir}/texdoc
%{_mandir}/man1/texdoc.1*
%{_texdir}/texmf-dist/scripts/texdoc/
%{_texdir}/texmf-dist/texdoc/
%doc %{_texdir}/texmf-dist/doc/support/texdoc/

%files -n %{shortname}-texdoctk
%license gpl.txt
%{_bindir}/texdoctk
%{_mandir}/man1/texdoctk.1*
%{_texdir}/texmf-dist/scripts/texdoctk/
%{_texdir}/texmf-dist/texdoctk/

%files -n %{shortname}-texfot
%license pd.txt
%{_bindir}/texfot
%{_mandir}/man1/texfot.1*
%{_texdir}/texmf-dist/scripts/texfot/
%doc %{_texdir}/texmf-dist/doc/support/texfot/

%files -n %{shortname}-texliveonfly
%license gpl3.txt
%{_bindir}/texliveonfly
%{_texdir}/texmf-dist/scripts/texliveonfly/
%doc %{_texdir}/texmf-dist/doc/support/texliveonfly/

%files -n %{shortname}-texlive-en
%{_infodir}/tlbuild.info*
%doc %{_texdir}/texmf-dist/doc/texlive/texlive-en/
%doc %{_texdir}/texmf-dist/doc/texlive/tlbuild/tlbuild.html
%doc %{_texdir}/texmf-dist/doc/texlive/tlbuild/tlbuild.pdf

%files -n %{shortname}-texlive-scripts
%license lppl1.txt
%{_bindir}/fmtutil
%{_bindir}/fmtutil-sys
%{_bindir}/fmtutil-user
%{_bindir}/mktexlsr
%{_bindir}/mktexmf
%{_bindir}/mktexpk
%{_bindir}/mktextfm
%{_bindir}/updmap
%{_bindir}/updmap-sys
%{_bindir}/updmap-user
%{_bindir}/rungs
%{_mandir}/man1/fmtutil.1*
%{_mandir}/man1/fmtutil-sys.1*
%{_mandir}/man1/fmtutil-user.1*
%{_mandir}/man1/install-tl.1*
%{_mandir}/man1/mktexlsr.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/updmap.1*
%{_mandir}/man1/updmap-sys.1*
%{_mandir}/man1/updmap-user.1*
%{_mandir}/man5/updmap.cfg.5*
%{_texdir}/texmf-config/web2c/updmap.cfg
%config(noreplace) %{_sysconfdir}/texlive/web2c/updmap.cfg
%{_texdir}/texmf-dist/dvips/tetex/
%{_texdir}/texmf-dist/fonts/enc/dvips/tetex/
%{_texdir}/texmf-dist/fonts/map/dvips/tetex/
%{_texdir}/texmf-dist/scripts/texlive/fmtutil-sys.sh
%{_texdir}/texmf-dist/scripts/texlive/fmtutil-user.sh
%{_texdir}/texmf-dist/scripts/texlive/fmtutil.pl
%{_texdir}/texmf-dist/scripts/texlive/mktexlsr*
%{_texdir}/texmf-dist/scripts/texlive/mktexmf
%{_texdir}/texmf-dist/scripts/texlive/mktexpk
%{_texdir}/texmf-dist/scripts/texlive/mktextfm
%{_texdir}/texmf-dist/scripts/texlive/rungs.tlu
%{_texdir}/texmf-dist/scripts/texlive/updmap-sys.sh
%{_texdir}/texmf-dist/scripts/texlive/updmap-user.sh
%{_texdir}/texmf-dist/scripts/texlive/updmap.pl
%{_texdir}/texmf-dist/web2c/updmap.cfg

%files -n %{shortname}-texlive-scripts-extra
%license gpl.txt
%license lppl1.txt
%{_bindir}/allcm
%{_bindir}/allec
%{_bindir}/allneeded
%{_bindir}/dvi2fax
%{_bindir}/dvired
%{_bindir}/e2pall
%{_bindir}/kpsepath
%{_bindir}/kpsetool
%{_bindir}/kpsewhere
%{_bindir}/kpsexpand
%{_bindir}/ps2frag
%{_bindir}/pslatex
%{_bindir}/texconfig-dialog
%{_bindir}/texconfig-sys
%{_bindir}/texconfig
%{_bindir}/texlinks
%{_mandir}/man1/allcm.1*
%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/e2pall.1*
%{_mandir}/man1/kpsepath.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhere.1*
%{_mandir}/man1/kpsexpand.1*
%{_mandir}/man1/ps2frag.1*
%{_mandir}/man1/pslatex.1*
%{_mandir}/man1/texconfig-sys.1*
%{_mandir}/man1/texconfig.1*
%{_mandir}/man1/texlinks.1*
%{_texdir}/texmf-dist/texconfig/
%{_texdir}/texmf-dist/scripts/texlive-extra/


%files -n %{shortname}-texlive.infra
%license lppl1.txt
%{_bindir}/tlmgr
%{_texdir}/texmf-dist/web2c/fmtutil-hdr.cnf
%{_texdir}/texmf-dist/web2c/updmap-hdr.cfg
%{_texdir}/LICENSE.CTAN
%{_texdir}/LICENSE.TL
%{_texdir}/README
%{_texdir}/README.usergroups
%{_texdir}/index.html
%{_texdir}/readme-html.dir/readme.cs.html
%{_texdir}/readme-html.dir/readme.de.html
%{_texdir}/readme-html.dir/readme.en.html
%{_texdir}/readme-html.dir/readme.es.html
%{_texdir}/readme-html.dir/readme.fr.html
%{_texdir}/readme-html.dir/readme.it.html
%{_texdir}/readme-html.dir/readme.ja.html
%{_texdir}/readme-html.dir/readme.pl.html
%{_texdir}/readme-html.dir/readme.pt-br.html
%{_texdir}/readme-html.dir/readme.ru.html
%{_texdir}/readme-html.dir/readme.sk.html
%{_texdir}/readme-html.dir/readme.sr.html
%{_texdir}/readme-html.dir/readme.vi.html
%{_texdir}/readme-html.dir/readme.zh-cn.html
%{_texdir}/release-texlive.txt
%{_texdir}/texmf-dist/scripts/texlive/tlmgr.pl
%{_texdir}/tlpkg/installer/config.guess
%{_texdir}/tlpkg/TeXLive/TLConfFile.pm
%{_texdir}/tlpkg/TeXLive/TLConfig.pm
%{_texdir}/tlpkg/TeXLive/TLCrypto.pm
%{_texdir}/tlpkg/TeXLive/TLDownload.pm
%{_texdir}/tlpkg/TeXLive/TLPDB.pm
%{_texdir}/tlpkg/TeXLive/TLPOBJ.pm
%{_texdir}/tlpkg/TeXLive/TLPSRC.pm
%{_texdir}/tlpkg/TeXLive/TLPaper.pm
%{_texdir}/tlpkg/TeXLive/TLTREE.pm
%{_texdir}/tlpkg/TeXLive/TLUtils.pm
%{_texdir}/tlpkg/TeXLive/TLWinGoo.pm
%{_texdir}/tlpkg/TeXLive/TeXCatalogue.pm
%{_texdir}/tlpkg/TeXLive/trans.pl
%{_datadir}/perl5/TeXLive
%{_mandir}/man1/tlmgr.1*
%doc %{_texdir}/texmf-dist/scripts/texlive/NEWS
%doc %{_texdir}/tlpkg/README

%files -n %{shortname}-texloganalyser
%{_bindir}/texloganalyser
%{_texdir}/texmf-dist/scripts/texloganalyser/
%doc %{_texdir}/texmf-dist/doc/support/texloganalyser/

%files -n %{shortname}-texosquery
%license lppl1.3.txt
%{_bindir}/texosquery*
%{_texdir}/texmf-dist/scripts/texosquery
%{_texdir}/texmf-dist/tex/latex/texosquery
%doc %{_texdir}/texmf-dist/doc/support/texosquery

%files -n %{shortname}-texplate
%license bsd.txt
%{_bindir}/texplate
%{_texdir}/texmf-dist/scripts/texplate
%doc %{_texdir}/texmf-dist/doc/support/texplate

%files -n %{shortname}-texsis
%license lppl1.txt
%{_bindir}/texsis
%{_mandir}/man1/texsis.1*
%{_texdir}/texmf-dist/bibtex/bst/texsis/
%{_texdir}/texmf-dist/tex/texsis/
%{fmtutil_cnf_d}/texsis
%doc %{_texdir}/texmf-dist/doc/otherformats/texsis/

%files -n %{shortname}-texware
%license knuth.txt
%{_bindir}/dvitype
%{_bindir}/pooltype
%{_mandir}/man1/dvitype.1*
%{_mandir}/man1/pooltype.1*

%files -n %{shortname}-thumbpdf
%license lppl1.txt
%{_bindir}/thumbpdf
%{_mandir}/man1/thumbpdf.1*
%{_texdir}/texmf-dist/scripts/thumbpdf/
%{_texdir}/texmf-dist/tex/generic/thumbpdf/
%doc %{_texdir}/texmf-dist/doc/generic/thumbpdf/

%files -n %{shortname}-tie
%{_bindir}/tie
%{_mandir}/man1/tie.1*

%files -n %{shortname}-tikztosvg
%license gpl3.txt
%{_bindir}/tikztosvg
%{_mandir}/man1/tikztosvg*
%doc %{_texdir}/texmf-dist/doc/support/tikztosvg
%{_texdir}/texmf-dist/scripts/tikztosvg

%files -n %{shortname}-tpic2pdftex
%license gpl.txt
%{_bindir}/tpic2pdftex
%{_mandir}/man1/tpic2pdftex.1*
%doc %{_texdir}/texmf-dist/doc/tpic2pdftex/

%files -n %{shortname}-ttfutils
%license lppl1.txt
%{_bindir}/ttf2afm
%{_bindir}/ttf2pk
%{_bindir}/ttf2tfm
%{_bindir}/ttfdump
%{_mandir}/man1/ttf2afm.1*
%{_mandir}/man1/ttf2pk.1*
%{_mandir}/man1/ttf2tfm.1*
%{_mandir}/man1/ttfdump.1*
%{_texdir}/texmf-dist/fonts/enc/ttf2pk/
%{_texdir}/texmf-dist/fonts/sfd/ttf2pk/
%{_texdir}/texmf-dist/ttf2pk/
%doc %{_texdir}/texmf-dist/doc/ttf2pk/

%files -n %{shortname}-typeoutfileinfo
%license lppl1.3.txt
%{_bindir}/typeoutfileinfo
%{_texdir}/texmf-dist/scripts/typeoutfileinfo/
%doc %{_texdir}/texmf-dist/doc/support/typeoutfileinfo/

%files -n %{shortname}-ulqda
%license lppl1.txt
%{_bindir}/ulqda
%{_texdir}/texmf-dist/scripts/ulqda/
%{_texdir}/texmf-dist/tex/latex/ulqda/
%doc %{_texdir}/texmf-dist/doc/latex/ulqda/

%files -n %{shortname}-uptex
%{_bindir}/euptex
%{_bindir}/r-upmpost
%{_bindir}/upbibtex
%{_bindir}/updvitomp
%{_bindir}/updvitype
%{_bindir}/uplatex
%{_bindir}/uplatex-dev
%{_bindir}/upmendex
%{_bindir}/upmpost
%{_bindir}/uppltotf
%{_bindir}/uptex
%{_bindir}/uptftopl
%{_bindir}/wovp2ovf
%{_mandir}/man1/euptex.1*
%{_mandir}/man1/uplatex.1*
%{_mandir}/man1/uplatex-dev.1*
%{_mandir}/man1/upmendex.1*
%{_mandir}/man1/uppltotf.1*
%{_mandir}/man1/uptex.1*
%{_mandir}/man1/uptftopl.1*
%{fmtutil_cnf_d}/uplatex
%{fmtutil_cnf_d}/uptex
%doc %{_texdir}/texmf-dist/doc/upmendex/
%doc %{_texdir}/texmf-dist/doc/uplatex/

%files -n %{shortname}-urlbst
%license gpl.txt
%{_bindir}/urlbst
%{_texdir}/texmf-dist/bibtex/bst/urlbst/
%{_texdir}/texmf-dist/scripts/urlbst/
%doc %{_texdir}/texmf-dist/doc/bibtex/urlbst/

%files -n %{shortname}-velthuis
%license gpl.txt
%{_bindir}/devnag
%{_mandir}/man1/devnag.1*
%{_texdir}/texmf-dist/fonts/afm/public/velthuis/
%{_texdir}/texmf-dist/fonts/map/dvips/velthuis/
%{_texdir}/texmf-dist/fonts/source/public/velthuis/
%{_texdir}/texmf-dist/fonts/tfm/public/velthuis/
%{_texdir}/texmf-dist/fonts/type1/public/velthuis/
%{_texdir}/texmf-dist/tex/generic/velthuis/
%{_texdir}/texmf-dist/tex/latex/velthuis/
%{_texdir}/texmf-dist/tex/plain/velthuis/
%{_texdir}/texmf-dist/tex/xelatex/velthuis/
%doc %{_texdir}/texmf-dist/doc/generic/velthuis/

%files -n %{shortname}-vlna
%license lppl1.txt
%{_bindir}/vlna
%{_mandir}/man1/vlna.1*
%doc %{_texdir}/texmf-dist/doc/vlna/

%files -n %{shortname}-vpe
%license lppl1.txt
%{_bindir}/vpe
%{_texdir}/texmf-dist/scripts/vpe/
%{_texdir}/texmf-dist/tex/latex/vpe/
%doc %{_texdir}/texmf-dist/doc/latex/vpe/

%files -n %{shortname}-web
%license knuth.txt
%{_bindir}/tangle
%{_bindir}/weave
%{_mandir}/man1/tangle.1*
%{_mandir}/man1/weave.1*

%files -n %{shortname}-webquiz
%license gpl.txt
%{_bindir}/webquiz
%{_mandir}/man1/webquiz.1*
%{_texdir}/texmf-dist/scripts/webquiz/
%{_texdir}/texmf-dist/tex/latex/webquiz/
%doc %{_texdir}/texmf-dist/doc/latex/webquiz/

%files -n %{shortname}-wordcount
%license lppl1.txt
%{_bindir}/wordcount
%{_texdir}/texmf-dist/scripts/wordcount/
%{_texdir}/texmf-dist/tex/latex/wordcount/
%doc %{_texdir}/texmf-dist/doc/latex/wordcount/

%files -n %{shortname}-xdvi
%{_bindir}/xdvi
%{_bindir}/xdvi-xaw
%{_mandir}/man1/xdvi.1*
%{_texdir}/texmf-dist/dvips/xdvi/
%{_texdir}/texmf-dist/xdvi/

%files -n %{shortname}-xetex
%license other-free.txt
%{_bindir}/xdvipdfmx
%{_bindir}/xelatex
%{_bindir}/xelatex-dev
%{_bindir}/xetex
%{_mandir}/man1/xelatex.1*
%{_mandir}/man1/xelatex-dev.1*
%{_mandir}/man1/xetex.1*
%{_texdir}/tlpkg/tlpostcode/xetex.pl
%{_texdir}/texmf-dist/fonts/misc/xetex/
%{fmtutil_cnf_d}/xelatex-dev
%{fmtutil_cnf_d}/xetex
%doc %{_texdir}/texmf-dist/doc/xetex/

%files -n %{shortname}-xindex
%license lppl1.3.txt
%{_bindir}/xindex
%{_texdir}/texmf-dist/scripts/xindex/
%{_texdir}/texmf-dist/tex/latex/xindex/
%{_texdir}/texmf-dist/tex/lualatex/xindex/
%doc %{_texdir}/texmf-dist/doc/lualatex/xindex/

%if ! 0%{?eln}
%files -n %{shortname}-xindy
%license gpl.txt
%if %{without bootstrap}
%{_bindir}/tex2xindy
%{_bindir}/texindy
%{_bindir}/xindy
%{_bindir}/xindy.mem
%endif
%{_mandir}/man1/xindy.1*
%{_mandir}/man1/texindy.1*
%{_mandir}/man1/tex2xindy.1*
%{_texdir}/texmf-dist/scripts/xindy/
%{_texdir}/texmf-dist/xindy/
%doc %{_texdir}/texmf-dist/doc/xindy/
%endif

%files -n %{shortname}-xml2pmx
%license gpl3.txt
%{_bindir}/xml2pmx
%{_mandir}/man1/xml2pmx*

%files -n %{shortname}-xmltex
%license lppl1.txt
%{_bindir}/pdfxmltex
%{_bindir}/xmltex
%{_texdir}/texmf-dist/tex/xmltex/
%{fmtutil_cnf_d}/xmltex
%doc %{_texdir}/texmf-dist/doc/otherformats/xmltex/

%files -n %{shortname}-xpdfopen
%{_bindir}/pdfclose
%{_bindir}/pdfopen
%{_mandir}/man1/pdfclose.1*
%{_mandir}/man1/pdfopen.1*

%files -n %{shortname}-yplan
%license lppl1.txt
%{_bindir}/yplan
%{_texdir}/texmf-dist/scripts/yplan/
%{_texdir}/texmf-dist/tex/latex/yplan/
%doc %{_texdir}/texmf-dist/doc/latex/yplan/

%changelog
* Thu May 27 2021 Tom Callaway <spot@fedoraproject.org> - 9:20210325-32
- 20210325

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 7:20200327-31
- Rebuild for ICU 69

* Thu Apr  1 2021 Tom Callaway <spot@fedoraproject.org> - 7:20200327-30
- update source urls (except tug urls) to https

* Thu Mar 18 2021 Tom Callaway <spot@fedoraproject.org> - 7:20200327-29
- force builtin copy of pygmentex to 0.10 (supports python3)

* Tue Feb 2  2021 Tom Callaway <spot@fedoraproject.org> - 7:20200327-28
- set TEXMFLOCAL during the context scriptlet to minimize the scope of where it looks during mtxrun --generate

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9:20200327-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 26 2021 Tomas Popela <tpopela@redhat.com> - 9:20200327-26
- Don't build texlive-xindy on ELN because of its requirements (clisp)

* Fri Jan 15 2021 Tom Callaway <spot@fedoraproject.org> - 9:20200327-25
- debootstrap

* Fri Jan 15 2021 Tom Callaway <spot@fedoraproject.org> - 9:20200327-24
- fix context shell binary to handle /home dirs that are symlinks (bz1913245)

* Wed Dec 30 2020 Tom Callaway <spot@fedoraproject.org> - 9:20200327-23
- update pygmentex (supports python3)
- update dviasm (supports python3)

* Mon Nov 16 2020 Tom Callaway <spot@fedoraproject.org> - 9:20200327-22
- make proper texlive-optex subpackage by moving it here
- bump epoch to 9 so this texlive-optex package replaces the one that used to live in texlive

* Thu Nov 12 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-21
- obsolete texlive-texconfig, texlive-pdftools, texlive-pstools (in texlive-texlive-scripts-extra)

* Tue Nov 10 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-20
- fix issues with file ownership duplication
- fix issue with obsoleting texlive-tetex
- turn LTO back off, as it was assuming code needed libcrypto for some unknown reason

* Thu Oct 29 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-19
- fix dependencies of texlive-ptex and texlive-uptex

* Sun Oct 11 2020 Jeff Law <law@redhat.com> - 7:20200327-18
- Re-enable LTO

* Wed Sep 23 2020 Than Ngo <than@redhat.com> - 7:20200327-17
- Fix pdflatex run out of memory

* Mon Sep 21 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-16
- move "mtxrun --generate" call from -kpathsea transfiletriggerin to -context
- drop Requires(post): texlive-context from -kpathsea
- add an explicit versioning on the dependency of texlive-texlive-scripts in -kpathsea (and vice versa)

* Thu Aug 13 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-15
- make texlive-latex have an explicit Requires on texlive-cm-super (bz1867927)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7:20200327-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Tom Stellard <tstellar@redhat.com> - 7:20200327-13
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jul 21 2020 Marek Kasik <mkasik@redhat.com> - 7:20200327-12
- rebuild for poppler 0.90.0
- bodhi needs latest build

* Tue Jul 14 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-11
- disable bootstrap

* Tue Jul 14 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-10.1
- unbootstrapped build (TEMPORARY, when -11 comes out of the side tag, it will replace this)

* Tue Jul 14 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-10
- bootstrap again again

* Tue Jul 14 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-9
- bootstrap again

* Tue Jul 14 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-8
- rebuild for poppler 0.90.0
- bootstrap on

* Wed Jul 01 2020 Jeff Law <law@redhat.com> - 7:20200327-7
- Disable LTO

* Wed May 27 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-6
- split off context-doc (bz1839593)
- add Requires: tex(psfonts.map) to gsftopk (bz1840379)
- update component sources to match main tree tarball (not doing this before was an epic fail on my part)

* Wed May 20 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-5
- rebuild with bootstrap off and triggers with debugging off

* Sun May 17 2020 Orion Poplawski <orion@nwra.com> - 7:20200327-4
- Add bootstrap flag to disable circular dep on latex due to xindy
- Fix --disable-xindy-rules configure parameter

* Sat May 16 2020 Orion Poplawski <orion@nwra.com> - 7:20200327-3
- Make texlive-kpathsea require texlive-texlive-scripts (bz#1836464)
- Update fedora/rhel conditionals
- Add (temporary) BR on texlive-texlive-scripts to fix latex dummy.tex

* Wed May 13 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-2
- fix symlink issues

* Mon Apr 20 2020 Tom Callaway <spot@fedoraproject.org> - 7:20200327-1
- update to 20200327

* Wed Feb 05 2020 Than Ngo <than@redhat.com> - 7:20190410-12
- fix bz#1798119 - buffer overflow in TexOpen() function, CVE-2019-19601

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7:20190410-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Tom Callaway <spot@fedoraproject.org> - 7:20190410-10
- fix gcc10 issues

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 7:20190410-9
- Bring back xindy and the circular dependency on texlive-latex

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 7:20190410-8
- Rebuild for poppler-0.84.0
- Don't include C++ headers in C sources
- Temporarily break circular dependency on texlive-latex (will be reverted)

* Fri Jan 10 2020 Tom Callaway <spot@fedoraproject.org> - 7:20190410-7
- fix python3 issue with pdfbook2 (thanks to "Mildred", bz1733794)
- fix python3 issue with latex-papersize (thanks to Silas S. Brown, bz1783964)

* Fri Nov 15 2019 Tom Callaway <spot@fedoraproject.org> - 7:20190410-6
- package up the TL fork of psutils to help tlmgr find all the configs it expects

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 7:20190410-5
- Rebuild for ICU 65

* Fri Oct 18 2019 Tom Callaway <spot@fedoraproject.org> - 7:20190410-4
- fix dir ownership

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 7:20190410-3
- Rebuild for mpfr 4

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7:20190410-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Tom Callaway <spot@fedoraproject.org> - 7:20190410-1
- update to 20190410
- update all component tarballs to latest available
- new subpackages: cluttex, ctanbib, dviout-util, pdftex-quiet, webquiz, xindex
- add a slightly neutered tlmgr back into texlive.infra because texconfig paper needs it
  IF YOU ARE READING THIS PLEASE DO NOT USE tlmgr install/update. IF YOU IGNORE ME
  PLEASE DO NOT FILE BUGS. PLEASE DO NOT REQUEST THE tlmgrgui BITS.

* Wed May 15 2019 Jerry James <loganjerry@gmail.com> - 7:20180414-36
- Fix xindy build by eliminating race to create latex.fmt
- Build xindy on all supported arches

* Tue Mar 19 2019 Tom Callaway <spot@fedoraproject.org> - 7:20180414-35
- do not throw no file error in synctex

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7:20180414-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Marek Kasik <mkasik@redhat.com> - 7:20180414-33
- Rebuild for poppler-0.73.0

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 7:20180414-32
- Rebuild for ICU 63

* Wed Jan 16 2019 Than Ngo <than@redhat.com> - 7:20180414-31
- fixed annocheck distro flag failure detected by rpmdiff

* Wed Dec 12 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-30
- add explicit Requires: texlive-xetex to texlive-dvipdfmx (bz1657755)

* Fri Dec  7 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-29
- use python3 properly in pdfbook2

* Mon Nov 26 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-28
- do not try to ls /usr/share/texlive/fmtutil.cnf.d, it can be empty, 
  and that makes for noisy errors in scripts (bz1650935)
  Thanks to Villy Kruse.
- fix pkgconfig cleanup sed to use %%{source_date} instead of %%{version}
  which is overridden with subpackage specific data at that point. (bz1426622)

* Mon Nov 12 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-27
- make texlive-kpathsea Requires: texlive-tetex so scriptlets don't fail noisily

* Thu Nov  8 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-26
- make a symlink so texdoc can find texlive.tlpdb

* Thu Nov  1 2018 Adam Williamson <awilliam@redhat.com> - 7:20180414-25
- Add missing dep from -tetex to -texconfig (bz1555931)

* Thu Oct  4 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-24
- disable test that fails on 32 bit arches in rawhide

* Mon Oct  1 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-23
- apply upstream fix for CVE-2018-17407

* Wed Sep 19 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-22
- fix lyluatex provides

* Tue Sep 18 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-21
- add lyluatex

* Fri Aug 24 2018 Marek Kasik <mkasik@redhat.com> - 7:20180414-20
- Install synctex_version.h to be able to build evince

* Tue Aug 14 2018 Marek Kasik <mkasik@redhat.com> - 7:20180414-19
- Rebuild for poppler-0.67.0
- Disable xindy temporarily (there is a cyclic dependency which
- prevents me from building texlive-base with new poppler)

* Mon Aug  6 2018 Marek Kasik <mkasik@redhat.com> - 7:20180414-18
- Fix paths in pkgconfig files
- Resolves: #1426622

* Wed Jul 11 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-17
- update latex2man to resolve perl issues
- use different ctan mirror, old one was out of date
- update pretty much everything since we're updating latex2man and we know the old mirror was outdated
- l3build and axodraw2 are now packaged properly in the tarball
- texdoctk is now its own package (reflecting upstream split)

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 7:20180414-16
- Rebuild for ICU 62

* Sat Jul  7 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-15
- revert trigger changes from -14

* Mon Jul  2 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-14
- fix triggers to force enable of new maps and run syncwithtrees before doing map operations
- add old "tex-foo-doc" provides for every package with doc provides (bz1593860, 1593863)

* Tue Jun 26 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-13
- apply tibbs's fix (PR#4) for fmtutil cnf handling without tons of ugly scriptlets
- explicitly run updmap-sys in the kpathsea triggers, bug reports imply this is needed

* Tue Jun 19 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-12
- add Requires: tex(fvextra.sty) to pythontex (bz1590621)

* Mon Jun 11 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-11
- add tex-jfontmaps(bin/doc) provides

* Fri Jun  8 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-10
- add tex-uplatex(bin/doc) provides

* Thu Jun  7 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-9
- add pretrans to handle /usr/share/texmf

* Mon Jun  4 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-8
- add Provides: tetex-dvips
- add symlink to /usr/share/texmf for legacy packages

* Fri Jun  1 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-7
- add Provides: xmltex

* Tue May 29 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-6
- add BR: texlive-metafont, texlive-cm-super, texlive-ec for xindy
- disable xindy for arm

* Tue May 29 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-5
- fix xindy and jfontmaps obsoletes
- fix typo preventing xindy subpackage

* Tue May 29 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-4
- add Provides: jadetex and Provides: tex-uptex-doc

* Mon May 21 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-3
- add posttrans to force latex scriptlets to work right

* Mon May 14 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-2
- fix arara-doc obsoletes (bz1576693)

* Tue May  1 2018 Tom Callaway <spot@fedoraproject.org> - 7:20180414-1
- update to 20180414
- fix synctex.pc (bz1426622)
- new subpackages: axodraw2, bib2gls, ctan-o-mat, dviinfox, jfmutil, l3build, wordcount

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 7:20170520-28
- Rebuild for ICU 61.1

* Fri Mar 30 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-27
- actually use the texmf.cnf we patch (not the vanilla one from the kpathsea.tar.xz)

* Tue Mar 27 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-26
- add lcdf-typetools provide to fix broken collection-fontutils (fixing that in texlive later) (bz1560379)
- add LatexIndent* to filtered Requires to prevent dep issues there (bz1560381)

* Sun Mar 25 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-25
- fix aleph obsoletes (bz1560355)

* Fri Mar 23 2018 Kevin Fenzi <kevin@scrye.com> - 7:20170520-24
- Rebuild for poppler soname bump.

* Thu Mar 15 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-23
- add Requires: tex(pdfpages.sty) to texlive-pdfjam (bz1164237)

* Sun Mar 11 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-22
- fix a2ping to work with gs 9.22

* Sat Mar 10 2018 Kevin Fenzi <kevin@scrye.com> - 7:20170520-21
- Make kpathsea scriptlets not fail in the installer env.

* Fri Mar  9 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-20
- disable cjk-gs-integrate 

* Fri Mar  9 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-19
- configure TEXMFLOCAL to point to /usr/share/texlive/texmf-local/ (bz1553462)

* Wed Mar  7 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-18
- switch to shebang mangling that does not change exec perms
  most/all of the mangling is correct, but we do not want to risk breaking
  ancient texlive scripts that are suddently -x
- add versions for arara bundled provides
- use spaces instead of tabs

* Mon Mar  5 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-17
- add Provides: tetex-latex to the latex subpackage
- fix obviously incorrect license tag on -base package
- use %%_rpmmacrodir instead of our local %%macrosdir
- add BuildRequires: gcc gcc-c++

* Mon Feb 26 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-16
- include uplatex docs in uptex
- conditionalize xindy because clisp doesn't have ppc64/aarch64 packages

* Sat Feb 24 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-15
- turn on xindy
- disable shebang mangling
- disable tests that fail on 32bit arches with gcc8

* Fri Feb 23 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-14
- pass LDFLAGS
- update lcdf-typetools to git current to fix test failures
- turn on xindy

* Thu Feb 22 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-13
- rebuild again for new poppler in rawhide/f28

* Sun Feb  4 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-12
- fix pathing so that texinfo files are found

* Thu Jan 18 2018 Tom Callaway <spot@fedoraproject.org> - 7:20170520-11
- add missing deps for texlive-pdfbook2
- fix ghostscript BR

* Wed Nov 29 2017 Tom Callaway <spot@fedoraproject.org> - 7:20170520-10
- kpathsea trigger uses mtxrun, which is in the context subpackage ...
  ... but the kpathsea subpackage did not have a Requires on it.
  It does now. How long was this broken?!?
- force texdir/texmf-var to be a symlink to /var/lib/texmf

* Tue Nov 14 2017 Tom Callaway <spot@fedoraproject.org> - 7:20170520-9
- var handling & perl cleanups & extra scriptlets

* Fri Nov 10 2017 Tom Callaway <spot@fedoraproject.org> - 7:20170520-8
- add additional provides for texlive-dvipng, texlive-dvipdfmx, and texlive-xdvi

* Fri Nov 10 2017 Tom Callaway <spot@fedoraproject.org> - 7:20170520-7
- add epoch to Obsolete versioning

* Thu Nov  9 2017 Tom Callaway <spot@fedoraproject.org> - 7:20170520-6
- try removing a version from the kpathsea-bin/kpathsea-doc Obsoletes
  to see if that will work with DNF. I miss yum.

* Thu Nov  9 2017 Tom Callaway <spot@fedoraproject.org> - 7:20170520-5
- lie about what texlive-kpathsea-lib(__isa) version we provide
  because rpm needs this to get over the dependency hurdle

* Thu Nov  9 2017 Tom Callaway <spot@fedoraproject.org> - 7:20170520-4
- add explicit provide for texlive-kpathsea-lib(__isa) to facilitate update

* Thu Nov  9 2017 Tom Callaway <spot@fedoraproject.org> - 7:20170520-3
- use more accurate provides

* Sun Oct 29 2017 Tom Callaway <spot@fedoraproject.org> - 7:20170520-2
- use new files from upstream that work with current poppler in rawhide

* Tue Sep 12 2017 Tom Callaway <spot@fedoraproject.org> - 7:20170520-1
- new package
