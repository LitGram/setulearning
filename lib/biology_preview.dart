import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'models/chapter.dart';
import 'theme/app_theme.dart';
import 'widgets/content_block_widget.dart';

/// Local review entry point; uses the actual bundled lessons and reader widgets.
void main() => runApp(MaterialApp(
      title: 'Science Setu • Biology graphics preview',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.createTheme(seedColor: const Color(0xff16765d)),
      home: const BiologyPreview(),
    ));

class BiologyPreview extends StatefulWidget {
  const BiologyPreview({super.key});
  @override
  State<BiologyPreview> createState() => _BiologyPreviewState();
}

class _BiologyPreviewState extends State<BiologyPreview> {
  static const _lessons = [
    ('vigyansetu_book5', 'ch1', '1 · जीव विज्ञान का परिचय'),
    ('vigyansetu_book5', 'ch2', '2 · वर्गिकी और वर्गीकरण'),
    ('vigyansetu_book5', 'ch3', 'कोशिका संरचना • Cell structure'),
    ('vigyansetu_book5', 'ch4', 'कोशिका विभाजन • Cell division'),
    ('vigyansetu_book5', 'ch5', '5 · ऊतक / Tissues'),
    ('vigyansetu_book5', 'ch6', '6 · जैव अणु / Biomolecules'),
    ('vigyansetu_book5', 'ch7', '7 · सूक्ष्मजीव / Microorganisms'),
    ('vigyansetu_book5', 'ch8', '8 · सूक्ष्मजीवों के उपयोग'),
    ('vigyansetu_book5', 'ch9', '9 · पादप जगत / Plant groups'),
    ('vigyansetu_book5', 'ch10', '10 · प्राणी जगत / Animal groups'),
    ('vigyansetu_book5', 'ch11', '17 · मेंडल के नियम / Mendel'),
    ('vigyansetu_book5', 'ch12', '18 · वंशागति / Inheritance'),
    ('vigyansetu_book5', 'ch13', '19 · उत्परिवर्तन / Mutations'),
    ('vigyansetu_book5', 'ch14', '20 · जैव विकास / Evolution'),
    ('vigyansetu_book5', 'ch15', '21 · जैव उर्वरक और राजस्थान के पौधे'),
    ('vigyansetu_book5', 'ch16', '22 · पुनरावृत्ति / Revision'),
    ('vigyansetu_book6', 'ch1', 'अध्याय 1: मानव शरीर का संगठन, समस्थापन एवं प्रमुख जंतु ऊतक'),
    ('vigyansetu_book6', 'ch2', 'अध्याय 2: अस्थि और पेशी तंत्र: कंकाल संरचना, संधियां एवं पेशी संकुचन क्रियाविधि'),
    ('vigyansetu_book6', 'ch3', 'अध्याय 3: मानव पाचन तंत्र, पाचक ग्रंथियां एवं पोषण क्रियाविधि'),
    ('vigyansetu_book6', 'ch4', 'अध्याय 4: मानव श्वसन तंत्र, गैस विनिमय एवं श्वसन नियमन'),
    ('vigyansetu_book6', 'ch5', 'अध्याय 5: मानव परिसंचरण तंत्र, रक्त संघटन, रक्त समूह, हृदय एवं कार्डियक चक्र'),
    ('vigyansetu_book6', 'ch6', 'अध्याय 6: मानव लसीका तंत्र, लसीका वाहिकाएं, लसीका अंग एवं शरीर के तरल'),
    ('vigyansetu_book6', 'ch7', 'अध्याय 7: मानव उत्सर्जन तंत्र, वृक्क, नेफ्रॉन कार्यिकी, मूत्र निर्माण एवं परासरण नियमन'),
    ('vigyansetu_book6', 'ch8', 'अध्याय 8: मानव तंत्रिका तंत्र, न्यूरॉन, केंद्रीय व परिधीय तंत्रिका तंत्र, मस्तिष्क एवं प्रतिवर्ती क्रिया'),
    ('vigyansetu_book6', 'ch9', 'अध्याय 9: संवेदी अंग: मानव नेत्र, कर्ण, घ्राण, स्वाद एवं त्वचा'),
    ('vigyansetu_book6', 'ch10', 'अध्याय 10: अन्तःस्रावी ग्रंथियाँ एवं हार्मोन तंत्र: रासायनिक समन्वय, प्रमुख ग्रंथियां, क्रियाविधि एवं विकार'),
    ('vigyansetu_book6', 'ch11', 'अध्याय 11: मानव जनन तंत्र, युग्मकजनन, निषेचन, भ्रूणीय परिवर्धन, सगर्भता एवं प्रसव'),
    ('vigyansetu_book6', 'ch12', 'अध्याय 12: किशोरावस्था, जनन स्वास्थ्य, गर्भनिरोधक विधियां, यौन संचारित रोग एवं सहायक जनन प्रौद्योगिकी (ART)'),
    ('vigyansetu_book6', 'ch13', 'अध्याय 13: भोजन के घटक: संतुलित आहार, कार्बोहाइड्रेट, वसा, प्रोटीन, आहारीय रेशे एवं पोषण मान'),
    ('vigyansetu_book6', 'ch14', 'अध्याय 14: विटामिन, खनिज लवण, जल, हीनताजन्य रोग एवं कुपोषण (PEM)'),
    ('vigyansetu_book6', 'ch15', 'अध्याय 15: रोगजनक, संक्रमण, संचरण के माध्यम एवं महामारी विज्ञान'),
    ('vigyansetu_book6', 'ch16', 'अध्याय 16: विषाणु जनित रोग: संरचना, प्रतिकृति, प्रमुख वायरल संक्रमण (HIV/AIDS, हेपेटाइटिस, कोविड-19, इन्फ्लूएंजा, डेंगू, रेबीज) एवं नियंत्रण'),
    ('vigyansetu_book6', 'ch17', 'अध्याय 17: जीवाणु, कवक एवं परजीवी जनित रोग: तपेदिक (TB), टाइफाइड, हैजा, मलेरिया, प्रोटोजोआ, कृमि रोग, फंगल संक्रमण एवं एंटीबायोटिक प्रतिरोध'),
    ('vigyansetu_book6', 'ch18', 'अध्याय 18: प्रतिरक्षा तंत्र, प्रतिरक्षी (Antibodies), टीकाकरण (Vaccines), राष्ट्रीय टीकाकरण सारणी एवं प्रतिरक्षा विकार'),
    ('vigyansetu_book6', 'ch19', 'अध्याय 19: असंक्रामक रोग एवं जीवनशैली जनित विकार: मधुमेह, उच्च रक्तचाप, हृदय रोग, कैंसर, श्वसन विकार एवं मानसिक स्वास्थ्य'),
    ('vigyansetu_book6', 'ch20', 'अध्याय 20: आनुवंशिक विकार एवं जन्मजात विकृतियां: गुणसूत्रीय विकार, मेंडेलियन विकार (थैलेसीमिया, सिकल सेल, हीमोफिलिया) एवं आनुवंशिक परामर्श'),
    ('vigyansetu_book6', 'ch21', 'अध्याय 21: जनस्वास्थ्य, स्वच्छता, अपशिष्ट प्रबंधन एवं प्राथमिक उपचार (CPR/AED)'),
    ('vigyansetu_book6', 'ch22', 'अध्याय 22: मादक द्रव्य दुरुपयोग, तंबाकू, मदिरा एवं व्यसनमुक्ति'),
    ('vigyansetu_book6', 'ch23', 'अध्याय 23: राष्ट्रीय एवं राजस्थान की प्रमुख स्वास्थ्य नीतियां, कार्यक्रम एवं डिजिटल स्वास्थ्य मिशन'),
    ('vigyansetu_book6', 'ch24', 'अध्याय 24: संपूर्ण जीव विज्ञान 2 (मानव शरीर, पोषण व स्वास्थ्य) - वृहद मॉडल प्रश्न-पत्र एवं समग्र पुनरावृत्ति'),
  ];
  int _selected = 17;
  bool _fullLesson = false;
  late Future<Chapter> _chapter = _load();

