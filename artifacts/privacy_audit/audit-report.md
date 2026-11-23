# Setu Learning privacy audit and resubmission

Completed: 13 October 2026 (Asia/Calcutta).

## Outcome
Published https://litgram.in/setu-learning-privacy-policy/ as public WordPress page 6541. Independently loaded without authentication in the in-app browser; verified all 14 sections. Mobile formatting verified with no document horizontal overflow after a CSS correction scoped solely to this page. Existing LitGram AI policy, themes, plugins and navigation were not edited.
Existing Indus app 2377093 was updated with that URL and submitted using Submit App followed by Submit For Review. Dashboard verified **In Review**. Existing uploaded binary 348a007a803b4d892bfaef53e7a5ae6b.apk was retained, package com.litgram.setulearning, version 1.0.0(1). Existing auto-publish setting was retained.

## Binary evidence
Inspected apk_output/SetuLearning-LitGram-Release.apk with Android aapt, apkanalyzer, ZIP inspection and native AOT string inspection.
Package com.litgram.setulearning; version 1.0.0, code 1; min SDK 24; target SDK 36; APK size 122343175 bytes.
SHA-256: 2de994118091ef0e277ee7e9825aec5606602f09fce848212e6f485b15e406ee.
This is the only local APK matching the submitted package/version. Console provides no checksum or binary download control, so exact submitted-byte identity remains unproven.
The newer Reader Layout Fix APK is 1.0.1(2) and was not uploaded. Other APKs have the earlier com.setulearning.app package.

## Educational features and storage
56 bundled JSON content files cover MathSetu, EnglishSetu, VigyanSetu, RASSetu and supplementary books, Great Works, MSc Physics, and UGC NET English, Hindi, History, Political Science and Commerce. Books contain chapters, notes, illustrations and MCQs with explanations. Source provides subject/book/chapter navigation, local search, reading resume, quizzes and progress views.
SQLite setu_learning.db stores chapter_progress, quiz_scores and last_position. Local preferences store reading offsets, unfinished quiz state, recent searches, theme and font scale. AOT strings confirm database/table names, study session/search functions, preferences and reset controls. No separate bookmark implementation found.
48 content files match current source byte-for-byte; 8 differ. Current source also has later RBSE content absent from audited 1.0.0 APK. No claim that current source exactly reproduces the historical binary is made.
No remote Markdown image references or missing explicit image assets were found in the audited content scan. Educational images use local assets.

## Network, permissions and integrations
Compiled manifest declares only com.litgram.setulearning.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION, a signature-level AndroidX internal receiver permission. No Internet, ACCESS_NETWORK_STATE, camera, microphone, contacts, location, shared-storage, phone or notification permission.
Native/Dex and source review found Flutter, AndroidX, sqflite, shared preferences, JNI/path utilities, Markdown and math rendering. No Firebase, AdMob, Facebook SDK, Crashlytics, WebView plugin, authentication, remote learning backend or app-defined network client found. AndroidX lifecycle/profile installation components are present; not telemetry integrations.
Offline operation is strongly supported by bundled content, local persistence and absent Internet permission. Runtime airplane-mode testing and packet observation were NOT performed: no emulator installation was found under the configured SDK and ADB could not start. No claim of measured runtime network traffic is made.

## Privacy caveats
allowBackup, fullBackupContent and dataExtractionRules are absent from compiled manifest; Android default backups are therefore allowed. OS/vendor backup or transfer may copy/restore study data according to device settings. Policy explicitly distinguishes this from app-operated transmission. SQLite has no separate app-level encryption. No code change is needed to truthfully describe these behaviors.
Official support address mukesh@litgram.in verified at https://litgram.in/contact-us/. Android backup behavior verified against https://developer.android.com/identity/data/autobackup.
Website has its own advertising/newsletter services; those are distinct from the offline Android app and the policy describes website use separately.

## Changes
No app source, build configuration or APK modified. Added only audit artifacts under artifacts/privacy_audit/: apk-inspection.json, compiled-manifest.txt, privacy-policy.html, public-policy-snapshot.txt, published-policy.png, policy-mobile.png, indus-final-status.txt, indus-resubmitted.png and this report.
External changes: one new public WordPress page with page-specific mobile CSS; one Privacy Policy URL change and resubmission on the existing Indus listing.
Remaining store action: wait for reviewer decision. Exact historical binary identity and runtime offline/traffic validation remain audit limitations.
