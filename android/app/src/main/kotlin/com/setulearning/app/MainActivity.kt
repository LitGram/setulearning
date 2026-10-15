package com.setulearning.app

import android.view.WindowManager
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel

class MainActivity: FlutterActivity() {
    companion object {
        // Preserve the request if Android recreates the Activity while the
        // Flutter engine still has an open reader or quiz.
        private var secureContentRequested = false
        private const val CHANNEL = "com.setulearning.app/screenshot_protection"
    }

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        applyScreenshotProtection(secureContentRequested)
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL)
            .setMethodCallHandler { call, result ->
                if (call.method != "setSecure") {
                    result.notImplemented()
                    return@setMethodCallHandler
                }
                val enabled = call.argument<Boolean>("enabled")
                if (enabled == null) {
                    result.error("INVALID_ARGUMENT", "enabled must be a boolean", null)
                    return@setMethodCallHandler
                }
                applyScreenshotProtection(enabled)
                secureContentRequested = enabled
                result.success(null)
            }
    }

    private fun applyScreenshotProtection(enabled: Boolean) {
        if (enabled) {
            window.addFlags(WindowManager.LayoutParams.FLAG_SECURE)
        } else {
            window.clearFlags(WindowManager.LayoutParams.FLAG_SECURE)
        }
    }
}