  Future<Chapter> _load() async {
    final lesson = _lessons[_selected];
    final raw = await rootBundle
        .loadString('assets/content/vigyansetu/${lesson.$1}.json');
    final data = jsonDecode(raw) as Map<String, dynamic>;
    final chapter = (data['chapters'] as List)
        .cast<Map<String, dynamic>>()
        .firstWhere((c) => c['id'] == lesson.$2);
    return Chapter.fromJson(chapter);
  }

  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(title: const Text('Science Setu • Biology')),
        body: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 760),
            child: Column(children: [
              Padding(
                padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
                child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      const Text('जीव विज्ञान को चित्रों से समझें',
                          style: TextStyle(
                              fontSize: 24, fontWeight: FontWeight.bold)),
                      const SizedBox(height: 6),
                      const Text(
                          'Book 1: 46 graphics · Book 2: 64 graphics • Tap to zoom'),
                      const SizedBox(height: 16),
                      DropdownButtonFormField<int>(
                        initialValue: _selected,
                        isExpanded: true,
                        decoration: const InputDecoration(
                            labelText: 'अध्याय चुनें / Choose chapter',
                            border: OutlineInputBorder()),
                        items: List.generate(
                            _lessons.length,
                            (i) => DropdownMenuItem(
                                value: i,
                                child: Text(_lessons[i].$3,
                                    maxLines: 1,
                                    overflow: TextOverflow.ellipsis))),
                        onChanged: (value) {
                          if (value == null) return;
                          setState(() {
                            _selected = value;
                            _chapter = _load();
                          });
                        },
                      ),
                      SwitchListTile(
                        contentPadding: EdgeInsets.zero,
                        title:
                            const Text('पूरा अध्याय पढ़ें / Read full chapter'),
                        subtitle: Text(_fullLesson
                            ? 'Original text and diagrams together'
                            : 'Diagrams and Hindi learning notes'),
                        value: _fullLesson,
                        onChanged: (value) =>
                            setState(() => _fullLesson = value),
                      ),
                    ]),
              ),
              Expanded(
                child: FutureBuilder<Chapter>(
                  future: _chapter,
                  builder: (context, snapshot) {
                    if (snapshot.hasError) {
                      return Center(
                          child: Text(
                              'Could not load chapter: ${snapshot.error}'));
                    }
                    if (!snapshot.hasData) {
                      return const Center(child: CircularProgressIndicator());
                    }
                    final chapter = snapshot.data!;
                    final blocks = _fullLesson
                        ? chapter.content
                        : chapter.content
                            .where((b) =>
                                b.type == 'image' ||
                                (b.type == 'callout' &&
                                    b.value.startsWith('**चित्र से सीखें')))
                            .toList();
                    return ListView.builder(
                      key: ValueKey('$_selected-$_fullLesson'),
                      padding: const EdgeInsets.fromLTRB(16, 0, 16, 32),
                      itemCount: blocks.length + 1,
                      itemBuilder: (context, index) => index == 0
                          ? Text(chapter.title,
                              style: Theme.of(context).textTheme.titleMedium)
                          : ContentBlockWidget(block: blocks[index - 1]),
                    );
                  },
                ),
              ),
            ]),
          ),
        ),
      );
}
