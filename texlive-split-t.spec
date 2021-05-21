%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-t
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source2033:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quattrocento.tar.xz
Source2034:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quattrocento.doc.tar.xz
Source2035:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/raleway.tar.xz
Source2036:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/raleway.doc.tar.xz
Source2037:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/recycle.tar.xz
Source2038:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/recycle.doc.tar.xz
Source2241:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/reverxii.doc.tar.xz
Source2451:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qobitree.tar.xz
Source2452:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qobitree.doc.tar.xz
Source2453:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qtree.tar.xz
Source2454:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qtree.doc.tar.xz
Source2455:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/reledmac.tar.xz
Source2456:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/reledmac.doc.tar.xz
Source2967:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qpxqtx.tar.xz
Source2968:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qpxqtx.doc.tar.xz
Source3079:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rcs.tar.xz
Source3080:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rcs.doc.tar.xz
Source3260:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qcircuit.tar.xz
Source3261:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qcircuit.doc.tar.xz
Source3262:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qrcode.tar.xz
Source3263:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qrcode.doc.tar.xz
Source3265:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/randbild.tar.xz
Source3266:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/randbild.doc.tar.xz
Source3268:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/randomwalk.tar.xz
Source3269:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/randomwalk.doc.tar.xz
Source3271:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/reotex.tar.xz
Source3272:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/reotex.doc.tar.xz
Source5025:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qcm.tar.xz
Source5026:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qcm.doc.tar.xz
Source5028:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qstest.tar.xz
Source5029:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qstest.doc.tar.xz
Source5031:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qsymbols.tar.xz
Source5032:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/qsymbols.doc.tar.xz
Source5034:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quotchap.tar.xz
Source5035:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quotchap.doc.tar.xz
Source5037:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quoting.tar.xz
Source5038:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quoting.doc.tar.xz
Source5040:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quotmark.tar.xz
Source5041:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quotmark.doc.tar.xz
Source5043:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ran_toks.tar.xz
Source5044:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ran_toks.doc.tar.xz
Source5046:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/randtext.tar.xz
Source5047:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/randtext.doc.tar.xz
Source5048:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rccol.tar.xz
Source5049:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rccol.doc.tar.xz
Source5051:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rcs-multi.tar.xz
Source5052:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rcs-multi.doc.tar.xz
Source5054:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rcsinfo.tar.xz
Source5055:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rcsinfo.doc.tar.xz
Source5057:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/readarray.tar.xz
Source5058:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/readarray.doc.tar.xz
Source5059:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/realboxes.tar.xz
Source5060:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/realboxes.doc.tar.xz
Source5062:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/recipe.tar.xz
Source5063:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/recipe.doc.tar.xz
Source5064:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/recipebook.tar.xz
Source5065:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/recipebook.doc.tar.xz
Source5066:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/recipecard.tar.xz
Source5067:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/recipecard.doc.tar.xz
Source5069:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rectopma.tar.xz
Source5070:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rectopma.doc.tar.xz
Source5071:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/refcheck.tar.xz
Source5072:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/refcheck.doc.tar.xz
Source5073:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/refenums.tar.xz
Source5074:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/refenums.doc.tar.xz
Source5075:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/reflectgraphics.tar.xz
Source5076:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/reflectgraphics.doc.tar.xz
Source5078:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/refman.tar.xz
Source5079:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/refman.doc.tar.xz
Source5081:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/refstyle.tar.xz
Source5082:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/refstyle.doc.tar.xz
Source5084:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/regcount.tar.xz
Source5085:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/regcount.doc.tar.xz
Source5087:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/regexpatch.tar.xz
Source5088:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/regexpatch.doc.tar.xz
Source5090:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/register.tar.xz
Source5091:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/register.doc.tar.xz
Source5093:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/regstats.tar.xz
Source5094:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/regstats.doc.tar.xz
Source5096:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/relenc.tar.xz
Source5097:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/relenc.doc.tar.xz
Source5099:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/relsize.tar.xz
Source5100:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/relsize.doc.tar.xz
Source5101:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/repeatindex.tar.xz
Source5102:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/repeatindex.doc.tar.xz
Source5103:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/repltext.tar.xz
Source5104:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/repltext.doc.tar.xz
Source5106:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rjlparshap.tar.xz
Source5107:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rjlparshap.doc.tar.xz
Source5109:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rlepsf.tar.xz
Source5110:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rlepsf.doc.tar.xz
Source5111:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rmpage.tar.xz
Source5112:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rmpage.doc.tar.xz
Source5891:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rec-thy.tar.xz
Source5892:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rec-thy.doc.tar.xz
Source5893:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ribbonproofs.tar.xz
Source5894:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ribbonproofs.doc.tar.xz
Source5895:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rmathbr.tar.xz
Source5896:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rmathbr.doc.tar.xz
Source6003:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/repere.tar.xz
Source6004:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/repere.doc.tar.xz
Source6110:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/resumemac.tar.xz
Source6111:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/resumemac.doc.tar.xz
Source6493:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/resphilosophica.tar.xz
Source6494:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/resphilosophica.doc.tar.xz
Source6496:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/resumecls.tar.xz
Source6497:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/resumecls.doc.tar.xz
Source6499:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/revtex.tar.xz
Source6500:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/revtex.doc.tar.xz
Source6502:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/revtex4.tar.xz
Source6503:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/revtex4.doc.tar.xz
Source6770:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quran.tar.xz
Source6771:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quran.doc.tar.xz
Source6772:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/realscripts.tar.xz
Source6773:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/realscripts.doc.tar.xz
Source7935:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quicktype.tar.xz
Source7936:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/quicktype.doc.tar.xz
Source8044:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/randomlist.doc.tar.xz
Source8045:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/randomlist.tar.xz
Source8298:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/revquantum.tar.xz
Source8299:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/revquantum.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-quattrocento
Provides:       tex-quattrocento = %{tl_version}
License:        LPPL
Summary:        LaTeX support for Quattrocento and Quattrocento Sans fonts
Version:        svn31763.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(textcomp.sty), tex(xkeyval.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty)
Provides:       tex(qtrcnt_464xel.enc) = %{tl_version}, tex(qtrcnt_4btof3.enc) = %{tl_version}
Provides:       tex(qtrcnt_6abmaa.enc) = %{tl_version}, tex(qtrcnt_arxkdo.enc) = %{tl_version}
Provides:       tex(qtrcnt_aykkbr.enc) = %{tl_version}, tex(qtrcnt_cpzb4n.enc) = %{tl_version}
Provides:       tex(qtrcnt_dhs3d3.enc) = %{tl_version}, tex(qtrcnt_dn5k7b.enc) = %{tl_version}
Provides:       tex(qtrcnt_dw2g3h.enc) = %{tl_version}, tex(qtrcnt_e45lg2.enc) = %{tl_version}
Provides:       tex(qtrcnt_h2bn35.enc) = %{tl_version}, tex(qtrcnt_iyhp72.enc) = %{tl_version}
Provides:       tex(qtrcnt_mamppr.enc) = %{tl_version}, tex(qtrcnt_n36lnh.enc) = %{tl_version}
Provides:       tex(qtrcnt_nfidqf.enc) = %{tl_version}, tex(qtrcnt_ptp2lu.enc) = %{tl_version}
Provides:       tex(qtrcnt_qceur4.enc) = %{tl_version}, tex(qtrcnt_tevtmb.enc) = %{tl_version}
Provides:       tex(qtrcnt_tixcdz.enc) = %{tl_version}, tex(qtrcnt_vzn2dc.enc) = %{tl_version}
Provides:       tex(qtrcnt_wpi2yi.enc) = %{tl_version}, tex(qtrcnt_xt7yz2.enc) = %{tl_version}
Provides:       tex(qtrcnt_xvywtm.enc) = %{tl_version}, tex(qtrcnt_zdiabs.enc) = %{tl_version}
Provides:       tex(qtrcnt_zievlx.enc) = %{tl_version}, tex(qtrcnt_zq54sp.enc) = %{tl_version}
Provides:       tex(quattrocento.map) = %{tl_version}, tex(Quattrocento-Bold.otf) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic.otf) = %{tl_version}
Provides:       tex(Quattrocento-Italic.otf) = %{tl_version}
Provides:       tex(Quattrocento.otf) = %{tl_version}, tex(QuattrocentoSans-Bold.otf) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic.otf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic.otf) = %{tl_version}
Provides:       tex(QuattrocentoSans.otf) = %{tl_version}
Provides:       tex(Quattrocento-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-sup-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoRegular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-ot1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ot1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-ot1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-ot1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-t1.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Quattrocento-Bold.pfb) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic.pfb) = %{tl_version}
Provides:       tex(QuattrocentoItalic.pfb) = %{tl_version}
Provides:       tex(QuattrocentoRegular.pfb) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold.pfb) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic.pfb) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic.pfb) = %{tl_version}
Provides:       tex(QuattrocentoSans-ItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(QuattrocentoSans.pfb) = %{tl_version}
Provides:       tex(QuattrocentoSansLCDFJ.pfb) = %{tl_version}
Provides:       tex(Quattrocento-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(Quattrocento-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(Quattrocento-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Quattrocento-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Quattrocento-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Quattrocento-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(QuattrocentoItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(QuattrocentoRegular-sup-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoRegular-sup-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoRegular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoRegular-tlf-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoRegular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-ot1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-ot1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-ot1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-ot1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-sup-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-ly1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-ot1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-t1.vf) = %{tl_version}
Provides:       tex(QuattrocentoSans-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Quattrocento-TLF.fd) = %{tl_version}
Provides:       tex(LY1QuattrocentoSans-TLF.fd) = %{tl_version}
Provides:       tex(OT1Quattrocento-TLF.fd) = %{tl_version}
Provides:       tex(OT1QuattrocentoSans-TLF.fd) = %{tl_version}
Provides:       tex(T1Quattrocento-TLF.fd) = %{tl_version}
Provides:       tex(T1QuattrocentoSans-TLF.fd) = %{tl_version}
Provides:       tex(TS1Quattrocento-TLF.fd) = %{tl_version}
Provides:       tex(TS1QuattrocentoSans-TLF.fd) = %{tl_version}
Provides:       tex(quattrocento.sty) = %{tl_version}

%description -n texlive-quattrocento
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Quattrocento and Quattrocento Sans families of
fonts, designed by Pablo Impallari; the fonts themselves are
also provided, in both Type 1 and OpenType format. Quattrocento
is a classic typeface with wide and open letterforms, and great
x-height, which makes it very legible for body text at small
sizes. Tiny details that only show up at bigger sizes make it
also great for display use. Quattrocento Sans is the perfect
sans-serif companion for Quattrocento.

%package -n texlive-quattrocento-doc
Summary:        Documentation for quattrocento
Version:        svn31763.0

Provides:       tex-quattrocento-doc
AutoReqProv:    No

%description -n texlive-quattrocento-doc
Documentation for quattrocento

%package -n texlive-raleway
Provides:       tex-raleway = %{tl_version}
License:        OFL
Summary:        Use Raleway with TeX(-alike) systems
Version:        svn42629
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(fontenc.sty)
Requires:       tex(textcomp.sty), tex(mweights.sty), tex(fontaxes.sty), tex(xkeyval.sty)
Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(fontspec.sty)
Provides:       tex(a_2bcjq6.enc) = %{tl_version}, tex(a_biciir.enc) = %{tl_version}
Provides:       tex(a_bzmckq.enc) = %{tl_version}, tex(a_f3uqdf.enc) = %{tl_version}
Provides:       tex(a_gvxmk7.enc) = %{tl_version}, tex(a_ioname.enc) = %{tl_version}
Provides:       tex(a_k2dfwc.enc) = %{tl_version}, tex(a_mgzrni.enc) = %{tl_version}
Provides:       tex(a_mzuigi.enc) = %{tl_version}, tex(a_oaf34p.enc) = %{tl_version}
Provides:       tex(a_pcwse4.enc) = %{tl_version}, tex(a_sor5xn.enc) = %{tl_version}
Provides:       tex(a_u6n666.enc) = %{tl_version}, tex(a_yqxcf3.enc) = %{tl_version}
Provides:       tex(Raleway.map) = %{tl_version}, tex(Raleway-Black-Italic.otf) = %{tl_version}
Provides:       tex(Raleway-Black.otf) = %{tl_version}, tex(Raleway-Bold-Italic.otf) = %{tl_version}
Provides:       tex(Raleway-Bold.otf) = %{tl_version}, tex(Raleway-ExtraBold-Italic.otf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold.otf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-Italic.otf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight.otf) = %{tl_version}
Provides:       tex(Raleway-Light-Italic.otf) = %{tl_version}
Provides:       tex(Raleway-Light.otf) = %{tl_version}, tex(Raleway-Medium-Italic.otf) = %{tl_version}
Provides:       tex(Raleway-Medium.otf) = %{tl_version}, tex(Raleway-Regular-Italic.otf) = %{tl_version}
Provides:       tex(Raleway-Regular.otf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-Italic.otf) = %{tl_version}
Provides:       tex(Raleway-SemiBold.otf) = %{tl_version}
Provides:       tex(Raleway-Thin-Italic.otf) = %{tl_version}
Provides:       tex(Raleway-Thin.otf) = %{tl_version}, tex(Raleway-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Raleway-Black.pfb) = %{tl_version}, tex(Raleway-BlackItalic.pfb) = %{tl_version}
Provides:       tex(Raleway-Bold.pfb) = %{tl_version}, tex(Raleway-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Raleway-ExtraBold.pfb) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic.pfb) = %{tl_version}
Provides:       tex(Raleway-ExtraLight.pfb) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic.pfb) = %{tl_version}
Provides:       tex(Raleway-Italic.pfb) = %{tl_version}, tex(Raleway-Light.pfb) = %{tl_version}
Provides:       tex(Raleway-LightItalic.pfb) = %{tl_version}
Provides:       tex(Raleway-Medium.pfb) = %{tl_version}, tex(Raleway-MediumItalic.pfb) = %{tl_version}
Provides:       tex(Raleway-Regular.pfb) = %{tl_version}
Provides:       tex(Raleway-SemiBold.pfb) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic.pfb) = %{tl_version}
Provides:       tex(Raleway-Thin.pfb) = %{tl_version}, tex(Raleway-ThinItalic.pfb) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Black-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-BlackItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraBoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLight-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ExtraLightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-LightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Medium-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-MediumItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-SemiBoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-Thin-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Raleway-ThinItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Raleway-TLF.fd) = %{tl_version}, tex(LY1Raleway-TOsF.fd) = %{tl_version}
Provides:       tex(OT1Raleway-TLF.fd) = %{tl_version}, tex(OT1Raleway-TOsF.fd) = %{tl_version}
Provides:       tex(T1Raleway-TLF.fd) = %{tl_version}, tex(T1Raleway-TOsF.fd) = %{tl_version}
Provides:       tex(TS1Raleway-TLF.fd) = %{tl_version}, tex(TS1Raleway-TOsF.fd) = %{tl_version}
Provides:       tex(raleway-type1-autoinst.sty) = %{tl_version}
Provides:       tex(Raleway.sty) = %{tl_version}, tex(raleway.sty) = %{tl_version}

%description -n texlive-raleway
The package provides the Raleway family in an easy to use way.
For XeLaTeX and LuaLaTeX users the original OpenType fonts are
used. The entire font family is included.

%package -n texlive-raleway-doc
Summary:        Documentation for raleway
Version:        svn42629
Provides:       tex-raleway-doc
AutoReqProv:    No

%description -n texlive-raleway-doc
Documentation for raleway

%package -n texlive-recycle
Provides:       tex-recycle = %{tl_version}
License:        GPL+
Summary:        A font providing the "recyclable" logo
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(recycle.map) = %{tl_version}, tex(recycle.tfm) = %{tl_version}
Provides:       tex(recycle.pfb) = %{tl_version}, tex(recycle.sty) = %{tl_version}

%description -n texlive-recycle
This single-character font is provided as Metafont source, and
in Adobe Type 1 format. It is accompanied by a trivial LaTeX
package to use the logo at various sizes.

%package -n texlive-recycle-doc
Summary:        Documentation for recycle
Version:        svn15878.0

Provides:       tex-recycle-doc
AutoReqProv:    No

%description -n texlive-recycle-doc
Documentation for recycle

%package -n texlive-reverxii-doc
Summary:        Documentation for reverxii
Version:        svn24976.0

Provides:       tex-reverxii-doc
AutoReqProv:    No

%description -n texlive-reverxii-doc
Documentation for reverxii

%package -n texlive-qobitree
Provides:       tex-qobitree = %{tl_version}
License:        LPPL
Summary:        LaTeX macros for typesetting trees
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(qobitree.tex) = %{tl_version}

%description -n texlive-qobitree
Provides commands \branch and \leaf for specifying the elements
of the tree; you build up your tree with those commands, and
then issue the \tree command to typeset the whole.

%package -n texlive-qobitree-doc
Summary:        Documentation for qobitree
Version:        svn15878.0

Provides:       tex-qobitree-doc
AutoReqProv:    No

%description -n texlive-qobitree-doc
Documentation for qobitree

%package -n texlive-qtree
Provides:       tex-qtree = %{tl_version}
License:        LPPL
Summary:        Draw tree structures
Version:        svn15878.3.1b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pict2e.sty)
Provides:       tex(qtree.sty) = %{tl_version}

