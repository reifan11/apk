[app]
title           = WiFi Killer
package.name    = wifikiller
package.domain  = org.netact
version         = 6.0

source.dir          = .
source.include_exts = py,png,kv,atlas

requirements = python3,kivy==2.3.0,pyjnius,android

orientation  = portrait
fullscreen   = 1

android.api              = 33
android.minapi           = 23
android.ndk              = 25c
android.ndk_api          = 23
android.archs            = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
android.allow_backup     = False

android.permissions = INTERNET, \
                      ACCESS_WIFI_STATE, \
                      CHANGE_WIFI_STATE, \
                      ACCESS_NETWORK_STATE, \
                      CHANGE_NETWORK_STATE, \
                      ACCESS_FINE_LOCATION, \
                      ACCESS_COARSE_LOCATION, \
                      CHANGE_WIFI_MULTICAST_STATE

android.extra_manifest_xml = \
    <uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" android:maxSdkVersion="28"/> \
    <uses-permission android:name="android.permission.NEARBY_WIFI_DEVICES" android:usesPermissionFlags="neverForLocation"/>

android.features         = android.hardware.wifi

android.logcat_filters   = *:S python:D

[buildozer]
log_level   = 2
warn_on_root = 1
