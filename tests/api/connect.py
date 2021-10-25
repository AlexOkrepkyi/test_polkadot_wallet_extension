from substrateinterface import SubstrateInterface, Keypair


substrate = SubstrateInterface(
    url="ws://127.0.0.1:9944",
    ss58_format=42,
    type_registry_preset='rococo'
)

ALICE_ADDRESS = "5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY"

block_header = substrate.get_block_header()
block_hash = block_header["header"]["hash"]
block_extrinsics = substrate.get_block(block_hash=block_hash)["extrinsics"]
block_id = block_header["header"]["number"]
block_hash_by_block_id = substrate.get_block_hash(block_id)
events = substrate.get_events()
name = substrate.name


print(block_header)
print(f"Block hash: {block_hash}")
print(block_extrinsics)
print(f"Block id: {block_id}")
print(block_hash_by_block_id)
print(f"Events: [{events}]")
print(f"Name: [{name}]")


print("--- " * 20)


alice_account_info_at_specific_block = substrate.query(
    module="System",
    storage_function="Account",
    params=[ALICE_ADDRESS],
    block_hash=block_hash
)

alice_account_info_at_specific_block_serialized = alice_account_info_at_specific_block.serialize()

alice_nonce_at_specific_block = alice_account_info_at_specific_block["nonce"]
alice_free_at_specific_block = alice_account_info_at_specific_block["data"]["free"]

print(f"[Alice] account info at block [{block_hash}]: {alice_account_info_at_specific_block}")
print(f"[Alice] serialized account info at block [{block_hash}]: {alice_account_info_at_specific_block_serialized}")
print(f"[Alice] current nonce at block [{block_hash}]: {alice_nonce_at_specific_block}")
print(f"[Alice] balance value at block [{block_hash}]: {alice_free_at_specific_block}")


print("--- " * 20)


# def subscription_handler(account_info_obj, update_nr, subscription_id):
#
#     if update_nr == 0:
#         print('Initial account data:', account_info_obj.value)
#
#     if update_nr > 0:
#         # Do something with the update
#         print('Account data changed:', account_info_obj.value)
#
#     # The execution will block until an arbitrary value is returned, which will be the result of the `query`
#     if update_nr > 5:
#         return account_info_obj
#
#
# result = substrate.query(
#     module="System",
#     storage_function="Account",
#     params=[alice_address],
#     subscription_handler=subscription_handler)
#
# print(result)


# keypair = Keypair.create_from_mnemonic('episode together nose spoon dose oil faculty zoo ankle evoke admit walnut')
alice_mnemonic = Keypair.create_from_uri("//Alice")
# print(f"Alice mnemonic: {alice_mnemonic}")

call = substrate.compose_call(
    call_module='Balances',
    call_function='transfer',
    call_params={
        'dest': ALICE_ADDRESS,
        'value': 1000000000
    },
    block_hash=block_hash
)
print(f"Call: {call}")

payment_info = substrate.get_payment_info(call=call, keypair=alice_mnemonic)
print(f"Payment info: {payment_info}")

extrinsic = substrate.create_signed_extrinsic(call=call, keypair=alice_mnemonic)
print(f"Extrinsic: {extrinsic}")

receipt = substrate.submit_extrinsic(extrinsic)
print(f"Receipt '{receipt.extrinsic_hash}' sent and included in block '{receipt.block_hash})'")
print(f"Receipt '{receipt.total_fee_amount})'")
print(f"Receipt is successful: '{receipt.is_success})'")