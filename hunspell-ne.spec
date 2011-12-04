Name: hunspell-ne
Summary: Nepali hunspell dictionaries
Version: 20080425
Release: 1.1%{?dist}
Source: http://nepalinux.org/downloads/ne_NP_dict.zip
Group: Applications/Text
URL: http://nepalinux.org/downloads
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2
BuildArch: noarch

Requires: hunspell

%description
Nepali hunspell dictionaries.

%prep
%setup -q -c -n ne_NP_dict

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ne_NP_aliases="ne_IN"
for lang in $ne_NP_aliases; do
        ln -s ne_NP.aff $lang.aff
        ln -s ne_NP.dic $lang.dic
done
popd


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_ne_NP.txt 
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20080425-1.1
- Rebuilt for RHEL 6

* Tue Aug 11 2009 Parag <pnemade@redhat.com> - 20080425-1
- Update to next upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061217-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061217-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Parag <pnemade@redhat.com> - 20061217-3
- Resolves:rh#475982 - Perhaps hunspell-ne suffices for ne_IN as well as ne_NP 

* Mon Jan 21 2008 Parag <pnemade@redhat.com> - 20061217-2
- Corrected License tag.

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20061217-1
- Initial Fedora release
