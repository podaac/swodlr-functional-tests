BEGIN TRANSACTION;

DELETE FROM "ProductHistory" WHERE "requestedById" = '54c6e625-d360-405b-b39a-59119b3c8133';
DELETE FROM "Users" WHERE username = 'podaaccloud' OR email = 'podaac-cloud-automation@jpl.nasa.gov';

INSERT INTO "Users" ("id", "username", "email", "firstName", "lastName")
VALUES ('54c6e625-d360-405b-b39a-59119b3c8133', 'podaaccloud', 'podaac-cloud-automation@jpl.nasa.gov', 'PODAAC', 'Cloud');

INSERT INTO "L2RasterProducts" ("id", "timestamp", "cycle", "pass", "scene", "outputGranuleExtentFlag", "outputSamplingGridType", "rasterResolution")
VALUES
('c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:00+00', 0, 0, 0, false, 'UTM', 90),
('19181b22-25db-4771-b14e-7885b48369d5', '2023-10-12 21:26:00+00', 0, 1, 2, false, 'UTM', 100),
('5368018e-b7bd-4039-bca1-2a0373d82904', '2023-10-12 21:27:00+00', 0, 2, 3, false, 'UTM', 120),
('ddb70419-92a5-454f-8afa-5038b383a867', '2023-10-12 21:28:00+00', 0, 3, 4, false, 'UTM', 125),
('c3ed8dab-4260-490c-b773-957dc3809bae', '2023-10-12 21:29:00+00', 0, 4, 5, false, 'UTM', 200),
('bd811a14-2be3-4a79-a179-024928f02f3d', '2023-10-12 21:30:00+00', 0, 5, 6, false, 'UTM', 250),
('e1ac0b5a-dceb-4713-944a-903d9d3f5e8e', '2023-10-12 21:31:00+00', 0, 6, 7, false, 'UTM', 500),
('aa48b4d7-b2ac-48d5-bd6a-4dc8c2348504', '2023-10-12 21:32:00+00', 0, 7, 8, false, 'UTM', 1000),
('2bcae863-5ca0-4cf1-bb87-659331ae234d', '2023-10-12 21:33:00+00', 0, 8, 9, false, 'UTM', 2500),
('433f154e-fb0b-42f6-bc3d-e781fe40667a', '2023-10-12 21:34:00+00', 0, 9, 10, false, 'UTM', 5000),
('08f20863-6039-4302-bde8-8dcb47afa6ad', '2023-10-12 21:35:00+00', 0, 10, 11, false, 'UTM', 10000),
('043e8841-32e3-43f4-b37f-5bb76a0017b2', '2023-10-12 21:36:00+00', 0, 11, 12, false, 'UTM', 90),
('9b864d64-b54b-45ee-a4c0-e2a2db131717', '2023-10-12 21:37:00+00', 0, 12, 13, false, 'UTM', 100),
('0d8a6f0a-b380-42ca-b543-a5ac732c3180', '2023-10-12 21:38:00+00', 0, 13, 14, false, 'UTM', 120),
('50eac559-2780-466b-95cb-1ac0170e3a36', '2023-10-12 21:39:00+00', 0, 14, 15, false, 'UTM', 125),
('aea81572-57d2-48c3-ae0c-bbcba15100b6', '2023-10-12 21:40:00+00', 0, 15, 16, false, 'UTM', 200),
('a36fb90c-231b-4c77-934a-5dc868f228cd', '2023-10-12 21:41:00+00', 0, 16, 17, false, 'UTM', 250),
('bb455e58-5b56-462c-8edd-db93b259ca18', '2023-10-12 21:42:00+00', 0, 17, 18, false, 'UTM', 500),
('7da54533-0601-41fe-a6b0-f3ecfdd60cbc', '2023-10-12 21:43:00+00', 0, 18, 19, false, 'UTM', 1000),
('bf51829b-887f-4457-a265-9607f5bda69b', '2023-10-12 21:44:00+00', 0, 19, 20, false, 'UTM', 2500),
('4f45ead8-814c-4af9-b3d8-eba9f87c30b9', '2023-10-12 21:45:00+00', 0, 20, 21, false, 'UTM', 5000),
('46a14b8a-e1f7-4e4c-8a11-3ff654207504', '2023-10-12 21:46:00+00', 0, 21, 22, false, 'UTM', 10000),
('011247ab-5cd8-4820-89d3-f40a40eb0521', '2023-10-12 21:47:00+00', 0, 22, 23, false, 'UTM', 90),
('33c18311-ce24-4f85-9338-2c8fe1c67d8f', '2023-10-12 21:48:00+00', 0, 23, 24, false, 'UTM', 100),
('82ae884b-e541-410e-a585-f3f40e184b34', '2023-10-12 21:49:00+00', 0, 24, 25, false, 'UTM', 120),
('6b8e254b-a04a-445f-80b8-0498315cae03', '2023-10-12 21:50:00+00', 0, 25, 26, false, 'UTM', 125);