%description -n texlive-qtree
The package offers support for drawing tree diagrams, and is
especially suitable for linguistics use. It allows trees to be
specified in a simple bracket notation, automatically
calculates branch sizes, and supports both DVI/PostScript and
PDF output by use of pict2e facilities. The package is a
development of the existing qobitree package, offering a new
front end.

%package -n texlive-qtree-doc
Summary:        Documentation for qtree
Version:        svn15878.3.1b

Provides:       tex-qtree-doc
AutoReqProv:    No

%description -n texlive-qtree-doc
Documentation for qtree

%package -n texlive-reledmac
Provides:       tex-reledmac = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset scholarly editions
Version:        svn48229
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(xargs.sty), tex(etoolbox.sty), tex(etex.sty)
Requires:       tex(suffix.sty), tex(xstring.sty), tex(ifluatex.sty), tex(ragged2e.sty)
Requires:       tex(ifxetex.sty), tex(xspace.sty)
Provides:       tex(reledmac.sty) = %{tl_version}, tex(reledpar.sty) = %{tl_version}

%description -n texlive-reledmac
A package for typesetting scholarly critical editions,
replacing the established ledmac and eledmac packages. Ledmac
itself was a LaTeX port of the plain TeX EDMAC macros. The
package supports indexing by page and by line numbers, and
simple tabular- and array-style environments. The package is
distributed with the related reledpar package.

