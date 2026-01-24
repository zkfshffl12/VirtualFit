import 'package:flutter/material.dart';

class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 30),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Spacer(flex: 2),
            // 타이틀과 로고 부분
            const Text(
              'Dailys',
              style: TextStyle(
                fontSize: 48,
                fontWeight: FontWeight.bold,
                color: Color(0xFFFF9E67),
              ),
            ),
            const SizedBox(height: 20),
            // 중앙 아이콘
            Image.asset('assets/images/1.png', height: 150),
            const SizedBox(height: 10),
            const Text('Staying your day ...', style: TextStyle(color: Colors.grey)),
            
            const Spacer(flex: 1),
            
            // SIGN UP 버튼
            SizedBox(
              width: double.infinity,
              height: 50,
              child: ElevatedButton(
                onPressed: () {
                  // Sign Up 화면으로 이동 (추후 구현)
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color(0xFFFF9E67),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                ),
                child: const Text('SIGN UP', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              ),
            ),
            
            // 로그인 유도 텍스트 버튼
            TextButton(
              onPressed: () {
                // Login 화면으로 이동 (추후 구현)
              },
              child: const Text(
                'ALREADY HAVE AN ACCOUNT?',
                style: TextStyle(color: Colors.black54, fontSize: 12),
              ),
            ),
            const SizedBox(height: 40),
          ],
        ),
      ),
    );
  }
}