%define		packname	Rgraphviz

Summary:	Plotting capabilities for R graph objects
Name:		R-%{packname}
Version:	2.2.1
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	dfb5ee6dd2cc11f08ef720fbf237e499
URL:		http://bioconductor.org/packages/release/bioc/html/Rgraphviz.html
BuildRequires:	R-graph
BuildRequires:	R
BuildRequires:	graphviz-devel
BuildRequires:	texlive-latex
Requires:	R-graph
Requires:	R
Requires:	graphviz
Suggests:	R-cran-RUnit
Suggests:	R-cran-XML
Suggests:	R-BiocGenerics
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interfaces R with the AT and T graphviz library for plotting R graph
objects from the graph package.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} --configure-args='--with-graphviz=/usr' -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/LICENSE
%doc %{_libdir}/R/library/%{packname}/NEWS.Rd
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/unitTests
%{_libdir}/R/library/%{packname}/prepare
%{_libdir}/R/library/%{packname}/usecases
