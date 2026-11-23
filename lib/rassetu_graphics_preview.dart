import 'package:flutter/material.dart';

/// Review gallery for integrated RASSetu series graphics.
void main() => runApp(const RASGraphicsPreviewApp());

class RASGraphicsPreviewApp extends StatelessWidget {
  const RASGraphicsPreviewApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
        title: 'RASSetu • Graphics preview',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(colorSchemeSeed: const Color(0xff7c2d12), useMaterial3: true),
        home: const RASGraphicsPreview(),
      );
}

class RASGraphicsPreview extends StatefulWidget {
  const RASGraphicsPreview({super.key});
  @override
  State<RASGraphicsPreview> createState() => _RASGraphicsPreviewState();
}

class _RASGraphicsPreviewState extends State<RASGraphicsPreview> {
  static const _graphics = [
    ('rassetu_b2_watershed.webp', 'अरावली: जल-विभाजक'),
    ('rassetu_b2_drainage.webp', 'अपवाह तंत्र और नदी-बेसिन'),
    ('rassetu_b2_monsoon.webp', 'मानसून और वर्षा-छाया'),
    ('rassetu_b2_crop_belts.webp', 'फसल और जलवायु संबंध'),
    ('rassetu_b2_water_harvesting.webp', 'पारंपरिक जल-संचयन'),
    ('rassetu_b2_rajasthan_physiography.webp', 'Book 2 · राजस्थान के चार भौतिक प्रदेश'),
    ('rassetu_b2_forest_ecology.webp', 'Book 2 · राजस्थान के वन-रूप'),
    ('rassetu_b2_woodland_scene.webp', 'Book 2 · शुष्क वन और घासभूमि — प्रतिनिधि दृश्य'),
    ('rassetu_b2_soil_parent_material.webp', 'Book 2 · पैतृक शैल से मृदा'),
    ('rassetu_b2_water_stress.webp', 'Book 2 · जल-संकट का भौतिक तंत्र'),
    ('rassetu_b2_pastoral_scene.webp', 'Book 2 · थार पशुधन — प्रतिनिधि दृश्य'),
    ('rassetu_b2_india_physiography.webp', 'Book 2 · भारत के भौतिक प्रदेश'),
    ('rassetu_b2_india_monsoon_mechanism.webp', 'Book 2 · भारतीय मानसून तंत्र'),
    ('rassetu_b2_india_drainage_compare.webp', 'Book 2 · हिमालयी और प्रायद्वीपीय अपवाह'),
    ('rassetu_b2_whittlesey_framework.webp', 'Book 2 · व्हिटलसी के कृषि-वर्गीकरण मानदंड'),
    ('rassetu_b2_dune_formation.webp', 'Book 2 · बालुका स्तूप और पवन'),
    ('rassetu_b2_thar_dunes_scene.webp', 'Book 2 · थार बालुका स्तूप — प्रतिनिधि दृश्य'),
    ('rassetu_b2_chambal_ravines.webp', 'Book 2 · चंबल बीहड़ निर्माण'),
    ('rassetu_b2_luni_salinity.webp', 'Book 2 · लूणी की लवणता'),
    ('rassetu_b2_sambhar_salt_basin.webp', 'Book 2 · सांभर बंद बेसिन और नमक'),
    ('rassetu_b2_india_plate_tectonics.webp', 'Book 2 · भारतीय प्लेट और हिमालय'),
    ('rassetu_b6_deduction_induction.webp', 'Book 6 · निगमन और आगमन'),
    ('rassetu_b6_flow_कथन_म_ल_य_कन.webp', 'Book 6 · कथन का मूल्यांकन'),
    ('rassetu_b6_number_series.webp', 'Book 6 · संख्या-श्रृंखला'),
    ('rassetu_b6_family_tree.webp', 'Book 6 · रक्त-संबंध वंशवृक्ष'),
    ('rassetu_b6_venn_models.webp', 'Book 6 · वेन आरेख'),
    ('rassetu_b6_ranking_formula.webp', 'Book 6 · क्रम-परीक्षण'),
    ('rassetu_b6_mirror_water.webp', 'Book 6 · दर्पण और जल प्रतिबिंब'),
    ('rassetu_b6_number_system.webp', 'Book 6 · संख्या पद्धति'),
    ('rassetu_b6_ratio_proportion.webp', 'Book 6 · अनुपात और समानुपात'),
    ('rassetu_b6_percent_fraction.webp', 'Book 6 · प्रतिशत रूपांतरण'),
    ('rassetu_b6_simple_compound_interest.webp', 'Book 6 · ब्याज'),
    ('rassetu_b6_geometry_shapes.webp', 'Book 6 · त्रिभुज'),
    ('rassetu_b6_mean_median_mode.webp', 'Book 6 · माध्य, माध्यिका, बहुलक'),
    ('rassetu_b6_probability.webp', 'Book 6 · प्रायिकता'),
    ('rassetu_b6_course_of_action_filter.webp', 'Book 6 · उचित कार्यवाही'),
    ('rassetu_b6_argument_cause_effect.webp', 'Book 6 · कारण–प्रभाव तर्क'),
    ('rassetu_b6_coding_alphabet_map.webp', 'Book 6 · कोडिंग–डिकोडिंग'),
    ('rassetu_b6_data_interpretation_reading.webp', 'Book 6 · आंकड़ा व्याख्या'),
    ('rassetu_b6_permutation_combination.webp', 'Book 6 · क्रमचय और संचय'),
    ('rassetu_b6_current_affairs_verification.webp', 'Book 6 · समसामयिकी सत्यापन'),
    ('rassetu_b6_omr_fifth_option_workflow.webp', 'Book 6 · OMR पांचवां विकल्प'),
    ('rassetu_b6_question_bank_review_loop.webp', 'Book 6 · प्रश्न बैंक अभ्यास-चक्र'),
    ('rassetu_b4_bill_to_act.webp', 'Book 4 · विधेयक से अधिनियम'),
    ('rassetu_b5_agriculture_value_chain.webp', 'Book 5 · कृषि मूल्य-शृंखला'),
    ('rassetu_b5_biotechnology_steps.webp', 'Book 5 · जैव-प्रौद्योगिकी'),
    ('rassetu_b1_fort_architecture.webp', 'Book 1 · दुर्ग स्थापत्य'),
    ('rassetu_b1_painting_schools.webp', 'Book 1 · चित्रशैलियां'),
    ('rassetu_b1_folk_dance_regions.webp', 'Book 1 · लोकनृत्य'),
    ('rassetu_b1x_archaeology_locator.webp', 'Book 1 · पुरातात्विक स्थल'),
    ('rassetu_b1x_prehistoric_sequence.webp', 'Book 1 · प्रागैतिहासिक क्रम'),
    ('rassetu_b1x_kalibanga_ahar_compare.webp', 'Book 1 · कालीबंगा और आहड़'),
    ('rassetu_b1x_dynasty_parallel_timeline.webp', 'Book 1 · राजवंश काल-रेखाएं'),
    ('rassetu_b1x_kingdoms_schematic_locator.webp', 'Book 1 · क्षेत्रीय राजवंश'),
    ('rassetu_b1x_mewar_capital_sequence.webp', 'Book 1 · मेवाड़ के सत्ता-केंद्र'),
    ('rassetu_b1x_fort_capital_schematic.webp', 'Book 1 · दुर्ग और क्षेत्र'),
    ('rassetu_b1x_people_movements_timeline.webp', 'Book 1 · किसान और जनजातीय आंदोलन'),
    ('rassetu_b1x_integration_seven_stages.webp', 'Book 1 · राजस्थान एकीकरण'),
    ('rassetu_b1x_craft_material_process.webp', 'Book 1 · शिल्प सामग्री और तकनीक'),
    ('rassetu_b1x_festival_month_cycle.webp', 'Book 1 · त्योहार और मेले'),
    ('rassetu_b1x_heritage_concept_web.webp', 'Book 1 · विरासत संकल्पना-जाल'),
    ('rassetu_b1x_heritage_recall_grid.webp', 'Book 1 · विरासत मिलान-अभ्यास'),
    ('rassetu_b1x_prehistory_scene.webp', 'Book 1 · प्रागैतिहासिक बस्ती — प्रतिनिधि पुनर्निर्माण'),
    ('rassetu_b1x_painting_scene.webp', 'Book 1 · लघुचित्र कार्यशाला — प्रतिनिधि दृश्य'),
    ('rassetu_b1x_craft_scene.webp', 'Book 1 · ब्लॉक-प्रिंटिंग कार्यशाला — प्रतिनिधि दृश्य'),
    ('rassetu_b1x_folk_music_scene.webp', 'Book 1 · लोकसंगीत — प्रतिनिधि दृश्य'),
    ('rassetu_b5_ecosystem_foodweb.webp', 'Book 5 · पारिस्थितिकी तंत्र'),
    ('rassetu_b5_renewable_energy.webp', 'Book 5 · ऊर्जा स्रोत'),
    ('rassetu_b3_freedom_movement.webp', 'Book 3 · राष्ट्रीय आंदोलन के पड़ाव'),
    ('rassetu_b4_preamble_constitution.webp', 'Book 4 · उद्देशिका के मूल्य'),
    ('rassetu_b5_gdp_price_indicators.webp', 'Book 5 · आर्थिक संकेतक'),
    ('rassetu_b1_fort_landscape_scene.webp', 'Book 1 · पहाड़ी दुर्ग का दृश्य'),
    ('rassetu_b1_folk_dance_scene.webp', 'Book 1 · घूमर-प्रेरित नृत्य दृश्य'),
    ('rassetu_b2_aravalli_landscape_scene.webp', 'Book 2 · अरावली का भू-दृश्य'),
    ('rassetu_b3_salt_march_scene.webp', 'Book 3 · नमक सत्याग्रह से प्रेरित दृश्य'),
    ('rassetu_b3_harappan_sites_planning.webp', 'Book 3 · हड़प्पाई स्थल और नगर-योजना'),
    ('rassetu_b3_harappan_scene.webp', 'Book 3 · हड़प्पाई सड़क और जल-निकास — प्रतिनिधि पुनर्निर्माण'),
    ('rassetu_b3_vedic_geography_shift.webp', 'Book 3 · वैदिक भूगोल का क्षेत्रीय बदलाव'),
    ('rassetu_b3_mahajanapada_magadh.webp', 'Book 3 · महाजनपद और मगध का उत्कर्ष'),
    ('rassetu_b3_buddhism_jainism_compare.webp', 'Book 3 · बौद्ध और जैन परंपराएं'),
    ('rassetu_b3_maurya_saptanga_edicts.webp', 'Book 3 · मौर्य राज्य-सिद्धांत और शासन'),
    ('rassetu_b3_gupta_harsha_knowledge.webp', 'Book 3 · गुप्त–हर्ष ज्ञान परंपराएं'),
    ('rassetu_b3_south_india_governance.webp', 'Book 3 · दक्षिण भारत और चोल स्थानीय शासन'),
    ('rassetu_b3_chola_town_scene.webp', 'Book 3 · दक्षिण भारतीय मंदिर-नगर — प्रतिनिधि दृश्य'),
    ('rassetu_b3_delhi_sultanate_system.webp', 'Book 3 · दिल्ली सल्तनत की संस्थाएं'),
    ('rassetu_b3_vijayanagara_bahmani_1565.webp', 'Book 3 · विजयनगर, दक्कन और 1565'),
    ('rassetu_b3_mughal_mansabdari_dahsala.webp', 'Book 3 · मनसबदारी और दहसाला'),
    ('rassetu_b3_bhakti_sufi_network.webp', 'Book 3 · भक्ति और सूफी परंपराएं'),
    ('rassetu_b3_european_expansion.webp', 'Book 3 · यूरोपीय व्यापार से औपनिवेशिक विस्तार'),
    ('rassetu_b3_revolt_1857_centres.webp', 'Book 3 · 1857 के चयनित केंद्र'),
    ('rassetu_b3_revolt_1857_scene.webp', 'Book 3 · 1857-प्रेरित दृश्य — प्रतिनिधि चित्रण'),
    ('rassetu_b3_reform_movements.webp', 'Book 3 · सामाजिक-सुधार आंदोलन'),
    ('rassetu_b3_early_nationalism.webp', 'Book 3 · आरंभिक राष्ट्रवाद के पड़ाव'),
    ('rassetu_b3_revolutionary_networks.webp', 'Book 3 · क्रांतिकारी गतिविधियों के केंद्र'),
    ('rassetu_b3_peasant_tribal_movements.webp', 'Book 3 · किसान और जनजातीय आंदोलन'),
    ('rassetu_b3_transfer_of_power.webp', 'Book 3 · कैबिनेट मिशन से सत्ता-हस्तांतरण'),
    ('rassetu_b3_princely_integration_reorg.webp', 'Book 3 · रियासतों का एकीकरण और पुनर्गठन'),
    ('rassetu_b4_constituent_assembly_scene.webp', 'Book 4 · संविधान सभा का प्रतिनिधि दृश्य'),
    ('rassetu_b5_agriculture_market_scene.webp', 'Book 5 · कृषि और स्थानीय बाजार'),
  ];
  int _selected = 0;

  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(title: const Text('RASSetu • अध्ययन ग्राफिक्स')),
        body: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 760),
            child: Column(children: [
              Padding(
                padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
                child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      const Text('RAS पुस्तकों के प्रतिनिधि चित्र',
                          style: TextStyle(fontSize: 23, fontWeight: FontWeight.bold)),
                      const SizedBox(height: 5),
                      const Text('99 graphics across Books 1–6 · Select and inspect'),
                      const SizedBox(height: 12),
                      DropdownButtonFormField<int>(
                        initialValue: _selected,
                        isExpanded: true,
                        decoration: const InputDecoration(
                            labelText: 'विषय चुनें', border: OutlineInputBorder()),
                        items: List.generate(
                            _graphics.length,
                            (i) => DropdownMenuItem(
                                value: i, child: Text(_graphics[i].$2))),
                        onChanged: (value) {
                          if (value != null) setState(() => _selected = value);
                        },
                      ),
                    ]),
              ),
              Expanded(
                child: Center(
                  child: ConstrainedBox(
                    constraints: const BoxConstraints(maxWidth: 760),
                    child: ListView(
                      padding: const EdgeInsets.fromLTRB(16, 0, 16, 28),
                      children: [
                        Text(_graphics[_selected].$2,
                            style: Theme.of(context).textTheme.titleLarge),
                        const SizedBox(height: 12),
                        InteractiveViewer(
                          minScale: 1,
                          maxScale: 5,
                          child: Image.asset(
                              'assets/images/${_graphics[_selected].$1}',
                              fit: BoxFit.contain),
                        ),
                        const SizedBox(height: 12),
                        const Text(
                          'चित्र में दिया शीर्षक और टिप्पणी पढ़ें: दृश्य-चित्र प्रतिनिधि हैं; schematic और वैचारिक आरेख पैमाने पर नहीं।',
                          textAlign: TextAlign.center,
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ]),
          ),
        ),
      );
}
