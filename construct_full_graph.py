import grapher

grapher.hops = 27 # Kālidāsa needs 26

grapher.exclude_list = []

main_subgraph_seed = ['41324']

seeds_for_double_digit_node_subgraphs = ['41358', '95157', '93860', '93577', '41305', '89693', '89117', '93987', '97226', '41816', '41613', '41573', '101471', '91283', '90533', '41276', '105849', '41270', '95253', '41292', '95246', '42495']

seeds_for_subgraphs_with_3_to_9_nodes = ['41413', '94687', '94401', '89073', '93218', '88034', '88358', '88933', '41226', '41225', '41260', '90921', '94423', '92072', '95783', '94701', '88116', '90780', '95345', '94121', '93155', '94388', '94841', '90739', '93926', '94230', '94059', '93089', '91485', '93933', '93574', '93181', '93726', '94202', '93178', '92074', '94621', '94142', '94674', '92998', '41710', '41716', '41369', '107388', '93193', '94163', '89373', '95321', '90401', '95927', '41643', '93430', '94183', '96599', '90507', '92111', '94784', '94697', '90707', '88713', '89660', '92588', '93440', '89805', '90473', '88187', '94995', '41651', '96262', '41478', '97355', '41802', '92223', '92591', '91670', '92585', '92081', '90751', '91279', '94816', '90468', '41810', '95949', '93801', '89131', '95343', '41480', '41466', '42129', '42136', '107166', '94295', '94729', '97239', '92575', '100891', '93069', '41633', '91211', '91467', '94837', '89796', '95741', '103777', '91894', '90856', '97070', '89992', '90247', '89306', '92982', '90695', '42426', '89126', '88558', '89123', '98172', '93063', '94965', '93197', '42455', '41951', '88216', '98192', '41404', '42130', '42535', '88799', '101410', '94915', '95514', '92477', '95087', '94814', '94981', '95787', '95260', '95581', '95114', '94306', '95667', '92596', '94618', '93502', '95528', '94840', '95615', '95348', '105986', '93408', '94152', '88209', '93402', '93065', '94891', '41547', '95134', '99338', '94888', '89611', '94879', '102289', '92816', '90520', '94775', '90517', '88753', '93050', '90504', '98017', '105682', '96418', '41841', '96400', '95508', '95386', '41386', '104040', '42320', '104052', '90461', '92674', '42228', '92707', '96712', '91124', '96476', '88907', '96003', '90039', '95056', '98305', '88033', '89531', '91461', '41498', '42266', '93110', '41502', '42148', '42039', '96015', '42474', '42479', '106582', '94849', '41461', '92162', '100415', '89528', '41382', '41238', '96586', '96273', '93207', '94093', '90452', '41673', '94873', '41820', '102230', '89188', '88864', '96699', '92703', '96041', '90960', '94755', '88922', '95761', '91736', '90966', '92119', '89288', '90798', '96714', '88481', '89881', '41497', '88022', '41886', '102253', '94477', '94588', '94539', '88288', '94110', '95377', '94140', '99966', '95522', '95638', '90571', '90665', '96078', '93948', '95069', '91215', '96082', '41450', '88020', '95173', '42076', '95657', '92058', '96092', '95445', '95030', '96095', '100177', '91731', '41973', '96097', '95371', '93192', '89994', '99440', '41394', '41487', '41299', '42116', '41391', '99378', '92908', '93006', '41399', '94511', '93341', '93158', '90792', '92124', '41956', '95628', '95027', '41374', '41492', '94530', '94829', '103732', '93074', '95749', '41539', '96130', '95333', '90618', '95001', '92924', '91538', '92936', '42481', '96328', '95217', '93210', '94343', '96155', '94627', '91192', '42465', '41389', '41401', '89382', '94769', '102353', '88813', '93562', '102729', '102272', '102424', '102633', '102265', '99250', '95135']