INSERT INTO "Status" ("id", "productId", "timestamp", "state", "reason") VALUES
('1a96aa37-0196-45ed-82df-6d71452ea54d', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:00+00', 'NEW', NULL),
('71ebcd85-c7c2-45b1-8995-dd7885ffcdbc', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:01+00', 'GENERATING', NULL),
('65d5b4c7-9c7f-41a4-932b-ba090ed05135', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:02+00', 'READY', NULL),
('13be3147-ef3e-4e8a-8367-4347c7f59dd6', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:03+00', 'AVAILABLE', NULL),
('cd70337d-b9f9-440d-9199-23008169b812', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:04+00', 'UNAVAILABLE', NULL),
('7dfc24a6-e1dc-4896-8524-87234ae72422', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:05+00', 'GENERATING', NULL),
('d43a8b3f-3a42-4912-9f91-f9f0a99bb8cc', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:06+00', 'READY', NULL),
('7995099a-b0b1-478d-bea7-9eecbddf6d5b', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:07+00', 'AVAILABLE', NULL),
('7534a88e-8e81-423d-af3a-96f1d5fb44a4', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:08+00', 'UNAVAILABLE', NULL),
('cc45cbfe-0c46-4304-aac9-3dae60186406', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:09+00', 'GENERATING', NULL),
('4fcaaa50-0da3-42df-ba72-c32043ca6bd7', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:10+00', 'READY', NULL),
('dbc4e15b-9f18-423b-b15f-2e2a804d261c', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:11+00', 'AVAILABLE', NULL),
('4b339e44-e1ac-47af-a48b-32528f6748c7', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:12+00', 'UNAVAILABLE', NULL),
('f223a621-94e6-4519-9fa1-e6b1e5bcb5d9', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:13+00', 'GENERATING', NULL),
('fbb7f6d8-ae53-4c4f-88d6-c80620c4472f', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:14+00', 'ERROR', 'SDS threw an unrecoverable error'),
('278096c7-cd63-4132-b259-bcc6010ea386', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:15+00', 'GENERATING', NULL),
('4b3ea384-7059-4982-9a63-e3308235aab0', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:16+00', 'READY', NULL),
('3745a283-9ecf-46a5-8b50-42f69fe37d8a', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:17+00', 'AVAILABLE', NULL),
('9868a0fa-c940-4581-a781-4402f2118fb8', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:18+00', 'UNAVAILABLE', NULL),
('bb3c27b3-c092-4965-b623-d8f66cf11a22', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:19+00', 'GENERATING', NULL),
('a612e99e-a905-490a-99fc-cd5c7024f6fc', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:20+00', 'READY', NULL),
('8854a58e-7d36-415c-903d-1b1e4bd7a601', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:21+00', 'AVAILABLE', NULL),
('a76254a5-90a2-4469-94fd-273b373b3c20', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:22+00', 'UNAVAILABLE', NULL),
('cfafc6aa-ba8b-4603-8cb7-f85441c727a3', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:23+00', 'GENERATING', NULL),
('f926a6fe-9d87-4917-8911-14982b58155d', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-12 21:25:24+00', 'AVAILABLE', NULL);

INSERT INTO "ProductHistory" ("requestedById", "rasterProductId", "timestamp") VALUES
('54c6e625-d360-405b-b39a-59119b3c8133', 'c2dd0b59-6ab4-4940-9db8-8cdc8317b64b', '2023-10-11 21:25:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '19181b22-25db-4771-b14e-7885b48369d5', '2023-10-12 21:26:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '5368018e-b7bd-4039-bca1-2a0373d82904', '2023-10-12 21:27:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', 'ddb70419-92a5-454f-8afa-5038b383a867', '2023-10-12 21:28:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', 'c3ed8dab-4260-490c-b773-957dc3809bae', '2023-10-12 21:29:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', 'bd811a14-2be3-4a79-a179-024928f02f3d', '2023-10-12 21:30:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', 'e1ac0b5a-dceb-4713-944a-903d9d3f5e8e', '2023-10-12 21:31:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', 'aa48b4d7-b2ac-48d5-bd6a-4dc8c2348504', '2023-10-12 21:32:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '2bcae863-5ca0-4cf1-bb87-659331ae234d', '2023-10-12 21:33:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '433f154e-fb0b-42f6-bc3d-e781fe40667a', '2023-10-12 21:34:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '08f20863-6039-4302-bde8-8dcb47afa6ad', '2023-10-12 21:35:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '043e8841-32e3-43f4-b37f-5bb76a0017b2', '2023-10-12 21:36:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '9b864d64-b54b-45ee-a4c0-e2a2db131717', '2023-10-12 21:37:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '0d8a6f0a-b380-42ca-b543-a5ac732c3180', '2023-10-12 21:38:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '50eac559-2780-466b-95cb-1ac0170e3a36', '2023-10-12 21:39:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', 'aea81572-57d2-48c3-ae0c-bbcba15100b6', '2023-10-12 21:40:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', 'a36fb90c-231b-4c77-934a-5dc868f228cd', '2023-10-12 21:41:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', 'bb455e58-5b56-462c-8edd-db93b259ca18', '2023-10-12 21:42:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '7da54533-0601-41fe-a6b0-f3ecfdd60cbc', '2023-10-12 21:43:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', 'bf51829b-887f-4457-a265-9607f5bda69b', '2023-10-12 21:44:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '4f45ead8-814c-4af9-b3d8-eba9f87c30b9', '2023-10-12 21:45:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '46a14b8a-e1f7-4e4c-8a11-3ff654207504', '2023-10-12 21:46:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '011247ab-5cd8-4820-89d3-f40a40eb0521', '2023-10-12 21:47:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '33c18311-ce24-4f85-9338-2c8fe1c67d8f', '2023-10-12 21:48:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '82ae884b-e541-410e-a585-f3f40e184b34', '2023-10-12 21:49:00+00'),
('54c6e625-d360-405b-b39a-59119b3c8133', '6b8e254b-a04a-445f-80b8-0498315cae03', '2023-10-12 21:50:00+00');

END TRANSACTION;