%package -n texlive-reledmac-doc
Summary:        Documentation for reledmac
Version:        svn48229
Provides:       tex-reledmac-doc
AutoReqProv:    No

%description -n texlive-reledmac-doc
Documentation for reledmac

%package -n texlive-qpxqtx
Provides:       tex-qpxqtx = %{tl_version}
License:        LPPL
Summary:        qpxqtx package
Version:        svn45797
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(qpxbmi.tfm) = %{tl_version}, tex(qpxbmia.tfm) = %{tl_version}
Provides:       tex(qpxmi.tfm) = %{tl_version}, tex(qpxmia.tfm) = %{tl_version}
Provides:       tex(qtxbmi.tfm) = %{tl_version}, tex(qtxbmia.tfm) = %{tl_version}
Provides:       tex(qtxmi.tfm) = %{tl_version}, tex(qtxmia.tfm) = %{tl_version}
Provides:       tex(qpxbmi.vf) = %{tl_version}, tex(qpxbmia.vf) = %{tl_version}
Provides:       tex(qpxmi.vf) = %{tl_version}, tex(qpxmia.vf) = %{tl_version}
Provides:       tex(qtxbmi.vf) = %{tl_version}, tex(qtxbmia.vf) = %{tl_version}
Provides:       tex(qtxmi.vf) = %{tl_version}, tex(qtxmia.vf) = %{tl_version}
Provides:       tex(amspbold.tex) = %{tl_version}, tex(amsqpx.def) = %{tl_version}
Provides:       tex(amsqpx.tex) = %{tl_version}, tex(amsqtx.def) = %{tl_version}
Provides:       tex(amsqtx.tex) = %{tl_version}, tex(amstbold.tex) = %{tl_version}
Provides:       tex(qpxmath.sty) = %{tl_version}, tex(qpxmath.tex) = %{tl_version}
Provides:       tex(qtxmath.sty) = %{tl_version}, tex(qtxmath.tex) = %{tl_version}

%description -n texlive-qpxqtx
qpxqtx package

%package -n texlive-qpxqtx-doc
Summary:        Documentation for qpxqtx
Version:        svn45797
Provides:       tex-qpxqtx-doc
AutoReqProv:    No

%description -n texlive-qpxqtx-doc
Documentation for qpxqtx

%package -n texlive-rcs
Provides:       tex-rcs = %{tl_version}
License:        GPL+
Summary:        Use RCS (revision control system) tags in LaTeX documents
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(rcs.sty) = %{tl_version}

%description -n texlive-rcs
The rcs package utilizes the inclusion of RCS supplied data in
LaTeX documents. It's upward compatible to *all* rcs styles I
know of. In particular, you can easily access values of every
RCS field in your document put the checkin date on the
titlepage put RCS fields in a footline You can typeset revision
logs. Not in verbatim -- real LaTeX text! But you need a
configurable RCS for that. Refer to the user manual for more
detailed information. You can also configure the rcs package
easily to do special things for any keyword. This bundle comes
with a user manual, an internal interface description, full
documentation of the implementation, style information for AUC-
TeX, and test cases.

%package -n texlive-rcs-doc
Summary:        Documentation for rcs
Version:        svn15878.0

Provides:       tex-rcs-doc
AutoReqProv:    No

%description -n texlive-rcs-doc
Documentation for rcs

%package -n texlive-qcircuit
Provides:       tex-qcircuit = %{tl_version}
License:        GPLv2+
Summary:        Macros to generate quantum ciruits
Version:        svn48400
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xy.sty)
Provides:       tex(qcircuit.sty) = %{tl_version}

%description -n texlive-qcircuit
The package supports those within the quantum information
community who typeset quantum circuits, using xy-pic package,
offering macros designed to help users generate circuits.

%package -n texlive-qcircuit-doc
Summary:        Documentation for qcircuit
Version:        svn48400
Provides:       tex-qcircuit-doc
AutoReqProv:    No

%description -n texlive-qcircuit-doc
Documentation for qcircuit

%package -n texlive-qrcode
Provides:       tex-qrcode = %{tl_version}
License:        LPPL 1.3
Summary:        Generate QR codes in LaTeX
Version:        svn36065.1.51

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xcolor.sty), tex(xkeyval.sty)
Provides:       tex(qrcode.sty) = %{tl_version}

%description -n texlive-qrcode
The package generates QR (Quick Response) codes in LaTeX,
without the need for PSTricks or any other graphical package.

%package -n texlive-qrcode-doc
Summary:        Documentation for qrcode
Version:        svn36065.1.51

Provides:       tex-qrcode-doc
AutoReqProv:    No

%description -n texlive-qrcode-doc
Documentation for qrcode

%package -n texlive-randbild
Provides:       tex-randbild = %{tl_version}
License:        LPPL
Summary:        Marginal pictures
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pst-plot.sty)
Provides:       tex(randbild.sty) = %{tl_version}

%description -n texlive-randbild
Provides environments randbild, to draw small marginal plots
(using the package pstricks package pst-plot), and
randbildbasis (the same, only without the automatically drawn
coordinate system).

%package -n texlive-randbild-doc
Summary:        Documentation for randbild
Version:        svn15878.0.2

Provides:       tex-randbild-doc
AutoReqProv:    No

%description -n texlive-randbild-doc
Documentation for randbild

%package -n texlive-randomwalk
Provides:       tex-randomwalk = %{tl_version}
License:        LPPL
Summary:        Random walks using TikZ
Version:        svn45954
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(tikz.sty), tex(lcg.sty)
Provides:       tex(randomwalk.sty) = %{tl_version}

%description -n texlive-randomwalk
The randomwalk package provides a user command, \RandomWalk, to
draw random walks with a given number of steps. Lengths and
angles of the steps can be customized in various ways. The
package uses lcg for its 'random' numbers and PGF/TikZ for its
graphical output.

%package -n texlive-randomwalk-doc
Summary:        Documentation for randomwalk
Version:        svn45954
Provides:       tex-randomwalk-doc
AutoReqProv:    No

%description -n texlive-randomwalk-doc
Documentation for randomwalk

%package -n texlive-reotex
Provides:       tex-reotex = %{tl_version}
License:        LPPL
Summary:        Draw Reo Channels and Circuits
Version:        svn34924.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(tikz.sty), tex(verbatim.sty)
Provides:       tex(reotex.sty) = %{tl_version}

%description -n texlive-reotex
The package defines macros and other utilities to design Reo
Circuits. The package requires PGF/TikZ support.

%package -n texlive-reotex-doc
Summary:        Documentation for reotex
Version:        svn34924.1.1

Provides:       tex-reotex-doc
AutoReqProv:    No

%description -n texlive-reotex-doc
Documentation for reotex

%package -n texlive-qcm
Provides:       tex-qcm = %{tl_version}
License:        LPPL
Summary:        A LaTeX2e class for making multiple choice questionnaires
Version:        svn15878.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty), tex(verbatim.sty), tex(tabularx.sty)
Provides:       tex(qcm.cls) = %{tl_version}, tex(qcm.sty) = %{tl_version}

%description -n texlive-qcm
QCM is a package for making multiple choices questionnaires
under LaTeX2e ("QCM" is the French acronym for this style of
test). A special environment allows you to define questions and
possible answers. You can specify which answers are correct and
which are not. QCM not only formats the questions for you, but
also generates a 'form' (a grid that your students will have to
fill in), and a 'mask' (the same grid, only with correct
answers properly checked in). You can then print the mask on a
slide and correct the questionnaires more easily by
superimposing the mask on top of students' forms. QCM can also
typeset exam corrections automatically, and comes with support
for AUC-TeX.

%package -n texlive-qcm-doc
Summary:        Documentation for qcm
Version:        svn15878.2.1

Provides:       tex-qcm-doc
AutoReqProv:    No

%description -n texlive-qcm-doc
Documentation for qcm

%package -n texlive-qstest
Provides:       tex-qstest = %{tl_version}
License:        LPPL
Summary:        Bundle for unit tests and pattern matching
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty)
Provides:       tex(makematch.sty) = %{tl_version}, tex(qstest.sty) = %{tl_version}

%description -n texlive-qstest
This is the public release of the qstest bundle (written for
DocScape Publisher) (C) 2006, 2007 QuinScape GmbH. The bundle
contains the packages 'makematch' for matching patterns to
targets (with a generalization in the form of pattern lists and
keyword lists), and 'qstest' for performing unit tests,
allowing the user to run a number of logged tests ensuring the
consistency of values, properties and call sequences during
execution of test code. Both packages make extensive use of in
their package documentation, providing illustrated examples
that are automatically verified to work as expected. Check the
README file for details.

%package -n texlive-qstest-doc
Summary:        Documentation for qstest
Version:        svn15878.0

Provides:       tex-qstest-doc
AutoReqProv:    No

%description -n texlive-qstest-doc
Documentation for qstest

%package -n texlive-qsymbols
Provides:       tex-qsymbols = %{tl_version}
License:        GPL+
Summary:        Maths symbol abbreviations
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amssymb.sty), tex(amsbsy.sty), tex(stmaryrd.sty), tex(xy.sty)
Provides:       tex(qsymbols.sty) = %{tl_version}

