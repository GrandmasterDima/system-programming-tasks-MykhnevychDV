Name:           count_files
Version:        1.0
Release:        1%{?dist}
Summary:        Script to count regular files in /etc

License:        GPL-3.0+
BuildArch:      noarch
Requires:       /bin/bash
Source0:        %{name}-%{version}.tar.gz

%description
This package installs a simple script that counts regular files
(excluding directories and symlinks) in the /etc directory.
It should be run as root.

%prep
# Розпаковуємо tarball у BUILD
%setup -q -n count-files-1.0

%build
# Нічого не компілюємо

%install
rm -rf %{buildroot}
# Створюємо директорію для бінарних файлів
install -d %{buildroot}%{_bindir}
# Встановлюємо скрипт
install -m 0755 count_files.sh %{buildroot}%{_bindir}/count_files

%files
%{_bindir}/count_files

%changelog
* Sat Oct 26 2025 Mykhnevych Dmytro <grandmasterdima@gmail.com> - 1.0-1
- Initial RPM release with count_files.sh



