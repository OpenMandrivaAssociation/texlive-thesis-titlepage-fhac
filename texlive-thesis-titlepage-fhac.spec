# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/thesis-titlepage-fhAC
# catalog-date 2007-03-12 14:32:12 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-thesis-titlepage-fhac
Version:	0.1
Release:	6
Summary:	Little style to create a standard titlepage for diploma thesis
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thesis-titlepage-fhAC
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-titlepage-fhac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-titlepage-fhac.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-titlepage-fhac.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 756830
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719727
- texlive-thesis-titlepage-fhac
- texlive-thesis-titlepage-fhac
- texlive-thesis-titlepage-fhac

