class constant:
    getParentData = ['ParentId','ParentFirstName','ParentLastName','ParentMobile','ParentRelationId','ParentRelation','ParentEmail']
    
    getActivityPlans=['actPlanId','thumbnail','title','description','areaAge','youNeed','filePath','fileType','article']
    
    AllCateg=['Id','Icon','Value']
    
    getActivitydtl=['Id','categoryId','activityTitle','activityThumbnail','activityDesc','activityHtml','activityFilePath','activityFileType']
    
    editChildDtl=['Id','MemberId','Name','DOB','Gender','Mobile','BloodGroup','Allergies','PreMeditation','ProfilePath','Relation','Address','Country','State','Zip','Abha','IdentityType','IdentityNumber','City']
    
    editFamilyDtl=['Id','MemberId','Name','DOB','Gender','Mobile','BloodGroup','Allergies','PreMeditation','ProfilePath','Address','Country','State','Zip','Profession','PrefferedLanguage','City']

    getFamilyDtl=['Id','MemberId','Name','DOB','DOB1']

    getServiceDoctors=['DoctorId','Name','Fees','ProfilePic','Category']
    
    serviceDoctorDetails=['DoctorId','Name','Fees','ProfilePic','Category','MedicalDegree','Registration','PracticingSince','MedicalExpertise','AwardRecognitions','Languages']

    getServices=['Id','Heading','Description']

    getUploadedFile = ['ID','Path','Patient Name','File Name','Add Date','DocName']
   
    getAppointment=['Id','memberId','Name','DOB']
    
    getAppointmentDetails=['Id','topicName']
    
    DevelopmentDropdown = ['key', 'label']

    T_AssessmentForms = ['FormId', 'FormTitle']

    T_Assessmentanswers = ['TAID', 'TA_Answers']

    getBranch = ['key', 'label']

    genderDropdown = ['key', 'label']

    bloodgroupDropdown = ['key', 'label']
    
    Childdtl = ['Id', 'Name']
    
    T_Articles = ['Id','articleTitle','articleThumbnail','articleDesc','articleHtml']
    
    getAllArticles = ['Id','articleTitle','articleThumbnail','articleDesc','articleHtml']
    
    getAllArticlesDtl = ['Id','articleTitle','articleThumbnail','articleDesc','articleHtml']

    getVideoes = ['Id','thumbnail','title','description','article','areaAge','youNeed','filePath','fileType','NoofDays']
    
    getAllVideoes = ['Id','thumbnail','title','description','article','areaAge','youNeed','filePath','fileType','NoofDays']
    
    getAllVideosDtl = ['Id','thumbnail','title','description','article','areaAge','youNeed','filePath','fileType','NoofDays']

    getdailyWits = ['Id','categoryId','activityTitle','activityThumbnail','activityDesc','activityHtml','activityFilePath','activityFileType']
    
    getAllAppointment = ['Id','Pid','Patient','procedure','date','time','doctor','status','ProfilePic']
    
    getUpcomingAppointment = ['Id','Pid','Patient','procedure','date','time','doctor','status','ProfilePic','DoctorId']
    
    getCompletedAppointment = ['Id','Pid','Patient','procedure','date','time','doctor','status','ProfilePic']
    
    getDetailOfAppointment = ['Id','Pid','Patient','procedure','date','time','doctor','status','ProfilePic','ProvisionalDiagnosis','Notes','ReviewDate','Expertise']
    
    getCancelledAppointment = ['Id','Pid','Patient','procedure','date','time','doctor','status','ProfilePic']

    getInvoicePdf = ['InvoiceNo','Date','InvoiceTotal','Balance','Description','TotalPayable','discountPercent',
                     'CGST','SGST','AmountPaid','Name','UHID','DOB','Procedure']
    
    getPrescriptionDtl = ['visitId','visitType','Procedure','DOB','AppointDate','Name','UHID','DoctorName','Branch']    
    
    Prescrip = ['MP_medication','MP_type','MP_route','MP_times','MP_duration','MP_dosage','MP_comments']

    getConditions=['Id','Heading','Description']

    getDetailedViewInvoice = ['InvoiceNo','Date','bankName','Card','CardType','Cash','CGST','SGST','doctorName','Discount','discountPercent',
                              'DiscountReason','Cheque','Comments','DueBalance','InvoiceTotal','invoiceType','lastDigits',
                              'Online','Prepaid','TotalPayable','Upi','AmountPaid','ServiceId','SettleInvoice','MainInvoiceNo',
                              'TotalAmount','PaidByPartner','PaidByPatient','TotalSessions','UsedSession','PaymentMode','InvoiceType',
                              'MedicineDetails','PartnerOrgId','ServiceName','AppointmentId','M_Branch_MBID','M_Patient_MPID',
                              'UHID','Name','DOB','PartnerOrgName','MPP_PackageId','MPP_PackagePrice','MPP_PackageName','Branch']

    ProvisionalDiagnosisReport = ['ProvisionalDiagnosis','AppointmentId','ICDCode','ICDDescription','Date']
    
    SessionNotesReport = ['Started','AppointmentId','todayfeel','dotoday','Notes','Date']
    
    VisitReasonReport = ['ID','Informed By','Present Concerns','Appointment Id']
    
    PastHistoryReport = ['ID','Appointment Id','Past Medications']

    PrenatalHistoryReport = ['ID','Appointment Id','Mother Conception','Mother Pregnancy','History Abortions','Gestational Diabetes',
                               'Neurological Disorder', 'Physical Emotional','Inompatibility','Jaundice','Seizures','TraumaInjury',
                               'Bleeding pregnancy','Adequate Nutrition','Infections','Smoking','Observations']

    PatientBirthHistoryReport = ['ID','Appointment ID','Mother Health','Delivery Type','Type of Delivery','Delivery Location',
                                   'Multiple Pregnancies','Complication Pregnancy','Child Birth','Child Birth Week','Birth Weight',
                                   'Birth Cry','Neonatal Condition','Special CareAny','Any Medical Events','Congenital','Observations']

    DevelopmentalHistoryReport = ['ID','Appointment ID','HoldUp HeadAge','Rollover age','Sit Age','Stand Alone Age','Walk Age','Talk Age',
                                    'Toilet Train Age','Feed Age','Dresshim Age','Observations']
    
    SpeechDevelopmentHistoryReport = ['ID','Appointment ID','Vocalization','Babbling','First Word','Phrases','Simple Sentences','Observations']
    
    socialhistoryReport = ['ID','Appointment ID','Social History']
    
    medicalhistoryReport =['ID','Appointment ID','Medical History']

    familyhistoryReport =['ID','Appointment Id','Family type','Consanguinity','Family History']
    
    educationhistoryReport =['ID','Appointment Id','Education History']
    
    GeneralExamReport =['ID','Appointment Id','Height','Weight','Head Circumference','Observations']

    VitalsExamReport =['ID','Appointment Id','Blood Pressure','Pulse Rate','Respiratory Rate','Temperator']

    SystemicExamReport =['ID','Appointment Id','Observations']

    STOroperipheralExam =['ID','Appointment Id','Lips Appearance','Lips Movements','Tongue Appearance','Tongue Movements','Teeth Appearance','Teeth Movements',
                                  'Hard Palate Appearance','Soft Palate Appearance','Soft Palate Movements','Uvula Appearance','Uvula Movements','Mandible Appearance','Mandible Movements','Drooling','Blowing','Biting','Sucking','Swallowing','Observations']

    STArticulationSpeechIntelligibilityReport =['ID','Appointment Id','Noonecan','memberscan','Strangerscan','Observations']

    STArticulationVoiceReport =['ID','Appointment Id','Pitch','Loudness','Quality','Observations']

    CognitivePrerequitesReport =['ID','Appointment Id','Imitation','Objectpermanence','Timeconcept','Colourconcept','Moneyconcept','Sequencing','Matching','Meanendrelationship','Observations']

    STVerbalCommunication =['ID','Appointment Id','Expression','Comprehension','Observations']

    STNonVerbalCommunicationReport =['ID','Appointment Id','Expression','Comprehension','Observations']

    OTHandFunctionsReport =['ID','Appointment Id','Hand Dominance','Hand Preference','Reach Forward','Reach Backward','Reach Lateral','Reach Downward','Grasp UlnarPalmar','Grasp Palmar',
                              'Grasp RadialPalmar','Grasp RadialDigital','Grasp InferiorPincer','Reach Upward','Grasp NeatPincer','Grasp Palmarsupinate','Grasp Digitalpronate','Grasp Statictripod','Grasp Dynamictripod','Prehension PadtoPad','Prehension TiptoTip','Prehension PadtoSide']

    OTNonEquilibriumCoordinationReport =['ID','Appointment Id','Fingertonose','Fingertotherapistfinger','Fingertofinger','Alternatnosefinger','Fingeropposition','Massgrasp',
                                           'Pronationsupination','Reboundtest','Tappinghand','Tappingfeet','Pointingandpastpointing','Alternateheeltokneeheeltoe','Toetoexaminersfinger','Heeltoshin','Drawingacircle','Fixationorpositionholding']

    OTEquilibriumCoordinationReport =['ID','Appointment Id','Standingwithnormalbaseofsupport','Standingwithnarrowbaseofsupport','Standingintandemposition','Standingononefeet','Perturbation','Standinginfunctionalreach','Standinglateralflexionofthetrunktoeachside','Tandemwalking','WalkingInastraightline','Walksidewaysbackwards','Walkinhorizontalvertical','Marchinplace','Startstopabruptly',
                                        'Walkandpivotincommand','Walkincircle','Walkonheelsandtoes','Turnsoncommand','Stepoveraroundobstacles','Stairclimbingwithhandrails','Jumpingjacks','Sittingontherapybal']

    OTCognitionAndPerceptionReport =['ID','Appointment Id','Praxis','Rightleftdiscrimination','Fingerindentification','Orientationtoperson','Orientationtoplace',
                                       'Conceputalseriescompletion','Selectiveattention','Focusedattention','Spatialperception','Visualmemory','Verbalmemory','Identificationofobjects','Proverbinterpretation','Randomlettertest','Overlappingfigures']

    OTSensoryExamReport =['ID','Appointment Id','Visual tracking','Choreiform movements','Tremor','Exaggerated associated','Graphesthesis','Stereognosis','Weight bearing hands','Prone extension pattern']

    OTSensoryProfileReport =['ID','Appointment Id','Observations']

    AddtionalinfoReport =['ID','Appointment Id','Observations']

    PTFunctionalAbilitiesReport =['ID','Appointment Id','Gross Motor','Fine Motor','Communication Speech','Feeding','Playskills','ADL']

    PTFunctionalLimitationsReport =['ID','Appointment Id','Gross Motor','Fine Motor','Communication Speech','Feeding','Playskills','ADL']

    PTPosturalSystemAlignmentReport =['ID','Appointment Id','Head Neck','Shoulder Scapular','Shoulder and Scapular','Shouldern Scapular','Ribcage and Chest','Trunk',
                                        'Trunks','Pelvic Complex Right','Pelvic Complex Left','Hipjoint Abduction','Hipjoint Adduction','Hipjoint Rotation','Symmetrical','Assymetrical','Observations']
    
    PTPosturalSystemBOSReport =['ID','Appointment Id','Base of Support']

    PTPosturalSystemCOMReport =['ID','Appointment Id','Center of Mass','Within support','Strategies posture']

    PTAnticipatoryControlReport =['ID','Appointment Id','Canchildanti','Observations']

    PTPosturalCounterbalanceReport =['ID','Appointment Id','Observations']

    PTPosturalSystemImpairmentsReport =['ID','Appointment Id','Muscle Architecture','Anycallosities','Anyother specific posture','Observations']

    PTMovementSystemReport =['ID','Appointment Id','Canthey overcome','How do','Strategies used']

    PTMovementStrategiesReport =['ID','Appointment Id','Childgenerallyperformsactivitie','CanperformLateralweightshifts','CanperformLateralweightshiftsleft',
                                   'CanperformDiagonalweightRight','CanperformDiagonalweightLeft','CanperformneckthoracicspineRight','CanperformneckthoracicspineLeft','HowarethedissociationsPelvicfemoral','HowaredissociationsInterlimb','HowthedissociationsScapulohumeral','HowthedissociationsUpperLowerbody']
    
    PTRangeSpeedofMovementReport =['ID','Appointment Id','Range Speed Movement','at Trunk','Extremities']

    PTStabilityMobilityReport =['ID','Appointment Id','Mobility Strategies']

    PTMovementSystemImpairmentReport =['ID','Appointment Id','Excessive movement','movement StaticPostures','Integration of PostureMovement','Balance Transitions','Accuracy of Movements','Observations']
    
    PTRegulatorySystemReport =['ID','Appointment Id','Affect','Arousal','Attention','Action','Observations']

    PTNeurometerSystemReport =['ID','Appointment Id','Initiation','Sustenance','Termination','Control and Gradation','Contraction Concentric',
                             'Contraction Isometric','Contraction Eccentric','Reciprocal Inhibition','Isolated work','Dynamic stiffness','Extraneous Movement','Observations']
    
    PTMusculoskeletalSystemReport =['ID','Appointment Id','Muscle Endurance','Skeletal Comments','Tardieu ScaleTR1','Tardieu ScaleTR2','Tardieu ScaleTR3',
                                      'Tardieu ScaleHamsR1','Tardieu ScaleHamsR2','Observations']
    
    PTSensorySystemReport =['ID','Appointment Id','Modulation Issues','Visual system','Auditory system','Auditory system Response','Vestibular system','Somatosensory system','Oromotor system','Olfactory system','Observations']
    
    PTCognitiveSystemReport =['ID','Appointment Id','Intelligence','Memory','Adaptability','Motor Planning','Observations']
   
    ReceptiveLanguageAssessmentReport =['ID','Appointment Id','Comprehends sounds','Comprehends loud','Comprehends categorizesounds','Comprehends animalsounds',
                                          'Comprehends fruitsname','Comprehends colorsname','Comprehends animalname','Comprehends vegetablename','Comprehends shapesname',
                                          'Comprehends bodyparts','Comprehends vehiclenames','Understandingrhymes','Respondscorrectly','Identifiessounds','Actsoutcommands','Comprehends stepscommands','Understandinggreeting','Understanding']
    
    ExpressiveLanguageAssessmentReport =['ID','Appointment Id','Imitates environmental sounds','Imitates loud and softsounds','Imitates lexical categories','Imitates colors name','Imitates body parts','Imitates singing and phrases',
                                           'Imitates alphabets AtoZ','articles','Watches','Imitates counting','Claps','Respondstosinglesigns','Imitates socialgreetings','Occassionallytrytoimitate','Imitates commonsyllables']
    
    ConnersParentRatingScaleReport =['ID','Appointment Id','Scores','Tscores','Range','Observations']
    
    
    SpecialEdassessmenttwoyearsReport =['ID','Appointment Id','Respondstoname','Makeseyecontact','Respondstolightandsoundtoys','canmoveeyesupanddown','canmoveeyesleftandright','repeatswords',
                                           'knowsidentificationofnumber','canrollpoundandsqueezeclay','vocabularyMom','vocabularyDad','Vocabularydog','vocabularycat','vocabularytree','vocabularytable','vocabularychair','vocabularycow',
                                           'vocabularycrayons','vocabularybus','vocabularycar','vocabularybook','vocabularyapple','vocabularybanana','vocabularybottle','Candostacking','canmaketower','respondstobubbles','Identifieshappyandsad',
                                           'Knowsshapes','knowscolors','knowsanimals','knowsvehicles','knowsbodyparts','knowsidentificationofalphabets','knowsmoreorless','knowsbigandsmall','knowsnearandfar','canidentifhisorher','canidentifybag','canidentifyshoes','canidentifybottle']
    SpecialEdassessmentthreeyearsReport =['ID','Appointment Id','respondstoname','makeseyecontact','cansitformins','canmoveeyesupanddown','canmoveeyesleftandright','cananswerfullname','vocabularybodyparts','canfollowstepsinstruction','cananswerold','cananswerwhatsyourmothersname','cananswerwhichisyoufavoritecolour',
                                            'canfixpiecepuzzle','vocabularyshapescircle','vocabularycolors','vocabularywild','Vocabularyfruits','canfollowstepinstruction','cansingrhymes','cangiveanswerseeinsky','cangiveanswerswiminwater','cangiveanswerseeontree','knowsidentificationofalphabets','knowsidentificationofnumbers','Canholdapencilcrayon'
                                            ,'canscribble','cancoloringivenshape','cantearandpaste','canidentifyemotionshappy','canidentifyemotionssad','canidentifyemotionsangry','canidentifyemotionsupset']
    
    SpecialEdassessmentthreefouryearsReport =['ID','Appointment Id','doesrespondtonamecall','doesmakeseyecontact','initiatesinteractiontoward','cansitformins','understandinstructionslikestand','getthatputthere',
                                                'givemegetthis','runwalkjump','lookdownup','cananswerwhatis','cananswerfavoritecolour','canfixpiecepuzzle','vocabularyshapes','vocabularycolors','vocabularywild','vocabularyfruits','vocabularybodyparts',
                                                'Canunderstandpositions','cansingrhymes','canunderstandstories','canWhatquestions','canidentifybasicobjects','canholdacrayonpencil','canmaketower','canimitate','canplaydoughballs','canheshethrow','canrecognisealphabet','Canrecognisenumerals','cancolourgivenshape']
    
    SpecialEdassessmentfouryearsReport =['ID','Appointment Id','respondnamecall','makeseyecontact','interactiontowardothers','cansitformins','cananswerwhatname','answerfavoritecolour','canfixpiecepuzzle','vocabularyshapes','vocabularycolors',
                                           'vocabularywild','vocabularybody','Vocabularyfruits','canunderstandpositions','cansingrhymes','canunderstandstories','replyWhatquestions','identifybasicobjects','holdcrayonpencil','canimitate','doughmakeballs','canthrow','recognisealphabets','recognisenumerals','cancolourshape']
    
    SpecialEdassessmentsevenyearsReport =['ID','Appointment Id','putneedsminimalassistance','eathandsonly','fixasandwich','givefirstlastname','cangiveaddress','awareofemotions','canzipper',
                                            'independentlyassistanct','asksmeaningfulquestions','tellsstorieswords','Doestellage','canobeysimplecommands','readsimplewords','writesimplewords',
                                            'namethingsaround','alternatesfeetupdownstairs','pedaltricycle','catchandthrowball','towersmallblocks','doughmakeballs','tieshoes','holdpencilproperly','drawsanyshape','usescissorscutshape']
    
    viewOTNonEquilibriumCoordinationReport =['ID','Appointment Id','Fingertonose','Fingertotherapistfinger','Fingertofinger','Alternatnosefinger','Fingeropposition','Massgrasp',
                                           'Pronationsupination','Reboundtest','Tappinghand','Tappingfeet','Pointingandpastpointing','Alternateheeltokneeheeltoe','Toetoexaminersfinger','Heeltoshin','Drawingacircle','Fixationorpositionholding']
    
    DSMVASDCriteriaReport= ['Id','persistentDeficit','persistentDeficitComment','restrictedRepetitive','restrictedRepetitiveComment','symptomsMust','symptomsMustComment','symptomsCause','symptomsCauseComment','theseDisturbances','theseDisturbancesComment','question7','question7Comment']
    
    viewPTPosturalSystemImpairments =['ID','Appointment Id','Muscle Architecture','Anycallosities','Anyother specific posture','Observations']

    viewHARSAssessmentForm =['ID','Appointment Id','anyAnxiousMood','AnyTensionFeeling','AnyFearsfeeling','AnyInsomnia','AnyIntellectual','AnyDipressedMood','AnySomaticpains',
                           'AnySomaticWeekness','AnyCardiovascular','AnyRespiratory','AnyGastrontedtinal','AnyGenitourinarySymptoms','AnyAutonomicSymptoms','AnyBehaviouratInterview']
    
    viewPHQAssessmentForm =['ID','Appointment Id','AnyPleasure','AnyDepression','AnyTrouble','Anytiredness','AnyOvereat','Anybadfeel','TroubledbyAnything','MovingAroundAlot','AnyHurtYourself']
    
    viewHRDSAssessmentForm =['ID','Appointment Id','HRDSDepressedMood','HRDSFeelingGuilt','HRDSSuide','HRDSInsomnia','HRDSMidNight','HRDSEarlyMorning',
                             'HRDSWork','HRDSRetardation','HRDSAgitation','HRDSPsychic','HRDSAnxietySomatic','HRDSSomatic','HDRSGeneralSomatic','HDRSLossOfLibido','HDRSHypochondriasis','HDRSLossofWeight','HDRSInsight']
    
    getBroadcastdtls = ['Id','Title','Message']

    viewCKADHDScreening = ['ID','Appointment Id','mistakesinschoolwork','playactivities','spokentodirectly','failstofinishschool','difficulttoorganize','reluctantlyengages','losethings',
                           'distractedbyextraneous','dailyactivities','maintainalertness','squirmsinseat','seatinclassroom','climbsexcessively','leisureactivities','drivenbyamotor','Talksexcessively','answersbefore',
                           'difficulttosit','symptomspresent','symptomsleading','symptomsaffecting']

    viewCKFU= ['ID','Appointment Id','Noncontextual','Picapresent','Responsetosound','Indicatepottyneeds','Givesattentionwhere','Indicateurineneeds',
               'Walksbetweenpeople','SleepProblemsinitiation','DoesNotUnderstandtone','Overtlysensitivetoweird','Isnotimaginativebad',
               'Overtlysensitivetotextures','Overtlysensitivetosmell','Toewalkingpresent','Notablecommunicatefeelings','unusualeyecontact',
               'Likesshadowssideward','Notabletoimitateothers','Doesnotplayproperly','Doesnotoffercomfort','Difficultyrelatingtoadults',
               'Difficultyrelatingtopeers','Doesnotrespondappropriately','Wandersaimlessly','Toosillyorlaughs','Difficultyanswering',
               'Talkswithunusualtone','Emotionallydistant','Movingincirclespresent','Seemsmorefidgety','Wouldratherbealone',
               'Likesparallelplay','Avoidsstartingsocial','Staresorgazesoff','Feedingchewingisaconcern','Hyperactivitypresent',
               'Behavesinwaysthat','Showsunusualsensory','Thinksortalksabout','Hasanunusuallynarrow','Doesextremelywell',
               'Hasrepetitiveodd','Dislikesbeing','DoesntrespondtoNo']

    viewCKDevelopScreening=['ID','grossmotoryes','grossmotorno','finemotoryes','finemotorno','selfhelpyes','selfhelpno','problemsolvingyes','problemsolvingno','emotionalyes','emotionalno',
                            'receptiveyes','receptiveno','expressiveyes','expressiveno','socialyes','socialno']
    
    
    viewCKASAssessmentForm = ['']
    viewCKADHDScreening = ['ID','A19','B1018','C1921']


    getPatientDetailFromAppointment = ['AppointId','Pid','date','Doctor Name','Branch','Gender','Email','UHID','DOB','Address','Mobile','Patient']
    
    viewVinelandSocialMaturityScaleReport =['ID','Appointment Id','Social Age','Social Quotient','Observations']
    
    viewChildhoodAutismRatingScaleReport =['ID','Appointment Id','Relating to People','Imitation','Emotional Response','Body Use','Object Use','Daptation Change','Visual Response','Listening Response','Taste Smell Use','Fear or Nervousness','Verbal','Non Verbal','Activity Level','Consistency Response','General Impression','Concluding Remark']
    
    viewIndianScaleAssessmentAutismReport = ['ID','Appointment Id','SOCIAL RECIPROCITY','EMOTIONAL RESPONSIVENESS','SPEECH COMMUNICATION','BEHAVIOUR PATTERNS','SENSORY ASPECTS','COGNITIVE COMPONENT','Final Comment']
    
    viewSequinFormBoardTestReport =['ID','Appointment Id','Mental Age','IQ','Shortest Time','Total Time','Corresponds Mental Age','Suggesting Intellectual Functioning']
    
    viewRavenStandardProgressiveMatricesReport =['ID','Appointment Id','Raw Score','Percentile','Grade','Interpretation','Corresponds To']
    
    viewGeselsDrawingTestofintelligenceReport =['ID','Appointment Id','Mental Age','IQ','Mental Age Months','Mental Age Years','IQ of','Depicting']
    
    viewDevelopmentalProfileReport =['ID','Appointment Id','Physical Score','Physical Category','Physical Age Equivalent','Adaptive Behavior Score','Adaptive Behavior Category','Adaptive Behavior Age Equivalent','Social Score','Social Category','Social Equivalent','Cognitive Score','Cognitive Category','Cognitive Age Equivalent','Comm Standard Score','Comm Category','Comm Age Equivalent','General Dev Score','General Dev Category','General Age Equivalent']
    
    viewPerceptualAndVisualMotorAbilityReport = ['Appointment Id','VisualDiscr','VisualDiscrComments','VisualMemoryTest','VisualMemoryTestComments','AuditoryMemory','AuditoryMemoryComments','Attention',
                           'AttentionComments','DoubleNumCancel','DoubleNumCancelComments','Language','LanguageComments','Reading','ReadingComments'
                           ,'Comprehension','ComprehensionComments','Spelling','SpellingComments','WritingAndCopy','WritingAndCopyComments','WritingSkills'
                           ,'WritingSkillsComments','ExpressiveWriting','ExpressiveWritingComments','Copying','CopyingComments','Arithmetic',
                        'ArithmeticComments']
    
    viewWechslerTestReport = ['Appointment Id','SubsetScore','ReadCompStandardScore','ReadCompConfidenceInterval','ReadCompPercentileRank','ReadCompGradeEquivalent','WordReadStandardScore',
                            'WordReadConfidence','WordReadPercentileRank','WordReadGradeEquivalent','EssayCompStandardScore','EssayCompConfidence','EssayCompPercentileRank'
                           ,'EssayCompGradeEquivalent','NumOperStandardScore','NumOperConfidence','NumOperPercentileRank','NumOperGradeEquivalent','SpelStandardScore'
                           ,'SpelConfidence','SpelPercentileRank','SpelGradeEquivalent','Comment','MathematicsComment','WrittenExpComment']
    
    viewChildBehaviorChecklistReport = ['Appointment Id','AnxiousScores','AnxiousTscore','AnxiousRange','WithdrawnScores','WithdrawnTscore','WithdrawnRange',
                           'SomaticComplaintScores','SomaticComplaintTscore','SomaticComplaintRange','SocialProblemScores','SocialProblemTscore','SocialProblemRange'
                           ,'ThoughtProblemScore','ThoughtProblemTscore','ThoughtProblemRange','AttentionProblemScore','AttentionProblemTscore','AttentionProblemRange'
                             ,'RuleBreakingBehaviorScore','RuleBreakingBehaviorTscore','RuleBreakingBehaviorRange','AggressiveBehaviorScores'
                             ,'AggressiveBehaviorTscore','AggressiveBehaviorRange','Comment']
    
    viewChildAnxietyRelatedDisordersReport =['ID','Appointment Id','PanicDisorderScore','GeneralizedAnxietyDisorderScore','SeparationAnxietyDisorderScore'
                                           ,'SocialAnxietyDisorderScore','SchoolAvoidanceScore','AnxietyDisorderScore','Comment']
    
    viewHumanTreePersonTestReport = ['ID','Appointment Id','findings','indicators','comment']
    
    viewHumanFormDrawingtestReport = ['ID','Appointment Id','findings','indicators','comment']

    viewDSMVCriteriaReport =['ID','Appointment Id','ACriteria','ACriteriaComment','BCriteria','BCriteriaComment','CCriteria','CCriteriaComment'
                           ,'DCriteria','DCriteriaComment','Question5','Question5Comment','Question6','Question6Comment','Question7','Question7Comment']
    
    viewEpidemiologicalStudiesDepressionScaleReport =['ID','Appointment Id','NotAtAllScore','ALittleScore','SomeScore','ALotScore','TotalRawScore','Comment']

    viewMalinIntelligenceScaleforIndianChildrenReport = ['ID','Appointment Id','InformationTestScores','PictureTestScores','GeneralTestScores','BlockDesignTestScores',
                                                     'ArithmeticTestScores','ObjectScores','VocabularyTestScores','MazeTestScores','AnalogiesScores',
                                                     'CodingScores','VQ','PQ','FullScaleIQ','Comment']

    viewNICHQVanderbiltADHDParentReport =['ID','Appointment Id','Inattention Score','Hyperactivity Score','Combined Score','Oppositional Score','Conduct Score','Anxiety Score']
    
    viewGrossMotorForm = ['ID','Appointment ID','0-3 Months','grossmotor03no','3-6 Months','grossmotor36no'
                          ,'6-9 Months','grossmotor69no','9-12 Months','grossmotor12no','12-18 Months',
                          'grossmotor1218no','18-24 Months','grossmotor1824no','24-30 Months','grossmotor2430no',
                          '30-36 Months','grossmotor3036no','36-42 Months','grossmotor3642no','42-48 Months',
                          'grossmotor4248no','48-54 Months','grossmotor4854no','54-60 Months','grossmotor5460no']
    
    viewFineMotorForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
    
    viewSelfHelpForm = ['ID','Appointment ID','0-3 Months','selfhelp03no','3-6 Months','selfhelp36no'
                          ,'6-9 Months','selfhelp69no','9-12 Months','selfhelp12no','12-18 Months',
                          'selfhelp1218no','18-24 Months','selfhelp1824no','24-30 Months','selfhelp2430no',
                          '30-36 Months','selfhelp3036no','36-42 Months','selfhelp3642no','42-48 Months',
                          'selfhelp4248no','48-54 Months','selfhelp4854no','54-60 Months','selfhelp5460no']
    
    viewProblemSolvingForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
    
    viewEmotionalForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
    
    viewReceptiveForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
    
    viewExpressiveLanguageForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
    
    viewSocialSkillsForm = ['ID','Appointment ID','0-3 Months','finemotor03no','3-6 Months','finemotor36no'
                          ,'6-9 Months','finemotor69no','9-12 Months','finemotor12no','12-18 Months',
                          'finemotor1218no','18-24 Months','finemotor1824no','24-30 Months','finemotor2430no',
                          '30-36 Months','finemotor3036no','36-42 Months','finemotor3642no','42-48 Months',
                          'finemotor4248no','48-54 Months','finemotor4854no','54-60 Months','finemotor5460no']
