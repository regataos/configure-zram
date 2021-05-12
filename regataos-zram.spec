Name: regataos-zram
Version: 1.0
Release: 0
Url: https://github.com/regataos/configure-zram
Summary: Configuration set for zRAM
Group: System/GUI/KDE
BuildRequires: xz
BuildRequires: desktop-file-utils
BuildRequires: update-desktop-files
BuildRequires: hicolor-icon-theme
BuildRequires: -post-build-checks
%{?systemd_requires}
BuildRequires: systemd
BuildRequires: grep
License: MIT
Source0: zram1.conf
Source1: zram2.conf
Source2: 99-zram.rules
Source3: zram.service
Source4: regataos-zram.sh
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
Set of configurations that helps to prepare the zRAM in Regata OS.

%build

%install
mkdir -p %{buildroot}/etc/modprobe.d/
install -D -m 644 %{SOURCE0} %{buildroot}/etc/modprobe.d/zram.conf

mkdir -p %{buildroot}/etc/modules-load.d/
install -D -m 644 %{SOURCE1} %{buildroot}/etc/modules-load.d/zram.conf

mkdir -p %{buildroot}/etc/udev/rules.d/
install -D -m 644 %{SOURCE2} %{buildroot}/etc/udev/rules.d/99-zram.rules

mkdir -p %{buildroot}%{_unitdir}
install -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/zram.service

mkdir -p %{buildroot}%{_bindir}
install -D -m 755 %{SOURCE4} %{buildroot}%{_bindir}/regataos-zram.sh

%post
# Enable ZRAM systemd service
%service_add_post zram.service
systemctl enable  zram.service || true

%clean

%files
%defattr(-,root,root)
/etc/modprobe.d/zram.conf
/etc/modules-load.d/zram.conf
/etc/udev/rules.d/99-zram.rules
%{_unitdir}/zram.service
%{_bindir}/regataos-zram.sh

%changelog