%description -n texlive-qsymbols
Provides macros for defining systematic mnemonic abbreviations,
starting with ` for math symbols and \" for arrows, using
standard symbols as well as those from the amsfonts bundle and
the stmaryrd package.

%package -n texlive-qsymbols-doc
Summary:        Documentation for qsymbols
Version:        svn15878.0

Provides:       tex-qsymbols-doc
AutoReqProv:    No

%description -n texlive-qsymbols-doc
Documentation for qsymbols

%package -n texlive-quotchap
Provides:       tex-quotchap = %{tl_version}
License:        GPL+
Summary:        Decorative chapter headings
Version:        svn28046.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(quotchap.sty) = %{tl_version}

%description -n texlive-quotchap
A package for creating decorative chapter headings with
quotations. Uses graphical and coloured output and by default
needs the "Adobe standard font set" (as supported by psnfss).

%package -n texlive-quotchap-doc
Summary:        Documentation for quotchap
Version:        svn28046.1.1

Provides:       tex-quotchap-doc
AutoReqProv:    No

%description -n texlive-quotchap-doc
Documentation for quotchap

%package -n texlive-quoting
Provides:       tex-quoting = %{tl_version}
License:        LPPL 1.3
Summary:        Consolidated environment for displayed text
Version:        svn32818.v0.1c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(kvoptions.sty)
Provides:       tex(quoting.sty) = %{tl_version}

%description -n texlive-quoting
As an alternative to the LaTeX standard environments quotation
and quote, the package provides a consolidated environment for
displayed text. First-line indentation may be activated by
adding a blank line before the quoting environment. A key-value
interface (using kvoptions) allows the user to configure font
properties and spacing and to control orphans within and after
the environment.

%package -n texlive-quoting-doc
Summary:        Documentation for quoting
Version:        svn32818.v0.1c

Provides:       tex-quoting-doc
AutoReqProv:    No

%description -n texlive-quoting-doc
Documentation for quoting

%package -n texlive-quotmark
Provides:       tex-quotmark = %{tl_version}
License:        LPPL
Summary:        Consistent quote marks
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(quotmark-UKenglish.def) = %{tl_version}
Provides:       tex(quotmark-USenglish.def) = %{tl_version}
Provides:       tex(quotmark-afrikaans.def) = %{tl_version}
Provides:       tex(quotmark-brazil.def) = %{tl_version}
Provides:       tex(quotmark-bulgarian.def) = %{tl_version}
Provides:       tex(quotmark-catalan.def) = %{tl_version}
Provides:       tex(quotmark-croatian.def) = %{tl_version}
Provides:       tex(quotmark-czech.def) = %{tl_version}, tex(quotmark-danish.def) = %{tl_version}
Provides:       tex(quotmark-dutch.def) = %{tl_version}, tex(quotmark-estonian.def) = %{tl_version}
Provides:       tex(quotmark-finnish.def) = %{tl_version}
Provides:       tex(quotmark-frenchb.def) = %{tl_version}
Provides:       tex(quotmark-germanb.def) = %{tl_version}
Provides:       tex(quotmark-greek.def) = %{tl_version}, tex(quotmark-hebrew.def) = %{tl_version}
Provides:       tex(quotmark-icelandic.def) = %{tl_version}
Provides:       tex(quotmark-irish.def) = %{tl_version}, tex(quotmark-italian.def) = %{tl_version}
Provides:       tex(quotmark-magyar.def) = %{tl_version}
Provides:       tex(quotmark-ngermanb.def) = %{tl_version}
Provides:       tex(quotmark-norsk.def) = %{tl_version}, tex(quotmark-polish.def) = %{tl_version}
Provides:       tex(quotmark-portuges.def) = %{tl_version}
Provides:       tex(quotmark-romanian.def) = %{tl_version}
Provides:       tex(quotmark-russianb.def) = %{tl_version}
Provides:       tex(quotmark-serbian.def) = %{tl_version}
Provides:       tex(quotmark-slovak.def) = %{tl_version}
Provides:       tex(quotmark-slovene.def) = %{tl_version}
Provides:       tex(quotmark-sorbian.def) = %{tl_version}
Provides:       tex(quotmark-spanish.def) = %{tl_version}
Provides:       tex(quotmark-swedish.def) = %{tl_version}
Provides:       tex(quotmark-swiss.def) = %{tl_version}, tex(quotmark-turkish.def) = %{tl_version}
Provides:       tex(quotmark-ukraineb.def) = %{tl_version}
Provides:       tex(quotmark-welsh.def) = %{tl_version}, tex(quotmark.sty) = %{tl_version}

%description -n texlive-quotmark
The package provides a means of ensuring consistent quote marks
throughout your document. The style can be changed either via
package option or command, and the package detects language
selections (from the babel or ngerman packages), and uses the
punctuation marks appropriate for the current language. The
author now considers the package obsolete, and recommends use
of csquotes in its place.

%package -n texlive-quotmark-doc
Summary:        Documentation for quotmark
Version:        svn15878.1.0

Provides:       tex-quotmark-doc
AutoReqProv:    No

%description -n texlive-quotmark-doc
Documentation for quotmark

%package -n texlive-ran_toks
Provides:       tex-ran_toks = %{tl_version}
License:        LPPL
Summary:        Randomise token strings
Version:        svn44429
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(verbatim.sty), tex(random.tex)
Provides:       tex(ran_toks.sty) = %{tl_version}

%description -n texlive-ran_toks
The package provides means of randomising lists of tokens, or
lists of chunks of tokens. Two mechanisms for defining chunks
are provided: the macro \ranToks command accepts an argument
containing tokens to be randomised; and the \bRTVToks/\eRTVToks
commands delimit a collection of tokens for randomising; each
group inside a rtVw constitutes one of these (typically larger)
token sets.

%package -n texlive-ran_toks-doc
Summary:        Documentation for ran_toks
Version:        svn44429
Provides:       tex-ran_toks-doc
AutoReqProv:    No

%description -n texlive-ran_toks-doc
Documentation for ran_toks

%package -n texlive-randtext
Provides:       tex-randtext = %{tl_version}
License:        LPPL
Summary:        Randomise the order of characters in strings
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(random.tex)
Provides:       tex(randtext.sty) = %{tl_version}

%description -n texlive-randtext
The package provides a single macro \randomize{TEXT} that
typesets the characters of TEXT in random order, such that the
resulting output appears correct, but most automated attempts
to read the file will misunderstand it. This function allows
one to include an email address in a TeX document and publish
it online without fear of email address harvesters or spammers
easily picking up the address.

%package -n texlive-randtext-doc
Summary:        Documentation for randtext
Version:        svn15878.0

Provides:       tex-randtext-doc
AutoReqProv:    No

%description -n texlive-randtext-doc
Documentation for randtext

%package -n texlive-rccol
Provides:       tex-rccol = %{tl_version}
License:        LPPL
Summary:        Decimal-centered optionally rounded numbers in tabular
Version:        svn15878.1.2c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty), tex(fltpoint.sty)
Provides:       tex(rccol.sty) = %{tl_version}

%description -n texlive-rccol
The rccol package provides decimal-centered numbers:
corresponding digits and decimal separators aligned.
Furthermore, rounding to the desired precision is possible. The
package makes use of the fltpoint package (as well as the LaTeX
required array package).

%package -n texlive-rccol-doc
Summary:        Documentation for rccol
Version:        svn15878.1.2c

Provides:       tex-rccol-doc
AutoReqProv:    No

%description -n texlive-rccol-doc
Documentation for rccol

%package -n texlive-rcs-multi
Provides:       tex-rcs-multi = %{tl_version}
License:        LPPL
Summary:        Typeset RCS version control in multiple-file documents
Version:        svn21939.0.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(rcs-multi.sty) = %{tl_version}

%description -n texlive-rcs-multi
The package enables the user to typeset version control
information provided by RCS keywords (e.g., $ID: ... $) in
LaTeX documents that contain multiple TeX files. The package is
based on the author's svn-multi package.

%package -n texlive-rcs-multi-doc
Summary:        Documentation for rcs-multi
Version:        svn21939.0.1a

Provides:       tex-rcs-multi-doc
AutoReqProv:    No

%description -n texlive-rcs-multi-doc
Documentation for rcs-multi

%package -n texlive-rcsinfo
Provides:       tex-rcsinfo = %{tl_version}
License:        LPPL
Summary:        Support for the revision control system
Version:        svn15878.1.11

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fancyheadings.sty), tex(fancyhdr.sty)
Requires:       tex(scrpage2.sty)
Provides:       tex(rcsinfo.cfg) = %{tl_version}, tex(rcsinfo.sty) = %{tl_version}

%description -n texlive-rcsinfo
A package to extract RCS (Revision Control System) information
and use it in a LaTeX document. For users of LaTeX2HTML
rcsinfo.perl is included.

%package -n texlive-rcsinfo-doc
Summary:        Documentation for rcsinfo
Version:        svn15878.1.11

Provides:       tex-rcsinfo-doc
AutoReqProv:    No

%description -n texlive-rcsinfo-doc
Documentation for rcsinfo

%package -n texlive-readarray
Provides:       tex-readarray = %{tl_version}
License:        LPPL 1.3
Summary:        Read, store and recall array-formatted data
Version:        svn42467
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(readarray.sty) = %{tl_version}

%description -n texlive-readarray
The package allows the user to input formatted data into
elements of a 2-D or 3-D array and to recall that data at will
by individual cell number. The data can be but need not be
numerical in nature. It can be, for example, formatted text.
While the package can be used for any application where indexed
data is called for, the package proves particularly useful when
elements of multiple arrays must be recallable and dynamically
combined at time of compilation, rather than in advance.

%package -n texlive-readarray-doc
Summary:        Documentation for readarray
Version:        svn42467
Provides:       tex-readarray-doc
AutoReqProv:    No

%description -n texlive-readarray-doc
Documentation for readarray

%package -n texlive-realboxes
Provides:       tex-realboxes = %{tl_version}
License:        LPPL 1.3
Summary:        Variants of common box-commands that read their content as real box and not as macro argument
Version:        svn23581.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(collectbox.sty), tex(adjcalc.sty), tex(calc.sty), tex(fancybox.sty)
Requires:       tex(xcolor.sty), tex(color.sty), tex(graphicx.sty), tex(graphics.sty)
Requires:       tex(dashbox.sty)
Provides:       tex(realboxes.sty) = %{tl_version}

%description -n texlive-realboxes
The package uses the author's package collectbox to define
variants of common box related macros which read the content as
real box and not as macro argument. This enables the use of
verbatim or other special material as part of this content. The
provided macros have the same names as the original versions
but start with an upper-case letter instead. The "long-form"
macros, like \Makebox, can also be used as environments, but
not the "short-form" macros, like \Mbox. However, normally the
long form uses the short form anyway when no optional arguments
are used.

%package -n texlive-realboxes-doc
Summary:        Documentation for realboxes
Version:        svn23581.0.2

Provides:       tex-realboxes-doc
AutoReqProv:    No

%description -n texlive-realboxes-doc
Documentation for realboxes

%package -n texlive-recipe
Provides:       tex-recipe = %{tl_version}
License:        Public Domain
Summary:        A LaTeX class to typeset recipes
Version:        svn15878.0.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(recipe.cls) = %{tl_version}

%description -n texlive-recipe
The layout design is relative straightforward (and traditional:
see 'sample output' under 'documentation'); the class needs
uses the Bookman and BrushScript-Italic fonts.

%package -n texlive-recipe-doc
Summary:        Documentation for recipe
Version:        svn15878.0.9

Provides:       tex-recipe-doc
AutoReqProv:    No

%description -n texlive-recipe-doc
Documentation for recipe

%package -n texlive-recipebook
Provides:       tex-recipebook = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset 5.5" x 8" recipes for browsing or printing
Version:        svn37026.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ragged2e.sty), tex(amsmath.sty), tex(amsfonts.sty), tex(amssymb.sty)
Requires:       tex(xparse.sty), tex(wrapfig.sty), tex(graphicx.sty), tex(eso-pic.sty)
Requires:       tex(anyfontsize.sty), tex(scrextend.sty)
Requires:       tex(multirow.sty), tex(multicol.sty), tex(nicefrac.sty), tex(xcolor.sty)
Requires:       tex(gensymb.sty), tex(booktabs.sty), tex(tabularx.sty), tex(calc.sty)
Requires:       tex(picture.sty), tex(parskip.sty), tex(tgtermes.sty), tex(fontenc.sty)
Requires:       tex(datetime.sty), tex(fancyhdr.sty), tex(tikz.sty), tex(tocloft.sty)
Requires:       tex(hyperref.sty), tex(geometry.sty), tex(environ.sty), tex(tcolorbox.sty)
Provides:       tex(RecipeBook.cls) = %{tl_version}

%description -n texlive-recipebook
This is a LaTeX2e class for typesetting recipes. It is designed
for typesetting one or two recipes per page, with dimensions of
5.5" x 8.5". The hyperlinked table of contents (ToC) and page
numbers make browsing recipes convenient, and the pages can be
joined together or printed two per sheet to normal letterpaper
easily. The size was chosen to work in half-page 3-ring binder
cover sheets.

%package -n texlive-recipebook-doc
Summary:        Documentation for recipebook
Version:        svn37026.0

Provides:       tex-recipebook-doc
AutoReqProv:    No

%description -n texlive-recipebook-doc
Documentation for recipebook

%package -n texlive-recipecard
Provides:       tex-recipecard = %{tl_version}
License:        LPPL
Summary:        Typeset recipes in note-card-sized boxes
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(ifthen.sty), tex(boxedminipage.sty), tex(geometry.sty)
Provides:       tex(recipecard.cls) = %{tl_version}

%description -n texlive-recipecard
The recipecard class typesets recipes into note card sized
boxes that can then be cut out and pasted on to note cards. The
recipe then looks elegant and fits in the box of recipes.

%package -n texlive-recipecard-doc
Summary:        Documentation for recipecard
Version:        svn15878.2.0

Provides:       tex-recipecard-doc
AutoReqProv:    No

%description -n texlive-recipecard-doc
Documentation for recipecard

%package -n texlive-rectopma
Provides:       tex-rectopma = %{tl_version}
License:        LPPL
Summary:        Recycle top matter
Version:        svn19980.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(rectopma.sty) = %{tl_version}

%description -n texlive-rectopma
Saves the arguments of \author and \title for reference (after
\maketitle) in a document. (\maketitle simply disposes of the
information, in the standard classes and some others.)

%package -n texlive-rectopma-doc
Summary:        Documentation for rectopma
Version:        svn19980.0

Provides:       tex-rectopma-doc
AutoReqProv:    No

%description -n texlive-rectopma-doc
Documentation for rectopma

%package -n texlive-refcheck
Provides:       tex-refcheck = %{tl_version}
License:        GPL+
Summary:        Check references (in figures, table, equations, etc)
Version:        svn29128.1.9.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(refcheck.sty) = %{tl_version}

%description -n texlive-refcheck
The package checks references in a document, looking for
numbered but unlabelled equations, for labels which are not
used in the text, for unused bibliography references. It can
also display label names in text near corresponding numbers of
equations and/or bibliography references.

%package -n texlive-refcheck-doc
Summary:        Documentation for refcheck
Version:        svn29128.1.9.1

Provides:       tex-refcheck-doc
AutoReqProv:    No

%description -n texlive-refcheck-doc
Documentation for refcheck

%package -n texlive-refenums
Provides:       tex-refenums = %{tl_version}
License:        LPPL 1.3
Summary:        Define reference labels items with names of their own
Version:        svn44131
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(csquotes.sty), tex(ifthen.sty), tex(hyperref.sty), tex(cleveref.sty)
Provides:       tex(refenums.sty) = %{tl_version}

%description -n texlive-refenums
The package provides commands to define enumerable items with a
number and a long name, which can be referenced referenced
later with the name or just the short form. For instance,
"Milestone M1: Specification created" can be defined and later
on be referenced with 'M1' or 'M1 ("Specification created")'.
The text in the references is derived from the definition and
also rendered as hyperlink to the definition.

%package -n texlive-refenums-doc
Summary:        Documentation for refenums
Version:        svn44131
Provides:       tex-refenums-doc
AutoReqProv:    No

%description -n texlive-refenums-doc
Documentation for refenums

%package -n texlive-reflectgraphics
Provides:       tex-reflectgraphics = %{tl_version}
License:        LPPL 1.3
Summary:        Techniques for reflecting graphics
Version:        svn40612

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(keyval.sty), tex(graphicx.sty), tex(calc.sty)
Requires:       tex(tikz.sty)
Provides:       tex(reflectgraphics.sty) = %{tl_version}

%description -n texlive-reflectgraphics
The package provides a macro for reflecting images, in a number
of different ways, in pursuit of "more striking" graphics in a
document.

%package -n texlive-reflectgraphics-doc
Summary:        Documentation for reflectgraphics
Version:        svn40612

Provides:       tex-reflectgraphics-doc
AutoReqProv:    No

%description -n texlive-reflectgraphics-doc
Documentation for reflectgraphics

%package -n texlive-refman
Provides:       tex-refman = %{tl_version}
License:        LPPL
Summary:        Format technical reference manuals
Version:        svn15878.2.0e

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(pagepc.sty) = %{tl_version}, tex(refart.cls) = %{tl_version}
Provides:       tex(refrep.cls) = %{tl_version}

%description -n texlive-refman
Document classes (report- and article-style) for writing
technical reference manuals. It offers a wide left margin for
notes to the reader, like some of the manuals distributed by
Adobe.

%package -n texlive-refman-doc
Summary:        Documentation for refman
Version:        svn15878.2.0e

Provides:       tex-refman-doc
AutoReqProv:    No

%description -n texlive-refman-doc
Documentation for refman

%package -n texlive-refstyle
Provides:       tex-refstyle = %{tl_version}
License:        LPPL
Summary:        Advanced formatting of cross references
Version:        svn20318.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(refstyle.cfg) = %{tl_version}, tex(refstyle.sty) = %{tl_version}

%description -n texlive-refstyle
The package provides a consistent way of producing references
throughout a project. Enough flexibility is provided to make
local changes to a single reference. The user can configure
their own setup. The package offers a direct interface to
varioref (for use, for example, in large projects such as a
series of books, or a multivolume thesis written as a series of
documents), and name references from the nameref package may be
incorporated with ease. For large projects such as a series of
books or a multi volume thesis, written as freestanding
documents, a facility is provided to interface to the xr
package for external document references.

%package -n texlive-refstyle-doc
Summary:        Documentation for refstyle
Version:        svn20318.0.5

Provides:       tex-refstyle-doc
AutoReqProv:    No

%description -n texlive-refstyle-doc
Documentation for refstyle

%package -n texlive-regcount
Provides:       tex-regcount = %{tl_version}
License:        LPPL
Summary:        Display the allocation status of the TeX registers
Version:        svn19979.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(regcount.sty) = %{tl_version}

%description -n texlive-regcount
Adds a macro \rgcounts which displays the allocation status of
the TeX registers. The display is written into the .log file as
it is a bit verbose. An automatic call to \rgcounts is done at
\begin{document} and \end{document}.

%package -n texlive-regcount-doc
Summary:        Documentation for regcount
Version:        svn19979.1.0

Provides:       tex-regcount-doc
AutoReqProv:    No

%description -n texlive-regcount-doc
Documentation for regcount

%package -n texlive-regexpatch
Provides:       tex-regexpatch = %{tl_version}
License:        LPPL 1.3
Summary:        High level patching of commands
Version:        svn47601
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3regex.sty)
Provides:       tex(regexpatch.sty) = %{tl_version}

%description -n texlive-regexpatch
The package generalises the macro patching commands provided by
P. Lehmann's etoolbox. The difference between this package and
its sibling xpatch is that this package sports a very powerful
\regexpatchcmd based on the l3regex module of the LaTeX3
experimental packages.

%package -n texlive-regexpatch-doc
Summary:        Documentation for regexpatch
Version:        svn47601
Provides:       tex-regexpatch-doc
AutoReqProv:    No

%description -n texlive-regexpatch-doc
Documentation for regexpatch

%package -n texlive-register
Provides:       tex-register = %{tl_version}
License:        LPPL
Summary:        Typeset programmable elements in digital hardware (registers)
Version:        svn47773
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(graphicx.sty), tex(float.sty), tex(calc.sty)
Provides:       tex(register.sty) = %{tl_version}

%description -n texlive-register
This package is designed for typesetting the programmable
elements in digital hardware, i.e., registers. Such registers
typically have many fields and can be quite wide; they are thus
a challenge to typeset in a consistent manner. Register is
similar in some aspects to the bytefield package. Anyone doing
hardware documentation using LaTeX should examine both
packages. Register requires a fairly recent version of the
float package. A Perl module and a Perl script are provided, to
translate the register specifications into programmable data
structures.

%package -n texlive-register-doc
Summary:        Documentation for register
Version:        svn47773
Provides:       tex-register-doc
AutoReqProv:    No

%description -n texlive-register-doc
Documentation for register

%package -n texlive-regstats
Provides:       tex-regstats = %{tl_version}
License:        LPPL 1.3
Summary:        Information about register use
Version:        svn25050.1.0h

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(atveryend.sty), tex(ltxcmds.sty), tex(intcalc.sty)
Requires:       tex(ifluatex.sty), tex(ifpdf.sty)
Provides:       tex(regstats.sty) = %{tl_version}

%description -n texlive-regstats
The package will report number of used registers (counter,
dimen, skip, muskip, box, token, input, output, math families,
languages, insertions), and will compare the number to the
maximum available number of such registers.

%package -n texlive-regstats-doc
Summary:        Documentation for regstats
Version:        svn25050.1.0h

Provides:       tex-regstats-doc
AutoReqProv:    No

%description -n texlive-regstats-doc
Documentation for regstats

%package -n texlive-relenc
Provides:       tex-relenc = %{tl_version}
License:        LPPL
Summary:        A "relaxed" font encoding
Version:        svn22050.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(zcmr8d.tfm) = %{tl_version}, tex(zcmra.tfm) = %{tl_version}
Provides:       tex(zcmr8d.vf) = %{tl_version}, tex(zcmra.vf) = %{tl_version}
Provides:       tex(2sidedoc.sty) = %{tl_version}, tex(ecsubzcm.sty) = %{tl_version}
Provides:       tex(relenc.sty) = %{tl_version}, tex(t1renc.def) = %{tl_version}
Provides:       tex(t1rzcm.fd) = %{tl_version}

%description -n texlive-relenc
LaTeX package providing a relaxed font encoding to make
available to a font designer more slots for insertion of
ligatures and accented characters.

%package -n texlive-relenc-doc
Summary:        Documentation for relenc
Version:        svn22050.0

Provides:       tex-relenc-doc
AutoReqProv:    No

%description -n texlive-relenc-doc
Documentation for relenc

%package -n texlive-relsize
Provides:       tex-relsize = %{tl_version}
License:        Public Domain
Summary:        Set the font size relative to the current font size
Version:        svn30707.4.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(relsize.sty) = %{tl_version}

%description -n texlive-relsize
The basic command of the package is \relsize, whose argument is
a number of \magsteps to change size; from this are defined
commands \larger, \smaller, \textlarger, etc.

%package -n texlive-relsize-doc
Summary:        Documentation for relsize
Version:        svn30707.4.1

Provides:       tex-relsize-doc
AutoReqProv:    No

%description -n texlive-relsize-doc
Documentation for relsize

%package -n texlive-repeatindex
Provides:       tex-repeatindex = %{tl_version}
License:        LPPL
Summary:        Repeat items in an index after a page or column break
Version:        svn24305.0.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(afterpage.sty), tex(makeidx.sty)
Provides:       tex(repeatindex.sty) = %{tl_version}

%description -n texlive-repeatindex
This Package repeats item of an index if a page or column break
occurs within a list of subitems. This helps to find out to
which main item a subitem belongs.

%package -n texlive-repeatindex-doc
Summary:        Documentation for repeatindex
Version:        svn24305.0.01

Provides:       tex-repeatindex-doc
AutoReqProv:    No

%description -n texlive-repeatindex-doc
Documentation for repeatindex

%package -n texlive-repltext
Provides:       tex-repltext = %{tl_version}
License:        LPPL 1.3
Summary:        Control how text gets copied from a PDF file
Version:        svn33442.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(graphicx.sty)
Provides:       tex(repltext.sty) = %{tl_version}

%description -n texlive-repltext
The repltext package exposes to LaTeX a relatively obscure PDF
feature: replacement text. When replacement text is specified
for a piece of text, it is the replacement text, not the
typeset text that is copied and pasted.

%package -n texlive-repltext-doc
Summary:        Documentation for repltext
Version:        svn33442.1.0

Provides:       tex-repltext-doc
AutoReqProv:    No

%description -n texlive-repltext-doc
Documentation for repltext

%package -n texlive-rjlparshap
Provides:       tex-rjlparshap = %{tl_version}
License:        LPPL 1.2
Summary:        Support for use of \parshape in LaTeX
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(arrayjob.sty), tex(forloop.sty)
Provides:       tex(rjlpshap.sty) = %{tl_version}

%description -n texlive-rjlparshap
The package provides macros and environments that relieve the
programmer of some of the difficulties of using \parshape in
LaTeX macros. It does not actually calculate shapes in the way
that the shapepar package does.

%package -n texlive-rjlparshap-doc
Summary:        Documentation for rjlparshap
Version:        svn15878.1.0

Provides:       tex-rjlparshap-doc
AutoReqProv:    No

%description -n texlive-rjlparshap-doc
Documentation for rjlparshap

%package -n texlive-rlepsf
Provides:       tex-rlepsf = %{tl_version}
License:        LPPL
Summary:        Rewrite labels in EPS graphics
Version:        svn19082.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(rlepsf.tex) = %{tl_version}

%description -n texlive-rlepsf
A macro package for use with epsf.tex which allows PostScript
labels in an Encapsulated PostScript file to be replaced by TeX
labels. The package provides commands \relabel (simply replace
a PostScript string), \adjustrelabel (replace a PostScript
string, with position adjustment), and \extralabel (add a label
at given coordinates). You can, if you so choose, use the
facilities of the labelfig package in place of using
\extralabel.

%package -n texlive-rlepsf-doc
Summary:        Documentation for rlepsf
Version:        svn19082.0

Provides:       tex-rlepsf-doc
AutoReqProv:    No

%description -n texlive-rlepsf-doc
Documentation for rlepsf

%package -n texlive-rmpage
Provides:       tex-rmpage = %{tl_version}
License:        GPL+
Summary:        A package to help change page layout parameters in LaTeX
Version:        svn20002.0.92

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(avant.sty), tex(bookman.sty), tex(chancery.sty), tex(helvet.sty)
Requires:       tex(newcent.sty), tex(palatino.sty), tex(times.sty), tex(utopia.sty)
Requires:       tex(beton.sty)
Provides:       tex(rmpage.sty) = %{tl_version}, tex(rmpgen.cfg) = %{tl_version}

%description -n texlive-rmpage
The package lets you change page layout parameters in small
steps over a range of values using options. It can set
\textwidth appropriately for the main fount, and ensure that
the text fits inside the printable area of a printer. An rmpage-
formatted document can be typeset identically without rmpage
after a single cut and paste operation. Local configuration can
set defaults: for all documents; and by class, by printer, and
by paper size. The geometry package is better if you want to
set page layout parameters to particular measurements.

%package -n texlive-rmpage-doc
Summary:        Documentation for rmpage
Version:        svn20002.0.92

Provides:       tex-rmpage-doc
AutoReqProv:    No

%description -n texlive-rmpage-doc
Documentation for rmpage

%package -n texlive-rec-thy
Provides:       tex-rec-thy = %{tl_version}
License:        Public Domain
Summary:        Commands to typeset recursion theory papers
Version:        svn46650
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(suffix.sty), tex(ifmtarg.sty), tex(xifthen.sty), tex(xkeyval.sty)
Requires:       tex(stmaryrd.sty), tex(amsmath.sty), tex(amssymb.sty), tex(marvosym.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(rec-thy.sty) = %{tl_version}

%description -n texlive-rec-thy
The package provides many macros to express standard notation
in recursion theory (otherwise known as computability theory).

%package -n texlive-rec-thy-doc
Summary:        Documentation for rec-thy
Version:        svn46650
Provides:       tex-rec-thy-doc
AutoReqProv:    No

%description -n texlive-rec-thy-doc
Documentation for rec-thy

%package -n texlive-ribbonproofs
Provides:       tex-ribbonproofs = %{tl_version}
License:        LPPL 1.3
Summary:        Drawing ribbon proofs
Version:        svn31137.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xcolor.sty), tex(tikz.sty), tex(xstring.sty), tex(etextools.sty)
Provides:       tex(ribbonproofs.sty) = %{tl_version}

%description -n texlive-ribbonproofs
The package provides a way to draw "ribbon proofs" in LaTeX. A
ribbon proof is a diagrammatic representation of a mathematical
proof that a computer program meets its specification. These
diagrams are more human-readable, more scalable, and more
easily modified than the corresponding textual proofs.

%package -n texlive-ribbonproofs-doc
Summary:        Documentation for ribbonproofs
Version:        svn31137.1.0

Provides:       tex-ribbonproofs-doc
AutoReqProv:    No

%description -n texlive-ribbonproofs-doc
Documentation for ribbonproofs

%package -n texlive-rmathbr
Provides:       tex-rmathbr = %{tl_version}
License:        LPPL 1.3
Summary:        Repeating of math operator at the broken line and the new line in inline equations
Version:        svn40415

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifetex.sty), tex(mathstyle.sty)
Provides:       tex(rmathbr.sty) = %{tl_version}

%description -n texlive-rmathbr
Repeating of math operators at the broken line and the new line
in inline equations is used in Cyrillic mathematical typography
(Russian for example), but unfortunately LaTeX does not provide
such an option. This package solves the problem by extending
ideas described in M. I. Grinchuk "TeX and Russian Traditions
of Typesetting", TUGboat 17(4) (1996) 385 and supports most of
LaTeX mathematical packages. See the documentation for details.

%package -n texlive-rmathbr-doc
Summary:        Documentation for rmathbr
Version:        svn40415

Provides:       tex-rmathbr-doc
AutoReqProv:    No

%description -n texlive-rmathbr-doc
Documentation for rmathbr

%package -n texlive-repere
Provides:       tex-repere = %{tl_version}
License:        LPPL 1.3
Summary:        Diagrams for school mathematics
Version:        svn45779
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-repere
The package simplifies drawing figures in a coordinate system;
the specific target is support of secondary school mathematics.

%package -n texlive-repere-doc
Summary:        Documentation for repere
Version:        svn45779
Provides:       tex-repere-doc
AutoReqProv:    No

%description -n texlive-repere-doc
Documentation for repere

%package -n texlive-resumemac
Provides:       tex-resumemac = %{tl_version}
License:        Public Domain
Summary:        Plain TeX macros for resumes
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(resumemac.tex) = %{tl_version}

%description -n texlive-resumemac
A set of macros is provided, together with an file that offers
an example of use.

%package -n texlive-resumemac-doc
Summary:        Documentation for resumemac
Version:        svn15878.0

Provides:       tex-resumemac-doc
AutoReqProv:    No

%description -n texlive-resumemac-doc
Documentation for resumemac

%package -n texlive-resphilosophica
Provides:       tex-resphilosophica = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset articles for the journal Res Philosophica
Version:        svn46713
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(microtype.sty), tex(fancyhdr.sty), tex(xcolor.sty)
Requires:       tex(lastpage.sty), tex(collect.sty), tex(footmisc.sty), tex(hyperref.sty)
Requires:       tex(mathdesign.sty), tex(natbib.sty)
Provides:       tex(resphilosophica.cls) = %{tl_version}

%description -n texlive-resphilosophica
The bundle provides a class for typesetting articles for the
journal Res Philosophica. Development was commissioned by Saint
Louis University.

%package -n texlive-resphilosophica-doc
Summary:        Documentation for resphilosophica
Version:        svn46713
Provides:       tex-resphilosophica-doc
AutoReqProv:    No

%description -n texlive-resphilosophica-doc
Documentation for resphilosophica

%package -n texlive-resumecls
Provides:       tex-resumecls = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset a resumee in both Chinese and English
Version:        svn38427

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(hyperref.sty), tex(ctex.sty), tex(tabularx.sty)
Requires:       tex(color.sty), tex(fancyhdr.sty), tex(natbib.sty)
Provides:       tex(resumecls.cls) = %{tl_version}

%description -n texlive-resumecls
The class provides a simple resumee structure that works,
natively, with both Chinese and English text.

%package -n texlive-resumecls-doc
Summary:        Documentation for resumecls
Version:        svn38427

Provides:       tex-resumecls-doc
AutoReqProv:    No

%description -n texlive-resumecls-doc
Documentation for resumecls

%package -n texlive-quicktype
Summary:        LaTeX package for quick typesetting
Version:        svn42183
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(quicktype.sty) = %{tl_version}

%description -n texlive-quicktype
Intended for the quick typesetting of basic documents using
LaTeX using shortcuts to existing commands and specific
commands for quick formatting and creation of tables and title
pages with a graphic image.

%package -n texlive-randomlist
Summary:        Deal with database, loop, and random in order to build personalized exercises
Version:        svn45281
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(randomlist.sty) = %{tl_version}, tex(randomlist.tex) = %{tl_version}

%description -n texlive-randomlist
The main aim of this package is to work on lists, especially
with random operations. The hidden aim is to build a personnal
collection of exercises with different data for each pupil.

%package -n texlive-realscripts
Provides:       tex-realscripts = %{tl_version}
License:        LPPL 1.3
Summary:        Access OpenType subscript and superscript glyphs
Version:        svn39706

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontspec.sty)
Provides:       tex(realscripts.sty) = %{tl_version}

%description -n texlive-realscripts
This small package replaces \textsuperscript and \textsubscript
commands by equivalent commands that use OpenType font features
to access appropriate glyphs if possible. The package also
patches LaTeX's default footnote command to use this new
\textsuperscript for footnote symbols. The package requires
fontspec running on either XeLaTeX or LuaLaTeX. The package
holds functions that were once parts of the xltxtra package,
which now loads realscripts by default.

%package -n texlive-realscripts-doc
Summary:        Documentation for realscripts
Version:        svn39706

Provides:       tex-realscripts-doc
AutoReqProv:    No

%description -n texlive-realscripts-doc
Documentation for realscripts

%package -n texlive-revtex
Provides:       tex-revtex = %{tl_version}
License:        LPPL 1.3
Summary:        Styles for various Physics Journals
Version:        svn19652.4.1r

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty), tex(shortvrb.sty), tex(textcase.sty), tex(amsfonts.sty)
Requires:       tex(amssymb.sty), tex(amsmath.sty), tex(lineno.sty), tex(url.sty)
Requires:       tex(natbib.sty)
Provides:       tex(ltxdocext.sty) = %{tl_version}, tex(ltxfront.sty) = %{tl_version}
Provides:       tex(ltxgrid.sty) = %{tl_version}, tex(ltxutil.sty) = %{tl_version}
Provides:       tex(reftest4-1.tex) = %{tl_version}, tex(revsymb4-1.sty) = %{tl_version}
Provides:       tex(revtex4-1.cls) = %{tl_version}

%description -n texlive-revtex
Includes styles for American Physical Society, American
Institute of Physics, and Optical Society of America. The
distribution consists of the RevTeX class itself, and several
support packages.

%package -n texlive-revtex-doc
Summary:        Documentation for revtex
Version:        svn19652.4.1r

Provides:       tex-revtex-doc
AutoReqProv:    No

%description -n texlive-revtex-doc
Documentation for revtex

%package -n texlive-revtex4
Provides:       tex-revtex4 = %{tl_version}
License:        LPPL
Summary:        revtex4 package
Version:        svn45873
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(amsfonts.sty), tex(amssymb.sty), tex(amsmath.sty), tex(url.sty)
Requires:       tex(natbib.sty)
Provides:       tex(docs.sty) = %{tl_version}, tex(revsymb.sty) = %{tl_version}
Provides:       tex(revtex4.cls) = %{tl_version}

%description -n texlive-revtex4
revtex4 package

%package -n texlive-revtex4-doc
Summary:        Documentation for revtex4
Version:        svn45873
Provides:       tex-revtex4-doc
AutoReqProv:    No

%description -n texlive-revtex4-doc
Documentation for revtex4

%package -n texlive-quran
Provides:       tex-quran = %{tl_version}
License:        LPPL 1.3
Summary:        An easy way to typeset any part of The Holy Quran
Version:        svn46133
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(biditools.sty)
Provides:       tex(quran.sty) = %{tl_version}

%description -n texlive-quran
This package offers the user an easy way to typeset The Holy
Quran. It has been inspired by the lipsum and ptext packages
and provides several macros for typesetting the whole or any
part of Quran based on its popular division. Available macros
are: \quransurah, \quranayah, \quranjuz, \quranhizb,
\quranquarter, \quranpage, \qurantext, \surahname, \basmalah.
The package only works with the "xelatex" format and should be
loaded before the bidi package.

%package -n texlive-quran-doc
Summary:        Documentation for quran
Version:        svn46133
Provides:       tex-quran-doc
AutoReqProv:    No

%description -n texlive-quran-doc
Documentation for quran

%package -n texlive-revquantum
Summary:        Hacks to make writing quantum papers for revtex4-1 less painful
Version:        svn43505
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(revquantum.sty) = %{tl_version}

%description -n texlive-revquantum
This package provides a number of useful hacks to solve common
annoyances with the revtex4-1 package, and to define notation
in common use within quantum information. In doing so, it
imports and configures a number of commonly-available and used
packages, and where reasonable, provides fallbacks. It also
warns when users try to load packages which are known to be
incompatible with revtex4-1.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="impallari/quattrocento impallari/raleway"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-quattrocento
%license lppl1.txt
%{_datadir}/fonts/quattrocento
%{_texdir}/texmf-dist/fonts/enc/dvips/quattrocento/
%{_texdir}/texmf-dist/fonts/map/dvips/quattrocento/
%{_texdir}/texmf-dist/fonts/opentype/impallari/quattrocento/
%{_texdir}/texmf-dist/fonts/tfm/impallari/quattrocento/
%{_texdir}/texmf-dist/fonts/type1/impallari/quattrocento/
%{_texdir}/texmf-dist/fonts/vf/impallari/quattrocento/
%{_texdir}/texmf-dist/tex/latex/quattrocento/

%files -n texlive-quattrocento-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/quattrocento/

%files -n texlive-raleway
%license ofl.txt
%{_datadir}/fonts/raleway
%{_texdir}/texmf-dist/fonts/enc/dvips/raleway/
%{_texdir}/texmf-dist/fonts/map/dvips/raleway/
%{_texdir}/texmf-dist/fonts/opentype/impallari/raleway/
%{_texdir}/texmf-dist/fonts/tfm/impallari/raleway/
%{_texdir}/texmf-dist/fonts/type1/impallari/raleway/
%{_texdir}/texmf-dist/fonts/vf/impallari/raleway/
%{_texdir}/texmf-dist/tex/latex/raleway/

%files -n texlive-raleway-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/latex/raleway/

%files -n texlive-recycle
%license gpl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/recycle/
%{_texdir}/texmf-dist/fonts/source/public/recycle/
%{_texdir}/texmf-dist/fonts/tfm/public/recycle/
%{_texdir}/texmf-dist/fonts/type1/public/recycle/
%{_texdir}/texmf-dist/tex/latex/recycle/

%files -n texlive-recycle-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/recycle/

%files -n texlive-reverxii-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/plain/reverxii/

%files -n texlive-qobitree
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/qobitree/

%files -n texlive-qobitree-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/qobitree/

%files -n texlive-qtree
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/qtree/

%files -n texlive-qtree-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/qtree/

%files -n texlive-reledmac
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/reledmac/

%files -n texlive-reledmac-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/reledmac/

%files -n texlive-rcs
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/rcs/

%files -n texlive-qpxqtx
%{_texdir}/texmf-dist/fonts/tfm/public/qpxqtx/
%{_texdir}/texmf-dist/fonts/vf/public/qpxqtx/
%{_texdir}/texmf-dist/tex/generic/qpxqtx/

%files -n texlive-qpxqtx-doc
%{_texdir}/texmf-dist/doc/fonts/qpxqtx/

%files -n texlive-rcs-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/rcs/

%files -n texlive-qcircuit
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/qcircuit/

%files -n texlive-qcircuit-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/qcircuit/

%files -n texlive-qrcode
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/qrcode/

%files -n texlive-qrcode-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/qrcode/

%files -n texlive-randbild
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/randbild/

%files -n texlive-randbild-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/randbild/

%files -n texlive-randomwalk
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/randomwalk/

%files -n texlive-randomwalk-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/randomwalk/

%files -n texlive-reotex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/reotex/

%files -n texlive-reotex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/reotex/

%files -n texlive-qcm
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/qcm/

%files -n texlive-qcm-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/qcm/

%files -n texlive-qstest
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/qstest/

%files -n texlive-qstest-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/qstest/

%files -n texlive-qsymbols
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/qsymbols/

%files -n texlive-qsymbols-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/qsymbols/

%files -n texlive-quotchap
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/quotchap/

%files -n texlive-quotchap-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/quotchap/

%files -n texlive-quoting
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/quoting/

%files -n texlive-quoting-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/quoting/

%files -n texlive-quotmark
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/quotmark/

%files -n texlive-quotmark-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/quotmark/

%files -n texlive-ran_toks
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ran_toks/

%files -n texlive-ran_toks-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ran_toks/

%files -n texlive-randtext
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/randtext/

%files -n texlive-randtext-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/randtext/

%files -n texlive-rccol
%{_texdir}/texmf-dist/tex/latex/rccol/

%files -n texlive-rccol-doc
%{_texdir}/texmf-dist/doc/latex/rccol/

%files -n texlive-rcs-multi
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/rcs-multi/

%files -n texlive-rcs-multi-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/rcs-multi/

%files -n texlive-rcsinfo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/rcsinfo/

%files -n texlive-rcsinfo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/rcsinfo/

%files -n texlive-readarray
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/readarray/

%files -n texlive-readarray-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/readarray/

%files -n texlive-realboxes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/realboxes/

%files -n texlive-realboxes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/realboxes/

%files -n texlive-recipe
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/recipe/

%files -n texlive-recipe-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/recipe/

%files -n texlive-recipebook
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/recipebook/

%files -n texlive-recipebook-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/recipebook/

%files -n texlive-recipecard
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/recipecard/

%files -n texlive-recipecard-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/recipecard/

%files -n texlive-rectopma
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/rectopma/

%files -n texlive-rectopma-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/rectopma/

%files -n texlive-refcheck
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/refcheck/

%files -n texlive-refcheck-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/refcheck/

%files -n texlive-refenums
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/refenums/

%files -n texlive-refenums-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/refenums/

%files -n texlive-reflectgraphics
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/reflectgraphics/

%files -n texlive-reflectgraphics-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/reflectgraphics/

%files -n texlive-refman
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/refman/

%files -n texlive-refman-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/refman/

%files -n texlive-refstyle
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/refstyle/

%files -n texlive-refstyle-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/refstyle/

%files -n texlive-regcount
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/regcount/

%files -n texlive-regcount-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/regcount/

%files -n texlive-regexpatch
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/regexpatch/

%files -n texlive-regexpatch-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/regexpatch/

%files -n texlive-register
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/register/

%files -n texlive-register-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/register/

%files -n texlive-regstats
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/regstats/

%files -n texlive-regstats-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/regstats/

%files -n texlive-relenc
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/tfm/public/relenc/
%{_texdir}/texmf-dist/fonts/vf/public/relenc/
%{_texdir}/texmf-dist/tex/latex/relenc/

%files -n texlive-relenc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/relenc/

%files -n texlive-relsize
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/relsize/

%files -n texlive-relsize-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/relsize/

%files -n texlive-repeatindex
%license lppl1.txt
%{_texdir}/texmf-dist/makeindex/repeatindex/
%{_texdir}/texmf-dist/tex/latex/repeatindex/

%files -n texlive-repeatindex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/repeatindex/

%files -n texlive-repltext
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/repltext/

%files -n texlive-repltext-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/repltext/

%files -n texlive-rjlparshap
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/rjlparshap/

%files -n texlive-rjlparshap-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/rjlparshap/

%files -n texlive-rlepsf
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/rlepsf/

%files -n texlive-rlepsf-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/rlepsf/

%files -n texlive-rmpage
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/rmpage/

%files -n texlive-rmpage-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/rmpage/

%files -n texlive-resumemac
%license pd.txt
%{_texdir}/texmf-dist/tex/plain/resumemac/

%files -n texlive-resumemac-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/plain/resumemac/

%files -n texlive-resphilosophica
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/resphilosophica/
%{_texdir}/texmf-dist/tex/latex/resphilosophica/

%files -n texlive-resphilosophica-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/resphilosophica/

%files -n texlive-resumecls
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/resumecls/

%files -n texlive-resumecls-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/resumecls/

%files -n texlive-randomlist
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/generic/randomlist/
%{_texdir}/texmf-dist/tex/generic/randomlist/

%files -n texlive-revtex
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/revtex/
%{_texdir}/texmf-dist/tex/latex/revtex/

%files -n texlive-revtex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/revtex/

%files -n texlive-revtex4
%{_texdir}/texmf-dist/bibtex/bib/revtex4/
%{_texdir}/texmf-dist/bibtex/bst/revtex4/
%{_texdir}/texmf-dist/tex/latex/revtex4/

%files -n texlive-revtex4-doc
%{_texdir}/texmf-dist/doc/latex/revtex4/

%files -n texlive-quicktype
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/quicktype/
%{_texdir}/texmf-dist/tex/latex/quicktype/

%files -n texlive-realscripts
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/realscripts/

%files -n texlive-realscripts-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/realscripts/

%files -n texlive-rec-thy
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/rec-thy/

%files -n texlive-rec-thy-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/rec-thy/

%files -n texlive-ribbonproofs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ribbonproofs/

%files -n texlive-ribbonproofs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ribbonproofs/

%files -n texlive-rmathbr
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/rmathbr/

%files -n texlive-rmathbr-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/rmathbr/

%files -n texlive-revquantum
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/revquantum/
%doc %{_texdir}/texmf-dist/doc/latex/revquantum/

%files -n texlive-repere
%license lppl1.3.txt
%{_texdir}/texmf-dist/metapost/repere/

%files -n texlive-repere-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/metapost/repere/

%files -n texlive-quran
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/quran/

%files -n texlive-quran-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/quran/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
