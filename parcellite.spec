Name:           parcellite
Version:        1.2.3
Release:        2%{?dist}
Summary:        Lightweight GTK+ Clipboard Manager
License:        GPL-3.0+
Url:            https://github.com/ZaWertun/parcellite
Source0:        https://github.com/ZaWertun/parcellite/archive/%{version}/parcellite-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Recommends:     xdotool
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  libappindicator-devel
BuildRequires:  gtk2-devel >= 2.10.0

%description
Lightweight GTK+ Clipboard Manager.

%prep
%setup -q

%build
%cmake
%__make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README.md
%{_bindir}/parcellite
%{_datadir}/applications/parcellite.desktop
%{_datadir}/icons/hicolor/*/apps/parcellite.png
%{_datadir}/icons/hicolor/scalable/apps/parcellite.svg
%{_mandir}/man1/parcellite.1.gz

%changelog
* Sat Feb 25 2017 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.2.3-2
- version 1.2.3

* Wed Feb 01 2017 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.2.2-1
- initial version