seeds_for_subgraphs_with_2_nodes = ['89291', '95883', '95511', '92233', '95433', '93812', '94646', '95510', '95140', '95248', '42352', '88527', '88067', '41434', '90622', '90334', '95098', '94956', '95409', '95407', '90702', '94887', '95553', '95643', '95477', '95393', '93028', '94685', '94655', '95289', '95251', '97299', '94119', '95412', '95181', '93189', '95303', '92108', '95805', '93810', '94063', '95252', '95543', '91516', '93652', '94851', '94796', '95755', '94219', '93492', '95567', '94116', '95107', '95196', '95330', '94171', '94502', '95186', '95586', '93978', '95062', '95099', '95698', '95201', '93944', '89534', '94019', '95461', '95414', '94993', '92304', '95137', '95339', '95066', '95428', '94292', '95298', '95259', '90741', '93215', '95383', '93539', '41705', '41706', '41719', '41718', '41696', '41676', '95770', '42142', '91520', '41688', '42252', '41813', '95179', '91484', '41691', '95728', '94962', '95512', '97951', '41245', '41222', '41234', '41236', '41552', '94882', '41392', '41475', '95802', '91472', '88433', '94964', '42155', '41408', '95129', '90106', '95086', '42091', '97238', '93107', '42347', '95451', '95467', '93415', '41411', '88721', '93859', '95197', '94967', '94429', '93298', '41473', '94708', '94120', '93281', '95747', '89800', '96544', '42134', '41800', '42420', '98691', '95500', '95245', '97934', '95475', '95580', '91704', '97337', '42301', '42323', '42274', '41811', '42271', '42015', '95478', '95482', '42383', '41875', '42287', '42303', '41431', '96812', '95496', '93222', '95546', '93696', '95100', '89098', '95169', '94846', '93967', '88995', '90591', '94488', '89543', '97885', '95471', '89802', '95152', '42366', '92173', '95520', '98713', '42396', '41437', '42413', '41474', '89745', '42514', '42319', '41344', '90403', '41805', '101209', '101426', '101418', '101441', '101484', '41439', '41854', '100833', '100840', '100957', '90803', '100817', '105742', '101522', '94052', '41583', '92135', '95296', '92717', '41876', '95680', '101531', '91292', '94693', '41807', '42006', '42372', '42355', '94242', '94921', '95256', '42409', '88749', '89641', '94810', '93708', '93633', '95049', '94246', '94445', '95097', '90749', '91274', '100707', '91591', '94822', '95479', '42179', '41739', '91395', '88528', '94789', '90621', '95768', '95235', '95192', '88416', '88437', '91644', '94944', '96450', '99308', '96482', '93797', '92932', '95688', '42411', '42247', '42205', '41373', '42382', '41453', '42009', '94807', '94804', '95645', '94018', '93719', '94157', '94311', '95582', '89436', '94448', '94145', '95695', '94690', '94815', '94571', '95733', '95150', '41494', '41534', '95015', '88493', '96731', '93771', '95463', '94736', '95374', '41895', '89121', '89482', '41674', '88015', '88027', '41599', '95013', '41435', '94909', '96541', '89034', '41350', '94895', '42368', '93443', '95573', '92564', '41808', '41551', '95684', '99058', '95778', '95556', '95476', '88228', '95426', '95697', '99135', '94960', '95727', '95562', '94487', '42518', '95121', '41249', '89429', '42443', '94660', '94943', '96663', '90732', '96570', '95115', '95635', '95686', '94548', '95408', '98084', '42283', '95182', '98185', '98179', '41623', '41440', '91128', '94910', '94877', '41266', '91295', '92034', '93639', '41855', '42174', '88585', '42248', '92151', '90678', '90574', '93597', '108415', '41447', '41784', '96446', '41787', '90398', '93628', '88313', '95497', '95603', '95425', '93742', '95579', '41427', '93643', '99349', '95249', '95619', '94916', '94680', '94147', '91635', '94997', '94745', '105544', '95538', '95081', '41264', '95646', '95073', '93038', '93114', '94678', '94788', '95661', '95021', '95176', '93770', '95269', '95132', '95328', '89217', '93496', '95302', '94852', '89837', '90279', '41368', '95735', '95576', '42034', '88121', '41937', '42311', '41930', '41526', '94126', '41625', '41419', '41536', '41443', '94733', '95054', '92547', '95443', '90595', '42253', '42243', '100418', '93609', '94038', '41495', '107818', '95626', '94174', '90413', '41418', '41237', '97075', '41248', '97064', '96525', '95112', '93764', '95272', '92704', '94667', '97080', '95782', '94746', '91210', '41320', '95319', '95652', '95462', '41678', '41553', '95437', '95172', '42325', '97554', '41445', '42290', '93638', '41436', '41444', '93607', '42442', '94443', '90736', '42384', '96341', '91273', '95113', '94978', '101589', '94760', '90167', '41914', '41730', '41741', '41686', '41728', '90585', '93718', '89568', '101652', '95065', '92109', '95745', '90395', '93772', '95077', '42309', '96641', '94169', '89299', '94365', '101617', '101575', '95636', '101632', '42122', '95116', '101823', '94581', '89792', '91512', '95204', '94505', '95491', '90593', '94984', '89731', '94424', '93634', '94040', '95664', '95128', '94676', '94994', '101853', '42404', '95071', '88434', '41441', '94238', '41873', '42327', '42354', '42139', '95616', '91702', '89032', '42178', '99473', '42120', '95716', '95715', '99180', '42114', '89659', '94762', '95444', '89775', '95286', '95737', '95187', '41806', '41919', '41346', '94683', '41766', '42143', '95612', '94830', '89887', '90942', '94922', '89974', '89518', '88984', '95047', '95189', '94012', '94740', '94057', '93323', '94848', '94878', '95706', '95552', '95151', '95427', '94724', '94428', '95092', '93602', '94647', '42207', '42284', '41675', '90674', '41782', '91463', '94499', '95792', '90941', '95498', '95540', '95391', '95183', '92481', '94983', '88539', '89529', '42151', '42047', '42423', '95023', '94749', '89048', '95455', '89305', '92701', '94351', '95332', '99162', '93706', '95295', '42516', '42470', '89388', '92926', '95175', '94560', '94244', '94977', '94899', '95687', '95147', '42440', '94526', '42449', '94146', '41726', '94688', '108342', '94827', '41433', '42109', '93288', '42441', '94737', '89973', '41798', '100086', '88120', '88019', '88028', '94489', '42477', '94990', '95759', '95798', '90537', '92853', '94592', '94495', '95485', '93625', '95261', '94946', '95365', '90870', '41594', '92181', '89449', '94061', '41422', '93497', '93495', '41430', '88349', '94395', '95119', '89458', '90503', '42216', '41396', '41484', '41345', '91364', '91448', '88761', '89656', '94985', '92597', '94876', '93307', '102178', '41414', '41900', '96331', '94158', '41795', '41827', '42387', '42268', '42361', '42335', '41309', '42278', '42101', '42030', '41893', '42364', '96593', '42046', '42060', '41938', '41834', '41899', '97061', '42107', '42340', '41348', '41680', '41406', '42386', '42519', '95109', '95442', '42040', '94728', '94799', '97248', '95329', '95470', '94653', '95139', '88314', '88017', '94085', '94753', '103484', '94918', '90144', '103625', '89685', '94694', '92473', '90689', '41849', '103493', '95423', '95647', '95666', '89502', '41428', '41785', '95634', '42157', '89535', '94170', '103579', '95420', '93649', '95144', '95379', '103598', '95106', '41407', '95464', '41954', '88053', '90560', '93216', '89536', '42185', '95473', '90963', '95076', '42281', '90467', '88176', '95171', '41420', '41788', '95117', '95019', '94756', '94808', '95198', '90516', '95593', '95036', '94774', '95703', '95257', '94874', '103845', '92171', '95331', '95035', '91225', '94027', '95679', '89643', '42093', '95301', '41786', '95349', '41527', '89777', '92033', '42227', '94861', '95526', '94696', '95270', '95518', '90522', '91465', '96612', '41929', '107221', '94666', '95101', '90987', '88622', '42379', '89907', '94274', '90755', '95675', '94188', '94190', '92595', '93262', '103899', '41410', '94496', '92049', '95005', '94551', '42398', '41421', '91376', '92553', '92712', '103929', '94177', '90994', '94907', '94717', '94835', '103944', '93803', '95085', '94692', '95524', '89873', '104016', '94273', '93650', '95708', '41451', '107771', '41838', '95224', '94750', '93432', '42226', '93697', '92814', '95773', '95004', '95561', '91705', '95725', '95726', '95227', '89427', '94963', '95557', '95610', '92543', '94397', '95050', '94826', '94114', '94945', '94628', '95406', '95103', '95757', '89791', '95145', '92914', '94771', '95381', '95048', '93998', '95577', '95551', '94917', '95267', '95309', '95717', '95709', '95710', '95758', '91473', '95578', '94102', '92913', '92620', '95400', '95340', '95613', '95382', '95208', '98635', '93060', '94831', '95618', '95230', '94751', '42062', '93608', '88928', '95799', '94824', '89428', '94797', '98419', '98881', '95555', '93629', '95466', '95308', '93264', '95250', '98653', '92078', '94725', '89289', '94237', '94559', '95011', '94218', '94159', '90399', '98517', '94988', '95662', '94823', '94832', '94806', '94869', '94818', '95385', '88921', '95665', '91522', '88894', '95280', '98426', '98435', '98443', '88616', '98778', '95111', '95399', '98918', '94800', '88590', '97017', '95642', '94689', '89919', '89387', '89548', '93814', '93590', '94366', '88591', '95623', '95624', '95801', '41731', '42486', '95419', '91536', '90145', '41449', '90588', '97526', '92852', '93263', '95732', '93190', '91178', '95614', '90673', '95771', '93784', '95288', '94989', '94111', '94839', '95375', '98112', '95584', '95568', '89640', '90610', '95421', '95178', '92170', '88757', '90536', '95043', '41489', '41491', '41446', '41765', '41429', '41442', '41376', '41275', '41416', '41952', '41415', '42096', '41400', '41367', '90871', '95670', '94890', '102345', '42156', '95034', '102326', '102332', '95091', '95454', '95589', '95529', '93640', '94933', '95335', '93444', '102748', '94992', '95677', '90246', '94135', '93635', '95501', '94387', '95037', '94118', '95704', '94902', '94705', '102984', '94847', '95052', '93540', '94949', '95531', '95796', '93819', '103145', '95748', '93159', '94979', '95185', '102793', '91748', '95299', '95517', '95205', '94735', '103204', '42463', '102740', '94582', '102716', '97241', '92910', '95282', '90791', '89788', '89799', '41476', '42502', '94189', '102463', '41405', '95170', '102434', '96618', '88029', '90519', '41546', '44720', '93206', '88174', '95653', '91464', '93411', '90737', '93925', '41988', '94718', '88862', '95141', '93778', '93259', '102705', '102662', '91214', '95346', '92035', '94479', '102492', '88545', '95075', '94955', '102547', '89798', '93071', '93412', '41528', '89842', '88208', '94658', '95456', '41267', '96692', '41621', '94575', '95388', '95342', '94659', '95206', '96378', '94112', '93013', '92661', '101861', '96426', '94976', '88388', '88041', '41318', '95122', '94098', '95200', '42234', '41438', '94894', '95067', '94355', '42333', '41366', '41472', '41377', '89033', '95000', '95055', '95142', '42276', '42118', '42085', '42373', '41935', '42405', '93594', '95631', '94758', '95024', '93880', '42088', '92713']

