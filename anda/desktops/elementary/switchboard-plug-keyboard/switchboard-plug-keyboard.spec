%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-keyboard

%global plug_type hardware
%global plug_name keyboard
%global plug_rdnn io.elementary.settings.keyboard

Name:           switchboard-plug-keyboard
Summary:        Switchboard Keyboard plug
Version:        8.0.0
Release:        1%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/switchboard-plug-keyboard
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  fdupes

BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.19
BuildRequires:  pkgconfig(switchboard-3)
BuildRequires:  pkgconfig(xkeyboard-config)

Requires:       gala
Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
This plug can be used to change several keyboard settings, for example
the delay and speed of the key repetition, or the cursor blinking speed.
You can change your keyboard layout, and use multiple layouts at the
same time. Keyboard shortcuts are also part of this plug.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%fdupes %buildroot%_datadir/locale/
%find_lang %{plug_rdnn}


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_rdnn}.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard-3/%{plug_type}/lib%{plug_name}.so
%{_datadir}/glib-2.0/schemas/%{plug_rdnn}.gschema.xml
%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com> - 2.7.0-1
- Repackaged for Terra
