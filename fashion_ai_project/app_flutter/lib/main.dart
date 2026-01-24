import 'package:flutter/material.dart';
import 'screens/welcome_screen.dart';

void main() {
  runApp(const DailysApp());
}

class DailysApp extends StatelessWidget {
  const DailysApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dailys',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        // 디자인의 메인 오렌지 색상 설정
        primaryColor: const Color(0xFFFF9E67),
        scaffoldBackgroundColor: const Color(0xFFF8F1EA), // 부드러운 배경색
      ),
      home: const WelcomeScreen(),
    );
  }
}