isolate_nodes = ['88179', '95837', '95824', '104418', '105102', '104142', '104344', '104148', '104144', '104161', '105146', '104554', '104173', '105128', '104793', '105081', '104808', '104780', '104826', '104252', '104256', '105153', '104906', '104909', '105157', '104296', '105046', '105164', '105171', '41958', '105236', '41887', '42024', '41771', '95810', '95811', '41779', '42167', '105099', '42407', '104784', '42052', '95813', '88472', '105298', '105288', '105285', '105279', '105319', '105311', '105207', '105323', '108221', '105313', '97266', '95917', '104364', '108229', '96851', '97438', '104463', '41693', '104465', '41704', '41714', '41715', '41713', '41722', '41723', '41721', '41720', '41717', '41700', '41703', '41694', '41695', '41985', '104086', '41698', '41699', '106338', '107361', '88467', '97099', '41911', '104480', '97547', '104482', '88054', '104467', '42337', '42362', '42177', '42112', '42110', '41864', '88266', '105277', '105275', '41843', '41689', '108281', '105325', '88594', '108279', '88056', '41232', '41235', '95815', '104491', '41926', '42121', '95816', '104472', '104470', '104493', '42343', '95924', '104474', '41925', '41791', '105169', '41998', '105077', '42400', '104476', '88466', '104478', '104496', '105327', '41687', '88360', '105774', '41789', '104498', '88222', '42049', '42053', '88351', '95817', '88279', '88070', '42331', '107044', '104294', '105329', '107587', '105209', '104226', '107331', '105212', '88123', '41831', '42213', '88583', '41957', '41781', '105216', '105218', '104370', '105214', '41907', '95809', '41724', '41725', '105220', '108283', '95818', '42406', '95819', '41351', '88414', '88350', '104373', '88408', '42345', '42189', '42520', '42521', '105254', '105224', '42197', '98481', '105222', '108260', '105226', '105228', '108258', '104375', '41971', '104426', '42196', '95820', '89003', '104738', '89004', '105232', '88563', '42016', '104081', '42097', '42023', '88124', '88366', '88125', '95933', '41986', '88126', '42250', '97336', '105257', '42194', '108407', '105234', '41833', '105079', '42342', '42258', '42080', '41997', '41832', '41945', '89005', '42025', '105239', '105261', '105243', '105241', '105266', '42422', '41920', '105245', '41959', '104383', '41891', '104391', '41976', '104389', '104432', '41769', '104387', '42169', '42166', '42285', '105247', '42186', '42523', '105249', '104396', '104443', '105083', '104082', '105199', '104435', '104394', '42296', '104439', '42241', '88175', '95937', '104450', '104448', '42302', '42140', '42020', '42306', '42089', '41912', '95822', '97724', '97619', '95821', '95823', '41936', '95944', '104424', '104570', '42313', '104686', '104300', '42082', '42232', '41868', '104084', '41773', '42391', '41979', '42172', '42348', '42288', '104410', '41857', '41943', '41882', '42014', '42056', '103330', '104408', '42377', '42308', '105173', '42222', '105113', '104248', '42236', '42029', '41768', '41767', '41949', '42329', '42334', '104177', '41977', '41975', '42137', '104962', '104420', '104414', '104416', '104950', '105085', '104412', '90549', '98730', '107584', '41861', '88570', '42273', '97346', '42188', '42221', '95825', '105273', '105691', '105271', '42251', '105269', '89006', '105087', '105093', '104288', '104458', '104124', '105201', '42419', '42418', '42055', '105118', '42204', '105114', '105116', '42259', '42176', '41424', '42277', '42371', '42369', '104698', '41916', '104128', '104703', '104126', '104163', '88050', '41942', '105180', '105178', '104352', '105251', '105252', '104422', '97252', '41969', '104461', '108262', '107953', '42021', '104206', '104131', '95826', '105803', '105772', '88047', '108306', '88127', '88584', '88128', '88470', '88223', '108127', '101319', '101447', '101027', '105801', '104110', '88181', '100862', '100825', '100900', '100941', '100970', '100987', '42292', '42113', '102298', '105776', '96218', '104284', '105104', '105730', '105755', '105757', '105759', '106983', '42346', '42100', '105761', '104678', '104676', '104694', '104681', '104786', '105791', '105795', '107075', '106859', '105770', '105766', '105763', '104684', '105930', '106915', '106256', '105932', '107043', '105870', '105872', '104133', '104716', '104340', '105878', '88976', '89007', '88881', '88882', '88342', '88280', '88292', '88322', '88038', '88194', '95961', '100296', '108294', '97296', '95962', '105868', '105866', '95828', '105880', '41828', '41953', '105885', '95831', '105657', '108488', '105130', '105847', '105835', '88541', '88436', '88184', '95968', '88270', '88271', '95969', '88402', '88564', '89099', '88382', '88195', '88129', '106645', '104711', '41908', '105910', '104122', '105912', '104135', '88318', '106003', '106001', '88196', '105934', '105936', '105966', '107454', '105962', '106075', '106879', '108162', '106642', '88130', '88977', '107052', '106224', '105969', '98203', '105972', '88469', '105938', '97347', '88131', '88277', '88571', '88298', '95832', '105740', '105793', '108300', '88052', '105940', '88069', '106099', '95834', '42043', '104138', '41890', '42415', '104666', '104140', '41772', '41819', '42153', '104726', '104146', '104736', '42310', '104274', '41955', '105108', '105944', '108302', '105948', '105946', '95835', '42164', '105981', '105983', '105977', '105979', '105950', '88978', '88883', '88290', '105990', '88367', '88133', '105954', '105952', '104742', '105992', '105995', '108202', '105956', '88103', '95836', '95977', '42141', '105988', '105958', '88415', '88272', '105960', '88565', '42257', '104155', '104153', '105111', '42190', '88197', '41804', '88064', '88363', '88468', '106022', '95838', '88368', '88979', '95981', '88226', '42048', '41871', '42530', '42235', '42193', '42295', '42270', '42356', '106014', '99045', '106020', '107337', '95840', '42069', '88573', '104115', '88060', '104760', '42192', '104758', '42191', '104755', '104183', '41940', '104181', '88057', '106494', '99076', '97250', '106094', '88465', '108502', '106018', '99103', '106120', '107876', '99125', '106722', '106917', '95841', '88293', '108314', '108400', '88445', '42159', '95842', '42349', '42108', '106261', '88193', '42173', '42289', '104157', '104746', '104244', '88281', '104753', '42525', '104346', '107878', '106005', '88074', '42267', '102308', '42332', '105142', '97998', '41984', '88595', '106119', '107131', '106213', '105678', '105684', '105680', '105697', '41839', '107583', '42099', '88134', '41928', '105686', '105700', '104613', '95988', '104611', '105688', '42524', '105694', '88198', '98052', '88572', '106229', '104688', '42272', '42098', '106126', '106234', '106095', '106124', '106916', '106241', '106127', '106237', '106236', '104170', '106309', '90111', '95844', '106168', '106161', '106132', '106247', '106131', '106245', '106135', '106243', '106134', '106288', '106294', '106123', '106248', '106249', '106250', '106096', '106130', '106296', '106290', '106287', '106280', '106694', '106255', '106594', '106136', '106277', '106268', '106266', '106153', '106155', '106151', '106258', '108472', '106158', '106159', '106278', '106293', '106281', '106257', '106284', '106252', '106157', '106253', '106271', '106275', '106137', '106164', '106162', '105707', '106307', '106167', '106175', '106176', '106178', '106181', '106179', '106185', '106188', '106317', '106729', '108465', '106186', '106190', '106192', '106182', '105035', '106315', '106097', '108467', '106184', '106171', '106318', '106172', '106173', '106319', '107154', '106320', '42353', '106312', '106333', '108411', '106329', '106337', '106331', '106332', '106328', '106325', '106326', '106327', '106170', '107005', '106335', '99255', '42225', '104117', '41504', '95845', '95846', '106706', '95847', '41793', '106129', '104033', '104619', '103394', '42045', '104099', '104059', '104617', '104615', '104607', '41939', '104065', '105636', '108413', '41859', '88135', '105638', '105640', '105642', '105667', '105665', '104609', '105654', '105672', '105675', '107401', '105650', '105648', '105646', '105652', '41934', '42198', '42017', '105659', '41901', '42388', '42293', '41910', '41858', '41960', '42529', '42260', '105661', '95848', '41848', '105501', '105464', '41846', '41921', '42165', '107746', '96448', '105528', '106231', '105538', '105531', '105536', '105540', '105542', '108421', '105468', '106677', '108423', '96001', '104530', '105597', '105556', '105558', '105565', '105560', '105546', '108431', '105615', '105569', '105567', '105548', '105623', '105625', '105628', '108478', '108427', '105575', '105579', '105581', '105584', '106914', '108428', '105586', '104104', '104430', '104168', '88105', '104091', '95849', '98356', '98381', '105630', '98364', '88582', '88365', '105590', '95851', '104532', '95850', '98392', '105592', '105588', '95852', '95853', '98370', '98375', '88136', '42264', '41866', '41822', '42395', '104509', '41872', '104089', '41794', '41932', '104515', '41824', '106360', '105346', '105351', '105362', '105360', '105379', '108455', '105375', '105383', '105365', '105331', '106121', '105480', '105367', '105373', '106207', '105371', '105369', '105386', '105381', '106030', '105430', '105441', '105466', '105425', '105437', '105434', '105432', '105444', '105449', '105451', '105446', '105448', '105412', '105453', '106499', '88323', '88294', '104524', '104526', '104535', '104578', '42254', '41869', '104537', '41777', '106201', '107426', '104960', '104657', '104580', '107745', '106727', '105595', '107330', '108490', '105715', '105703', '107888', '105144', '96010', '106228', '105705', '105718', '42389', '42239', '42127', '88885', '104636', '104647', '42528', '42328', '42376', '104106', '104637', '41880', '41933', '108128', '104640', '41845', '105720', '42265', '104642', '41770', '104455', '42360', '88299', '96014', '42170', '104286', '42286', '88395', '104643', '42416', '42223', '41847', '42027', '42375', '42201', '104649', '41581', '42527', '105711', '88401', '42126', '105713', '42160', '88478', '88283', '95855', '108495', '97251', '42298', '42135', '42083', '41812', '42414', '42035', '104645', '106548', '88273', '88137', '104659', '42339', '42150', '41783', '41995', '42318', '42162', '41963', '42022', '41829', '41826', '42255', '105728', '104350', '42013', '88040', '105722', '88941', '105724', '41837', '41974', '42168', '106027', '106061', '106025', '106023', '106065', '106032', '106040', '106692', '106622', '108499', '106029', '106072', '97584', '104762', '107038', '88985', '88968', '106058', '104304', '96343', '95857', '106092', '106090', '106088', '108500', '88106', '88374', '88267', '105013', '106641', '42315', '104772', '106199', '106202', '106203', '106198', '106321', '106197', '106195', '106196', '107402', '88199', '88328', '89008', '42210', '42184', '104520', '104503', '105338', '105340', '106688', '105342', '108358', '104088', '105344', '104522', '42010', '41902', '105456', '42338', '106877', '105458', '105495', '108360', '104528', '96032', '96033', '105571', '105573', '104568', '104366', '104533', '104572', '104093', '104576', '88435', '96034', '42510', '104584', '88138', '88058', '88412', '107880', '105632', '106358', '88048', '104545', '104540', '104095', '105126', '104543', '104547', '104551', '104604', '104097', '104564', '104561', '42336', '104558', '101595', '104632', '42378', '88476', '42078', '96038', '88297', '88473', '88440', '41758', '104782', '88461', '105726', '88107', '88409', '88295', '88352', '88200', '88274', '88139', '41448', '42018', '108363', '89009', '88980', '88475', '88287', '88326', '89010', '88140', '101705', '101717', '101663', '101722', '101698', '101680', '88182', '88439', '95860', '88141', '42180', '42344', '41894', '88385', '88389', '88399', '88065', '96047', '88201', '88324', '42077', '106048', '106082', '108367', '106990', '106046', '106043', '106085', '106049', '105091', '42321', '88320', '104765', '107069', '101602', '101734', '88562', '108316', '88396', '106628', '92182', '106055', '88487', '106052', '88142', '88896', '89047', '88384', '95863', '88369', '88479', '88143', '88144', '42522', '104258', '104165', '106100', '107153', '104175', '106101', '88387', '96053', '41999', '42399', '106103', '106208', '106108', '106106', '105016', '42146', '106110', '108318', '106209', '106211', '108369', '88300', '106216', '106219', '106214', '106221', '42059', '106112', '106118', '106116', '106227', '42299', '106631', '106399', '106503', '41778', '106501', '88319', '106401', '106508', '106506', '106400', '106428', '106417', '106515', '106431', '106415', '106533', '106536', '106433', '106435', '106368', '106459', '106292', '106461', '106450', '106673', '106448', '106452', '101847', '106464', '95866', '106468', '41964', '42111', '41862', '41948', '104185', '42229', '104801', '104795', '41983', '41962', '42195', '42242', '104187', '88301', '89011', '106554', '106549', '106665', '106469', '106550', '106553', '108382', '106552', '106562', '106567', '106565', '106570', '106484', '106556', '106122', '106205', '106206', '108329', '106341', '106559', '107359', '106909', '106476', '106479', '106477', '106470', '106555', '106472', '106482', '106480', '106589', '106578', '106577', '106574', '106576', '106579', '104189', '96058', '106590', '106471', '108405', '108385', '104774', '104179', '106596', '96059', '104806', '106593', '99174', '88145', '88566', '88108', '106485', '106757', '106361', '106597', '106362', '95867', '99453', '106683', '99458', '41874', '42019', '42145', '106685', '106619', '107879', '106662', '96216', '106624', '106286', '106623', '108336', '106690', '106691', '106910', '106340', '106626', '106693', '106696', '106695', '108338', '95868', '104198', '42119', '41972', '104204', '41821', '105136', '41967', '42005', '104810', '105134', '104200', '99479', '41947', '42224', '104193', '104208', '104195', '42008', '42158', '95869', '104191', '104824', '106629', '106697', '42279', '106806', '88192', '42374', '99490', '92646', '106305', '101902', '88390', '42245', '95870', '95872', '96073', '42058', '41815', '41870', '106369', '106343', '106342', '106372', '106371', '88460', '42408', '106345', '42054', '42125', '104159', '106376', '106347', '106374', '106349', '106377', '108340', '106351', '106379', '95873', '99161', '106353', '106354', '108388', '106355', '106398', '108390', '106390', '106392', '106381', '106383', '106384', '106356', '88561', '97348', '96077', '88471', '99816', '106637', '89046', '106636', '106632', '106633', '106702', '106639', '99160', '106708', '106709', '42187', '88391', '88146', '99960', '106730', '106738', '106732', '106734', '41417', '108538', '42305', '106779', '106740', '106781', '106783', '106782', '106743', '106627', '96085', '106646', '108345', '42322', '41885', '41991', '104828', '104814', '42421', '42300', '42094', '42381', '106223', '106650', '106651', '106648', '95876', '104819', '108349', '106679', '106675', '106723', '106725', '106724', '108393', '106367', '106655', '106680', '88446', '104891', '88411', '95878', '106911', '41780', '95879', '100143', '100029', '104211', '95880', '100077', '107125', '88567', '106807', '106811', '106846', '108396', '106848', '106844', '106813', '106812', '106821', '106864', '106872', '106871', '106873', '106825', '106880', '106823', '106826', '106828', '106860', '106863', '106861', '106855', '106815', '106850', '106851', '106819', '106818', '106820', '106868', '106817', '106889', '106893', '106887', '106884', '106891', '106885', '106896', '106895', '106833', '106898', '106897', '100210', '106900', '106881', '106835', '106838', '106904', '106836', '104886', '106876', '88893', '95899', '41636', '88373', '41927', '88059', '88147', '41635', '42041', '41913', '106905', '88049', '41931', '106907', '96098', '106232', '106323', '108356', '41867', '104888', '88109', '106912', '95882', '96100', '106394', '107585', '107155', '106396', '106497', '88428', '88325', '106487', '106395', '106486', '42011', '42171', '107090', '107251', '106595', '102200', '107100', '107106', '107102', '107104', '107095', '107098', '107254', '107260', '107259', '107257', '107093', '102210', '107108', '107110', '106993', '107085', '106999', '96104', '107116', '104851', '42237', '42002', '41906', '104832', '104830', '104869', '42424', '42249', '42412', '42208', '104875', '41922', '41889', '42291', '104236', '104838', '104221', '42124', '104853', '104240', '104232', '104229', '104867', '42102', '104863', '104865', '41818', '42370', '42028', '104849', '41994', '104878', '41863', '104845', '104108', '42219', '106204', '106749', '106750', '106748', '106747', '106200', '106746', '107586', '88542', '107126', '41851', '42297', '88148', '106678', '88149', '88392', '88150', '106752', '106756', '104883', '104881', '88151', '106793', '106754', '88275', '106798', '88379', '106788', '106751', '88886', '88362', '88227', '106803', '106802', '106776', '106775', '89012', '106643', '106630', '88044', '42280', '41993', '42182', '106105', '41944', '42106', '42057', '107121', '41775', '104272', '41825', '104360', '88203', '88284', '88154', '88568', '41903', '104930', '107305', '106913', '88981', '107006', '106926', '106925', '106924', '106919', '106920', '106918', '104261', '42350', '104254', '104898', '104263', '107008', '88092', '88180', '88703', '88155', '88348', '107011', '106929', '106945', '106927', '41638', '106947', '107889', '106948', '88386', '95885', '106952', '106950', '88218', '104904', '107128', '41637', '104690', '96642', '106956', '106953', '107019', '106964', '108513', '106966', '108511', '107035', '103499', '41483', '106972', '106974', '42138', '107883', '106973', '107918', '106977', '106976', '106979', '106322', '106842', '106988', '106986', '107127', '95888', '88104', '42215', '42326', '105151', '42103', '41640', '41608', '107881', '107036', '88410', '42037', '41917', '107039', '88062', '88982', '106251', '108516', '106302', '106989', '104362', '107046', '107080', '42095', '104267', '106996', '42484', '107132', '88023', '88202', '105155', '107143', '103230', '42392', '104276', '104278', '104292', '88383', '107144', '95890', '88219', '88983', '88474', '88887', '42079', '88888', '88156', '41897', '107146', '41797', '42468', '104921', '103586', '89567', '88157', '107150', '41896', '41970', '42380', '42104', '42050', '41878', '103438', '104280', '107156', '88032', '103444', '42211', '95892', '107894', '106304', '88046', '106365', '107185', '107205', '107200', '103803', '107246', '107244', '107003', '107291', '107292', '107078', '107196', '107194', '107192', '107189', '107187', '107249', '104282', '105183', '42003', '104932', '106875', '107327', '88377', '88158', '41493', '105011', '104934', '42115', '42394', '41992', '42123', '107357', '41764', '107329', '107332', '92594', '107336', '41990', '42038', '88393', '42269', '107365', '107366', '108529', '104788', '107370', '107362', '88364', '41641', '95895', '103400', '103411', '88462', '88221', '103405', '96360', '88159', '88160', '107375', '42212', '96139', '107380', '101903', '107390', '107404', '107381', '41941', '107394', '107590', '107398', '88161', '107588', '88177', '107406', '103395', '107391', '107392', '107393', '103865', '107660', '107408', '41639', '107423', '107413', '88315', '88311', '107427', '107428', '88178', '106366', '106644', '107803', '107865', '42504', '88162', '107805', '107812', '107810', '88413', '88204', '88063', '96144', '88110', '107432', '107668', '107670', '107808', '107434', '107442', '107435', '88276', '107436', '107455', '107448', '107446', '107443', '107453', '107460', '107459', '106098', '106012', '107082', '107524', '88163', '103872', '107526', '88317', '88316', '88224', '88477', '88464', '88398', '88517', '88321', '96146', '104298', '88456', '88955', '108536', '107712', '107707', '107733', '107338', '106364', '107564', '88164', '107558', '107563', '107576', '107578', '107589', '97253', '107751', '104028', '42483', '104943', '41774', '106843', '107759', '107642', '103949', '104003', '104010', '42133', '94117', '93881', '104945', '104953', '42417', '42330', '104947', '41898', '42397', '42233', '107852', '107854', '107861', '107863', '107761', '107827', '107766', '107836', '107984', '105089', '105044', '105042', '104302', '104246', '104171', '106878', '95897', '88341', '95900', '88165', '88166', '88205', '88282', '88225', '88111', '88889', '88112', '88463', '88099', '98641', '98646', '107869', '98449', '98461', '98873', '98790', '98804', '98682', '42505', '96159', '107896', '107904', '107820', '107902', '106324', '107901', '106841', '107371', '107874', '107912', '107909', '107917', '107915', '106222', '107907', '41423', '104957', '104321', '107910', '108126', '42363', '41905', '107425', '88285', '107975', '88039', '88432', '88296', '107977', '95901', '42316', '42051', '42317', '41836', '41597', '88167', '107919', '107979', '88068', '88168', '42500', '41865', '42390', '104072', '98117', '95903', '107982', '95902', '89793', '88206', '41853', '89562', '101901', '104308', '88169', '42230', '42081', '41981', '104306', '95904', '107871', '106339', '42007', '96174', '95906', '107973', '42033', '42175', '105166', '41505', '104992', '104983', '104981', '88170', '42000', '42410', '105005', '42385', '105007', '42393', '105003', '42218', '42217', '105009', '42324', '41755', '105038', '41980', '41856', '105175', '105023', '104357', '41965', '41978', '42090', '104318', '42087', '104242', '105032', '105030', '42147', '42132', '104331', '41987', '105019', '42294', '104101', '41879', '104265', '41961', '41567', '88596', '108039', '105189', '105187', '88890', '88375', '88891', '88286', '41989', '108419', '106707', '41881', '105070', '41982', '104338', '108085', '105072', '107431', '42220', '108082', '88480', '108087', '108097', '108116', '107175', '107152', '108090', '108118', '41790', '102410', '108099', '89897', '91362', '108121', '108130', '42351', '88118', '95907', '102780', '102763', '102948', '103186', '103126', '102973', '102966', '103210', '95909', '88431', '88430', '88171', '105193', '88429', '42533', '88207', '88397', '88093', '108042', '88172', '42202', '42084', '42203', '42256', '88173', '96184', '102627', '102263', '41776', '105195', '108052', '108044', '108046', '102518', '102523', '95913', '95914', '108054', '104663', '41877', '42403', '42402', '108080', '105197', '108205', '42128', '88394', '108275', '105095', '106490', '108273', '88061', '105492', '104964', '42042', '41892', '107925', '107923', '107927', '107924', '107939', '107931', '107934', '107936', '107943', '105864', '88051', '88045', '107945', '104966', '104969', '106840', '106125', '107890', '42199', '104310', '107947', '41884', '107949', '104323', '41883', '107993', '108010', '41842', '41950', '107958', '42206', '41915', '105055', '105058', '104326', '107955', '42200', '102122', '107963', '106689', '108017', '107965', '107971', '106303', '41803', '108037', '108022', '108034', '108031', '104328', '104979']

all_seeds = (	main_subgraph_seed + # 8281
				seeds_for_double_digit_node_subgraphs + # 432
				seeds_for_subgraphs_with_3_to_9_nodes + # 1320
				seeds_for_subgraphs_with_2_nodes + # 2344
				isolate_nodes # 2370
			) # total 14747

PG = grapher.construct_subgraph(all_seeds, 27, [])

label_map, color_map = grapher.assign_node_labels_and_colors(PG)

grapher.export_to_gephi(PG, label_map, color_map)
