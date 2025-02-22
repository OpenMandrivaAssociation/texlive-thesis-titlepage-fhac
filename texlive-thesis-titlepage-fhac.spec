Name:		texlive-thesis-titlepage-fhac
Version:	15878
Release:	2
Summary:	Little style to create a standard titlepage for diploma thesis
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thesis-titlepage-fhAC
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-titlepage-fhac.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-titlepage-fhac.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-titlepage-fhac.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Yet another thesis titlepage style: support of Fachhochschule
Aachen (Standort Juelich).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/thesis-titlepage-fhac/fhACtitlepage.cfg
%{_texmfdistdir}/tex/latex/thesis-titlepage-fhac/fhACtitlepage.sty
%{_texmfdistdir}/tex/latex/thesis-titlepage-fhac/figbib_add.sty
%{_texmfdistdir}/tex/latex/thesis-titlepage-fhac/gloss_add.sty
%doc %{_texmfdistdir}/doc/latex/thesis-titlepage-fhac/LogoFH.eps
%doc %{_texmfdistdir}/doc/latex/thesis-titlepage-fhac/LogoFH.pdf
%doc %{_texmfdistdir}/doc/latex/thesis-titlepage-fhac/LogoFH.png
%doc %{_texmfdistdir}/doc/latex/thesis-titlepage-fhac/LogoFH.tif
%doc %{_texmfdistdir}/doc/latex/thesis-titlepage-fhac/README
%doc %{_texmfdistdir}/doc/latex/thesis-titlepage-fhac/antrc_pre.bat
%doc %{_texmfdistdir}/doc/latex/thesis-titlepage-fhac/build.xml
%doc %{_texmfdistdir}/doc/latex/thesis-titlepage-fhac/diplomArbeit.ltx
%doc %{_texmfdistdir}/doc/latex/thesis-titlepage-fhac/doxygen_header.tex
%doc %{_texmfdistdir}/doc/latex/thesis-titlepage-fhac/fhACtitlepage.pdf
%doc %{_texmfdistdir}/doc/latex/thesis-titlepage-fhac/pdf_with_figbig_and_glossar.tco
#- source
%doc %{_texmfdistdir}/source/latex/thesis-titlepage-fhac/doxygen_header.dtx.input
%doc %{_texmfdistdir}/source/latex/thesis-titlepage-fhac/fhACtitlepage.dtx
%doc %{_texmfdistdir}/source/latex/thesis-titlepage-fhac/fhACtitlepage.ins
%doc %{_texmfdistdir}/source/latex/thesis-titlepage-fhac/gloss_add.dtx.input

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
