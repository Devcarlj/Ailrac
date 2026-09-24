                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
```
Ailrac
├─ ailrac.py
├─ backend
│  ├─ ailrac_core.py
│  ├─ assets
│  ├─ bot_state.py
│  ├─ code_approval.py
│  ├─ database.py
│  ├─ execution_guard.py
│  ├─ gemini_client.py
│  ├─ main.py
│  ├─ models.py
│  ├─ openrouter_client.py
│  ├─ request_context.py
│  ├─ requirements.txt
│  ├─ security.py
│  ├─ services.py
│  ├─ spotify_player.py
│  ├─ streaming_tts.py
│  ├─ telegram_approval.py
│  ├─ test_dual_mode_pipeline.py
│  └─ _test_gemini_auth.py
├─ frontend
│  ├─ eslint.config.js
│  ├─ index.html
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  ├─ favicon.svg
│  │  └─ icons.svg
│  ├─ README.md
│  ├─ src
│  │  ├─ App.css
│  │  ├─ App.jsx
│  │  ├─ assets
│  │  │  ├─ react.svg
│  │  │  └─ vite.svg
│  │  ├─ components
│  │  │  ├─ ChatWindow.jsx
│  │  │  ├─ CodeApprovalModal.jsx
│  │  │  ├─ MessageInput.jsx
│  │  │  ├─ SettingsPage.jsx
│  │  │  ├─ SettingsPanel.jsx
│  │  │  └─ Sidebar.jsx
│  │  ├─ hooks
│  │  │  └─ useChat.js
│  │  ├─ index.css
│  │  └─ main.jsx
│  └─ vite.config.js
├─ README.md
├─ start_all.bat
├─ start_backend.bat
├─ start_frontend.bat
└─ venv
   ├─ COPYING
   ├─ Include
   │  └─ site
   │     └─ python3.13
   │        └─ greenlet
   │           └─ greenlet.h
   ├─ Lib
   │  └─ site-packages
   │     ├─ 81d243bd2c585b0f4821__mypyc.cp313-win_amd64.pyd
   │     ├─ adodbapi
   │     │  ├─ adodbapi.py
   │     │  ├─ ado_consts.py
   │     │  ├─ apibase.py
   │     │  ├─ examples
   │     │  │  ├─ db_print.py
   │     │  │  ├─ db_table_names.py
   │     │  │  ├─ xls_read.py
   │     │  │  └─ xls_write.py
   │     │  ├─ is64bit.py
   │     │  ├─ license.txt
   │     │  ├─ process_connect_string.py
   │     │  ├─ readme.txt
   │     │  ├─ schema_table.py
   │     │  ├─ setup.py
   │     │  ├─ test
   │     │  │  ├─ adodbapitest.py
   │     │  │  ├─ adodbapitestconfig.py
   │     │  │  ├─ dbapi20.py
   │     │  │  ├─ is64bit.py
   │     │  │  ├─ setuptestframework.py
   │     │  │  ├─ test_adodbapi_dbapi20.py
   │     │  │  └─ tryconnection.py
   │     │  └─ __init__.py
   │     ├─ aifc
   │     │  └─ __init__.py
   │     ├─ annotated_doc
   │     │  ├─ main.py
   │     │  ├─ py.typed
   │     │  └─ __init__.py
   │     ├─ annotated_types
   │     │  ├─ py.typed
   │     │  ├─ test_cases.py
   │     │  └─ __init__.py
   │     ├─ anyio
   │     │  ├─ abc
   │     │  │  ├─ _eventloop.py
   │     │  │  ├─ _resources.py
   │     │  │  ├─ _sockets.py
   │     │  │  ├─ _streams.py
   │     │  │  ├─ _subprocesses.py
   │     │  │  ├─ _tasks.py
   │     │  │  ├─ _testing.py
   │     │  │  └─ __init__.py
   │     │  ├─ from_thread.py
   │     │  ├─ functools.py
   │     │  ├─ lowlevel.py
   │     │  ├─ py.typed
   │     │  ├─ pytest_plugin.py
   │     │  ├─ streams
   │     │  │  ├─ buffered.py
   │     │  │  ├─ file.py
   │     │  │  ├─ memory.py
   │     │  │  ├─ stapled.py
   │     │  │  ├─ text.py
   │     │  │  ├─ tls.py
   │     │  │  └─ __init__.py
   │     │  ├─ to_interpreter.py
   │     │  ├─ to_process.py
   │     │  ├─ to_thread.py
   │     │  ├─ _backends
   │     │  │  ├─ _asyncio.py
   │     │  │  ├─ _trio.py
   │     │  │  └─ __init__.py
   │     │  ├─ _core
   │     │  │  ├─ _asyncio_selector_thread.py
   │     │  │  ├─ _contextmanagers.py
   │     │  │  ├─ _eventloop.py
   │     │  │  ├─ _exceptions.py
   │     │  │  ├─ _fileio.py
   │     │  │  ├─ _resources.py
   │     │  │  ├─ _signals.py
   │     │  │  ├─ _sockets.py
   │     │  │  ├─ _streams.py
   │     │  │  ├─ _subprocesses.py
   │     │  │  ├─ _synchronization.py
   │     │  │  ├─ _tasks.py
   │     │  │  ├─ _tempfile.py
   │     │  │  ├─ _testing.py
   │     │  │  ├─ _typedattr.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ apiclient
   │     │  └─ __init__.py
   │     ├─ audioop
   │     │  ├─ py.typed
   │     │  ├─ _audioop.pyd
   │     │  ├─ __init__.py
   │     │  └─ __init__.pyi
   │     ├─ certifi
   │     │  ├─ cacert.pem
   │     │  ├─ core.py
   │     │  ├─ py.typed
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ cffi
   │     │  ├─ api.py
   │     │  ├─ backend_ctypes.py
   │     │  ├─ cffi_opcode.py
   │     │  ├─ commontypes.py
   │     │  ├─ cparser.py
   │     │  ├─ error.py
   │     │  ├─ ffiplatform.py
   │     │  ├─ lock.py
   │     │  ├─ model.py
   │     │  ├─ parse_c_type.h
   │     │  ├─ pkgconfig.py
   │     │  ├─ recompiler.py
   │     │  ├─ setuptools_ext.py
   │     │  ├─ vengine_cpy.py
   │     │  ├─ vengine_gen.py
   │     │  ├─ verifier.py
   │     │  ├─ _cffi_errors.h
   │     │  ├─ _cffi_include.h
   │     │  ├─ _embedding.h
   │     │  ├─ _imp_emulation.py
   │     │  └─ __init__.py
   │     ├─ charset_normalizer
   │     │  ├─ api.py
   │     │  ├─ cd.cp313-win_amd64.pyd
   │     │  ├─ cd.py
   │     │  ├─ cli
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ constant.py
   │     │  ├─ legacy.py
   │     │  ├─ md.cp313-win_amd64.pyd
   │     │  ├─ md.py
   │     │  ├─ models.py
   │     │  ├─ py.typed
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ chunk
   │     │  └─ __init__.py
   │     ├─ click
   │     │  ├─ core.py
   │     │  ├─ decorators.py
   │     │  ├─ exceptions.py
   │     │  ├─ formatting.py
   │     │  ├─ globals.py
   │     │  ├─ parser.py
   │     │  ├─ py.typed
   │     │  ├─ shell_completion.py
   │     │  ├─ termui.py
   │     │  ├─ testing.py
   │     │  ├─ types.py
   │     │  ├─ utils.py
   │     │  ├─ _compat.py
   │     │  ├─ _termui_impl.py
   │     │  ├─ _textwrap.py
   │     │  ├─ _utils.py
   │     │  ├─ _winconsole.py
   │     │  └─ __init__.py
   │     ├─ colorama
   │     │  ├─ ansi.py
   │     │  ├─ ansitowin32.py
   │     │  ├─ initialise.py
   │     │  ├─ tests
   │     │  │  ├─ ansitowin32_test.py
   │     │  │  ├─ ansi_test.py
   │     │  │  ├─ initialise_test.py
   │     │  │  ├─ isatty_test.py
   │     │  │  ├─ utils.py
   │     │  │  ├─ winterm_test.py
   │     │  │  └─ __init__.py
   │     │  ├─ win32.py
   │     │  ├─ winterm.py
   │     │  └─ __init__.py
   │     ├─ comtypes
   │     │  ├─ automation.py
   │     │  ├─ clear_cache.py
   │     │  ├─ client
   │     │  │  ├─ dynamic.py
   │     │  │  ├─ lazybind.py
   │     │  │  ├─ _activeobj.py
   │     │  │  ├─ _code_cache.py
   │     │  │  ├─ _constants.py
   │     │  │  ├─ _create.py
   │     │  │  ├─ _events.py
   │     │  │  ├─ _generate.py
   │     │  │  ├─ _managing.py
   │     │  │  └─ __init__.py
   │     │  ├─ connectionpoints.py
   │     │  ├─ errorinfo.py
   │     │  ├─ gen
   │     │  │  ├─ SpeechLib.py
   │     │  │  ├─ stdole.py
   │     │  │  ├─ _00020430_0000_0000_C000_000000000046_0_2_0.py
   │     │  │  ├─ _C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4.py
   │     │  │  └─ __init__.py
   │     │  ├─ git.py
   │     │  ├─ GUID.py
   │     │  ├─ hints.pyi
   │     │  ├─ hresult.py
   │     │  ├─ logutil.py
   │     │  ├─ malloc.py
   │     │  ├─ messageloop.py
   │     │  ├─ patcher.py
   │     │  ├─ persist.py
   │     │  ├─ safearray.py
   │     │  ├─ server
   │     │  │  ├─ automation.py
   │     │  │  ├─ connectionpoints.py
   │     │  │  ├─ inprocserver.py
   │     │  │  ├─ localserver.py
   │     │  │  ├─ register.py
   │     │  │  ├─ w_getopt.py
   │     │  │  └─ __init__.py
   │     │  ├─ shelllink.py
   │     │  ├─ stream.py
   │     │  ├─ test
   │     │  │  ├─ find_memleak.py
   │     │  │  ├─ gdi_helper.py
   │     │  │  ├─ monikers_helper.py
   │     │  │  ├─ mylib.idl
   │     │  │  ├─ mylib.tlb
   │     │  │  ├─ mytypelib.idl
   │     │  │  ├─ runtests.py
   │     │  │  ├─ setup.py
   │     │  │  ├─ TestComServer.idl
   │     │  │  ├─ TestComServer.py
   │     │  │  ├─ TestComServer.tlb
   │     │  │  ├─ TestDispServer.idl
   │     │  │  ├─ TestDispServer.py
   │     │  │  ├─ TestDispServer.tlb
   │     │  │  ├─ test_agilent.py
   │     │  │  ├─ test_avmc.py
   │     │  │  ├─ test_basic.py
   │     │  │  ├─ test_bctx.py
   │     │  │  ├─ test_BSTR.py
   │     │  │  ├─ test_casesensitivity.py
   │     │  │  ├─ test_classfactory.py
   │     │  │  ├─ test_clear_cache.py
   │     │  │  ├─ test_client.py
   │     │  │  ├─ test_client_dynamic.py
   │     │  │  ├─ test_client_regenerate_modules.py
   │     │  │  ├─ test_collections.py
   │     │  │  ├─ test_comobject.py
   │     │  │  ├─ test_comserver.py
   │     │  │  ├─ test_connectionpoints.py
   │     │  │  ├─ test_createwrappers.py
   │     │  │  ├─ test_dict.py
   │     │  │  ├─ test_dispifc_records.py
   │     │  │  ├─ test_dispifc_safearrays.py
   │     │  │  ├─ test_dispinterface.py
   │     │  │  ├─ test_DISPPARAMS.py
   │     │  │  ├─ test_dyndispatch.py
   │     │  │  ├─ test_errorinfo.py
   │     │  │  ├─ test_eventinterface.py
   │     │  │  ├─ test_excel.py
   │     │  │  ├─ test_findgendir.py
   │     │  │  ├─ test_getactiveobj.py
   │     │  │  ├─ test_git.py
   │     │  │  ├─ test_GUID.py
   │     │  │  ├─ test_hresult.py
   │     │  │  ├─ test_ienum.py
   │     │  │  ├─ test_imfattributes.py
   │     │  │  ├─ test_inout_args.py
   │     │  │  ├─ test_jscript.js
   │     │  │  ├─ test_logutil.py
   │     │  │  ├─ test_malloc.py
   │     │  │  ├─ test_messageloop.py
   │     │  │  ├─ test_midl_safearray_create.py
   │     │  │  ├─ test_moniker.py
   │     │  │  ├─ test_msscript.py
   │     │  │  ├─ test_npsupport.py
   │     │  │  ├─ test_outparam.py
   │     │  │  ├─ test_persist.py
   │     │  │  ├─ test_pump_events.py
   │     │  │  ├─ test_puredispatch.py
   │     │  │  ├─ test_QueryService.py
   │     │  │  ├─ test_recordinfo.py
   │     │  │  ├─ test_rot.py
   │     │  │  ├─ test_safearray.py
   │     │  │  ├─ test_sapi.py
   │     │  │  ├─ test_server.py
   │     │  │  ├─ test_server_automation.py
   │     │  │  ├─ test_server_register.py
   │     │  │  ├─ test_shelllink.py
   │     │  │  ├─ test_showevents.py
   │     │  │  ├─ test_storage.py
   │     │  │  ├─ test_stream.py
   │     │  │  ├─ test_subinterface.py
   │     │  │  ├─ test_typeannotator.py
   │     │  │  ├─ test_typeinfo.py
   │     │  │  ├─ test_typeinfo_create.py
   │     │  │  ├─ test_urlhistory.py
   │     │  │  ├─ test_util.py
   │     │  │  ├─ test_variant.py
   │     │  │  ├─ test_variant_outparam.py
   │     │  │  ├─ test_viewobject.py
   │     │  │  ├─ test_win32com_interop.py
   │     │  │  ├─ test_word.py
   │     │  │  ├─ test_w_getopt.py
   │     │  │  ├─ time_structs_helper.py
   │     │  │  ├─ urlhist.tlb
   │     │  │  └─ __init__.py
   │     │  ├─ tools
   │     │  │  ├─ codegenerator
   │     │  │  │  ├─ codegenerator.py
   │     │  │  │  ├─ comments.py
   │     │  │  │  ├─ heads.py
   │     │  │  │  ├─ helpers.py
   │     │  │  │  ├─ modulenamer.py
   │     │  │  │  ├─ namespaces.py
   │     │  │  │  ├─ packing.py
   │     │  │  │  ├─ typeannotator.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tlbparser.py
   │     │  │  ├─ typedesc.py
   │     │  │  ├─ typedesc_base.py
   │     │  │  └─ __init__.py
   │     │  ├─ typeinfo.py
   │     │  ├─ util.py
   │     │  ├─ viewobject.py
   │     │  ├─ _comobject.py
   │     │  ├─ _memberspec.py
   │     │  ├─ _meta.py
   │     │  ├─ _npsupport.py
   │     │  ├─ _post_coinit
   │     │  │  ├─ activeobj.py
   │     │  │  ├─ bstr.py
   │     │  │  ├─ instancemethod.py
   │     │  │  ├─ misc.py
   │     │  │  ├─ unknwn.py
   │     │  │  ├─ _cominterface_meta_patcher.py
   │     │  │  └─ __init__.py
   │     │  ├─ _safearray.py
   │     │  ├─ _tlib_version_checker.py
   │     │  ├─ _vtbl.py
   │     │  └─ __init__.py
   │     ├─ cryptography
   │     │  ├─ exceptions.py
   │     │  ├─ fernet.py
   │     │  ├─ hazmat
   │     │  │  ├─ asn1
   │     │  │  │  ├─ asn1.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ backends
   │     │  │  │  ├─ openssl
   │     │  │  │  │  ├─ backend.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ bindings
   │     │  │  │  ├─ openssl
   │     │  │  │  │  ├─ binding.py
   │     │  │  │  │  ├─ _conditional.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _rust
   │     │  │  │  │  ├─ asn1.pyi
   │     │  │  │  │  ├─ declarative_asn1.pyi
   │     │  │  │  │  ├─ exceptions.pyi
   │     │  │  │  │  ├─ ocsp.pyi
   │     │  │  │  │  ├─ openssl
   │     │  │  │  │  │  ├─ aead.pyi
   │     │  │  │  │  │  ├─ ciphers.pyi
   │     │  │  │  │  │  ├─ cmac.pyi
   │     │  │  │  │  │  ├─ dh.pyi
   │     │  │  │  │  │  ├─ dsa.pyi
   │     │  │  │  │  │  ├─ ec.pyi
   │     │  │  │  │  │  ├─ ed25519.pyi
   │     │  │  │  │  │  ├─ ed448.pyi
   │     │  │  │  │  │  ├─ hashes.pyi
   │     │  │  │  │  │  ├─ hmac.pyi
   │     │  │  │  │  │  ├─ hpke.pyi
   │     │  │  │  │  │  ├─ kdf.pyi
   │     │  │  │  │  │  ├─ keys.pyi
   │     │  │  │  │  │  ├─ mldsa.pyi
   │     │  │  │  │  │  ├─ mlkem.pyi
   │     │  │  │  │  │  ├─ poly1305.pyi
   │     │  │  │  │  │  ├─ rsa.pyi
   │     │  │  │  │  │  ├─ x25519.pyi
   │     │  │  │  │  │  ├─ x448.pyi
   │     │  │  │  │  │  └─ __init__.pyi
   │     │  │  │  │  ├─ pkcs12.pyi
   │     │  │  │  │  ├─ pkcs7.pyi
   │     │  │  │  │  ├─ test_support.pyi
   │     │  │  │  │  ├─ x509.pyi
   │     │  │  │  │  ├─ _openssl.pyi
   │     │  │  │  │  └─ __init__.pyi
   │     │  │  │  ├─ _rust.pyd
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ decrepit
   │     │  │  │  ├─ ciphers
   │     │  │  │  │  ├─ algorithms.py
   │     │  │  │  │  ├─ modes.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ primitives
   │     │  │  │  ├─ asymmetric
   │     │  │  │  │  ├─ dh.py
   │     │  │  │  │  ├─ dsa.py
   │     │  │  │  │  ├─ ec.py
   │     │  │  │  │  ├─ ed25519.py
   │     │  │  │  │  ├─ ed448.py
   │     │  │  │  │  ├─ mldsa.py
   │     │  │  │  │  ├─ mlkem.py
   │     │  │  │  │  ├─ padding.py
   │     │  │  │  │  ├─ rsa.py
   │     │  │  │  │  ├─ types.py
   │     │  │  │  │  ├─ utils.py
   │     │  │  │  │  ├─ x25519.py
   │     │  │  │  │  ├─ x448.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ciphers
   │     │  │  │  │  ├─ aead.py
   │     │  │  │  │  ├─ algorithms.py
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ modes.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ cmac.py
   │     │  │  │  ├─ constant_time.py
   │     │  │  │  ├─ hashes.py
   │     │  │  │  ├─ hmac.py
   │     │  │  │  ├─ hpke.py
   │     │  │  │  ├─ kdf
   │     │  │  │  │  ├─ argon2.py
   │     │  │  │  │  ├─ concatkdf.py
   │     │  │  │  │  ├─ hkdf.py
   │     │  │  │  │  ├─ kbkdf.py
   │     │  │  │  │  ├─ pbkdf2.py
   │     │  │  │  │  ├─ scrypt.py
   │     │  │  │  │  ├─ x963kdf.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ keywrap.py
   │     │  │  │  ├─ padding.py
   │     │  │  │  ├─ poly1305.py
   │     │  │  │  ├─ serialization
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ pkcs12.py
   │     │  │  │  │  ├─ pkcs7.py
   │     │  │  │  │  ├─ ssh.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ twofactor
   │     │  │  │  │  ├─ hotp.py
   │     │  │  │  │  ├─ totp.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _asymmetric.py
   │     │  │  │  ├─ _cipheralgorithm.py
   │     │  │  │  ├─ _modes.py
   │     │  │  │  ├─ _serialization.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _oid.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ utils.py
   │     │  ├─ x509
   │     │  │  ├─ base.py
   │     │  │  ├─ certificate_transparency.py
   │     │  │  ├─ extensions.py
   │     │  │  ├─ general_name.py
   │     │  │  ├─ name.py
   │     │  │  ├─ ocsp.py
   │     │  │  ├─ oid.py
   │     │  │  ├─ verification.py
   │     │  │  └─ __init__.py
   │     │  ├─ __about__.py
   │     │  └─ __init__.py
   │     ├─ dotenv
   │     │  ├─ cli.py
   │     │  ├─ ipython.py
   │     │  ├─ main.py
   │     │  ├─ parser.py
   │     │  ├─ py.typed
   │     │  ├─ variables.py
   │     │  ├─ version.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ duckduckgo_search
   │     │  ├─ cli.py
   │     │  ├─ duckduckgo_search.py
   │     │  ├─ exceptions.py
   │     │  ├─ py.typed
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ fastapi
   │     │  ├─ .agents
   │     │  │  └─ skills
   │     │  │     └─ fastapi
   │     │  │        ├─ references
   │     │  │        │  ├─ dependencies.md
   │     │  │        │  ├─ other-tools.md
   │     │  │        │  └─ streaming.md
   │     │  │        └─ SKILL.md
   │     │  ├─ applications.py
   │     │  ├─ background.py
   │     │  ├─ cli.py
   │     │  ├─ concurrency.py
   │     │  ├─ datastructures.py
   │     │  ├─ dependencies
   │     │  │  ├─ models.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ encoders.py
   │     │  ├─ exceptions.py
   │     │  ├─ exception_handlers.py
   │     │  ├─ logger.py
   │     │  ├─ middleware
   │     │  │  ├─ asyncexitstack.py
   │     │  │  ├─ cors.py
   │     │  │  ├─ gzip.py
   │     │  │  ├─ httpsredirect.py
   │     │  │  ├─ trustedhost.py
   │     │  │  ├─ wsgi.py
   │     │  │  └─ __init__.py
   │     │  ├─ openapi
   │     │  │  ├─ constants.py
   │     │  │  ├─ docs.py
   │     │  │  ├─ models.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ params.py
   │     │  ├─ param_functions.py
   │     │  ├─ py.typed
   │     │  ├─ requests.py
   │     │  ├─ responses.py
   │     │  ├─ routing.py
   │     │  ├─ security
   │     │  │  ├─ api_key.py
   │     │  │  ├─ base.py
   │     │  │  ├─ http.py
   │     │  │  ├─ oauth2.py
   │     │  │  ├─ open_id_connect_url.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ sse.py
   │     │  ├─ staticfiles.py
   │     │  ├─ templating.py
   │     │  ├─ testclient.py
   │     │  ├─ types.py
   │     │  ├─ utils.py
   │     │  ├─ websockets.py
   │     │  ├─ _compat
   │     │  │  ├─ shared.py
   │     │  │  ├─ v2.py
   │     │  │  └─ __init__.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ flatbuffers
   │     │  ├─ builder.py
   │     │  ├─ compat.py
   │     │  ├─ encode.py
   │     │  ├─ flexbuffers.py
   │     │  ├─ number_types.py
   │     │  ├─ packer.py
   │     │  ├─ table.py
   │     │  ├─ util.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ google
   │     │  ├─ ai
   │     │  │  ├─ generativelanguage
   │     │  │  │  ├─ gapic_version.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ generativelanguage_v1
   │     │  │  │  ├─ gapic_metadata.json
   │     │  │  │  ├─ gapic_version.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ services
   │     │  │  │  │  ├─ generative_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ model_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ types
   │     │  │  │  │  ├─ citation.py
   │     │  │  │  │  ├─ content.py
   │     │  │  │  │  ├─ generative_service.py
   │     │  │  │  │  ├─ model.py
   │     │  │  │  │  ├─ model_service.py
   │     │  │  │  │  ├─ safety.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ generativelanguage_v1alpha
   │     │  │  │  ├─ gapic_metadata.json
   │     │  │  │  ├─ gapic_version.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ services
   │     │  │  │  │  ├─ cache_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ discuss_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ file_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ generative_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ model_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ permission_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ prediction_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ retriever_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ text_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ types
   │     │  │  │  │  ├─ cached_content.py
   │     │  │  │  │  ├─ cache_service.py
   │     │  │  │  │  ├─ citation.py
   │     │  │  │  │  ├─ content.py
   │     │  │  │  │  ├─ discuss_service.py
   │     │  │  │  │  ├─ file.py
   │     │  │  │  │  ├─ file_service.py
   │     │  │  │  │  ├─ generative_service.py
   │     │  │  │  │  ├─ model.py
   │     │  │  │  │  ├─ model_service.py
   │     │  │  │  │  ├─ permission.py
   │     │  │  │  │  ├─ permission_service.py
   │     │  │  │  │  ├─ prediction_service.py
   │     │  │  │  │  ├─ retriever.py
   │     │  │  │  │  ├─ retriever_service.py
   │     │  │  │  │  ├─ safety.py
   │     │  │  │  │  ├─ text_service.py
   │     │  │  │  │  ├─ tuned_model.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ generativelanguage_v1beta
   │     │  │  │  ├─ gapic_metadata.json
   │     │  │  │  ├─ gapic_version.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ services
   │     │  │  │  │  ├─ cache_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ discuss_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ file_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ generative_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ model_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ permission_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ prediction_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ retriever_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ text_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ types
   │     │  │  │  │  ├─ cached_content.py
   │     │  │  │  │  ├─ cache_service.py
   │     │  │  │  │  ├─ citation.py
   │     │  │  │  │  ├─ content.py
   │     │  │  │  │  ├─ discuss_service.py
   │     │  │  │  │  ├─ file.py
   │     │  │  │  │  ├─ file_service.py
   │     │  │  │  │  ├─ generative_service.py
   │     │  │  │  │  ├─ model.py
   │     │  │  │  │  ├─ model_service.py
   │     │  │  │  │  ├─ permission.py
   │     │  │  │  │  ├─ permission_service.py
   │     │  │  │  │  ├─ prediction_service.py
   │     │  │  │  │  ├─ retriever.py
   │     │  │  │  │  ├─ retriever_service.py
   │     │  │  │  │  ├─ safety.py
   │     │  │  │  │  ├─ text_service.py
   │     │  │  │  │  ├─ tuned_model.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ generativelanguage_v1beta2
   │     │  │  │  ├─ gapic_metadata.json
   │     │  │  │  ├─ gapic_version.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ services
   │     │  │  │  │  ├─ discuss_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ model_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ pagers.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ text_service
   │     │  │  │  │  │  ├─ async_client.py
   │     │  │  │  │  │  ├─ client.py
   │     │  │  │  │  │  ├─ transports
   │     │  │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  │  ├─ grpc.py
   │     │  │  │  │  │  │  ├─ grpc_asyncio.py
   │     │  │  │  │  │  │  ├─ rest.py
   │     │  │  │  │  │  │  ├─ rest_base.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ types
   │     │  │  │  │  ├─ citation.py
   │     │  │  │  │  ├─ discuss_service.py
   │     │  │  │  │  ├─ model.py
   │     │  │  │  │  ├─ model_service.py
   │     │  │  │  │  ├─ safety.py
   │     │  │  │  │  ├─ text_service.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ generativelanguage_v1beta3
   │     │  │     ├─ gapic_metadata.json
   │     │  │     ├─ gapic_version.py
   │     │  │     ├─ py.typed
   │     │  │     ├─ services
   │     │  │     │  ├─ discuss_service
   │     │  │     │  │  ├─ async_client.py
   │     │  │     │  │  ├─ client.py
   │     │  │     │  │  ├─ transports
   │     │  │     │  │  │  ├─ base.py
   │     │  │     │  │  │  ├─ grpc.py
   │     │  │     │  │  │  ├─ grpc_asyncio.py
   │     │  │     │  │  │  ├─ rest.py
   │     │  │     │  │  │  ├─ rest_base.py
   │     │  │     │  │  │  └─ __init__.py
   │     │  │     │  │  └─ __init__.py
   │     │  │     │  ├─ model_service
   │     │  │     │  │  ├─ async_client.py
   │     │  │     │  │  ├─ client.py
   │     │  │     │  │  ├─ pagers.py
   │     │  │     │  │  ├─ transports
   │     │  │     │  │  │  ├─ base.py
   │     │  │     │  │  │  ├─ grpc.py
   │     │  │     │  │  │  ├─ grpc_asyncio.py
   │     │  │     │  │  │  ├─ rest.py
   │     │  │     │  │  │  ├─ rest_base.py
   │     │  │     │  │  │  └─ __init__.py
   │     │  │     │  │  └─ __init__.py
   │     │  │     │  ├─ permission_service
   │     │  │     │  │  ├─ async_client.py
   │     │  │     │  │  ├─ client.py
   │     │  │     │  │  ├─ pagers.py
   │     │  │     │  │  ├─ transports
   │     │  │     │  │  │  ├─ base.py
   │     │  │     │  │  │  ├─ grpc.py
   │     │  │     │  │  │  ├─ grpc_asyncio.py
   │     │  │     │  │  │  ├─ rest.py
   │     │  │     │  │  │  ├─ rest_base.py
   │     │  │     │  │  │  └─ __init__.py
   │     │  │     │  │  └─ __init__.py
   │     │  │     │  ├─ text_service
   │     │  │     │  │  ├─ async_client.py
   │     │  │     │  │  ├─ client.py
   │     │  │     │  │  ├─ transports
   │     │  │     │  │  │  ├─ base.py
   │     │  │     │  │  │  ├─ grpc.py
   │     │  │     │  │  │  ├─ grpc_asyncio.py
   │     │  │     │  │  │  ├─ rest.py
   │     │  │     │  │  │  ├─ rest_base.py
   │     │  │     │  │  │  └─ __init__.py
   │     │  │     │  │  └─ __init__.py
   │     │  │     │  └─ __init__.py
   │     │  │     ├─ types
   │     │  │     │  ├─ citation.py
   │     │  │     │  ├─ discuss_service.py
   │     │  │     │  ├─ model.py
   │     │  │     │  ├─ model_service.py
   │     │  │     │  ├─ permission.py
   │     │  │     │  ├─ permission_service.py
   │     │  │     │  ├─ safety.py
   │     │  │     │  ├─ text_service.py
   │     │  │     │  ├─ tuned_model.py
   │     │  │     │  └─ __init__.py
   │     │  │     └─ __init__.py
   │     │  ├─ api
   │     │  │  ├─ annotations.proto
   │     │  │  ├─ annotations_pb2.py
   │     │  │  ├─ annotations_pb2.pyi
   │     │  │  ├─ auth.proto
   │     │  │  ├─ auth_pb2.py
   │     │  │  ├─ auth_pb2.pyi
   │     │  │  ├─ backend.proto
   │     │  │  ├─ backend_pb2.py
   │     │  │  ├─ backend_pb2.pyi
   │     │  │  ├─ billing.proto
   │     │  │  ├─ billing_pb2.py
   │     │  │  ├─ billing_pb2.pyi
   │     │  │  ├─ client.proto
   │     │  │  ├─ client_pb2.py
   │     │  │  ├─ client_pb2.pyi
   │     │  │  ├─ config_change.proto
   │     │  │  ├─ config_change_pb2.py
   │     │  │  ├─ config_change_pb2.pyi
   │     │  │  ├─ consumer.proto
   │     │  │  ├─ consumer_pb2.py
   │     │  │  ├─ consumer_pb2.pyi
   │     │  │  ├─ context.proto
   │     │  │  ├─ context_pb2.py
   │     │  │  ├─ context_pb2.pyi
   │     │  │  ├─ control.proto
   │     │  │  ├─ control_pb2.py
   │     │  │  ├─ control_pb2.pyi
   │     │  │  ├─ documentation.proto
   │     │  │  ├─ documentation_pb2.py
   │     │  │  ├─ documentation_pb2.pyi
   │     │  │  ├─ endpoint.proto
   │     │  │  ├─ endpoint_pb2.py
   │     │  │  ├─ endpoint_pb2.pyi
   │     │  │  ├─ error_reason.proto
   │     │  │  ├─ error_reason_pb2.py
   │     │  │  ├─ error_reason_pb2.pyi
   │     │  │  ├─ field_behavior.proto
   │     │  │  ├─ field_behavior_pb2.py
   │     │  │  ├─ field_behavior_pb2.pyi
   │     │  │  ├─ field_info.proto
   │     │  │  ├─ field_info_pb2.py
   │     │  │  ├─ field_info_pb2.pyi
   │     │  │  ├─ http.proto
   │     │  │  ├─ httpbody.proto
   │     │  │  ├─ httpbody_pb2.py
   │     │  │  ├─ httpbody_pb2.pyi
   │     │  │  ├─ http_pb2.py
   │     │  │  ├─ http_pb2.pyi
   │     │  │  ├─ label.proto
   │     │  │  ├─ label_pb2.py
   │     │  │  ├─ label_pb2.pyi
   │     │  │  ├─ launch_stage.proto
   │     │  │  ├─ launch_stage_pb2.py
   │     │  │  ├─ launch_stage_pb2.pyi
   │     │  │  ├─ log.proto
   │     │  │  ├─ logging.proto
   │     │  │  ├─ logging_pb2.py
   │     │  │  ├─ logging_pb2.pyi
   │     │  │  ├─ log_pb2.py
   │     │  │  ├─ log_pb2.pyi
   │     │  │  ├─ metric.proto
   │     │  │  ├─ metric_pb2.py
   │     │  │  ├─ metric_pb2.pyi
   │     │  │  ├─ monitored_resource.proto
   │     │  │  ├─ monitored_resource_pb2.py
   │     │  │  ├─ monitored_resource_pb2.pyi
   │     │  │  ├─ monitoring.proto
   │     │  │  ├─ monitoring_pb2.py
   │     │  │  ├─ monitoring_pb2.pyi
   │     │  │  ├─ policy.proto
   │     │  │  ├─ policy_pb2.py
   │     │  │  ├─ policy_pb2.pyi
   │     │  │  ├─ quota.proto
   │     │  │  ├─ quota_pb2.py
   │     │  │  ├─ quota_pb2.pyi
   │     │  │  ├─ resource.proto
   │     │  │  ├─ resource_pb2.py
   │     │  │  ├─ resource_pb2.pyi
   │     │  │  ├─ routing.proto
   │     │  │  ├─ routing_pb2.py
   │     │  │  ├─ routing_pb2.pyi
   │     │  │  ├─ service.proto
   │     │  │  ├─ service_pb2.py
   │     │  │  ├─ service_pb2.pyi
   │     │  │  ├─ source_info.proto
   │     │  │  ├─ source_info_pb2.py
   │     │  │  ├─ source_info_pb2.pyi
   │     │  │  ├─ system_parameter.proto
   │     │  │  ├─ system_parameter_pb2.py
   │     │  │  ├─ system_parameter_pb2.pyi
   │     │  │  ├─ usage.proto
   │     │  │  ├─ usage_pb2.py
   │     │  │  ├─ usage_pb2.pyi
   │     │  │  ├─ visibility.proto
   │     │  │  ├─ visibility_pb2.py
   │     │  │  └─ visibility_pb2.pyi
   │     │  ├─ api_core
   │     │  │  ├─ bidi.py
   │     │  │  ├─ bidi_async.py
   │     │  │  ├─ bidi_base.py
   │     │  │  ├─ client_info.py
   │     │  │  ├─ client_logging.py
   │     │  │  ├─ client_options.py
   │     │  │  ├─ datetime_helpers.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ extended_operation.py
   │     │  │  ├─ future
   │     │  │  │  ├─ async_future.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ polling.py
   │     │  │  │  ├─ _helpers.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ gapic_v1
   │     │  │  │  ├─ client_info.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ config_async.py
   │     │  │  │  ├─ method.py
   │     │  │  │  ├─ method_async.py
   │     │  │  │  ├─ routing_header.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ general_helpers.py
   │     │  │  ├─ grpc_helpers.py
   │     │  │  ├─ grpc_helpers_async.py
   │     │  │  ├─ iam.py
   │     │  │  ├─ operation.py
   │     │  │  ├─ operations_v1
   │     │  │  │  ├─ abstract_operations_base_client.py
   │     │  │  │  ├─ abstract_operations_client.py
   │     │  │  │  ├─ operations_async_client.py
   │     │  │  │  ├─ operations_client.py
   │     │  │  │  ├─ operations_client_config.py
   │     │  │  │  ├─ operations_rest_client_async.py
   │     │  │  │  ├─ pagers.py
   │     │  │  │  ├─ pagers_async.py
   │     │  │  │  ├─ pagers_base.py
   │     │  │  │  ├─ transports
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ rest.py
   │     │  │  │  │  ├─ rest_asyncio.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ operation_async.py
   │     │  │  ├─ page_iterator.py
   │     │  │  ├─ page_iterator_async.py
   │     │  │  ├─ path_template.py
   │     │  │  ├─ protobuf_helpers.py
   │     │  │  ├─ py.typed
   │     │  │  ├─ rest_helpers.py
   │     │  │  ├─ rest_streaming.py
   │     │  │  ├─ rest_streaming_async.py
   │     │  │  ├─ retry
   │     │  │  │  ├─ retry_base.py
   │     │  │  │  ├─ retry_streaming.py
   │     │  │  │  ├─ retry_streaming_async.py
   │     │  │  │  ├─ retry_unary.py
   │     │  │  │  ├─ retry_unary_async.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ retry_async.py
   │     │  │  ├─ timeout.py
   │     │  │  ├─ universe.py
   │     │  │  ├─ version.py
   │     │  │  ├─ version_header.py
   │     │  │  ├─ _python_package_support.py
   │     │  │  ├─ _python_version_support.py
   │     │  │  ├─ _rest_streaming_base.py
   │     │  │  └─ __init__.py
   │     │  ├─ auth
   │     │  │  ├─ aio
   │     │  │  │  ├─ credentials.py
   │     │  │  │  ├─ transport
   │     │  │  │  │  ├─ aiohttp.py
   │     │  │  │  │  ├─ mtls.py
   │     │  │  │  │  ├─ sessions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _helpers.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ api_key.py
   │     │  │  ├─ app_engine.py
   │     │  │  ├─ aws.py
   │     │  │  ├─ compute_engine
   │     │  │  │  ├─ credentials.py
   │     │  │  │  ├─ _metadata.py
   │     │  │  │  ├─ _mtls.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ credentials.py
   │     │  │  ├─ crypt
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ es.py
   │     │  │  │  ├─ es256.py
   │     │  │  │  ├─ rsa.py
   │     │  │  │  ├─ _cryptography_rsa.py
   │     │  │  │  ├─ _helpers.py
   │     │  │  │  ├─ _python_rsa.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ downscoped.py
   │     │  │  ├─ environment_vars.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ external_account.py
   │     │  │  ├─ external_account_authorized_user.py
   │     │  │  ├─ iam.py
   │     │  │  ├─ identity_pool.py
   │     │  │  ├─ impersonated_credentials.py
   │     │  │  ├─ jwt.py
   │     │  │  ├─ metrics.py
   │     │  │  ├─ pluggable.py
   │     │  │  ├─ py.typed
   │     │  │  ├─ transport
   │     │  │  │  ├─ grpc.py
   │     │  │  │  ├─ mtls.py
   │     │  │  │  ├─ requests.py
   │     │  │  │  ├─ urllib3.py
   │     │  │  │  ├─ _aiohttp_requests.py
   │     │  │  │  ├─ _custom_tls_signer.py
   │     │  │  │  ├─ _http_client.py
   │     │  │  │  ├─ _mtls_helper.py
   │     │  │  │  ├─ _requests_base.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ version.py
   │     │  │  ├─ _agent_identity_utils.py
   │     │  │  ├─ _cache.py
   │     │  │  ├─ _cloud_sdk.py
   │     │  │  ├─ _credentials_async.py
   │     │  │  ├─ _credentials_base.py
   │     │  │  ├─ _default.py
   │     │  │  ├─ _default_async.py
   │     │  │  ├─ _exponential_backoff.py
   │     │  │  ├─ _helpers.py
   │     │  │  ├─ _jwt_async.py
   │     │  │  ├─ _oauth2client.py
   │     │  │  ├─ _refresh_worker.py
   │     │  │  ├─ _regional_access_boundary_utils.py
   │     │  │  ├─ _service_account_info.py
   │     │  │  └─ __init__.py
   │     │  ├─ cloud
   │     │  │  ├─ common_resources.proto
   │     │  │  ├─ common_resources_pb2.py
   │     │  │  ├─ common_resources_pb2.pyi
   │     │  │  ├─ extended_operations.proto
   │     │  │  ├─ extended_operations_pb2.py
   │     │  │  ├─ extended_operations_pb2.pyi
   │     │  │  └─ location
   │     │  │     ├─ locations.proto
   │     │  │     ├─ locations_pb2.py
   │     │  │     └─ locations_pb2.pyi
   │     │  ├─ gapic
   │     │  │  └─ metadata
   │     │  │     ├─ gapic_metadata.proto
   │     │  │     ├─ gapic_metadata_pb2.py
   │     │  │     └─ gapic_metadata_pb2.pyi
   │     │  ├─ genai
   │     │  │  ├─ batches.py
   │     │  │  ├─ caches.py
   │     │  │  ├─ chats.py
   │     │  │  ├─ client.py
   │     │  │  ├─ documents.py
   │     │  │  ├─ errors.py
   │     │  │  ├─ files.py
   │     │  │  ├─ file_search_stores.py
   │     │  │  ├─ interactions.py
   │     │  │  ├─ live.py
   │     │  │  ├─ live_music.py
   │     │  │  ├─ local_tokenizer.py
   │     │  │  ├─ models.py
   │     │  │  ├─ operations.py
   │     │  │  ├─ pagers.py
   │     │  │  ├─ py.typed
   │     │  │  ├─ tests
   │     │  │  │  ├─ afc
   │     │  │  │  │  ├─ test_convert_if_exist_pydantic_model.py
   │     │  │  │  │  ├─ test_convert_number_values_for_function_call_args.py
   │     │  │  │  │  ├─ test_find_afc_incompatible_tool_indexes.py
   │     │  │  │  │  ├─ test_generate_content_stream_afc.py
   │     │  │  │  │  ├─ test_generate_content_stream_afc_thoughts.py
   │     │  │  │  │  ├─ test_get_function_map.py
   │     │  │  │  │  ├─ test_get_function_response_parts.py
   │     │  │  │  │  ├─ test_get_max_remote_calls_for_afc.py
   │     │  │  │  │  ├─ test_invoke_function_from_dict_args.py
   │     │  │  │  │  ├─ test_raise_error_for_afc_incompatible_config.py
   │     │  │  │  │  ├─ test_should_append_afc_history.py
   │     │  │  │  │  ├─ test_should_disable_afc.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ batches
   │     │  │  │  │  ├─ test_cancel.py
   │     │  │  │  │  ├─ test_create.py
   │     │  │  │  │  ├─ test_create_with_bigquery.py
   │     │  │  │  │  ├─ test_create_with_file.py
   │     │  │  │  │  ├─ test_create_with_gcs.py
   │     │  │  │  │  ├─ test_create_with_inlined_requests.py
   │     │  │  │  │  ├─ test_create_with_vertex_dataset.py
   │     │  │  │  │  ├─ test_delete.py
   │     │  │  │  │  ├─ test_embedding.py
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  ├─ test_list.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ caches
   │     │  │  │  │  ├─ constants.py
   │     │  │  │  │  ├─ test_create.py
   │     │  │  │  │  ├─ test_create_custom_url.py
   │     │  │  │  │  ├─ test_delete.py
   │     │  │  │  │  ├─ test_delete_custom_url.py
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  ├─ test_get_custom_url.py
   │     │  │  │  │  ├─ test_list.py
   │     │  │  │  │  ├─ test_update.py
   │     │  │  │  │  ├─ test_update_custom_url.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ chats
   │     │  │  │  │  ├─ test_get_history.py
   │     │  │  │  │  ├─ test_send_message.py
   │     │  │  │  │  ├─ test_validate_response.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ client
   │     │  │  │  │  ├─ test_async_stream.py
   │     │  │  │  │  ├─ test_client_close.py
   │     │  │  │  │  ├─ test_client_initialization.py
   │     │  │  │  │  ├─ test_client_requests.py
   │     │  │  │  │  ├─ test_custom_client.py
   │     │  │  │  │  ├─ test_http_options.py
   │     │  │  │  │  ├─ test_replay_client_equality.py
   │     │  │  │  │  ├─ test_retries.py
   │     │  │  │  │  ├─ test_upload_errors.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ common
   │     │  │  │  │  ├─ test_common.py
   │     │  │  │  │  ├─ test_duck_type.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ documents
   │     │  │  │  │  ├─ test_delete.py
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  ├─ test_list.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ errors
   │     │  │  │  │  ├─ test_api_error.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ files
   │     │  │  │  │  ├─ test_delete.py
   │     │  │  │  │  ├─ test_download.py
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  ├─ test_list.py
   │     │  │  │  │  ├─ test_register.py
   │     │  │  │  │  ├─ test_register_table.py
   │     │  │  │  │  ├─ test_upload.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ file_search_stores
   │     │  │  │  │  ├─ test_create.py
   │     │  │  │  │  ├─ test_delete.py
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  ├─ test_import_file.py
   │     │  │  │  │  ├─ test_list.py
   │     │  │  │  │  ├─ test_multimodal_flow.py
   │     │  │  │  │  ├─ test_upload_to_file_search_store.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ imports
   │     │  │  │  │  └─ test_no_optional_imports.py
   │     │  │  │  ├─ interactions
   │     │  │  │  │  ├─ test_auth.py
   │     │  │  │  │  ├─ test_integration.py
   │     │  │  │  │  ├─ test_paths.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ live
   │     │  │  │  │  ├─ test_live.py
   │     │  │  │  │  ├─ test_live_music.py
   │     │  │  │  │  ├─ test_live_response.py
   │     │  │  │  │  ├─ test_send_client_content.py
   │     │  │  │  │  ├─ test_send_realtime_input.py
   │     │  │  │  │  ├─ test_send_tool_response.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ local_tokenizer
   │     │  │  │  │  ├─ test_local_tokenizer.py
   │     │  │  │  │  ├─ test_local_tokenizer_loader.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ mcp
   │     │  │  │  │  ├─ test_has_mcp_tool_usage.py
   │     │  │  │  │  ├─ test_mcp_to_gemini_tools.py
   │     │  │  │  │  ├─ test_parse_config_for_mcp_sessions.py
   │     │  │  │  │  ├─ test_parse_config_for_mcp_usage.py
   │     │  │  │  │  ├─ test_set_mcp_usage_header.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ models
   │     │  │  │  │  ├─ constants.py
   │     │  │  │  │  ├─ test_compute_tokens.py
   │     │  │  │  │  ├─ test_count_tokens.py
   │     │  │  │  │  ├─ test_delete.py
   │     │  │  │  │  ├─ test_edit_image.py
   │     │  │  │  │  ├─ test_embed_content.py
   │     │  │  │  │  ├─ test_function_call_streaming.py
   │     │  │  │  │  ├─ test_generate_content.py
   │     │  │  │  │  ├─ test_generate_content_cached_content.py
   │     │  │  │  │  ├─ test_generate_content_config_zero_value.py
   │     │  │  │  │  ├─ test_generate_content_from_apikey.py
   │     │  │  │  │  ├─ test_generate_content_http_options.py
   │     │  │  │  │  ├─ test_generate_content_image_generation.py
   │     │  │  │  │  ├─ test_generate_content_mcp.py
   │     │  │  │  │  ├─ test_generate_content_media_resolution.py
   │     │  │  │  │  ├─ test_generate_content_model.py
   │     │  │  │  │  ├─ test_generate_content_multi_regional.py
   │     │  │  │  │  ├─ test_generate_content_part.py
   │     │  │  │  │  ├─ test_generate_content_thought.py
   │     │  │  │  │  ├─ test_generate_content_tools.py
   │     │  │  │  │  ├─ test_generate_images.py
   │     │  │  │  │  ├─ test_generate_videos.py
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  ├─ test_list.py
   │     │  │  │  │  ├─ test_recontext_image.py
   │     │  │  │  │  ├─ test_segment_image.py
   │     │  │  │  │  ├─ test_update.py
   │     │  │  │  │  ├─ test_upscale_image.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ operations
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ public_samples
   │     │  │  │  │  ├─ test_gemini_text_only.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ pytest_helper.py
   │     │  │  │  ├─ shared
   │     │  │  │  │  ├─ batches
   │     │  │  │  │  │  ├─ test_create_delete.py
   │     │  │  │  │  │  ├─ test_create_get_cancel.py
   │     │  │  │  │  │  ├─ test_list.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ caches
   │     │  │  │  │  │  ├─ test_create_get_delete.py
   │     │  │  │  │  │  ├─ test_create_update_get.py
   │     │  │  │  │  │  ├─ test_list.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ chats
   │     │  │  │  │  │  ├─ test_send_message.py
   │     │  │  │  │  │  ├─ test_send_message_stream.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ files
   │     │  │  │  │  │  ├─ test_list.py
   │     │  │  │  │  │  ├─ test_upload_get_delete.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ models
   │     │  │  │  │  │  ├─ test_compute_tokens.py
   │     │  │  │  │  │  ├─ test_count_tokens.py
   │     │  │  │  │  │  ├─ test_edit_image.py
   │     │  │  │  │  │  ├─ test_embed.py
   │     │  │  │  │  │  ├─ test_generate_content.py
   │     │  │  │  │  │  ├─ test_generate_content_stream.py
   │     │  │  │  │  │  ├─ test_generate_images.py
   │     │  │  │  │  │  ├─ test_generate_videos.py
   │     │  │  │  │  │  ├─ test_list.py
   │     │  │  │  │  │  ├─ test_recontext_image.py
   │     │  │  │  │  │  ├─ test_segment_image.py
   │     │  │  │  │  │  ├─ test_upscale_image.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ tunings
   │     │  │  │  │  │  ├─ test_create.py
   │     │  │  │  │  │  ├─ test_create_get_cancel.py
   │     │  │  │  │  │  ├─ test_list.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tokens
   │     │  │  │  │  ├─ test_create.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ transformers
   │     │  │  │  │  ├─ test_blobs.py
   │     │  │  │  │  ├─ test_bytes.py
   │     │  │  │  │  ├─ test_function_responses.py
   │     │  │  │  │  ├─ test_schema.py
   │     │  │  │  │  ├─ test_t_batch.py
   │     │  │  │  │  ├─ test_t_content.py
   │     │  │  │  │  ├─ test_t_contents.py
   │     │  │  │  │  ├─ test_t_part.py
   │     │  │  │  │  ├─ test_t_parts.py
   │     │  │  │  │  ├─ test_t_tool.py
   │     │  │  │  │  ├─ test_t_tools.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tunings
   │     │  │  │  │  ├─ test_cancel.py
   │     │  │  │  │  ├─ test_end_to_end.py
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  ├─ test_list.py
   │     │  │  │  │  ├─ test_tune.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ types
   │     │  │  │  │  ├─ test_bytes_internal.py
   │     │  │  │  │  ├─ test_bytes_type.py
   │     │  │  │  │  ├─ test_future.py
   │     │  │  │  │  ├─ test_optional_types.py
   │     │  │  │  │  ├─ test_part_type.py
   │     │  │  │  │  ├─ test_schema_from_json_schema.py
   │     │  │  │  │  ├─ test_schema_json_schema.py
   │     │  │  │  │  ├─ test_types.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tokens.py
   │     │  │  ├─ tunings.py
   │     │  │  ├─ types.py
   │     │  │  ├─ version.py
   │     │  │  ├─ _adapters.py
   │     │  │  ├─ _api_client.py
   │     │  │  ├─ _api_module.py
   │     │  │  ├─ _automatic_function_calling_util.py
   │     │  │  ├─ _base_transformers.py
   │     │  │  ├─ _base_url.py
   │     │  │  ├─ _common.py
   │     │  │  ├─ _extra_utils.py
   │     │  │  ├─ _interactions
   │     │  │  │  ├─ resources
   │     │  │  │  │  ├─ agents.py
   │     │  │  │  │  ├─ interactions.py
   │     │  │  │  │  ├─ webhooks.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ types
   │     │  │  │  │  ├─ agent.py
   │     │  │  │  │  ├─ agent_create_params.py
   │     │  │  │  │  ├─ agent_delete_response.py
   │     │  │  │  │  ├─ agent_list_params.py
   │     │  │  │  │  ├─ agent_list_response.py
   │     │  │  │  │  ├─ allowed_tools.py
   │     │  │  │  │  ├─ allowed_tools_param.py
   │     │  │  │  │  ├─ annotation.py
   │     │  │  │  │  ├─ annotation_param.py
   │     │  │  │  │  ├─ audio_content.py
   │     │  │  │  │  ├─ audio_content_param.py
   │     │  │  │  │  ├─ audio_response_format.py
   │     │  │  │  │  ├─ audio_response_format_param.py
   │     │  │  │  │  ├─ code_execution_call_arguments.py
   │     │  │  │  │  ├─ code_execution_call_step.py
   │     │  │  │  │  ├─ code_execution_call_step_param.py
   │     │  │  │  │  ├─ code_execution_result_step.py
   │     │  │  │  │  ├─ code_execution_result_step_param.py
   │     │  │  │  │  ├─ content.py
   │     │  │  │  │  ├─ content_param.py
   │     │  │  │  │  ├─ deep_research_agent_config.py
   │     │  │  │  │  ├─ deep_research_agent_config_param.py
   │     │  │  │  │  ├─ document_content.py
   │     │  │  │  │  ├─ document_content_param.py
   │     │  │  │  │  ├─ dynamic_agent_config.py
   │     │  │  │  │  ├─ dynamic_agent_config_param.py
   │     │  │  │  │  ├─ environment.py
   │     │  │  │  │  ├─ environment_param.py
   │     │  │  │  │  ├─ error_event.py
   │     │  │  │  │  ├─ file_citation.py
   │     │  │  │  │  ├─ file_citation_param.py
   │     │  │  │  │  ├─ file_search_call_step.py
   │     │  │  │  │  ├─ file_search_call_step_param.py
   │     │  │  │  │  ├─ file_search_result_step.py
   │     │  │  │  │  ├─ file_search_result_step_param.py
   │     │  │  │  │  ├─ function.py
   │     │  │  │  │  ├─ function_call_step.py
   │     │  │  │  │  ├─ function_call_step_param.py
   │     │  │  │  │  ├─ function_param.py
   │     │  │  │  │  ├─ function_result_step.py
   │     │  │  │  │  ├─ function_result_step_param.py
   │     │  │  │  │  ├─ generation_config.py
   │     │  │  │  │  ├─ generation_config_param.py
   │     │  │  │  │  ├─ google_maps_call_arguments.py
   │     │  │  │  │  ├─ google_maps_call_step.py
   │     │  │  │  │  ├─ google_maps_call_step_param.py
   │     │  │  │  │  ├─ google_maps_result.py
   │     │  │  │  │  ├─ google_maps_result_step.py
   │     │  │  │  │  ├─ google_maps_result_step_param.py
   │     │  │  │  │  ├─ google_search_call_arguments.py
   │     │  │  │  │  ├─ google_search_call_step.py
   │     │  │  │  │  ├─ google_search_call_step_param.py
   │     │  │  │  │  ├─ google_search_result.py
   │     │  │  │  │  ├─ google_search_result_step.py
   │     │  │  │  │  ├─ google_search_result_step_param.py
   │     │  │  │  │  ├─ image_config.py
   │     │  │  │  │  ├─ image_config_param.py
   │     │  │  │  │  ├─ image_content.py
   │     │  │  │  │  ├─ image_content_param.py
   │     │  │  │  │  ├─ image_response_format.py
   │     │  │  │  │  ├─ image_response_format_param.py
   │     │  │  │  │  ├─ interaction.py
   │     │  │  │  │  ├─ interaction_completed_event.py
   │     │  │  │  │  ├─ interaction_created_event.py
   │     │  │  │  │  ├─ interaction_create_params.py
   │     │  │  │  │  ├─ interaction_get_params.py
   │     │  │  │  │  ├─ interaction_sse_event.py
   │     │  │  │  │  ├─ interaction_status_update.py
   │     │  │  │  │  ├─ mcp_server_tool_call_step.py
   │     │  │  │  │  ├─ mcp_server_tool_call_step_param.py
   │     │  │  │  │  ├─ mcp_server_tool_result_step.py
   │     │  │  │  │  ├─ mcp_server_tool_result_step_param.py
   │     │  │  │  │  ├─ model.py
   │     │  │  │  │  ├─ model_output_step.py
   │     │  │  │  │  ├─ model_output_step_param.py
   │     │  │  │  │  ├─ model_param.py
   │     │  │  │  │  ├─ place_citation.py
   │     │  │  │  │  ├─ place_citation_param.py
   │     │  │  │  │  ├─ signing_secret.py
   │     │  │  │  │  ├─ speech_config.py
   │     │  │  │  │  ├─ speech_config_param.py
   │     │  │  │  │  ├─ step.py
   │     │  │  │  │  ├─ step_delta.py
   │     │  │  │  │  ├─ step_param.py
   │     │  │  │  │  ├─ step_start.py
   │     │  │  │  │  ├─ step_stop.py
   │     │  │  │  │  ├─ text_content.py
   │     │  │  │  │  ├─ text_content_param.py
   │     │  │  │  │  ├─ text_response_format.py
   │     │  │  │  │  ├─ text_response_format_param.py
   │     │  │  │  │  ├─ thinking_level.py
   │     │  │  │  │  ├─ thought_step.py
   │     │  │  │  │  ├─ thought_step_param.py
   │     │  │  │  │  ├─ tool.py
   │     │  │  │  │  ├─ tool_choice_config.py
   │     │  │  │  │  ├─ tool_choice_config_param.py
   │     │  │  │  │  ├─ tool_choice_type.py
   │     │  │  │  │  ├─ tool_param.py
   │     │  │  │  │  ├─ url_citation.py
   │     │  │  │  │  ├─ url_citation_param.py
   │     │  │  │  │  ├─ url_context_call_arguments.py
   │     │  │  │  │  ├─ url_context_call_step.py
   │     │  │  │  │  ├─ url_context_call_step_param.py
   │     │  │  │  │  ├─ url_context_result.py
   │     │  │  │  │  ├─ url_context_result_step.py
   │     │  │  │  │  ├─ url_context_result_step_param.py
   │     │  │  │  │  ├─ usage.py
   │     │  │  │  │  ├─ usage_param.py
   │     │  │  │  │  ├─ user_input_step.py
   │     │  │  │  │  ├─ user_input_step_param.py
   │     │  │  │  │  ├─ video_content.py
   │     │  │  │  │  ├─ video_content_param.py
   │     │  │  │  │  ├─ webhook.py
   │     │  │  │  │  ├─ webhook_config.py
   │     │  │  │  │  ├─ webhook_config_param.py
   │     │  │  │  │  ├─ webhook_create_params.py
   │     │  │  │  │  ├─ webhook_delete_response.py
   │     │  │  │  │  ├─ webhook_list_params.py
   │     │  │  │  │  ├─ webhook_list_response.py
   │     │  │  │  │  ├─ webhook_ping_params.py
   │     │  │  │  │  ├─ webhook_ping_response.py
   │     │  │  │  │  ├─ webhook_rotate_signing_secret_params.py
   │     │  │  │  │  ├─ webhook_rotate_signing_secret_response.py
   │     │  │  │  │  ├─ webhook_update_params.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _base_client.py
   │     │  │  │  ├─ _client.py
   │     │  │  │  ├─ _client_adapter.py
   │     │  │  │  ├─ _compat.py
   │     │  │  │  ├─ _constants.py
   │     │  │  │  ├─ _exceptions.py
   │     │  │  │  ├─ _files.py
   │     │  │  │  ├─ _legacy_lyria.py
   │     │  │  │  ├─ _models.py
   │     │  │  │  ├─ _qs.py
   │     │  │  │  ├─ _resource.py
   │     │  │  │  ├─ _response.py
   │     │  │  │  ├─ _streaming.py
   │     │  │  │  ├─ _types.py
   │     │  │  │  ├─ _utils
   │     │  │  │  │  ├─ _compat.py
   │     │  │  │  │  ├─ _datetime_parse.py
   │     │  │  │  │  ├─ _json.py
   │     │  │  │  │  ├─ _path.py
   │     │  │  │  │  ├─ _proxy.py
   │     │  │  │  │  ├─ _reflection.py
   │     │  │  │  │  ├─ _resources_proxy.py
   │     │  │  │  │  ├─ _streams.py
   │     │  │  │  │  ├─ _sync.py
   │     │  │  │  │  ├─ _transform.py
   │     │  │  │  │  ├─ _typing.py
   │     │  │  │  │  ├─ _utils.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _version.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _live_converters.py
   │     │  │  ├─ _local_tokenizer_loader.py
   │     │  │  ├─ _mcp_utils.py
   │     │  │  ├─ _operations_converters.py
   │     │  │  ├─ _replay_api_client.py
   │     │  │  ├─ _test_api_client.py
   │     │  │  ├─ _tokens_converters.py
   │     │  │  ├─ _transformers.py
   │     │  │  └─ __init__.py
   │     │  ├─ logging
   │     │  │  └─ type
   │     │  │     ├─ http_request.proto
   │     │  │     ├─ http_request_pb2.py
   │     │  │     ├─ http_request_pb2.pyi
   │     │  │     ├─ log_severity.proto
   │     │  │     ├─ log_severity_pb2.py
   │     │  │     └─ log_severity_pb2.pyi
   │     │  ├─ longrunning
   │     │  │  ├─ operations_grpc.py
   │     │  │  ├─ operations_grpc_pb2.py
   │     │  │  ├─ operations_pb2.py
   │     │  │  ├─ operations_pb2_grpc.py
   │     │  │  ├─ operations_proto.proto
   │     │  │  ├─ operations_proto.py
   │     │  │  ├─ operations_proto_pb2.py
   │     │  │  └─ operations_proto_pb2.pyi
   │     │  ├─ oauth2
   │     │  │  ├─ challenges.py
   │     │  │  ├─ credentials.py
   │     │  │  ├─ gdch_credentials.py
   │     │  │  ├─ id_token.py
   │     │  │  ├─ py.typed
   │     │  │  ├─ reauth.py
   │     │  │  ├─ service_account.py
   │     │  │  ├─ sts.py
   │     │  │  ├─ utils.py
   │     │  │  ├─ webauthn_handler.py
   │     │  │  ├─ webauthn_handler_factory.py
   │     │  │  ├─ webauthn_types.py
   │     │  │  ├─ _client.py
   │     │  │  ├─ _client_async.py
   │     │  │  ├─ _credentials_async.py
   │     │  │  ├─ _id_token_async.py
   │     │  │  ├─ _reauth_async.py
   │     │  │  ├─ _service_account_async.py
   │     │  │  └─ __init__.py
   │     │  ├─ protobuf
   │     │  │  ├─ any.py
   │     │  │  ├─ any_pb2.py
   │     │  │  ├─ api_pb2.py
   │     │  │  ├─ compiler
   │     │  │  │  ├─ plugin_pb2.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ descriptor.py
   │     │  │  ├─ descriptor_database.py
   │     │  │  ├─ descriptor_pb2.py
   │     │  │  ├─ descriptor_pool.py
   │     │  │  ├─ duration.py
   │     │  │  ├─ duration_pb2.py
   │     │  │  ├─ empty_pb2.py
   │     │  │  ├─ field_mask_pb2.py
   │     │  │  ├─ internal
   │     │  │  │  ├─ api_implementation.py
   │     │  │  │  ├─ builder.py
   │     │  │  │  ├─ containers.py
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  ├─ enum_type_wrapper.py
   │     │  │  │  ├─ extension_dict.py
   │     │  │  │  ├─ field_mask.py
   │     │  │  │  ├─ message_listener.py
   │     │  │  │  ├─ python_edition_defaults.py
   │     │  │  │  ├─ python_message.py
   │     │  │  │  ├─ testing_refleaks.py
   │     │  │  │  ├─ type_checkers.py
   │     │  │  │  ├─ well_known_types.py
   │     │  │  │  ├─ wire_format.py
   │     │  │  │  ├─ _parameterized.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ json_format.py
   │     │  │  ├─ message.py
   │     │  │  ├─ message_factory.py
   │     │  │  ├─ proto.py
   │     │  │  ├─ proto_builder.py
   │     │  │  ├─ proto_json.py
   │     │  │  ├─ pyext
   │     │  │  │  ├─ cpp_message.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ reflection.py
   │     │  │  ├─ runtime_version.py
   │     │  │  ├─ service.py
   │     │  │  ├─ service_reflection.py
   │     │  │  ├─ source_context_pb2.py
   │     │  │  ├─ struct_pb2.py
   │     │  │  ├─ symbol_database.py
   │     │  │  ├─ testdata
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ text_encoding.py
   │     │  │  ├─ text_format.py
   │     │  │  ├─ timestamp.py
   │     │  │  ├─ timestamp_pb2.py
   │     │  │  ├─ type_pb2.py
   │     │  │  ├─ unknown_fields.py
   │     │  │  ├─ util
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ wrappers_pb2.py
   │     │  │  └─ __init__.py
   │     │  ├─ rpc
   │     │  │  ├─ code.proto
   │     │  │  ├─ code_pb2.py
   │     │  │  ├─ code_pb2.pyi
   │     │  │  ├─ context
   │     │  │  │  ├─ attribute_context.proto
   │     │  │  │  ├─ attribute_context_pb2.py
   │     │  │  │  ├─ attribute_context_pb2.pyi
   │     │  │  │  ├─ audit_context.proto
   │     │  │  │  ├─ audit_context_pb2.py
   │     │  │  │  └─ audit_context_pb2.pyi
   │     │  │  ├─ error_details.proto
   │     │  │  ├─ error_details_pb2.py
   │     │  │  ├─ error_details_pb2.pyi
   │     │  │  ├─ http.proto
   │     │  │  ├─ http_pb2.py
   │     │  │  ├─ http_pb2.pyi
   │     │  │  ├─ status.proto
   │     │  │  ├─ status_pb2.py
   │     │  │  └─ status_pb2.pyi
   │     │  ├─ type
   │     │  │  ├─ calendar_period.proto
   │     │  │  ├─ calendar_period_pb2.py
   │     │  │  ├─ calendar_period_pb2.pyi
   │     │  │  ├─ color.proto
   │     │  │  ├─ color_pb2.py
   │     │  │  ├─ color_pb2.pyi
   │     │  │  ├─ date.proto
   │     │  │  ├─ datetime.proto
   │     │  │  ├─ datetime_pb2.py
   │     │  │  ├─ datetime_pb2.pyi
   │     │  │  ├─ date_pb2.py
   │     │  │  ├─ date_pb2.pyi
   │     │  │  ├─ dayofweek.proto
   │     │  │  ├─ dayofweek_pb2.py
   │     │  │  ├─ dayofweek_pb2.pyi
   │     │  │  ├─ decimal.proto
   │     │  │  ├─ decimal_pb2.py
   │     │  │  ├─ decimal_pb2.pyi
   │     │  │  ├─ expr.proto
   │     │  │  ├─ expr_pb2.py
   │     │  │  ├─ expr_pb2.pyi
   │     │  │  ├─ fraction.proto
   │     │  │  ├─ fraction_pb2.py
   │     │  │  ├─ fraction_pb2.pyi
   │     │  │  ├─ interval.proto
   │     │  │  ├─ interval_pb2.py
   │     │  │  ├─ interval_pb2.pyi
   │     │  │  ├─ latlng.proto
   │     │  │  ├─ latlng_pb2.py
   │     │  │  ├─ latlng_pb2.pyi
   │     │  │  ├─ localized_text.proto
   │     │  │  ├─ localized_text_pb2.py
   │     │  │  ├─ localized_text_pb2.pyi
   │     │  │  ├─ money.proto
   │     │  │  ├─ money_pb2.py
   │     │  │  ├─ money_pb2.pyi
   │     │  │  ├─ month.proto
   │     │  │  ├─ month_pb2.py
   │     │  │  ├─ month_pb2.pyi
   │     │  │  ├─ phone_number.proto
   │     │  │  ├─ phone_number_pb2.py
   │     │  │  ├─ phone_number_pb2.pyi
   │     │  │  ├─ postal_address.proto
   │     │  │  ├─ postal_address_pb2.py
   │     │  │  ├─ postal_address_pb2.pyi
   │     │  │  ├─ quaternion.proto
   │     │  │  ├─ quaternion_pb2.py
   │     │  │  ├─ quaternion_pb2.pyi
   │     │  │  ├─ timeofday.proto
   │     │  │  ├─ timeofday_pb2.py
   │     │  │  └─ timeofday_pb2.pyi
   │     │  └─ _upb
   │     │     └─ _message.pyd
   │     ├─ googleapiclient
   │     │  ├─ channel.py
   │     │  ├─ discovery.py
   │     │  ├─ discovery_cache
   │     │  │  ├─ appengine_memcache.py
   │     │  │  ├─ base.py
   │     │  │  ├─ documents
   │     │  │  │  ├─ abusiveexperiencereport.v1.json
   │     │  │  │  ├─ acceleratedmobilepageurl.v1.json
   │     │  │  │  ├─ accessapproval.v1.json
   │     │  │  │  ├─ accesscontextmanager.v1.json
   │     │  │  │  ├─ accesscontextmanager.v1beta.json
   │     │  │  │  ├─ acmedns.v1.json
   │     │  │  │  ├─ addressvalidation.v1.json
   │     │  │  │  ├─ adexchangebuyer.v1.2.json
   │     │  │  │  ├─ adexchangebuyer.v1.3.json
   │     │  │  │  ├─ adexchangebuyer.v1.4.json
   │     │  │  │  ├─ adexchangebuyer2.v2beta1.json
   │     │  │  │  ├─ adexperiencereport.v1.json
   │     │  │  │  ├─ admin.datatransferv1.json
   │     │  │  │  ├─ admin.datatransfer_v1.json
   │     │  │  │  ├─ admin.directoryv1.json
   │     │  │  │  ├─ admin.directory_v1.json
   │     │  │  │  ├─ admin.reportsv1.json
   │     │  │  │  ├─ admin.reports_v1.json
   │     │  │  │  ├─ admob.v1.json
   │     │  │  │  ├─ admob.v1beta.json
   │     │  │  │  ├─ adsense.v2.json
   │     │  │  │  ├─ adsensehost.v4.1.json
   │     │  │  │  ├─ adsenseplatform.v1.json
   │     │  │  │  ├─ adsenseplatform.v1alpha.json
   │     │  │  │  ├─ advisorynotifications.v1.json
   │     │  │  │  ├─ agentregistry.v1alpha.json
   │     │  │  │  ├─ aiplatform.v1.json
   │     │  │  │  ├─ aiplatform.v1beta1.json
   │     │  │  │  ├─ airquality.v1.json
   │     │  │  │  ├─ alertcenter.v1beta1.json
   │     │  │  │  ├─ alloydb.v1.json
   │     │  │  │  ├─ alloydb.v1alpha.json
   │     │  │  │  ├─ alloydb.v1beta.json
   │     │  │  │  ├─ analytics.v3.json
   │     │  │  │  ├─ analyticsadmin.v1alpha.json
   │     │  │  │  ├─ analyticsadmin.v1beta.json
   │     │  │  │  ├─ analyticsdata.v1alpha.json
   │     │  │  │  ├─ analyticsdata.v1beta.json
   │     │  │  │  ├─ analyticshub.v1.json
   │     │  │  │  ├─ analyticshub.v1beta1.json
   │     │  │  │  ├─ analyticsreporting.v4.json
   │     │  │  │  ├─ androiddeviceprovisioning.v1.json
   │     │  │  │  ├─ androidenterprise.v1.json
   │     │  │  │  ├─ androidmanagement.v1.json
   │     │  │  │  ├─ androidpublisher.v3.json
   │     │  │  │  ├─ apigateway.v1.json
   │     │  │  │  ├─ apigateway.v1beta.json
   │     │  │  │  ├─ apigee.v1.json
   │     │  │  │  ├─ apigeeregistry.v1.json
   │     │  │  │  ├─ apihub.v1.json
   │     │  │  │  ├─ apikeys.v2.json
   │     │  │  │  ├─ apim.v1alpha.json
   │     │  │  │  ├─ appengine.v1.json
   │     │  │  │  ├─ appengine.v1alpha.json
   │     │  │  │  ├─ appengine.v1beta.json
   │     │  │  │  ├─ appengine.v1beta4.json
   │     │  │  │  ├─ appengine.v1beta5.json
   │     │  │  │  ├─ apphub.v1.json
   │     │  │  │  ├─ apphub.v1alpha.json
   │     │  │  │  ├─ appsmarket.v2.json
   │     │  │  │  ├─ area120tables.v1alpha1.json
   │     │  │  │  ├─ areainsights.v1.json
   │     │  │  │  ├─ artifactregistry.v1.json
   │     │  │  │  ├─ artifactregistry.v1beta1.json
   │     │  │  │  ├─ artifactregistry.v1beta2.json
   │     │  │  │  ├─ assuredworkloads.v1.json
   │     │  │  │  ├─ assuredworkloads.v1beta1.json
   │     │  │  │  ├─ authorizedbuyersmarketplace.v1.json
   │     │  │  │  ├─ authorizedbuyersmarketplace.v1alpha.json
   │     │  │  │  ├─ authorizedbuyersmarketplace.v1beta.json
   │     │  │  │  ├─ backupdr.v1.json
   │     │  │  │  ├─ baremetalsolution.v1.json
   │     │  │  │  ├─ baremetalsolution.v1alpha1.json
   │     │  │  │  ├─ baremetalsolution.v2.json
   │     │  │  │  ├─ batch.v1.json
   │     │  │  │  ├─ beyondcorp.v1.json
   │     │  │  │  ├─ beyondcorp.v1alpha.json
   │     │  │  │  ├─ biglake.v1.json
   │     │  │  │  ├─ bigquery.v2.json
   │     │  │  │  ├─ bigqueryconnection.v1.json
   │     │  │  │  ├─ bigqueryconnection.v1beta1.json
   │     │  │  │  ├─ bigquerydatapolicy.v1.json
   │     │  │  │  ├─ bigquerydatapolicy.v2.json
   │     │  │  │  ├─ bigquerydatatransfer.v1.json
   │     │  │  │  ├─ bigqueryreservation.v1.json
   │     │  │  │  ├─ bigqueryreservation.v1alpha2.json
   │     │  │  │  ├─ bigqueryreservation.v1beta1.json
   │     │  │  │  ├─ bigtableadmin.v1.json
   │     │  │  │  ├─ bigtableadmin.v2.json
   │     │  │  │  ├─ billingbudgets.v1.json
   │     │  │  │  ├─ billingbudgets.v1beta1.json
   │     │  │  │  ├─ binaryauthorization.v1.json
   │     │  │  │  ├─ binaryauthorization.v1beta1.json
   │     │  │  │  ├─ blockchainnodeengine.v1.json
   │     │  │  │  ├─ blogger.v2.json
   │     │  │  │  ├─ blogger.v3.json
   │     │  │  │  ├─ books.v1.json
   │     │  │  │  ├─ businessprofileperformance.v1.json
   │     │  │  │  ├─ calendar.v3.json
   │     │  │  │  ├─ certificatemanager.v1.json
   │     │  │  │  ├─ ces.v1.json
   │     │  │  │  ├─ ces.v1beta.json
   │     │  │  │  ├─ chat.v1.json
   │     │  │  │  ├─ checks.v1alpha.json
   │     │  │  │  ├─ chromemanagement.v1.json
   │     │  │  │  ├─ chromepolicy.v1.json
   │     │  │  │  ├─ chromeuxreport.v1.json
   │     │  │  │  ├─ chromewebstore.v1.1.json
   │     │  │  │  ├─ chromewebstore.v2.json
   │     │  │  │  ├─ civicinfo.v2.json
   │     │  │  │  ├─ classroom.v1.json
   │     │  │  │  ├─ cloudasset.v1.json
   │     │  │  │  ├─ cloudasset.v1beta1.json
   │     │  │  │  ├─ cloudasset.v1p1beta1.json
   │     │  │  │  ├─ cloudasset.v1p4beta1.json
   │     │  │  │  ├─ cloudasset.v1p5beta1.json
   │     │  │  │  ├─ cloudasset.v1p7beta1.json
   │     │  │  │  ├─ cloudbilling.v1.json
   │     │  │  │  ├─ cloudbilling.v1beta.json
   │     │  │  │  ├─ cloudbuild.v1.json
   │     │  │  │  ├─ cloudbuild.v1alpha1.json
   │     │  │  │  ├─ cloudbuild.v1alpha2.json
   │     │  │  │  ├─ cloudbuild.v1beta1.json
   │     │  │  │  ├─ cloudbuild.v2.json
   │     │  │  │  ├─ cloudchannel.v1.json
   │     │  │  │  ├─ cloudcommerceprocurement.v1.json
   │     │  │  │  ├─ cloudcontrolspartner.v1.json
   │     │  │  │  ├─ cloudcontrolspartner.v1beta.json
   │     │  │  │  ├─ clouddebugger.v2.json
   │     │  │  │  ├─ clouddeploy.v1.json
   │     │  │  │  ├─ clouderrorreporting.v1beta1.json
   │     │  │  │  ├─ cloudfunctions.v1.json
   │     │  │  │  ├─ cloudfunctions.v2.json
   │     │  │  │  ├─ cloudfunctions.v2alpha.json
   │     │  │  │  ├─ cloudfunctions.v2beta.json
   │     │  │  │  ├─ cloudidentity.v1.json
   │     │  │  │  ├─ cloudidentity.v1beta1.json
   │     │  │  │  ├─ cloudiot.v1.json
   │     │  │  │  ├─ cloudkms.v1.json
   │     │  │  │  ├─ cloudlocationfinder.v1.json
   │     │  │  │  ├─ cloudlocationfinder.v1alpha.json
   │     │  │  │  ├─ cloudnumberregistry.v1alpha.json
   │     │  │  │  ├─ cloudprofiler.v2.json
   │     │  │  │  ├─ cloudresourcemanager.v1.json
   │     │  │  │  ├─ cloudresourcemanager.v1beta1.json
   │     │  │  │  ├─ cloudresourcemanager.v2.json
   │     │  │  │  ├─ cloudresourcemanager.v2beta1.json
   │     │  │  │  ├─ cloudresourcemanager.v3.json
   │     │  │  │  ├─ cloudscheduler.v1.json
   │     │  │  │  ├─ cloudscheduler.v1beta1.json
   │     │  │  │  ├─ cloudsearch.v1.json
   │     │  │  │  ├─ cloudshell.v1.json
   │     │  │  │  ├─ cloudshell.v1alpha1.json
   │     │  │  │  ├─ cloudsupport.v2.json
   │     │  │  │  ├─ cloudsupport.v2beta.json
   │     │  │  │  ├─ cloudtasks.v2.json
   │     │  │  │  ├─ cloudtasks.v2beta2.json
   │     │  │  │  ├─ cloudtasks.v2beta3.json
   │     │  │  │  ├─ cloudtrace.v1.json
   │     │  │  │  ├─ cloudtrace.v2.json
   │     │  │  │  ├─ cloudtrace.v2beta1.json
   │     │  │  │  ├─ composer.v1.json
   │     │  │  │  ├─ composer.v1beta1.json
   │     │  │  │  ├─ compute.alpha.json
   │     │  │  │  ├─ compute.beta.json
   │     │  │  │  ├─ compute.v1.json
   │     │  │  │  ├─ config.v1.json
   │     │  │  │  ├─ connectors.v1.json
   │     │  │  │  ├─ connectors.v2.json
   │     │  │  │  ├─ contactcenteraiplatform.v1alpha1.json
   │     │  │  │  ├─ contactcenterinsights.v1.json
   │     │  │  │  ├─ container.v1.json
   │     │  │  │  ├─ container.v1beta1.json
   │     │  │  │  ├─ containeranalysis.v1.json
   │     │  │  │  ├─ containeranalysis.v1alpha1.json
   │     │  │  │  ├─ containeranalysis.v1beta1.json
   │     │  │  │  ├─ content.v2.1.json
   │     │  │  │  ├─ content.v2.json
   │     │  │  │  ├─ contentwarehouse.v1.json
   │     │  │  │  ├─ css.v1.json
   │     │  │  │  ├─ customsearch.v1.json
   │     │  │  │  ├─ datacatalog.v1.json
   │     │  │  │  ├─ datacatalog.v1beta1.json
   │     │  │  │  ├─ dataflow.v1b3.json
   │     │  │  │  ├─ dataform.v1.json
   │     │  │  │  ├─ dataform.v1beta1.json
   │     │  │  │  ├─ datafusion.v1.json
   │     │  │  │  ├─ datafusion.v1beta1.json
   │     │  │  │  ├─ datalabeling.v1beta1.json
   │     │  │  │  ├─ datalineage.v1.json
   │     │  │  │  ├─ datamanager.v1.json
   │     │  │  │  ├─ datamigration.v1.json
   │     │  │  │  ├─ datamigration.v1beta1.json
   │     │  │  │  ├─ datapipelines.v1.json
   │     │  │  │  ├─ dataplex.v1.json
   │     │  │  │  ├─ dataportability.v1.json
   │     │  │  │  ├─ dataportability.v1beta.json
   │     │  │  │  ├─ dataproc.v1.json
   │     │  │  │  ├─ dataproc.v1beta2.json
   │     │  │  │  ├─ datastore.v1.json
   │     │  │  │  ├─ datastore.v1beta1.json
   │     │  │  │  ├─ datastore.v1beta3.json
   │     │  │  │  ├─ datastream.v1.json
   │     │  │  │  ├─ datastream.v1alpha1.json
   │     │  │  │  ├─ deploymentmanager.alpha.json
   │     │  │  │  ├─ deploymentmanager.v2.json
   │     │  │  │  ├─ deploymentmanager.v2beta.json
   │     │  │  │  ├─ developerconnect.v1.json
   │     │  │  │  ├─ developerknowledge.v1.json
   │     │  │  │  ├─ developerknowledge.v1alpha.json
   │     │  │  │  ├─ dfareporting.v3.3.json
   │     │  │  │  ├─ dfareporting.v3.4.json
   │     │  │  │  ├─ dfareporting.v3.5.json
   │     │  │  │  ├─ dfareporting.v4.json
   │     │  │  │  ├─ dfareporting.v5.json
   │     │  │  │  ├─ dialogflow.v2.json
   │     │  │  │  ├─ dialogflow.v2beta1.json
   │     │  │  │  ├─ dialogflow.v3.json
   │     │  │  │  ├─ dialogflow.v3beta1.json
   │     │  │  │  ├─ digitalassetlinks.v1.json
   │     │  │  │  ├─ discovery.v1.json
   │     │  │  │  ├─ discoveryengine.v1.json
   │     │  │  │  ├─ discoveryengine.v1alpha.json
   │     │  │  │  ├─ discoveryengine.v1beta.json
   │     │  │  │  ├─ displayvideo.v1.json
   │     │  │  │  ├─ displayvideo.v2.json
   │     │  │  │  ├─ displayvideo.v3.json
   │     │  │  │  ├─ displayvideo.v4.json
   │     │  │  │  ├─ dlp.v2.json
   │     │  │  │  ├─ dns.v1.json
   │     │  │  │  ├─ dns.v1beta2.json
   │     │  │  │  ├─ dns.v2.json
   │     │  │  │  ├─ docs.v1.json
   │     │  │  │  ├─ documentai.v1.json
   │     │  │  │  ├─ documentai.v1beta2.json
   │     │  │  │  ├─ documentai.v1beta3.json
   │     │  │  │  ├─ domains.v1.json
   │     │  │  │  ├─ domains.v1alpha2.json
   │     │  │  │  ├─ domains.v1beta1.json
   │     │  │  │  ├─ domainsrdap.v1.json
   │     │  │  │  ├─ doubleclickbidmanager.v1.1.json
   │     │  │  │  ├─ doubleclickbidmanager.v1.json
   │     │  │  │  ├─ doubleclickbidmanager.v2.json
   │     │  │  │  ├─ doubleclicksearch.v2.json
   │     │  │  │  ├─ drive.v2.json
   │     │  │  │  ├─ drive.v3.json
   │     │  │  │  ├─ driveactivity.v2.json
   │     │  │  │  ├─ drivelabels.v2.json
   │     │  │  │  ├─ drivelabels.v2beta.json
   │     │  │  │  ├─ essentialcontacts.v1.json
   │     │  │  │  ├─ eventarc.v1.json
   │     │  │  │  ├─ eventarc.v1beta1.json
   │     │  │  │  ├─ factchecktools.v1alpha1.json
   │     │  │  │  ├─ fcm.v1.json
   │     │  │  │  ├─ fcmdata.v1beta1.json
   │     │  │  │  ├─ file.v1.json
   │     │  │  │  ├─ file.v1beta1.json
   │     │  │  │  ├─ firebase.v1beta1.json
   │     │  │  │  ├─ firebaseappcheck.v1.json
   │     │  │  │  ├─ firebaseappcheck.v1beta.json
   │     │  │  │  ├─ firebaseapphosting.v1.json
   │     │  │  │  ├─ firebaseapphosting.v1beta.json
   │     │  │  │  ├─ firebasedatabase.v1beta.json
   │     │  │  │  ├─ firebasedataconnect.v1.json
   │     │  │  │  ├─ firebasedataconnect.v1beta.json
   │     │  │  │  ├─ firebasedynamiclinks.v1.json
   │     │  │  │  ├─ firebasehosting.v1.json
   │     │  │  │  ├─ firebasehosting.v1beta1.json
   │     │  │  │  ├─ firebaseml.v1.json
   │     │  │  │  ├─ firebaseml.v1beta2.json
   │     │  │  │  ├─ firebaseml.v2beta.json
   │     │  │  │  ├─ firebaserules.v1.json
   │     │  │  │  ├─ firebasestorage.v1beta.json
   │     │  │  │  ├─ firestore.v1.json
   │     │  │  │  ├─ firestore.v1beta1.json
   │     │  │  │  ├─ firestore.v1beta2.json
   │     │  │  │  ├─ fitness.v1.json
   │     │  │  │  ├─ forms.v1.json
   │     │  │  │  ├─ games.v1.json
   │     │  │  │  ├─ gamesConfiguration.v1configuration.json
   │     │  │  │  ├─ gameservices.v1.json
   │     │  │  │  ├─ gameservices.v1beta.json
   │     │  │  │  ├─ gamesManagement.v1management.json
   │     │  │  │  ├─ genomics.v1.json
   │     │  │  │  ├─ genomics.v1alpha2.json
   │     │  │  │  ├─ genomics.v2alpha1.json
   │     │  │  │  ├─ gkebackup.v1.json
   │     │  │  │  ├─ gkehub.v1.json
   │     │  │  │  ├─ gkehub.v1alpha.json
   │     │  │  │  ├─ gkehub.v1alpha2.json
   │     │  │  │  ├─ gkehub.v1beta.json
   │     │  │  │  ├─ gkehub.v1beta1.json
   │     │  │  │  ├─ gkehub.v2.json
   │     │  │  │  ├─ gkehub.v2alpha.json
   │     │  │  │  ├─ gkehub.v2beta.json
   │     │  │  │  ├─ gkeonprem.v1.json
   │     │  │  │  ├─ gmail.v1.json
   │     │  │  │  ├─ gmailpostmastertools.v1.json
   │     │  │  │  ├─ gmailpostmastertools.v1beta1.json
   │     │  │  │  ├─ gmailpostmastertools.v2.json
   │     │  │  │  ├─ groupsmigration.v1.json
   │     │  │  │  ├─ groupssettings.v1.json
   │     │  │  │  ├─ health.v4.json
   │     │  │  │  ├─ healthcare.v1.json
   │     │  │  │  ├─ healthcare.v1beta1.json
   │     │  │  │  ├─ homegraph.v1.json
   │     │  │  │  ├─ hypercomputecluster.v1.json
   │     │  │  │  ├─ iam.v1.json
   │     │  │  │  ├─ iam.v2.json
   │     │  │  │  ├─ iam.v2beta.json
   │     │  │  │  ├─ iamcredentials.v1.json
   │     │  │  │  ├─ iap.v1.json
   │     │  │  │  ├─ iap.v1beta1.json
   │     │  │  │  ├─ ideahub.v1alpha.json
   │     │  │  │  ├─ ideahub.v1beta.json
   │     │  │  │  ├─ identitytoolkit.v1.json
   │     │  │  │  ├─ identitytoolkit.v2.json
   │     │  │  │  ├─ identitytoolkit.v3.json
   │     │  │  │  ├─ ids.v1.json
   │     │  │  │  ├─ index.json
   │     │  │  │  ├─ indexing.v3.json
   │     │  │  │  ├─ integrations.v1.json
   │     │  │  │  ├─ integrations.v1alpha.json
   │     │  │  │  ├─ jobs.v2.json
   │     │  │  │  ├─ jobs.v3.json
   │     │  │  │  ├─ jobs.v3p1beta1.json
   │     │  │  │  ├─ jobs.v4.json
   │     │  │  │  ├─ keep.v1.json
   │     │  │  │  ├─ kgsearch.v1.json
   │     │  │  │  ├─ kmsinventory.v1.json
   │     │  │  │  ├─ language.v1.json
   │     │  │  │  ├─ language.v1beta1.json
   │     │  │  │  ├─ language.v1beta2.json
   │     │  │  │  ├─ language.v2.json
   │     │  │  │  ├─ libraryagent.v1.json
   │     │  │  │  ├─ licensing.v1.json
   │     │  │  │  ├─ lifesciences.v2beta.json
   │     │  │  │  ├─ localservices.v1.json
   │     │  │  │  ├─ logging.v2.json
   │     │  │  │  ├─ looker.v1.json
   │     │  │  │  ├─ managedidentities.v1.json
   │     │  │  │  ├─ managedidentities.v1alpha1.json
   │     │  │  │  ├─ managedidentities.v1beta1.json
   │     │  │  │  ├─ managedkafka.v1.json
   │     │  │  │  ├─ manufacturers.v1.json
   │     │  │  │  ├─ marketingplatformadmin.v1alpha.json
   │     │  │  │  ├─ meet.v2.json
   │     │  │  │  ├─ memcache.v1.json
   │     │  │  │  ├─ memcache.v1beta2.json
   │     │  │  │  ├─ merchantapi.accounts_v1.json
   │     │  │  │  ├─ merchantapi.accounts_v1beta.json
   │     │  │  │  ├─ merchantapi.conversions_v1.json
   │     │  │  │  ├─ merchantapi.conversions_v1beta.json
   │     │  │  │  ├─ merchantapi.datasources_v1.json
   │     │  │  │  ├─ merchantapi.datasources_v1beta.json
   │     │  │  │  ├─ merchantapi.inventories_v1.json
   │     │  │  │  ├─ merchantapi.inventories_v1beta.json
   │     │  │  │  ├─ merchantapi.issueresolution_v1.json
   │     │  │  │  ├─ merchantapi.issueresolution_v1beta.json
   │     │  │  │  ├─ merchantapi.lfp_v1.json
   │     │  │  │  ├─ merchantapi.lfp_v1beta.json
   │     │  │  │  ├─ merchantapi.notifications_v1.json
   │     │  │  │  ├─ merchantapi.notifications_v1beta.json
   │     │  │  │  ├─ merchantapi.ordertracking_v1.json
   │     │  │  │  ├─ merchantapi.ordertracking_v1beta.json
   │     │  │  │  ├─ merchantapi.products_v1.json
   │     │  │  │  ├─ merchantapi.products_v1beta.json
   │     │  │  │  ├─ merchantapi.promotions_v1.json
   │     │  │  │  ├─ merchantapi.promotions_v1beta.json
   │     │  │  │  ├─ merchantapi.quota_v1.json
   │     │  │  │  ├─ merchantapi.quota_v1beta.json
   │     │  │  │  ├─ merchantapi.reports_v1.json
   │     │  │  │  ├─ merchantapi.reports_v1beta.json
   │     │  │  │  ├─ merchantapi.reviews_v1beta.json
   │     │  │  │  ├─ metastore.v1.json
   │     │  │  │  ├─ metastore.v1alpha.json
   │     │  │  │  ├─ metastore.v1beta.json
   │     │  │  │  ├─ metastore.v2.json
   │     │  │  │  ├─ metastore.v2alpha.json
   │     │  │  │  ├─ metastore.v2beta.json
   │     │  │  │  ├─ migrationcenter.v1.json
   │     │  │  │  ├─ migrationcenter.v1alpha1.json
   │     │  │  │  ├─ ml.v1.json
   │     │  │  │  ├─ monitoring.v1.json
   │     │  │  │  ├─ monitoring.v3.json
   │     │  │  │  ├─ mybusinessaccountmanagement.v1.json
   │     │  │  │  ├─ mybusinessbusinesscalls.v1.json
   │     │  │  │  ├─ mybusinessbusinessinformation.v1.json
   │     │  │  │  ├─ mybusinesslodging.v1.json
   │     │  │  │  ├─ mybusinessnotifications.v1.json
   │     │  │  │  ├─ mybusinessplaceactions.v1.json
   │     │  │  │  ├─ mybusinessqanda.v1.json
   │     │  │  │  ├─ mybusinessverifications.v1.json
   │     │  │  │  ├─ netapp.v1.json
   │     │  │  │  ├─ netapp.v1beta1.json
   │     │  │  │  ├─ networkconnectivity.v1.json
   │     │  │  │  ├─ networkconnectivity.v1alpha1.json
   │     │  │  │  ├─ networkmanagement.v1.json
   │     │  │  │  ├─ networkmanagement.v1beta1.json
   │     │  │  │  ├─ networksecurity.v1.json
   │     │  │  │  ├─ networksecurity.v1beta1.json
   │     │  │  │  ├─ networkservices.v1.json
   │     │  │  │  ├─ networkservices.v1beta1.json
   │     │  │  │  ├─ notebooks.v1.json
   │     │  │  │  ├─ notebooks.v2.json
   │     │  │  │  ├─ oauth2.v2.json
   │     │  │  │  ├─ observability.v1.json
   │     │  │  │  ├─ ondemandscanning.v1.json
   │     │  │  │  ├─ ondemandscanning.v1beta1.json
   │     │  │  │  ├─ oracledatabase.v1.json
   │     │  │  │  ├─ orgpolicy.v2.json
   │     │  │  │  ├─ osconfig.v1.json
   │     │  │  │  ├─ osconfig.v1alpha.json
   │     │  │  │  ├─ osconfig.v1beta.json
   │     │  │  │  ├─ osconfig.v2.json
   │     │  │  │  ├─ osconfig.v2beta.json
   │     │  │  │  ├─ oslogin.v1.json
   │     │  │  │  ├─ oslogin.v1alpha.json
   │     │  │  │  ├─ oslogin.v1beta.json
   │     │  │  │  ├─ pagespeedonline.v5.json
   │     │  │  │  ├─ parallelstore.v1.json
   │     │  │  │  ├─ parallelstore.v1beta.json
   │     │  │  │  ├─ parametermanager.v1.json
   │     │  │  │  ├─ paymentsresellersubscription.v1.json
   │     │  │  │  ├─ people.v1.json
   │     │  │  │  ├─ places.v1.json
   │     │  │  │  ├─ playablelocations.v3.json
   │     │  │  │  ├─ playcustomapp.v1.json
   │     │  │  │  ├─ playdeveloperreporting.v1alpha1.json
   │     │  │  │  ├─ playdeveloperreporting.v1beta1.json
   │     │  │  │  ├─ playgrouping.v1alpha1.json
   │     │  │  │  ├─ playintegrity.v1.json
   │     │  │  │  ├─ policyanalyzer.v1.json
   │     │  │  │  ├─ policyanalyzer.v1beta1.json
   │     │  │  │  ├─ policysimulator.v1.json
   │     │  │  │  ├─ policysimulator.v1alpha.json
   │     │  │  │  ├─ policysimulator.v1beta.json
   │     │  │  │  ├─ policysimulator.v1beta1.json
   │     │  │  │  ├─ policytroubleshooter.v1.json
   │     │  │  │  ├─ policytroubleshooter.v1beta.json
   │     │  │  │  ├─ policytroubleshooter.v3.json
   │     │  │  │  ├─ policytroubleshooter.v3beta.json
   │     │  │  │  ├─ pollen.v1.json
   │     │  │  │  ├─ poly.v1.json
   │     │  │  │  ├─ privateca.v1.json
   │     │  │  │  ├─ privateca.v1beta1.json
   │     │  │  │  ├─ prod_tt_sasportal.v1alpha1.json
   │     │  │  │  ├─ publicca.v1.json
   │     │  │  │  ├─ publicca.v1alpha1.json
   │     │  │  │  ├─ publicca.v1beta1.json
   │     │  │  │  ├─ pubsub.v1.json
   │     │  │  │  ├─ pubsub.v1beta1a.json
   │     │  │  │  ├─ pubsub.v1beta2.json
   │     │  │  │  ├─ pubsublite.v1.json
   │     │  │  │  ├─ rapidmigrationassessment.v1.json
   │     │  │  │  ├─ readerrevenuesubscriptionlinking.v1.json
   │     │  │  │  ├─ realtimebidding.v1.json
   │     │  │  │  ├─ realtimebidding.v1alpha.json
   │     │  │  │  ├─ recaptchaenterprise.v1.json
   │     │  │  │  ├─ recommendationengine.v1beta1.json
   │     │  │  │  ├─ recommender.v1.json
   │     │  │  │  ├─ recommender.v1beta1.json
   │     │  │  │  ├─ redis.v1.json
   │     │  │  │  ├─ redis.v1beta1.json
   │     │  │  │  ├─ remotebuildexecution.v1.json
   │     │  │  │  ├─ remotebuildexecution.v1alpha.json
   │     │  │  │  ├─ remotebuildexecution.v2.json
   │     │  │  │  ├─ reseller.v1.json
   │     │  │  │  ├─ resourcesettings.v1.json
   │     │  │  │  ├─ retail.v2.json
   │     │  │  │  ├─ retail.v2alpha.json
   │     │  │  │  ├─ retail.v2beta.json
   │     │  │  │  ├─ run.v1.json
   │     │  │  │  ├─ run.v1alpha1.json
   │     │  │  │  ├─ run.v1beta1.json
   │     │  │  │  ├─ run.v2.json
   │     │  │  │  ├─ runtimeconfig.v1.json
   │     │  │  │  ├─ runtimeconfig.v1beta1.json
   │     │  │  │  ├─ saasservicemgmt.v1.json
   │     │  │  │  ├─ saasservicemgmt.v1beta1.json
   │     │  │  │  ├─ safebrowsing.v4.json
   │     │  │  │  ├─ safebrowsing.v5.json
   │     │  │  │  ├─ sasportal.v1alpha1.json
   │     │  │  │  ├─ script.v1.json
   │     │  │  │  ├─ searchads360.v0.json
   │     │  │  │  ├─ searchconsole.v1.json
   │     │  │  │  ├─ secretmanager.v1.json
   │     │  │  │  ├─ secretmanager.v1beta1.json
   │     │  │  │  ├─ secretmanager.v1beta2.json
   │     │  │  │  ├─ securesourcemanager.v1.json
   │     │  │  │  ├─ securitycenter.v1.json
   │     │  │  │  ├─ securitycenter.v1beta1.json
   │     │  │  │  ├─ securitycenter.v1beta2.json
   │     │  │  │  ├─ securityposture.v1.json
   │     │  │  │  ├─ serviceconsumermanagement.v1.json
   │     │  │  │  ├─ serviceconsumermanagement.v1beta1.json
   │     │  │  │  ├─ servicecontrol.v1.json
   │     │  │  │  ├─ servicecontrol.v2.json
   │     │  │  │  ├─ servicedirectory.v1.json
   │     │  │  │  ├─ servicedirectory.v1beta1.json
   │     │  │  │  ├─ servicemanagement.v1.json
   │     │  │  │  ├─ servicenetworking.v1.json
   │     │  │  │  ├─ servicenetworking.v1beta.json
   │     │  │  │  ├─ serviceusage.v1.json
   │     │  │  │  ├─ serviceusage.v1beta1.json
   │     │  │  │  ├─ sheets.v4.json
   │     │  │  │  ├─ siteVerification.v1.json
   │     │  │  │  ├─ slides.v1.json
   │     │  │  │  ├─ smartdevicemanagement.v1.json
   │     │  │  │  ├─ solar.v1.json
   │     │  │  │  ├─ sourcerepo.v1.json
   │     │  │  │  ├─ spanner.v1.json
   │     │  │  │  ├─ speech.v1.json
   │     │  │  │  ├─ speech.v1p1beta1.json
   │     │  │  │  ├─ speech.v2beta1.json
   │     │  │  │  ├─ sqladmin.v1.json
   │     │  │  │  ├─ sqladmin.v1beta4.json
   │     │  │  │  ├─ storage.v1.json
   │     │  │  │  ├─ storagebatchoperations.v1.json
   │     │  │  │  ├─ storagetransfer.v1.json
   │     │  │  │  ├─ streetviewpublish.v1.json
   │     │  │  │  ├─ sts.v1.json
   │     │  │  │  ├─ sts.v1beta.json
   │     │  │  │  ├─ tagmanager.v1.json
   │     │  │  │  ├─ tagmanager.v2.json
   │     │  │  │  ├─ tasks.v1.json
   │     │  │  │  ├─ testing.v1.json
   │     │  │  │  ├─ texttospeech.v1.json
   │     │  │  │  ├─ texttospeech.v1beta1.json
   │     │  │  │  ├─ threatintelligence.v1beta.json
   │     │  │  │  ├─ toolresults.v1beta3.json
   │     │  │  │  ├─ tpu.v1.json
   │     │  │  │  ├─ tpu.v1alpha1.json
   │     │  │  │  ├─ tpu.v2.json
   │     │  │  │  ├─ tpu.v2alpha1.json
   │     │  │  │  ├─ trafficdirector.v2.json
   │     │  │  │  ├─ trafficdirector.v3.json
   │     │  │  │  ├─ transcoder.v1.json
   │     │  │  │  ├─ transcoder.v1beta1.json
   │     │  │  │  ├─ translate.v2.json
   │     │  │  │  ├─ translate.v3.json
   │     │  │  │  ├─ translate.v3beta1.json
   │     │  │  │  ├─ travelimpactmodel.v1.json
   │     │  │  │  ├─ vault.v1.json
   │     │  │  │  ├─ vectortile.v1.json
   │     │  │  │  ├─ verifiedaccess.v1.json
   │     │  │  │  ├─ verifiedaccess.v2.json
   │     │  │  │  ├─ versionhistory.v1.json
   │     │  │  │  ├─ videointelligence.v1.json
   │     │  │  │  ├─ videointelligence.v1beta2.json
   │     │  │  │  ├─ videointelligence.v1p1beta1.json
   │     │  │  │  ├─ videointelligence.v1p2beta1.json
   │     │  │  │  ├─ videointelligence.v1p3beta1.json
   │     │  │  │  ├─ vision.v1.json
   │     │  │  │  ├─ vision.v1p1beta1.json
   │     │  │  │  ├─ vision.v1p2beta1.json
   │     │  │  │  ├─ vmmigration.v1.json
   │     │  │  │  ├─ vmmigration.v1alpha1.json
   │     │  │  │  ├─ vmwareengine.v1.json
   │     │  │  │  ├─ vpcaccess.v1.json
   │     │  │  │  ├─ vpcaccess.v1beta1.json
   │     │  │  │  ├─ walletobjects.v1.json
   │     │  │  │  ├─ webfonts.v1.json
   │     │  │  │  ├─ webmasters.v3.json
   │     │  │  │  ├─ webrisk.v1.json
   │     │  │  │  ├─ websecurityscanner.v1.json
   │     │  │  │  ├─ websecurityscanner.v1alpha.json
   │     │  │  │  ├─ websecurityscanner.v1beta.json
   │     │  │  │  ├─ workflowexecutions.v1.json
   │     │  │  │  ├─ workflowexecutions.v1beta.json
   │     │  │  │  ├─ workflows.v1.json
   │     │  │  │  ├─ workflows.v1beta.json
   │     │  │  │  ├─ workloadmanager.v1.json
   │     │  │  │  ├─ workspaceevents.v1.json
   │     │  │  │  ├─ workstations.v1.json
   │     │  │  │  ├─ workstations.v1beta.json
   │     │  │  │  ├─ youtube.v3.json
   │     │  │  │  ├─ youtubeAnalytics.v1.json
   │     │  │  │  ├─ youtubeAnalytics.v2.json
   │     │  │  │  └─ youtubereporting.v1.json
   │     │  │  ├─ file_cache.py
   │     │  │  └─ __init__.py
   │     │  ├─ errors.py
   │     │  ├─ http.py
   │     │  ├─ mimeparse.py
   │     │  ├─ model.py
   │     │  ├─ sample_tools.py
   │     │  ├─ schema.py
   │     │  ├─ version.py
   │     │  ├─ _auth.py
   │     │  ├─ _helpers.py
   │     │  └─ __init__.py
   │     ├─ google_auth_httplib2.py
   │     ├─ greenlet
   │     │  ├─ CObjects.cpp
   │     │  ├─ greenlet.cpp
   │     │  ├─ greenlet.h
   │     │  ├─ greenlet_allocator.hpp
   │     │  ├─ greenlet_compiler_compat.hpp
   │     │  ├─ greenlet_cpython_compat.hpp
   │     │  ├─ greenlet_exceptions.hpp
   │     │  ├─ greenlet_internal.hpp
   │     │  ├─ greenlet_msvc_compat.hpp
   │     │  ├─ greenlet_refs.hpp
   │     │  ├─ greenlet_slp_switch.hpp
   │     │  ├─ greenlet_thread_support.hpp
   │     │  ├─ platform
   │     │  │  ├─ setup_switch_x64_masm.cmd
   │     │  │  ├─ switch_aarch64_gcc.h
   │     │  │  ├─ switch_alpha_unix.h
   │     │  │  ├─ switch_amd64_unix.h
   │     │  │  ├─ switch_arm32_gcc.h
   │     │  │  ├─ switch_arm32_ios.h
   │     │  │  ├─ switch_arm64_masm.asm
   │     │  │  ├─ switch_arm64_masm.obj
   │     │  │  ├─ switch_arm64_msvc.h
   │     │  │  ├─ switch_csky_gcc.h
   │     │  │  ├─ switch_loongarch64_linux.h
   │     │  │  ├─ switch_m68k_gcc.h
   │     │  │  ├─ switch_mips_unix.h
   │     │  │  ├─ switch_ppc64_aix.h
   │     │  │  ├─ switch_ppc64_linux.h
   │     │  │  ├─ switch_ppc_aix.h
   │     │  │  ├─ switch_ppc_linux.h
   │     │  │  ├─ switch_ppc_macosx.h
   │     │  │  ├─ switch_ppc_unix.h
   │     │  │  ├─ switch_riscv_unix.h
   │     │  │  ├─ switch_s390_unix.h
   │     │  │  ├─ switch_sh_gcc.h
   │     │  │  ├─ switch_sparc_sun_gcc.h
   │     │  │  ├─ switch_x32_unix.h
   │     │  │  ├─ switch_x64_masm.asm
   │     │  │  ├─ switch_x64_masm.obj
   │     │  │  ├─ switch_x64_msvc.h
   │     │  │  ├─ switch_x86_msvc.h
   │     │  │  ├─ switch_x86_unix.h
   │     │  │  └─ __init__.py
   │     │  ├─ PyGreenlet.cpp
   │     │  ├─ PyGreenlet.hpp
   │     │  ├─ PyGreenletUnswitchable.cpp
   │     │  ├─ PyModule.cpp
   │     │  ├─ slp_platformselect.h
   │     │  ├─ TBrokenGreenlet.cpp
   │     │  ├─ tests
   │     │  │  ├─ fail_clearing_run_switches.py
   │     │  │  ├─ fail_cpp_exception.py
   │     │  │  ├─ fail_initialstub_already_started.py
   │     │  │  ├─ fail_slp_switch.py
   │     │  │  ├─ fail_switch_three_greenlets.py
   │     │  │  ├─ fail_switch_three_greenlets2.py
   │     │  │  ├─ fail_switch_two_greenlets.py
   │     │  │  ├─ leakcheck.py
   │     │  │  ├─ test_contextvars.py
   │     │  │  ├─ test_cpp.py
   │     │  │  ├─ test_extension_interface.py
   │     │  │  ├─ test_gc.py
   │     │  │  ├─ test_generator.py
   │     │  │  ├─ test_generator_nested.py
   │     │  │  ├─ test_greenlet.py
   │     │  │  ├─ test_greenlet_trash.py
   │     │  │  ├─ test_interpreter_shutdown.py
   │     │  │  ├─ test_leaks.py
   │     │  │  ├─ test_stack_saved.py
   │     │  │  ├─ test_throw.py
   │     │  │  ├─ test_tracing.py
   │     │  │  ├─ test_version.py
   │     │  │  ├─ test_weakref.py
   │     │  │  ├─ _test_extension.c
   │     │  │  ├─ _test_extension.cp313-win_amd64.pyd
   │     │  │  ├─ _test_extension_cpp.cp313-win_amd64.pyd
   │     │  │  ├─ _test_extension_cpp.cpp
   │     │  │  └─ __init__.py
   │     │  ├─ TExceptionState.cpp
   │     │  ├─ TGreenlet.cpp
   │     │  ├─ TGreenlet.hpp
   │     │  ├─ TGreenletGlobals.cpp
   │     │  ├─ TMainGreenlet.cpp
   │     │  ├─ TPythonState.cpp
   │     │  ├─ TStackState.cpp
   │     │  ├─ TThreadState.hpp
   │     │  ├─ TThreadStateCreator.hpp
   │     │  ├─ TThreadStateDestroy.cpp
   │     │  ├─ TUserGreenlet.cpp
   │     │  ├─ _greenlet.cp313-win_amd64.pyd
   │     │  └─ __init__.py
   │     ├─ grpc
   │     │  ├─ aio
   │     │  │  ├─ _base_call.py
   │     │  │  ├─ _base_channel.py
   │     │  │  ├─ _base_server.py
   │     │  │  ├─ _call.py
   │     │  │  ├─ _channel.py
   │     │  │  ├─ _interceptor.py
   │     │  │  ├─ _metadata.py
   │     │  │  ├─ _server.py
   │     │  │  ├─ _typing.py
   │     │  │  ├─ _utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ beta
   │     │  │  ├─ implementations.py
   │     │  │  ├─ interfaces.py
   │     │  │  ├─ utilities.py
   │     │  │  ├─ _client_adaptations.py
   │     │  │  ├─ _metadata.py
   │     │  │  ├─ _server_adaptations.py
   │     │  │  └─ __init__.py
   │     │  ├─ experimental
   │     │  │  ├─ aio
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ gevent.py
   │     │  │  ├─ session_cache.py
   │     │  │  └─ __init__.py
   │     │  ├─ framework
   │     │  │  ├─ common
   │     │  │  │  ├─ cardinality.py
   │     │  │  │  ├─ style.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ foundation
   │     │  │  │  ├─ abandonment.py
   │     │  │  │  ├─ callable_util.py
   │     │  │  │  ├─ future.py
   │     │  │  │  ├─ logging_pool.py
   │     │  │  │  ├─ stream.py
   │     │  │  │  ├─ stream_util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ interfaces
   │     │  │  │  ├─ base
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ utilities.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ face
   │     │  │  │  │  ├─ face.py
   │     │  │  │  │  ├─ utilities.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ _auth.py
   │     │  ├─ _channel.py
   │     │  ├─ _common.py
   │     │  ├─ _compression.py
   │     │  ├─ _cython
   │     │  │  ├─ cygrpc.cp313-win_amd64.pyd
   │     │  │  ├─ _credentials
   │     │  │  │  └─ roots.pem
   │     │  │  ├─ _cygrpc
   │     │  │  │  ├─ private_key_signing
   │     │  │  │  │  ├─ private_key_signer_py_wrapper.cc
   │     │  │  │  │  └─ private_key_signer_py_wrapper.h
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ _grpcio_metadata.py
   │     │  ├─ _interceptor.py
   │     │  ├─ _observability.py
   │     │  ├─ _plugin_wrapping.py
   │     │  ├─ _runtime_protos.py
   │     │  ├─ _server.py
   │     │  ├─ _simple_stubs.py
   │     │  ├─ _typing.py
   │     │  ├─ _utilities.py
   │     │  └─ __init__.py
   │     ├─ grpc_status
   │     │  ├─ rpc_status.py
   │     │  ├─ _async.py
   │     │  ├─ _common.py
   │     │  └─ __init__.py
   │     ├─ h11
   │     │  ├─ py.typed
   │     │  ├─ _abnf.py
   │     │  ├─ _connection.py
   │     │  ├─ _events.py
   │     │  ├─ _headers.py
   │     │  ├─ _readers.py
   │     │  ├─ _receivebuffer.py
   │     │  ├─ _state.py
   │     │  ├─ _util.py
   │     │  ├─ _version.py
   │     │  ├─ _writers.py
   │     │  └─ __init__.py
   │     ├─ httpcore
   │     │  ├─ py.typed
   │     │  ├─ _api.py
   │     │  ├─ _async
   │     │  │  ├─ connection.py
   │     │  │  ├─ connection_pool.py
   │     │  │  ├─ http11.py
   │     │  │  ├─ http2.py
   │     │  │  ├─ http_proxy.py
   │     │  │  ├─ interfaces.py
   │     │  │  ├─ socks_proxy.py
   │     │  │  └─ __init__.py
   │     │  ├─ _backends
   │     │  │  ├─ anyio.py
   │     │  │  ├─ auto.py
   │     │  │  ├─ base.py
   │     │  │  ├─ mock.py
   │     │  │  ├─ sync.py
   │     │  │  ├─ trio.py
   │     │  │  └─ __init__.py
   │     │  ├─ _exceptions.py
   │     │  ├─ _models.py
   │     │  ├─ _ssl.py
   │     │  ├─ _sync
   │     │  │  ├─ connection.py
   │     │  │  ├─ connection_pool.py
   │     │  │  ├─ http11.py
   │     │  │  ├─ http2.py
   │     │  │  ├─ http_proxy.py
   │     │  │  ├─ interfaces.py
   │     │  │  ├─ socks_proxy.py
   │     │  │  └─ __init__.py
   │     │  ├─ _synchronization.py
   │     │  ├─ _trace.py
   │     │  ├─ _utils.py
   │     │  └─ __init__.py
   │     ├─ httpcore2
   │     │  ├─ py.typed
   │     │  ├─ _api.py
   │     │  ├─ _async
   │     │  │  ├─ connection.py
   │     │  │  ├─ connection_pool.py
   │     │  │  ├─ http11.py
   │     │  │  ├─ http2.py
   │     │  │  ├─ http_proxy.py
   │     │  │  ├─ interfaces.py
   │     │  │  ├─ socks_proxy.py
   │     │  │  └─ __init__.py
   │     │  ├─ _backends
   │     │  │  ├─ anyio.py
   │     │  │  ├─ auto.py
   │     │  │  ├─ base.py
   │     │  │  ├─ mock.py
   │     │  │  ├─ sync.py
   │     │  │  ├─ trio.py
   │     │  │  └─ __init__.py
   │     │  ├─ _exceptions.py
   │     │  ├─ _models.py
   │     │  ├─ _ssl.py
   │     │  ├─ _sync
   │     │  │  ├─ connection.py
   │     │  │  ├─ connection_pool.py
   │     │  │  ├─ http11.py
   │     │  │  ├─ http2.py
   │     │  │  ├─ http_proxy.py
   │     │  │  ├─ interfaces.py
   │     │  │  ├─ socks_proxy.py
   │     │  │  └─ __init__.py
   │     │  ├─ _synchronization.py
   │     │  ├─ _trace.py
   │     │  ├─ _utils.py
   │     │  └─ __init__.py
   │     ├─ httplib2
   │     │  ├─ auth.py
   │     │  ├─ cacerts.txt
   │     │  ├─ certs.py
   │     │  ├─ error.py
   │     │  ├─ iri2uri.py
   │     │  └─ __init__.py
   │     ├─ httptools
   │     │  ├─ parser
   │     │  │  ├─ cparser.pxd
   │     │  │  ├─ errors.py
   │     │  │  ├─ parser.cp313-win_amd64.pyd
   │     │  │  ├─ parser.pyi
   │     │  │  ├─ parser.pyx
   │     │  │  ├─ protocol.py
   │     │  │  ├─ python.pxd
   │     │  │  ├─ url_cparser.pxd
   │     │  │  ├─ url_parser.cp313-win_amd64.pyd
   │     │  │  ├─ url_parser.pyi
   │     │  │  ├─ url_parser.pyx
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ httpx
   │     │  ├─ py.typed
   │     │  ├─ _api.py
   │     │  ├─ _auth.py
   │     │  ├─ _client.py
   │     │  ├─ _config.py
   │     │  ├─ _content.py
   │     │  ├─ _decoders.py
   │     │  ├─ _exceptions.py
   │     │  ├─ _main.py
   │     │  ├─ _models.py
   │     │  ├─ _multipart.py
   │     │  ├─ _status_codes.py
   │     │  ├─ _transports
   │     │  │  ├─ asgi.py
   │     │  │  ├─ base.py
   │     │  │  ├─ default.py
   │     │  │  ├─ mock.py
   │     │  │  ├─ wsgi.py
   │     │  │  └─ __init__.py
   │     │  ├─ _types.py
   │     │  ├─ _urlparse.py
   │     │  ├─ _urls.py
   │     │  ├─ _utils.py
   │     │  ├─ __init__.py
   │     │  └─ __version__.py
   │     ├─ httpx2
   │     │  ├─ py.typed
   │     │  ├─ websockets
   │     │  │  ├─ _api.py
   │     │  │  ├─ _exceptions.py
   │     │  │  ├─ _ping.py
   │     │  │  ├─ _transport.py
   │     │  │  └─ __init__.py
   │     │  ├─ _alias.py
   │     │  ├─ _api.py
   │     │  ├─ _auth.py
   │     │  ├─ _client.py
   │     │  ├─ _config.py
   │     │  ├─ _content.py
   │     │  ├─ _decoders.py
   │     │  ├─ _exceptions.py
   │     │  ├─ _main.py
   │     │  ├─ _models.py
   │     │  ├─ _multipart.py
   │     │  ├─ _sse.py
   │     │  ├─ _status_codes.py
   │     │  ├─ _transports
   │     │  │  ├─ asgi.py
   │     │  │  ├─ base.py
   │     │  │  ├─ default.py
   │     │  │  ├─ mock.py
   │     │  │  ├─ wsgi.py
   │     │  │  └─ __init__.py
   │     │  ├─ _types.py
   │     │  ├─ _urlparse.py
   │     │  ├─ _urls.py
   │     │  ├─ _utils.py
   │     │  ├─ __init__.py
   │     │  └─ __version__.py
   │     ├─ idna
   │     │  ├─ cli.py
   │     │  ├─ codec.py
   │     │  ├─ compat.py
   │     │  ├─ core.py
   │     │  ├─ idnadata.py
   │     │  ├─ intranges.py
   │     │  ├─ package_data.py
   │     │  ├─ py.typed
   │     │  ├─ uts46data.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ isapi
   │     │  ├─ doc
   │     │  │  └─ isapi.html
   │     │  ├─ install.py
   │     │  ├─ isapicon.py
   │     │  ├─ PyISAPI_loader.dll
   │     │  ├─ README.txt
   │     │  ├─ samples
   │     │  │  ├─ advanced.py
   │     │  │  ├─ README.txt
   │     │  │  ├─ redirector.py
   │     │  │  ├─ redirector_asynch.py
   │     │  │  ├─ redirector_with_filter.py
   │     │  │  └─ test.py
   │     │  ├─ simple.py
   │     │  ├─ test
   │     │  │  ├─ extension_simple.py
   │     │  │  └─ README.txt
   │     │  ├─ threaded_extension.py
   │     │  └─ __init__.py
   │     ├─ jiter
   │     │  ├─ jiter.cp313-win_amd64.pyd
   │     │  ├─ py.typed
   │     │  ├─ __init__.py
   │     │  └─ __init__.pyi
   │     ├─ lxml
   │     │  ├─ apihelpers.pxi
   │     │  ├─ builder.cp313-win_amd64.pyd
   │     │  ├─ builder.py
   │     │  ├─ classlookup.pxi
   │     │  ├─ cleanup.pxi
   │     │  ├─ cssselect.py
   │     │  ├─ debug.pxi
   │     │  ├─ docloader.pxi
   │     │  ├─ doctestcompare.py
   │     │  ├─ dtd.pxi
   │     │  ├─ ElementInclude.py
   │     │  ├─ etree.cp313-win_amd64.pyd
   │     │  ├─ etree.h
   │     │  ├─ etree.pyx
   │     │  ├─ etree_api.h
   │     │  ├─ extensions.pxi
   │     │  ├─ html
   │     │  │  ├─ builder.py
   │     │  │  ├─ clean.py
   │     │  │  ├─ defs.py
   │     │  │  ├─ diff.cp313-win_amd64.pyd
   │     │  │  ├─ diff.py
   │     │  │  ├─ ElementSoup.py
   │     │  │  ├─ formfill.py
   │     │  │  ├─ html5parser.py
   │     │  │  ├─ soupparser.py
   │     │  │  ├─ usedoctest.py
   │     │  │  ├─ _diffcommand.py
   │     │  │  ├─ _difflib.cp313-win_amd64.pyd
   │     │  │  ├─ _difflib.py
   │     │  │  ├─ _html5builder.py
   │     │  │  ├─ _setmixin.py
   │     │  │  └─ __init__.py
   │     │  ├─ includes
   │     │  │  ├─ c14n.pxd
   │     │  │  ├─ config.pxd
   │     │  │  ├─ dtdvalid.pxd
   │     │  │  ├─ etreepublic.pxd
   │     │  │  ├─ etree_defs.h
   │     │  │  ├─ extlibs
   │     │  │  │  ├─ zconf.h
   │     │  │  │  ├─ zlib.h
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ htmlparser.pxd
   │     │  │  ├─ libexslt
   │     │  │  │  ├─ exslt.h
   │     │  │  │  ├─ exsltconfig.h
   │     │  │  │  ├─ exsltexports.h
   │     │  │  │  ├─ libexslt.h
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ libxml
   │     │  │  │  ├─ c14n.h
   │     │  │  │  ├─ catalog.h
   │     │  │  │  ├─ chvalid.h
   │     │  │  │  ├─ debugXML.h
   │     │  │  │  ├─ dict.h
   │     │  │  │  ├─ encoding.h
   │     │  │  │  ├─ entities.h
   │     │  │  │  ├─ globals.h
   │     │  │  │  ├─ hash.h
   │     │  │  │  ├─ HTMLparser.h
   │     │  │  │  ├─ HTMLtree.h
   │     │  │  │  ├─ list.h
   │     │  │  │  ├─ nanoftp.h
   │     │  │  │  ├─ nanohttp.h
   │     │  │  │  ├─ parser.h
   │     │  │  │  ├─ parserInternals.h
   │     │  │  │  ├─ pattern.h
   │     │  │  │  ├─ relaxng.h
   │     │  │  │  ├─ SAX.h
   │     │  │  │  ├─ SAX2.h
   │     │  │  │  ├─ schemasInternals.h
   │     │  │  │  ├─ schematron.h
   │     │  │  │  ├─ threads.h
   │     │  │  │  ├─ tree.h
   │     │  │  │  ├─ uri.h
   │     │  │  │  ├─ valid.h
   │     │  │  │  ├─ xinclude.h
   │     │  │  │  ├─ xlink.h
   │     │  │  │  ├─ xmlautomata.h
   │     │  │  │  ├─ xmlerror.h
   │     │  │  │  ├─ xmlexports.h
   │     │  │  │  ├─ xmlIO.h
   │     │  │  │  ├─ xmlmemory.h
   │     │  │  │  ├─ xmlmodule.h
   │     │  │  │  ├─ xmlreader.h
   │     │  │  │  ├─ xmlregexp.h
   │     │  │  │  ├─ xmlsave.h
   │     │  │  │  ├─ xmlschemas.h
   │     │  │  │  ├─ xmlschemastypes.h
   │     │  │  │  ├─ xmlstring.h
   │     │  │  │  ├─ xmlunicode.h
   │     │  │  │  ├─ xmlversion.h
   │     │  │  │  ├─ xmlwriter.h
   │     │  │  │  ├─ xpath.h
   │     │  │  │  ├─ xpathInternals.h
   │     │  │  │  ├─ xpointer.h
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ libxslt
   │     │  │  │  ├─ attributes.h
   │     │  │  │  ├─ documents.h
   │     │  │  │  ├─ extensions.h
   │     │  │  │  ├─ extra.h
   │     │  │  │  ├─ functions.h
   │     │  │  │  ├─ imports.h
   │     │  │  │  ├─ keys.h
   │     │  │  │  ├─ libxslt.h
   │     │  │  │  ├─ namespaces.h
   │     │  │  │  ├─ numbersInternals.h
   │     │  │  │  ├─ preproc.h
   │     │  │  │  ├─ security.h
   │     │  │  │  ├─ templates.h
   │     │  │  │  ├─ transform.h
   │     │  │  │  ├─ transformInternals.h
   │     │  │  │  ├─ trio.h
   │     │  │  │  ├─ triodef.h
   │     │  │  │  ├─ variables.h
   │     │  │  │  ├─ win32config.h
   │     │  │  │  ├─ xslt.h
   │     │  │  │  ├─ xsltconfig.h
   │     │  │  │  ├─ xsltexports.h
   │     │  │  │  ├─ xsltInternals.h
   │     │  │  │  ├─ xsltlocale.h
   │     │  │  │  ├─ xsltutils.h
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ lxml-version.h
   │     │  │  ├─ relaxng.pxd
   │     │  │  ├─ schematron.pxd
   │     │  │  ├─ tree.pxd
   │     │  │  ├─ uri.pxd
   │     │  │  ├─ xinclude.pxd
   │     │  │  ├─ xmlerror.pxd
   │     │  │  ├─ xmlparser.pxd
   │     │  │  ├─ xmlschema.pxd
   │     │  │  ├─ xpath.pxd
   │     │  │  ├─ xslt.pxd
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ isoschematron
   │     │  │  ├─ resources
   │     │  │  │  ├─ rng
   │     │  │  │  │  └─ iso-schematron.rng
   │     │  │  │  └─ xsl
   │     │  │  │     ├─ iso-schematron-xslt1
   │     │  │  │     │  ├─ iso_abstract_expand.xsl
   │     │  │  │     │  ├─ iso_dsdl_include.xsl
   │     │  │  │     │  ├─ iso_schematron_message.xsl
   │     │  │  │     │  ├─ iso_schematron_skeleton_for_xslt1.xsl
   │     │  │  │     │  ├─ iso_svrl_for_xslt1.xsl
   │     │  │  │     │  └─ readme.txt
   │     │  │  │     ├─ RNG2Schtrn.xsl
   │     │  │  │     └─ XSD2Schtrn.xsl
   │     │  │  └─ __init__.py
   │     │  ├─ iterparse.pxi
   │     │  ├─ lxml.etree.h
   │     │  ├─ lxml.etree_api.h
   │     │  ├─ nsclasses.pxi
   │     │  ├─ objectify.cp313-win_amd64.pyd
   │     │  ├─ objectify.pyx
   │     │  ├─ objectpath.pxi
   │     │  ├─ parser.pxi
   │     │  ├─ parsertarget.pxi
   │     │  ├─ proxy.pxi
   │     │  ├─ public-api.pxi
   │     │  ├─ pyclasslookup.py
   │     │  ├─ readonlytree.pxi
   │     │  ├─ relaxng.pxi
   │     │  ├─ sax.cp313-win_amd64.pyd
   │     │  ├─ sax.py
   │     │  ├─ saxparser.pxi
   │     │  ├─ schematron.pxi
   │     │  ├─ serializer.pxi
   │     │  ├─ usedoctest.py
   │     │  ├─ xinclude.pxi
   │     │  ├─ xmlerror.pxi
   │     │  ├─ xmlid.pxi
   │     │  ├─ xmlschema.pxi
   │     │  ├─ xpath.pxi
   │     │  ├─ xslt.pxi
   │     │  ├─ xsltext.pxi
   │     │  ├─ _elementpath.cp313-win_amd64.pyd
   │     │  ├─ _elementpath.py
   │     │  └─ __init__.py
   │     ├─ mouseinfo
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ numpy
   │     │  ├─ char
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ conftest.py
   │     │  ├─ core
   │     │  │  ├─ arrayprint.py
   │     │  │  ├─ defchararray.py
   │     │  │  ├─ einsumfunc.py
   │     │  │  ├─ fromnumeric.py
   │     │  │  ├─ function_base.py
   │     │  │  ├─ getlimits.py
   │     │  │  ├─ multiarray.py
   │     │  │  ├─ numeric.py
   │     │  │  ├─ numerictypes.py
   │     │  │  ├─ overrides.py
   │     │  │  ├─ overrides.pyi
   │     │  │  ├─ records.py
   │     │  │  ├─ shape_base.py
   │     │  │  ├─ umath.py
   │     │  │  ├─ _dtype.py
   │     │  │  ├─ _dtype.pyi
   │     │  │  ├─ _dtype_ctypes.py
   │     │  │  ├─ _dtype_ctypes.pyi
   │     │  │  ├─ _internal.py
   │     │  │  ├─ _multiarray_umath.py
   │     │  │  ├─ _utils.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ ctypeslib
   │     │  │  ├─ _ctypeslib.py
   │     │  │  ├─ _ctypeslib.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ doc
   │     │  │  └─ ufuncs.py
   │     │  ├─ dtypes.py
   │     │  ├─ dtypes.pyi
   │     │  ├─ exceptions.py
   │     │  ├─ exceptions.pyi
   │     │  ├─ f2py
   │     │  │  ├─ auxfuncs.py
   │     │  │  ├─ auxfuncs.pyi
   │     │  │  ├─ capi_maps.py
   │     │  │  ├─ capi_maps.pyi
   │     │  │  ├─ cb_rules.py
   │     │  │  ├─ cb_rules.pyi
   │     │  │  ├─ cfuncs.py
   │     │  │  ├─ cfuncs.pyi
   │     │  │  ├─ common_rules.py
   │     │  │  ├─ common_rules.pyi
   │     │  │  ├─ crackfortran.py
   │     │  │  ├─ crackfortran.pyi
   │     │  │  ├─ diagnose.py
   │     │  │  ├─ diagnose.pyi
   │     │  │  ├─ f2py2e.py
   │     │  │  ├─ f2py2e.pyi
   │     │  │  ├─ f90mod_rules.py
   │     │  │  ├─ f90mod_rules.pyi
   │     │  │  ├─ func2subr.py
   │     │  │  ├─ func2subr.pyi
   │     │  │  ├─ rules.py
   │     │  │  ├─ rules.pyi
   │     │  │  ├─ setup.cfg
   │     │  │  ├─ src
   │     │  │  │  ├─ fortranobject.c
   │     │  │  │  └─ fortranobject.h
   │     │  │  ├─ symbolic.py
   │     │  │  ├─ symbolic.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ src
   │     │  │  │  │  ├─ abstract_interface
   │     │  │  │  │  │  ├─ foo.f90
   │     │  │  │  │  │  └─ gh18403_mod.f90
   │     │  │  │  │  ├─ array_from_pyobj
   │     │  │  │  │  │  └─ wrapmodule.c
   │     │  │  │  │  ├─ assumed_shape
   │     │  │  │  │  │  ├─ .f2py_f2cmap
   │     │  │  │  │  │  ├─ foo_free.f90
   │     │  │  │  │  │  ├─ foo_mod.f90
   │     │  │  │  │  │  ├─ foo_use.f90
   │     │  │  │  │  │  └─ precision.f90
   │     │  │  │  │  ├─ block_docstring
   │     │  │  │  │  │  └─ foo.f
   │     │  │  │  │  ├─ callback
   │     │  │  │  │  │  ├─ foo.f
   │     │  │  │  │  │  ├─ gh17797.f90
   │     │  │  │  │  │  ├─ gh18335.f90
   │     │  │  │  │  │  ├─ gh25211.f
   │     │  │  │  │  │  ├─ gh25211.pyf
   │     │  │  │  │  │  └─ gh26681.f90
   │     │  │  │  │  ├─ cli
   │     │  │  │  │  │  ├─ gh_22819.pyf
   │     │  │  │  │  │  ├─ hi77.f
   │     │  │  │  │  │  └─ hiworld.f90
   │     │  │  │  │  ├─ common
   │     │  │  │  │  │  ├─ block.f
   │     │  │  │  │  │  └─ gh19161.f90
   │     │  │  │  │  ├─ crackfortran
   │     │  │  │  │  │  ├─ accesstype.f90
   │     │  │  │  │  │  ├─ common_with_division.f
   │     │  │  │  │  │  ├─ data_common.f
   │     │  │  │  │  │  ├─ data_multiplier.f
   │     │  │  │  │  │  ├─ data_stmts.f90
   │     │  │  │  │  │  ├─ data_with_comments.f
   │     │  │  │  │  │  ├─ foo_deps.f90
   │     │  │  │  │  │  ├─ gh15035.f
   │     │  │  │  │  │  ├─ gh17859.f
   │     │  │  │  │  │  ├─ gh22648.pyf
   │     │  │  │  │  │  ├─ gh23533.f
   │     │  │  │  │  │  ├─ gh23598.f90
   │     │  │  │  │  │  ├─ gh23598Warn.f90
   │     │  │  │  │  │  ├─ gh23879.f90
   │     │  │  │  │  │  ├─ gh27697.f90
   │     │  │  │  │  │  ├─ gh2848.f90
   │     │  │  │  │  │  ├─ operators.f90
   │     │  │  │  │  │  ├─ privatemod.f90
   │     │  │  │  │  │  ├─ publicmod.f90
   │     │  │  │  │  │  ├─ pubprivmod.f90
   │     │  │  │  │  │  └─ unicode_comment.f90
   │     │  │  │  │  ├─ f2cmap
   │     │  │  │  │  │  ├─ .f2py_f2cmap
   │     │  │  │  │  │  └─ isoFortranEnvMap.f90
   │     │  │  │  │  ├─ isocintrin
   │     │  │  │  │  │  └─ isoCtests.f90
   │     │  │  │  │  ├─ kind
   │     │  │  │  │  │  └─ foo.f90
   │     │  │  │  │  ├─ mixed
   │     │  │  │  │  │  ├─ foo.f
   │     │  │  │  │  │  ├─ foo_fixed.f90
   │     │  │  │  │  │  └─ foo_free.f90
   │     │  │  │  │  ├─ modules
   │     │  │  │  │  │  ├─ gh25337
   │     │  │  │  │  │  │  ├─ data.f90
   │     │  │  │  │  │  │  └─ use_data.f90
   │     │  │  │  │  │  ├─ gh26920
   │     │  │  │  │  │  │  ├─ two_mods_with_no_public_entities.f90
   │     │  │  │  │  │  │  └─ two_mods_with_one_public_routine.f90
   │     │  │  │  │  │  ├─ module_data_docstring.f90
   │     │  │  │  │  │  └─ use_modules.f90
   │     │  │  │  │  ├─ negative_bounds
   │     │  │  │  │  │  └─ issue_20853.f90
   │     │  │  │  │  ├─ parameter
   │     │  │  │  │  │  ├─ constant_array.f90
   │     │  │  │  │  │  ├─ constant_both.f90
   │     │  │  │  │  │  ├─ constant_compound.f90
   │     │  │  │  │  │  ├─ constant_integer.f90
   │     │  │  │  │  │  ├─ constant_non_compound.f90
   │     │  │  │  │  │  └─ constant_real.f90
   │     │  │  │  │  ├─ quoted_character
   │     │  │  │  │  │  └─ foo.f
   │     │  │  │  │  ├─ regression
   │     │  │  │  │  │  ├─ AB.inc
   │     │  │  │  │  │  ├─ assignOnlyModule.f90
   │     │  │  │  │  │  ├─ datonly.f90
   │     │  │  │  │  │  ├─ f77comments.f
   │     │  │  │  │  │  ├─ f77fixedform.f95
   │     │  │  │  │  │  ├─ f90continuation.f90
   │     │  │  │  │  │  ├─ incfile.f90
   │     │  │  │  │  │  ├─ inout.f90
   │     │  │  │  │  │  ├─ lower_f2py_fortran.f90
   │     │  │  │  │  │  └─ mod_derived_types.f90
   │     │  │  │  │  ├─ return_character
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_complex
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_integer
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_logical
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_real
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ routines
   │     │  │  │  │  │  ├─ funcfortranname.f
   │     │  │  │  │  │  ├─ funcfortranname.pyf
   │     │  │  │  │  │  ├─ subrout.f
   │     │  │  │  │  │  └─ subrout.pyf
   │     │  │  │  │  ├─ size
   │     │  │  │  │  │  └─ foo.f90
   │     │  │  │  │  ├─ string
   │     │  │  │  │  │  ├─ char.f90
   │     │  │  │  │  │  ├─ fixed_string.f90
   │     │  │  │  │  │  ├─ gh24008.f
   │     │  │  │  │  │  ├─ gh24662.f90
   │     │  │  │  │  │  ├─ gh25286.f90
   │     │  │  │  │  │  ├─ gh25286.pyf
   │     │  │  │  │  │  ├─ gh25286_bc.pyf
   │     │  │  │  │  │  ├─ scalar_string.f90
   │     │  │  │  │  │  └─ string.f
   │     │  │  │  │  └─ value_attrspec
   │     │  │  │  │     └─ gh21665.f90
   │     │  │  │  ├─ test_abstract_interface.py
   │     │  │  │  ├─ test_array_from_pyobj.py
   │     │  │  │  ├─ test_assumed_shape.py
   │     │  │  │  ├─ test_block_docstring.py
   │     │  │  │  ├─ test_callback.py
   │     │  │  │  ├─ test_capi_maps.py
   │     │  │  │  ├─ test_character.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_crackfortran.py
   │     │  │  │  ├─ test_data.py
   │     │  │  │  ├─ test_docs.py
   │     │  │  │  ├─ test_f2cmap.py
   │     │  │  │  ├─ test_f2py2e.py
   │     │  │  │  ├─ test_isoc.py
   │     │  │  │  ├─ test_kind.py
   │     │  │  │  ├─ test_mixed.py
   │     │  │  │  ├─ test_modules.py
   │     │  │  │  ├─ test_parameter.py
   │     │  │  │  ├─ test_pyf_src.py
   │     │  │  │  ├─ test_quoted_character.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_return_character.py
   │     │  │  │  ├─ test_return_complex.py
   │     │  │  │  ├─ test_return_integer.py
   │     │  │  │  ├─ test_return_logical.py
   │     │  │  │  ├─ test_return_real.py
   │     │  │  │  ├─ test_routines.py
   │     │  │  │  ├─ test_semicolon_split.py
   │     │  │  │  ├─ test_size.py
   │     │  │  │  ├─ test_string.py
   │     │  │  │  ├─ test_symbolic.py
   │     │  │  │  ├─ test_value_attrspec.py
   │     │  │  │  ├─ util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ use_rules.py
   │     │  │  ├─ use_rules.pyi
   │     │  │  ├─ _backends
   │     │  │  │  ├─ meson.build.template
   │     │  │  │  ├─ _backend.py
   │     │  │  │  ├─ _backend.pyi
   │     │  │  │  ├─ _meson.py
   │     │  │  │  ├─ _meson.pyi
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __init__.pyi
   │     │  │  ├─ _isocbind.py
   │     │  │  ├─ _isocbind.pyi
   │     │  │  ├─ _src_pyf.py
   │     │  │  ├─ _src_pyf.pyi
   │     │  │  ├─ __init__.py
   │     │  │  ├─ __init__.pyi
   │     │  │  ├─ __main__.py
   │     │  │  ├─ __version__.py
   │     │  │  └─ __version__.pyi
   │     │  ├─ fft
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_helper.py
   │     │  │  │  ├─ test_pocketfft.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _helper.py
   │     │  │  ├─ _helper.pyi
   │     │  │  ├─ _pocketfft.py
   │     │  │  ├─ _pocketfft.pyi
   │     │  │  ├─ _pocketfft_umath.cp313-win_amd64.lib
   │     │  │  ├─ _pocketfft_umath.cp313-win_amd64.pyd
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ lib
   │     │  │  ├─ array_utils.py
   │     │  │  ├─ array_utils.pyi
   │     │  │  ├─ format.py
   │     │  │  ├─ format.pyi
   │     │  │  ├─ introspect.py
   │     │  │  ├─ introspect.pyi
   │     │  │  ├─ mixins.py
   │     │  │  ├─ mixins.pyi
   │     │  │  ├─ npyio.py
   │     │  │  ├─ npyio.pyi
   │     │  │  ├─ recfunctions.py
   │     │  │  ├─ recfunctions.pyi
   │     │  │  ├─ scimath.py
   │     │  │  ├─ scimath.pyi
   │     │  │  ├─ stride_tricks.py
   │     │  │  ├─ stride_tricks.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ py2-np0-objarr.npy
   │     │  │  │  │  ├─ py2-objarr.npy
   │     │  │  │  │  ├─ py2-objarr.npz
   │     │  │  │  │  ├─ py3-objarr.npy
   │     │  │  │  │  ├─ py3-objarr.npz
   │     │  │  │  │  ├─ python3.npy
   │     │  │  │  │  └─ win64python2.npy
   │     │  │  │  ├─ test_arraypad.py
   │     │  │  │  ├─ test_arraysetops.py
   │     │  │  │  ├─ test_arrayterator.py
   │     │  │  │  ├─ test_array_utils.py
   │     │  │  │  ├─ test_format.py
   │     │  │  │  ├─ test_function_base.py
   │     │  │  │  ├─ test_histograms.py
   │     │  │  │  ├─ test_index_tricks.py
   │     │  │  │  ├─ test_io.py
   │     │  │  │  ├─ test_loadtxt.py
   │     │  │  │  ├─ test_mixins.py
   │     │  │  │  ├─ test_nanfunctions.py
   │     │  │  │  ├─ test_packbits.py
   │     │  │  │  ├─ test_polynomial.py
   │     │  │  │  ├─ test_recfunctions.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_shape_base.py
   │     │  │  │  ├─ test_stride_tricks.py
   │     │  │  │  ├─ test_twodim_base.py
   │     │  │  │  ├─ test_type_check.py
   │     │  │  │  ├─ test_ufunclike.py
   │     │  │  │  ├─ test_utils.py
   │     │  │  │  ├─ test__datasource.py
   │     │  │  │  ├─ test__iotools.py
   │     │  │  │  ├─ test__version.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ user_array.py
   │     │  │  ├─ user_array.pyi
   │     │  │  ├─ _arraypad_impl.py
   │     │  │  ├─ _arraypad_impl.pyi
   │     │  │  ├─ _arraysetops_impl.py
   │     │  │  ├─ _arraysetops_impl.pyi
   │     │  │  ├─ _arrayterator_impl.py
   │     │  │  ├─ _arrayterator_impl.pyi
   │     │  │  ├─ _array_utils_impl.py
   │     │  │  ├─ _array_utils_impl.pyi
   │     │  │  ├─ _datasource.py
   │     │  │  ├─ _datasource.pyi
   │     │  │  ├─ _format_impl.py
   │     │  │  ├─ _format_impl.pyi
   │     │  │  ├─ _function_base_impl.py
   │     │  │  ├─ _function_base_impl.pyi
   │     │  │  ├─ _histograms_impl.py
   │     │  │  ├─ _histograms_impl.pyi
   │     │  │  ├─ _index_tricks_impl.py
   │     │  │  ├─ _index_tricks_impl.pyi
   │     │  │  ├─ _iotools.py
   │     │  │  ├─ _iotools.pyi
   │     │  │  ├─ _nanfunctions_impl.py
   │     │  │  ├─ _nanfunctions_impl.pyi
   │     │  │  ├─ _npyio_impl.py
   │     │  │  ├─ _npyio_impl.pyi
   │     │  │  ├─ _polynomial_impl.py
   │     │  │  ├─ _polynomial_impl.pyi
   │     │  │  ├─ _scimath_impl.py
   │     │  │  ├─ _scimath_impl.pyi
   │     │  │  ├─ _shape_base_impl.py
   │     │  │  ├─ _shape_base_impl.pyi
   │     │  │  ├─ _stride_tricks_impl.py
   │     │  │  ├─ _stride_tricks_impl.pyi
   │     │  │  ├─ _twodim_base_impl.py
   │     │  │  ├─ _twodim_base_impl.pyi
   │     │  │  ├─ _type_check_impl.py
   │     │  │  ├─ _type_check_impl.pyi
   │     │  │  ├─ _ufunclike_impl.py
   │     │  │  ├─ _ufunclike_impl.pyi
   │     │  │  ├─ _user_array_impl.py
   │     │  │  ├─ _user_array_impl.pyi
   │     │  │  ├─ _utils_impl.py
   │     │  │  ├─ _utils_impl.pyi
   │     │  │  ├─ _version.py
   │     │  │  ├─ _version.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ linalg
   │     │  │  ├─ lapack_lite.cp313-win_amd64.lib
   │     │  │  ├─ lapack_lite.cp313-win_amd64.pyd
   │     │  │  ├─ lapack_lite.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_deprecations.py
   │     │  │  │  ├─ test_linalg.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _linalg.py
   │     │  │  ├─ _linalg.pyi
   │     │  │  ├─ _umath_linalg.cp313-win_amd64.lib
   │     │  │  ├─ _umath_linalg.cp313-win_amd64.pyd
   │     │  │  ├─ _umath_linalg.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ ma
   │     │  │  ├─ API_CHANGES.txt
   │     │  │  ├─ core.py
   │     │  │  ├─ core.pyi
   │     │  │  ├─ extras.py
   │     │  │  ├─ extras.pyi
   │     │  │  ├─ LICENSE
   │     │  │  ├─ mrecords.py
   │     │  │  ├─ mrecords.pyi
   │     │  │  ├─ README.rst
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_arrayobject.py
   │     │  │  │  ├─ test_core.py
   │     │  │  │  ├─ test_deprecations.py
   │     │  │  │  ├─ test_extras.py
   │     │  │  │  ├─ test_mrecords.py
   │     │  │  │  ├─ test_old_ma.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_subclassing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ testutils.py
   │     │  │  ├─ testutils.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ matlib.py
   │     │  ├─ matlib.pyi
   │     │  ├─ matrixlib
   │     │  │  ├─ defmatrix.py
   │     │  │  ├─ defmatrix.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_defmatrix.py
   │     │  │  │  ├─ test_interaction.py
   │     │  │  │  ├─ test_masked_matrix.py
   │     │  │  │  ├─ test_matrix_linalg.py
   │     │  │  │  ├─ test_multiarray.py
   │     │  │  │  ├─ test_numeric.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ polynomial
   │     │  │  ├─ chebyshev.py
   │     │  │  ├─ chebyshev.pyi
   │     │  │  ├─ hermite.py
   │     │  │  ├─ hermite.pyi
   │     │  │  ├─ hermite_e.py
   │     │  │  ├─ hermite_e.pyi
   │     │  │  ├─ laguerre.py
   │     │  │  ├─ laguerre.pyi
   │     │  │  ├─ legendre.py
   │     │  │  ├─ legendre.pyi
   │     │  │  ├─ polynomial.py
   │     │  │  ├─ polynomial.pyi
   │     │  │  ├─ polyutils.py
   │     │  │  ├─ polyutils.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_chebyshev.py
   │     │  │  │  ├─ test_classes.py
   │     │  │  │  ├─ test_hermite.py
   │     │  │  │  ├─ test_hermite_e.py
   │     │  │  │  ├─ test_laguerre.py
   │     │  │  │  ├─ test_legendre.py
   │     │  │  │  ├─ test_polynomial.py
   │     │  │  │  ├─ test_polyutils.py
   │     │  │  │  ├─ test_printing.py
   │     │  │  │  ├─ test_symbol.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _polybase.py
   │     │  │  ├─ _polybase.pyi
   │     │  │  ├─ _polytypes.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ py.typed
   │     │  ├─ random
   │     │  │  ├─ bit_generator.cp313-win_amd64.lib
   │     │  │  ├─ bit_generator.cp313-win_amd64.pyd
   │     │  │  ├─ bit_generator.pxd
   │     │  │  ├─ bit_generator.pyi
   │     │  │  ├─ lib
   │     │  │  │  └─ npyrandom.lib
   │     │  │  ├─ LICENSE.md
   │     │  │  ├─ mtrand.cp313-win_amd64.lib
   │     │  │  ├─ mtrand.cp313-win_amd64.pyd
   │     │  │  ├─ mtrand.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ generator_pcg64_np121.pkl.gz
   │     │  │  │  │  ├─ generator_pcg64_np126.pkl.gz
   │     │  │  │  │  ├─ mt19937-testset-1.csv
   │     │  │  │  │  ├─ mt19937-testset-2.csv
   │     │  │  │  │  ├─ pcg64-testset-1.csv
   │     │  │  │  │  ├─ pcg64-testset-2.csv
   │     │  │  │  │  ├─ pcg64dxsm-testset-1.csv
   │     │  │  │  │  ├─ pcg64dxsm-testset-2.csv
   │     │  │  │  │  ├─ philox-testset-1.csv
   │     │  │  │  │  ├─ philox-testset-2.csv
   │     │  │  │  │  ├─ sfc64-testset-1.csv
   │     │  │  │  │  ├─ sfc64-testset-2.csv
   │     │  │  │  │  ├─ sfc64_np126.pkl.gz
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_direct.py
   │     │  │  │  ├─ test_extending.py
   │     │  │  │  ├─ test_generator_mt19937.py
   │     │  │  │  ├─ test_generator_mt19937_regressions.py
   │     │  │  │  ├─ test_random.py
   │     │  │  │  ├─ test_randomstate.py
   │     │  │  │  ├─ test_randomstate_regression.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_seed_sequence.py
   │     │  │  │  ├─ test_smoke.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _bounded_integers.cp313-win_amd64.lib
   │     │  │  ├─ _bounded_integers.cp313-win_amd64.pyd
   │     │  │  ├─ _bounded_integers.pxd
   │     │  │  ├─ _bounded_integers.pyi
   │     │  │  ├─ _common.cp313-win_amd64.lib
   │     │  │  ├─ _common.cp313-win_amd64.pyd
   │     │  │  ├─ _common.pxd
   │     │  │  ├─ _common.pyi
   │     │  │  ├─ _examples
   │     │  │  │  ├─ cffi
   │     │  │  │  │  ├─ extending.py
   │     │  │  │  │  └─ parse.py
   │     │  │  │  ├─ cython
   │     │  │  │  │  ├─ extending.pyx
   │     │  │  │  │  └─ meson.build
   │     │  │  │  └─ numba
   │     │  │  │     └─ extending.py
   │     │  │  ├─ _generator.cp313-win_amd64.lib
   │     │  │  ├─ _generator.cp313-win_amd64.pyd
   │     │  │  ├─ _generator.pyi
   │     │  │  ├─ _mt19937.cp313-win_amd64.lib
   │     │  │  ├─ _mt19937.cp313-win_amd64.pyd
   │     │  │  ├─ _mt19937.pyi
   │     │  │  ├─ _pcg64.cp313-win_amd64.lib
   │     │  │  ├─ _pcg64.cp313-win_amd64.pyd
   │     │  │  ├─ _pcg64.pyi
   │     │  │  ├─ _philox.cp313-win_amd64.lib
   │     │  │  ├─ _philox.cp313-win_amd64.pyd
   │     │  │  ├─ _philox.pyi
   │     │  │  ├─ _pickle.py
   │     │  │  ├─ _pickle.pyi
   │     │  │  ├─ _sfc64.cp313-win_amd64.lib
   │     │  │  ├─ _sfc64.cp313-win_amd64.pyd
   │     │  │  ├─ _sfc64.pyi
   │     │  │  ├─ __init__.pxd
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ rec
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ strings
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ testing
   │     │  │  ├─ overrides.py
   │     │  │  ├─ overrides.pyi
   │     │  │  ├─ print_coercion_tables.py
   │     │  │  ├─ print_coercion_tables.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _private
   │     │  │  │  ├─ extbuild.py
   │     │  │  │  ├─ extbuild.pyi
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ utils.pyi
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __init__.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ tests
   │     │  │  ├─ test_configtool.py
   │     │  │  ├─ test_ctypeslib.py
   │     │  │  ├─ test_lazyloading.py
   │     │  │  ├─ test_matlib.py
   │     │  │  ├─ test_numpy_config.py
   │     │  │  ├─ test_numpy_version.py
   │     │  │  ├─ test_public_api.py
   │     │  │  ├─ test_reloading.py
   │     │  │  ├─ test_scripts.py
   │     │  │  ├─ test_warnings.py
   │     │  │  ├─ test__all__.py
   │     │  │  └─ __init__.py
   │     │  ├─ typing
   │     │  │  ├─ mypy_plugin.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ fail
   │     │  │  │  │  │  ├─ arithmetic.pyi
   │     │  │  │  │  │  ├─ arrayprint.pyi
   │     │  │  │  │  │  ├─ arrayterator.pyi
   │     │  │  │  │  │  ├─ array_constructors.pyi
   │     │  │  │  │  │  ├─ array_like.pyi
   │     │  │  │  │  │  ├─ array_pad.pyi
   │     │  │  │  │  │  ├─ bitwise_ops.pyi
   │     │  │  │  │  │  ├─ char.pyi
   │     │  │  │  │  │  ├─ chararray.pyi
   │     │  │  │  │  │  ├─ comparisons.pyi
   │     │  │  │  │  │  ├─ constants.pyi
   │     │  │  │  │  │  ├─ datasource.pyi
   │     │  │  │  │  │  ├─ dtype.pyi
   │     │  │  │  │  │  ├─ einsumfunc.pyi
   │     │  │  │  │  │  ├─ flatiter.pyi
   │     │  │  │  │  │  ├─ fromnumeric.pyi
   │     │  │  │  │  │  ├─ histograms.pyi
   │     │  │  │  │  │  ├─ index_tricks.pyi
   │     │  │  │  │  │  ├─ lib_function_base.pyi
   │     │  │  │  │  │  ├─ lib_polynomial.pyi
   │     │  │  │  │  │  ├─ lib_utils.pyi
   │     │  │  │  │  │  ├─ lib_version.pyi
   │     │  │  │  │  │  ├─ linalg.pyi
   │     │  │  │  │  │  ├─ ma.pyi
   │     │  │  │  │  │  ├─ memmap.pyi
   │     │  │  │  │  │  ├─ modules.pyi
   │     │  │  │  │  │  ├─ multiarray.pyi
   │     │  │  │  │  │  ├─ ndarray.pyi
   │     │  │  │  │  │  ├─ ndarray_misc.pyi
   │     │  │  │  │  │  ├─ nditer.pyi
   │     │  │  │  │  │  ├─ nested_sequence.pyi
   │     │  │  │  │  │  ├─ npyio.pyi
   │     │  │  │  │  │  ├─ numerictypes.pyi
   │     │  │  │  │  │  ├─ random.pyi
   │     │  │  │  │  │  ├─ rec.pyi
   │     │  │  │  │  │  ├─ scalars.pyi
   │     │  │  │  │  │  ├─ shape.pyi
   │     │  │  │  │  │  ├─ shape_base.pyi
   │     │  │  │  │  │  ├─ stride_tricks.pyi
   │     │  │  │  │  │  ├─ strings.pyi
   │     │  │  │  │  │  ├─ testing.pyi
   │     │  │  │  │  │  ├─ twodim_base.pyi
   │     │  │  │  │  │  ├─ type_check.pyi
   │     │  │  │  │  │  ├─ ufunclike.pyi
   │     │  │  │  │  │  ├─ ufuncs.pyi
   │     │  │  │  │  │  ├─ ufunc_config.pyi
   │     │  │  │  │  │  └─ warnings_and_errors.pyi
   │     │  │  │  │  ├─ misc
   │     │  │  │  │  │  └─ extended_precision.pyi
   │     │  │  │  │  ├─ mypy.ini
   │     │  │  │  │  ├─ pass
   │     │  │  │  │  │  ├─ arithmetic.py
   │     │  │  │  │  │  ├─ arrayprint.py
   │     │  │  │  │  │  ├─ arrayterator.py
   │     │  │  │  │  │  ├─ array_constructors.py
   │     │  │  │  │  │  ├─ array_like.py
   │     │  │  │  │  │  ├─ bitwise_ops.py
   │     │  │  │  │  │  ├─ comparisons.py
   │     │  │  │  │  │  ├─ dtype.py
   │     │  │  │  │  │  ├─ einsumfunc.py
   │     │  │  │  │  │  ├─ flatiter.py
   │     │  │  │  │  │  ├─ fromnumeric.py
   │     │  │  │  │  │  ├─ index_tricks.py
   │     │  │  │  │  │  ├─ lib_user_array.py
   │     │  │  │  │  │  ├─ lib_utils.py
   │     │  │  │  │  │  ├─ lib_version.py
   │     │  │  │  │  │  ├─ literal.py
   │     │  │  │  │  │  ├─ ma.py
   │     │  │  │  │  │  ├─ mod.py
   │     │  │  │  │  │  ├─ modules.py
   │     │  │  │  │  │  ├─ multiarray.py
   │     │  │  │  │  │  ├─ ndarray_conversion.py
   │     │  │  │  │  │  ├─ ndarray_misc.py
   │     │  │  │  │  │  ├─ ndarray_shape_manipulation.py
   │     │  │  │  │  │  ├─ nditer.py
   │     │  │  │  │  │  ├─ numeric.py
   │     │  │  │  │  │  ├─ numerictypes.py
   │     │  │  │  │  │  ├─ random.py
   │     │  │  │  │  │  ├─ recfunctions.py
   │     │  │  │  │  │  ├─ scalars.py
   │     │  │  │  │  │  ├─ shape.py
   │     │  │  │  │  │  ├─ simple.py
   │     │  │  │  │  │  ├─ ufunclike.py
   │     │  │  │  │  │  ├─ ufuncs.py
   │     │  │  │  │  │  ├─ ufunc_config.py
   │     │  │  │  │  │  └─ warnings_and_errors.py
   │     │  │  │  │  └─ reveal
   │     │  │  │  │     ├─ arithmetic.pyi
   │     │  │  │  │     ├─ arraypad.pyi
   │     │  │  │  │     ├─ arrayprint.pyi
   │     │  │  │  │     ├─ arraysetops.pyi
   │     │  │  │  │     ├─ arrayterator.pyi
   │     │  │  │  │     ├─ array_api_info.pyi
   │     │  │  │  │     ├─ array_constructors.pyi
   │     │  │  │  │     ├─ bitwise_ops.pyi
   │     │  │  │  │     ├─ char.pyi
   │     │  │  │  │     ├─ chararray.pyi
   │     │  │  │  │     ├─ comparisons.pyi
   │     │  │  │  │     ├─ constants.pyi
   │     │  │  │  │     ├─ ctypeslib.pyi
   │     │  │  │  │     ├─ datasource.pyi
   │     │  │  │  │     ├─ dtype.pyi
   │     │  │  │  │     ├─ einsumfunc.pyi
   │     │  │  │  │     ├─ emath.pyi
   │     │  │  │  │     ├─ fft.pyi
   │     │  │  │  │     ├─ flatiter.pyi
   │     │  │  │  │     ├─ fromnumeric.pyi
   │     │  │  │  │     ├─ getlimits.pyi
   │     │  │  │  │     ├─ histograms.pyi
   │     │  │  │  │     ├─ index_tricks.pyi
   │     │  │  │  │     ├─ lib_function_base.pyi
   │     │  │  │  │     ├─ lib_polynomial.pyi
   │     │  │  │  │     ├─ lib_utils.pyi
   │     │  │  │  │     ├─ lib_version.pyi
   │     │  │  │  │     ├─ linalg.pyi
   │     │  │  │  │     ├─ ma.pyi
   │     │  │  │  │     ├─ matrix.pyi
   │     │  │  │  │     ├─ memmap.pyi
   │     │  │  │  │     ├─ mod.pyi
   │     │  │  │  │     ├─ modules.pyi
   │     │  │  │  │     ├─ multiarray.pyi
   │     │  │  │  │     ├─ nbit_base_example.pyi
   │     │  │  │  │     ├─ ndarray_assignability.pyi
   │     │  │  │  │     ├─ ndarray_conversion.pyi
   │     │  │  │  │     ├─ ndarray_misc.pyi
   │     │  │  │  │     ├─ ndarray_shape_manipulation.pyi
   │     │  │  │  │     ├─ nditer.pyi
   │     │  │  │  │     ├─ nested_sequence.pyi
   │     │  │  │  │     ├─ npyio.pyi
   │     │  │  │  │     ├─ numeric.pyi
   │     │  │  │  │     ├─ numerictypes.pyi
   │     │  │  │  │     ├─ polynomial_polybase.pyi
   │     │  │  │  │     ├─ polynomial_polyutils.pyi
   │     │  │  │  │     ├─ polynomial_series.pyi
   │     │  │  │  │     ├─ random.pyi
   │     │  │  │  │     ├─ rec.pyi
   │     │  │  │  │     ├─ scalars.pyi
   │     │  │  │  │     ├─ shape.pyi
   │     │  │  │  │     ├─ shape_base.pyi
   │     │  │  │  │     ├─ stride_tricks.pyi
   │     │  │  │  │     ├─ strings.pyi
   │     │  │  │  │     ├─ testing.pyi
   │     │  │  │  │     ├─ twodim_base.pyi
   │     │  │  │  │     ├─ type_check.pyi
   │     │  │  │  │     ├─ ufunclike.pyi
   │     │  │  │  │     ├─ ufuncs.pyi
   │     │  │  │  │     ├─ ufunc_config.pyi
   │     │  │  │  │     └─ warnings_and_errors.pyi
   │     │  │  │  ├─ test_isfile.py
   │     │  │  │  ├─ test_runtime.py
   │     │  │  │  ├─ test_typing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ version.py
   │     │  ├─ version.pyi
   │     │  ├─ _array_api_info.py
   │     │  ├─ _array_api_info.pyi
   │     │  ├─ _configtool.py
   │     │  ├─ _configtool.pyi
   │     │  ├─ _core
   │     │  │  ├─ arrayprint.py
   │     │  │  ├─ arrayprint.pyi
   │     │  │  ├─ cversions.py
   │     │  │  ├─ defchararray.py
   │     │  │  ├─ defchararray.pyi
   │     │  │  ├─ einsumfunc.py
   │     │  │  ├─ einsumfunc.pyi
   │     │  │  ├─ fromnumeric.py
   │     │  │  ├─ fromnumeric.pyi
   │     │  │  ├─ function_base.py
   │     │  │  ├─ function_base.pyi
   │     │  │  ├─ getlimits.py
   │     │  │  ├─ getlimits.pyi
   │     │  │  ├─ include
   │     │  │  │  └─ numpy
   │     │  │  │     ├─ arrayobject.h
   │     │  │  │     ├─ arrayscalars.h
   │     │  │  │     ├─ dtype_api.h
   │     │  │  │     ├─ halffloat.h
   │     │  │  │     ├─ ndarrayobject.h
   │     │  │  │     ├─ ndarraytypes.h
   │     │  │  │     ├─ npy_2_compat.h
   │     │  │  │     ├─ npy_2_complexcompat.h
   │     │  │  │     ├─ npy_3kcompat.h
   │     │  │  │     ├─ npy_common.h
   │     │  │  │     ├─ npy_cpu.h
   │     │  │  │     ├─ npy_endian.h
   │     │  │  │     ├─ npy_math.h
   │     │  │  │     ├─ npy_no_deprecated_api.h
   │     │  │  │     ├─ npy_os.h
   │     │  │  │     ├─ numpyconfig.h
   │     │  │  │     ├─ random
   │     │  │  │     │  ├─ bitgen.h
   │     │  │  │     │  ├─ libdivide.h
   │     │  │  │     │  └─ LICENSE.txt
   │     │  │  │     ├─ ufuncobject.h
   │     │  │  │     ├─ utils.h
   │     │  │  │     ├─ _neighborhood_iterator_imp.h
   │     │  │  │     ├─ _numpyconfig.h
   │     │  │  │     ├─ _public_dtype_api_table.h
   │     │  │  │     ├─ __multiarray_api.c
   │     │  │  │     ├─ __multiarray_api.h
   │     │  │  │     ├─ __ufunc_api.c
   │     │  │  │     └─ __ufunc_api.h
   │     │  │  ├─ lib
   │     │  │  │  ├─ npy-pkg-config
   │     │  │  │  │  ├─ mlib.ini
   │     │  │  │  │  └─ npymath.ini
   │     │  │  │  ├─ npymath.lib
   │     │  │  │  └─ pkgconfig
   │     │  │  │     └─ numpy.pc
   │     │  │  ├─ memmap.py
   │     │  │  ├─ memmap.pyi
   │     │  │  ├─ multiarray.py
   │     │  │  ├─ multiarray.pyi
   │     │  │  ├─ numeric.py
   │     │  │  ├─ numeric.pyi
   │     │  │  ├─ numerictypes.py
   │     │  │  ├─ numerictypes.pyi
   │     │  │  ├─ overrides.py
   │     │  │  ├─ overrides.pyi
   │     │  │  ├─ printoptions.py
   │     │  │  ├─ printoptions.pyi
   │     │  │  ├─ records.py
   │     │  │  ├─ records.pyi
   │     │  │  ├─ shape_base.py
   │     │  │  ├─ shape_base.pyi
   │     │  │  ├─ strings.py
   │     │  │  ├─ strings.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ astype_copy.pkl
   │     │  │  │  │  ├─ generate_umath_validation_data.cpp
   │     │  │  │  │  ├─ recarray_from_file.fits
   │     │  │  │  │  ├─ umath-validation-set-arccos.csv
   │     │  │  │  │  ├─ umath-validation-set-arccosh.csv
   │     │  │  │  │  ├─ umath-validation-set-arcsin.csv
   │     │  │  │  │  ├─ umath-validation-set-arcsinh.csv
   │     │  │  │  │  ├─ umath-validation-set-arctan.csv
   │     │  │  │  │  ├─ umath-validation-set-arctanh.csv
   │     │  │  │  │  ├─ umath-validation-set-cbrt.csv
   │     │  │  │  │  ├─ umath-validation-set-cos.csv
   │     │  │  │  │  ├─ umath-validation-set-cosh.csv
   │     │  │  │  │  ├─ umath-validation-set-exp.csv
   │     │  │  │  │  ├─ umath-validation-set-exp2.csv
   │     │  │  │  │  ├─ umath-validation-set-expm1.csv
   │     │  │  │  │  ├─ umath-validation-set-log.csv
   │     │  │  │  │  ├─ umath-validation-set-log10.csv
   │     │  │  │  │  ├─ umath-validation-set-log1p.csv
   │     │  │  │  │  ├─ umath-validation-set-log2.csv
   │     │  │  │  │  ├─ umath-validation-set-README.txt
   │     │  │  │  │  ├─ umath-validation-set-sin.csv
   │     │  │  │  │  ├─ umath-validation-set-sinh.csv
   │     │  │  │  │  ├─ umath-validation-set-tan.csv
   │     │  │  │  │  └─ umath-validation-set-tanh.csv
   │     │  │  │  ├─ examples
   │     │  │  │  │  ├─ cython
   │     │  │  │  │  │  ├─ checks.pyx
   │     │  │  │  │  │  ├─ meson.build
   │     │  │  │  │  │  └─ setup.py
   │     │  │  │  │  └─ limited_api
   │     │  │  │  │     ├─ limited_api1.c
   │     │  │  │  │     ├─ limited_api2.pyx
   │     │  │  │  │     ├─ limited_api_latest.c
   │     │  │  │  │     ├─ meson.build
   │     │  │  │  │     └─ setup.py
   │     │  │  │  ├─ test_abc.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_argparse.py
   │     │  │  │  ├─ test_arraymethod.py
   │     │  │  │  ├─ test_arrayobject.py
   │     │  │  │  ├─ test_arrayprint.py
   │     │  │  │  ├─ test_array_api_info.py
   │     │  │  │  ├─ test_array_coercion.py
   │     │  │  │  ├─ test_array_interface.py
   │     │  │  │  ├─ test_casting_floatingpoint_errors.py
   │     │  │  │  ├─ test_casting_unittests.py
   │     │  │  │  ├─ test_conversion_utils.py
   │     │  │  │  ├─ test_cpu_dispatcher.py
   │     │  │  │  ├─ test_cpu_features.py
   │     │  │  │  ├─ test_custom_dtypes.py
   │     │  │  │  ├─ test_cython.py
   │     │  │  │  ├─ test_datetime.py
   │     │  │  │  ├─ test_defchararray.py
   │     │  │  │  ├─ test_deprecations.py
   │     │  │  │  ├─ test_dlpack.py
   │     │  │  │  ├─ test_dtype.py
   │     │  │  │  ├─ test_einsum.py
   │     │  │  │  ├─ test_errstate.py
   │     │  │  │  ├─ test_extint128.py
   │     │  │  │  ├─ test_finfo.py
   │     │  │  │  ├─ test_function_base.py
   │     │  │  │  ├─ test_getlimits.py
   │     │  │  │  ├─ test_half.py
   │     │  │  │  ├─ test_hashtable.py
   │     │  │  │  ├─ test_indexerrors.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_item_selection.py
   │     │  │  │  ├─ test_limited_api.py
   │     │  │  │  ├─ test_longdouble.py
   │     │  │  │  ├─ test_memmap.py
   │     │  │  │  ├─ test_mem_overlap.py
   │     │  │  │  ├─ test_mem_policy.py
   │     │  │  │  ├─ test_multiarray.py
   │     │  │  │  ├─ test_multiprocessing.py
   │     │  │  │  ├─ test_multithreading.py
   │     │  │  │  ├─ test_nditer.py
   │     │  │  │  ├─ test_nep50_promotions.py
   │     │  │  │  ├─ test_numeric.py
   │     │  │  │  ├─ test_numerictypes.py
   │     │  │  │  ├─ test_overrides.py
   │     │  │  │  ├─ test_print.py
   │     │  │  │  ├─ test_protocols.py
   │     │  │  │  ├─ test_records.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_scalarbuffer.py
   │     │  │  │  ├─ test_scalarinherit.py
   │     │  │  │  ├─ test_scalarmath.py
   │     │  │  │  ├─ test_scalarprint.py
   │     │  │  │  ├─ test_scalar_ctors.py
   │     │  │  │  ├─ test_scalar_methods.py
   │     │  │  │  ├─ test_shape_base.py
   │     │  │  │  ├─ test_simd.py
   │     │  │  │  ├─ test_simd_module.py
   │     │  │  │  ├─ test_stringdtype.py
   │     │  │  │  ├─ test_strings.py
   │     │  │  │  ├─ test_ufunc.py
   │     │  │  │  ├─ test_umath.py
   │     │  │  │  ├─ test_umath_accuracy.py
   │     │  │  │  ├─ test_umath_complex.py
   │     │  │  │  ├─ test_unicode.py
   │     │  │  │  ├─ test__exceptions.py
   │     │  │  │  ├─ _locales.py
   │     │  │  │  └─ _natype.py
   │     │  │  ├─ umath.py
   │     │  │  ├─ umath.pyi
   │     │  │  ├─ _add_newdocs.py
   │     │  │  ├─ _add_newdocs.pyi
   │     │  │  ├─ _add_newdocs_scalars.py
   │     │  │  ├─ _add_newdocs_scalars.pyi
   │     │  │  ├─ _asarray.py
   │     │  │  ├─ _asarray.pyi
   │     │  │  ├─ _dtype.py
   │     │  │  ├─ _dtype.pyi
   │     │  │  ├─ _dtype_ctypes.py
   │     │  │  ├─ _dtype_ctypes.pyi
   │     │  │  ├─ _exceptions.py
   │     │  │  ├─ _exceptions.pyi
   │     │  │  ├─ _internal.py
   │     │  │  ├─ _internal.pyi
   │     │  │  ├─ _methods.py
   │     │  │  ├─ _methods.pyi
   │     │  │  ├─ _multiarray_tests.cp313-win_amd64.lib
   │     │  │  ├─ _multiarray_tests.cp313-win_amd64.pyd
   │     │  │  ├─ _multiarray_umath.cp313-win_amd64.lib
   │     │  │  ├─ _multiarray_umath.cp313-win_amd64.pyd
   │     │  │  ├─ _operand_flag_tests.cp313-win_amd64.lib
   │     │  │  ├─ _operand_flag_tests.cp313-win_amd64.pyd
   │     │  │  ├─ _rational_tests.cp313-win_amd64.lib
   │     │  │  ├─ _rational_tests.cp313-win_amd64.pyd
   │     │  │  ├─ _simd.cp313-win_amd64.lib
   │     │  │  ├─ _simd.cp313-win_amd64.pyd
   │     │  │  ├─ _simd.pyi
   │     │  │  ├─ _string_helpers.py
   │     │  │  ├─ _string_helpers.pyi
   │     │  │  ├─ _struct_ufunc_tests.cp313-win_amd64.lib
   │     │  │  ├─ _struct_ufunc_tests.cp313-win_amd64.pyd
   │     │  │  ├─ _type_aliases.py
   │     │  │  ├─ _type_aliases.pyi
   │     │  │  ├─ _ufunc_config.py
   │     │  │  ├─ _ufunc_config.pyi
   │     │  │  ├─ _umath_tests.cp313-win_amd64.lib
   │     │  │  ├─ _umath_tests.cp313-win_amd64.pyd
   │     │  │  ├─ _umath_tests.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ _expired_attrs_2_0.py
   │     │  ├─ _expired_attrs_2_0.pyi
   │     │  ├─ _globals.py
   │     │  ├─ _globals.pyi
   │     │  ├─ _pyinstaller
   │     │  │  ├─ hook-numpy.py
   │     │  │  ├─ hook-numpy.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ pyinstaller-smoke.py
   │     │  │  │  ├─ test_pyinstaller.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ _pytesttester.py
   │     │  ├─ _pytesttester.pyi
   │     │  ├─ _typing
   │     │  │  ├─ _add_docstring.py
   │     │  │  ├─ _array_like.py
   │     │  │  ├─ _char_codes.py
   │     │  │  ├─ _dtype_like.py
   │     │  │  ├─ _extended_precision.py
   │     │  │  ├─ _nbit.py
   │     │  │  ├─ _nbit_base.py
   │     │  │  ├─ _nbit_base.pyi
   │     │  │  ├─ _nested_sequence.py
   │     │  │  ├─ _scalars.py
   │     │  │  ├─ _shape.py
   │     │  │  ├─ _ufunc.py
   │     │  │  ├─ _ufunc.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ _utils
   │     │  │  ├─ _convertions.py
   │     │  │  ├─ _convertions.pyi
   │     │  │  ├─ _inspect.py
   │     │  │  ├─ _inspect.pyi
   │     │  │  ├─ _pep440.py
   │     │  │  ├─ _pep440.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ __config__.py
   │     │  ├─ __config__.pyi
   │     │  ├─ __init__.cython-30.pxd
   │     │  ├─ __init__.pxd
   │     │  ├─ __init__.py
   │     │  └─ __init__.pyi
   │     ├─ numpy.libs
   │     │  ├─ libscipy_openblas64_-63c857e738469261263c764a36be9436.dll
   │     │  └─ msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
   │     ├─ onnxruntime
   │     │  ├─ backend
   │     │  │  ├─ backend.py
   │     │  │  ├─ backend_rep.py
   │     │  │  └─ __init__.py
   │     │  ├─ capi
   │     │  │  ├─ build_and_package_info.py
   │     │  │  ├─ convert_npz_to_onnx_adapter.py
   │     │  │  ├─ onnxruntime.dll
   │     │  │  ├─ onnxruntime_collect_build_info.py
   │     │  │  ├─ onnxruntime_inference_collection.py
   │     │  │  ├─ onnxruntime_providers_shared.dll
   │     │  │  ├─ onnxruntime_pybind11_state.pyd
   │     │  │  ├─ onnxruntime_validation.py
   │     │  │  ├─ version_info.py
   │     │  │  ├─ _ld_preload.py
   │     │  │  ├─ _pybind_state.py
   │     │  │  └─ __init__.py
   │     │  ├─ datasets
   │     │  │  ├─ logreg_iris.onnx
   │     │  │  ├─ mul_1.onnx
   │     │  │  ├─ sigmoid.onnx
   │     │  │  └─ __init__.py
   │     │  ├─ LICENSE
   │     │  ├─ Privacy.md
   │     │  ├─ quantization
   │     │  │  ├─ base_quantizer.py
   │     │  │  ├─ calibrate.py
   │     │  │  ├─ CalTableFlatBuffers
   │     │  │  │  ├─ KeyValue.py
   │     │  │  │  ├─ TrtTable.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ execution_providers
   │     │  │  │  └─ qnn
   │     │  │  │     ├─ fusion_lpnorm.py
   │     │  │  │     ├─ fusion_spacetodepth.py
   │     │  │  │     ├─ mixed_precision_overrides_utils.py
   │     │  │  │     ├─ preprocess.py
   │     │  │  │     ├─ quant_config.py
   │     │  │  │     └─ __init__.py
   │     │  │  ├─ fusions
   │     │  │  │  ├─ fusion.py
   │     │  │  │  ├─ fusion_gelu.py
   │     │  │  │  ├─ fusion_layernorm.py
   │     │  │  │  ├─ replace_upsample_with_resize.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ matmul_bnb4_quantizer.py
   │     │  │  ├─ matmul_nbits_quantizer.py
   │     │  │  ├─ neural_compressor
   │     │  │  │  ├─ onnx_model.py
   │     │  │  │  ├─ util.py
   │     │  │  │  ├─ weight_only.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ onnx_model.py
   │     │  │  ├─ onnx_quantizer.py
   │     │  │  ├─ operators
   │     │  │  │  ├─ activation.py
   │     │  │  │  ├─ argmax.py
   │     │  │  │  ├─ attention.py
   │     │  │  │  ├─ base_operator.py
   │     │  │  │  ├─ binary_op.py
   │     │  │  │  ├─ concat.py
   │     │  │  │  ├─ conv.py
   │     │  │  │  ├─ direct_q8.py
   │     │  │  │  ├─ embed_layernorm.py
   │     │  │  │  ├─ gather.py
   │     │  │  │  ├─ gavgpool.py
   │     │  │  │  ├─ gemm.py
   │     │  │  │  ├─ lstm.py
   │     │  │  │  ├─ matmul.py
   │     │  │  │  ├─ maxpool.py
   │     │  │  │  ├─ norm.py
   │     │  │  │  ├─ pad.py
   │     │  │  │  ├─ pooling.py
   │     │  │  │  ├─ qdq_base_operator.py
   │     │  │  │  ├─ resize.py
   │     │  │  │  ├─ softmax.py
   │     │  │  │  ├─ split.py
   │     │  │  │  ├─ where.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ preprocess.py
   │     │  │  ├─ qdq_loss_debug.py
   │     │  │  ├─ qdq_quantizer.py
   │     │  │  ├─ quantize.py
   │     │  │  ├─ quant_utils.py
   │     │  │  ├─ registry.py
   │     │  │  ├─ shape_inference.py
   │     │  │  ├─ static_quantize_runner.py
   │     │  │  ├─ tensor_quant_overrides.py
   │     │  │  └─ __init__.py
   │     │  ├─ ThirdPartyNotices.txt
   │     │  ├─ tools
   │     │  │  ├─ check_onnx_model_mobile_usability.py
   │     │  │  ├─ convert_onnx_models_to_ort.py
   │     │  │  ├─ file_utils.py
   │     │  │  ├─ logger.py
   │     │  │  ├─ make_dynamic_shape_fixed.py
   │     │  │  ├─ mobile_helpers
   │     │  │  │  ├─ coreml_supported_mlprogram_ops.md
   │     │  │  │  ├─ coreml_supported_neuralnetwork_ops.md
   │     │  │  │  ├─ nnapi_supported_ops.md
   │     │  │  │  ├─ usability_checker.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ offline_tuning.py
   │     │  │  ├─ onnxruntime_test.py
   │     │  │  ├─ onnx_model_utils.py
   │     │  │  ├─ onnx_randomizer.py
   │     │  │  ├─ optimize_onnx_model.py
   │     │  │  ├─ ort_format_model
   │     │  │  │  ├─ operator_type_usage_processors.py
   │     │  │  │  ├─ ort_flatbuffers_py
   │     │  │  │  │  ├─ fbs
   │     │  │  │  │  │  ├─ ArgType.py
   │     │  │  │  │  │  ├─ ArgTypeAndIndex.py
   │     │  │  │  │  │  ├─ Attribute.py
   │     │  │  │  │  │  ├─ AttributeType.py
   │     │  │  │  │  │  ├─ Checkpoint.py
   │     │  │  │  │  │  ├─ DeprecatedKernelCreateInfos.py
   │     │  │  │  │  │  ├─ DeprecatedNodeIndexAndKernelDefHash.py
   │     │  │  │  │  │  ├─ DeprecatedSessionState.py
   │     │  │  │  │  │  ├─ DeprecatedSubGraphSessionState.py
   │     │  │  │  │  │  ├─ Dimension.py
   │     │  │  │  │  │  ├─ DimensionValue.py
   │     │  │  │  │  │  ├─ DimensionValueType.py
   │     │  │  │  │  │  ├─ EdgeEnd.py
   │     │  │  │  │  │  ├─ FloatProperty.py
   │     │  │  │  │  │  ├─ Graph.py
   │     │  │  │  │  │  ├─ InferenceSession.py
   │     │  │  │  │  │  ├─ IntProperty.py
   │     │  │  │  │  │  ├─ KernelTypeStrArgsEntry.py
   │     │  │  │  │  │  ├─ KernelTypeStrResolver.py
   │     │  │  │  │  │  ├─ MapType.py
   │     │  │  │  │  │  ├─ Model.py
   │     │  │  │  │  │  ├─ ModuleState.py
   │     │  │  │  │  │  ├─ Node.py
   │     │  │  │  │  │  ├─ NodeEdge.py
   │     │  │  │  │  │  ├─ NodesToOptimizeIndices.py
   │     │  │  │  │  │  ├─ NodeType.py
   │     │  │  │  │  │  ├─ OperatorSetId.py
   │     │  │  │  │  │  ├─ OpIdKernelTypeStrArgsEntry.py
   │     │  │  │  │  │  ├─ OptimizerGroup.py
   │     │  │  │  │  │  ├─ ParameterOptimizerState.py
   │     │  │  │  │  │  ├─ PropertyBag.py
   │     │  │  │  │  │  ├─ RuntimeOptimizationRecord.py
   │     │  │  │  │  │  ├─ RuntimeOptimizationRecordContainerEntry.py
   │     │  │  │  │  │  ├─ RuntimeOptimizations.py
   │     │  │  │  │  │  ├─ SequenceType.py
   │     │  │  │  │  │  ├─ Shape.py
   │     │  │  │  │  │  ├─ SparseTensor.py
   │     │  │  │  │  │  ├─ StringProperty.py
   │     │  │  │  │  │  ├─ StringStringEntry.py
   │     │  │  │  │  │  ├─ Tensor.py
   │     │  │  │  │  │  ├─ TensorDataType.py
   │     │  │  │  │  │  ├─ TensorTypeAndShape.py
   │     │  │  │  │  │  ├─ TypeInfo.py
   │     │  │  │  │  │  ├─ TypeInfoValue.py
   │     │  │  │  │  │  ├─ ValueInfo.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ort_model_processor.py
   │     │  │  │  ├─ types.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pytorch_export_contrib_ops.py
   │     │  │  ├─ pytorch_export_helpers.py
   │     │  │  ├─ qdq_helpers
   │     │  │  │  ├─ optimize_qdq_model.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ qnn
   │     │  │  │  ├─ add_trans_cast.py
   │     │  │  │  ├─ gen_qnn_ctx_onnx_model.py
   │     │  │  │  └─ preprocess.py
   │     │  │  ├─ reduced_build_config_parser.py
   │     │  │  ├─ remove_initializer_from_input.py
   │     │  │  ├─ symbolic_shape_infer.py
   │     │  │  ├─ update_onnx_opset.py
   │     │  │  └─ __init__.py
   │     │  ├─ transformers
   │     │  │  ├─ affinity_helper.py
   │     │  │  ├─ benchmark.py
   │     │  │  ├─ benchmark_helper.py
   │     │  │  ├─ bert_perf_test.py
   │     │  │  ├─ bert_test_data.py
   │     │  │  ├─ compare_bert_results.py
   │     │  │  ├─ constants.py
   │     │  │  ├─ convert_generation.py
   │     │  │  ├─ convert_tf_models_to_pytorch.py
   │     │  │  ├─ convert_to_packing_mode.py
   │     │  │  ├─ dynamo_onnx_helper.py
   │     │  │  ├─ float16.py
   │     │  │  ├─ fusion_attention.py
   │     │  │  ├─ fusion_attention_clip.py
   │     │  │  ├─ fusion_attention_sam2.py
   │     │  │  ├─ fusion_attention_unet.py
   │     │  │  ├─ fusion_attention_vae.py
   │     │  │  ├─ fusion_bart_attention.py
   │     │  │  ├─ fusion_base.py
   │     │  │  ├─ fusion_biasgelu.py
   │     │  │  ├─ fusion_biassplitgelu.py
   │     │  │  ├─ fusion_bias_add.py
   │     │  │  ├─ fusion_conformer_attention.py
   │     │  │  ├─ fusion_constant_fold.py
   │     │  │  ├─ fusion_embedlayer.py
   │     │  │  ├─ fusion_fastgelu.py
   │     │  │  ├─ fusion_gelu.py
   │     │  │  ├─ fusion_gelu_approximation.py
   │     │  │  ├─ fusion_gemmfastgelu.py
   │     │  │  ├─ fusion_gpt_attention.py
   │     │  │  ├─ fusion_gpt_attention_megatron.py
   │     │  │  ├─ fusion_gpt_attention_no_past.py
   │     │  │  ├─ fusion_group_norm.py
   │     │  │  ├─ fusion_layernorm.py
   │     │  │  ├─ fusion_mha_mmdit.py
   │     │  │  ├─ fusion_nhwc_conv.py
   │     │  │  ├─ fusion_options.py
   │     │  │  ├─ fusion_qordered_attention.py
   │     │  │  ├─ fusion_qordered_gelu.py
   │     │  │  ├─ fusion_qordered_layernorm.py
   │     │  │  ├─ fusion_qordered_matmul.py
   │     │  │  ├─ fusion_quickgelu.py
   │     │  │  ├─ fusion_reshape.py
   │     │  │  ├─ fusion_rotary_attention.py
   │     │  │  ├─ fusion_shape.py
   │     │  │  ├─ fusion_simplified_layernorm.py
   │     │  │  ├─ fusion_skiplayernorm.py
   │     │  │  ├─ fusion_skip_group_norm.py
   │     │  │  ├─ fusion_transpose.py
   │     │  │  ├─ fusion_utils.py
   │     │  │  ├─ huggingface_models.py
   │     │  │  ├─ import_utils.py
   │     │  │  ├─ io_binding_helper.py
   │     │  │  ├─ large_model_exporter.py
   │     │  │  ├─ machine_info.py
   │     │  │  ├─ metrics.py
   │     │  │  ├─ models
   │     │  │  │  ├─ bart
   │     │  │  │  │  ├─ export.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ bert
   │     │  │  │  │  ├─ eval_squad.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ gpt2
   │     │  │  │  │  ├─ benchmark_gpt2.py
   │     │  │  │  │  ├─ convert_to_onnx.py
   │     │  │  │  │  ├─ gpt2_helper.py
   │     │  │  │  │  ├─ gpt2_parity.py
   │     │  │  │  │  ├─ gpt2_tester.py
   │     │  │  │  │  ├─ parity_check_helper.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ llama
   │     │  │  │  │  ├─ benchmark.py
   │     │  │  │  │  ├─ benchmark_all.py
   │     │  │  │  │  ├─ benchmark_e2e.py
   │     │  │  │  │  ├─ convert_to_onnx.py
   │     │  │  │  │  ├─ llama_inputs.py
   │     │  │  │  │  ├─ llama_parity.py
   │     │  │  │  │  ├─ llama_torch.py
   │     │  │  │  │  ├─ quant_kv_dataloader.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ longformer
   │     │  │  │  │  ├─ benchmark_longformer.py
   │     │  │  │  │  ├─ convert_to_onnx.py
   │     │  │  │  │  ├─ generate_test_data.py
   │     │  │  │  │  ├─ longformer_helper.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ phi2
   │     │  │  │  │  ├─ convert_to_onnx.py
   │     │  │  │  │  ├─ inference_example.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sam2
   │     │  │  │  │  ├─ benchmark_sam2.py
   │     │  │  │  │  ├─ convert_to_onnx.py
   │     │  │  │  │  ├─ image_decoder.py
   │     │  │  │  │  ├─ image_encoder.py
   │     │  │  │  │  ├─ mask_decoder.py
   │     │  │  │  │  ├─ nvtx_helper.py
   │     │  │  │  │  ├─ prompt_encoder.py
   │     │  │  │  │  ├─ sam2_demo.py
   │     │  │  │  │  ├─ sam2_image_onnx_predictor.py
   │     │  │  │  │  ├─ sam2_utils.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ stable_diffusion
   │     │  │  │  │  ├─ benchmark.py
   │     │  │  │  │  ├─ benchmark_controlnet.py
   │     │  │  │  │  ├─ demo_txt2img.py
   │     │  │  │  │  ├─ demo_txt2img_xl.py
   │     │  │  │  │  ├─ demo_utils.py
   │     │  │  │  │  ├─ diffusion_models.py
   │     │  │  │  │  ├─ diffusion_schedulers.py
   │     │  │  │  │  ├─ engine_builder.py
   │     │  │  │  │  ├─ engine_builder_ort_cuda.py
   │     │  │  │  │  ├─ engine_builder_ort_trt.py
   │     │  │  │  │  ├─ engine_builder_tensorrt.py
   │     │  │  │  │  ├─ engine_builder_torch.py
   │     │  │  │  │  ├─ optimize_pipeline.py
   │     │  │  │  │  ├─ ort_optimizer.py
   │     │  │  │  │  ├─ pipeline_stable_diffusion.py
   │     │  │  │  │  ├─ trt_utilities.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ t5
   │     │  │  │  │  ├─ convert_to_onnx.py
   │     │  │  │  │  ├─ t5_decoder.py
   │     │  │  │  │  ├─ t5_encoder.py
   │     │  │  │  │  ├─ t5_encoder_decoder_init.py
   │     │  │  │  │  ├─ t5_helper.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ whisper
   │     │  │  │     ├─ benchmark.py
   │     │  │  │     ├─ benchmark_all.py
   │     │  │  │     ├─ convert_to_onnx.py
   │     │  │  │     ├─ whisper_chain.py
   │     │  │  │     ├─ whisper_decoder.py
   │     │  │  │     ├─ whisper_encoder.py
   │     │  │  │     ├─ whisper_encoder_decoder_init.py
   │     │  │  │     ├─ whisper_helper.py
   │     │  │  │     ├─ whisper_inputs.py
   │     │  │  │     ├─ whisper_jump_times.py
   │     │  │  │     └─ __init__.py
   │     │  │  ├─ onnx_exporter.py
   │     │  │  ├─ onnx_model.py
   │     │  │  ├─ onnx_model_bart.py
   │     │  │  ├─ onnx_model_bert.py
   │     │  │  ├─ onnx_model_bert_keras.py
   │     │  │  ├─ onnx_model_bert_tf.py
   │     │  │  ├─ onnx_model_clip.py
   │     │  │  ├─ onnx_model_conformer.py
   │     │  │  ├─ onnx_model_gpt2.py
   │     │  │  ├─ onnx_model_mmdit.py
   │     │  │  ├─ onnx_model_phi.py
   │     │  │  ├─ onnx_model_sam2.py
   │     │  │  ├─ onnx_model_t5.py
   │     │  │  ├─ onnx_model_tnlr.py
   │     │  │  ├─ onnx_model_unet.py
   │     │  │  ├─ onnx_model_vae.py
   │     │  │  ├─ onnx_utils.py
   │     │  │  ├─ optimizer.py
   │     │  │  ├─ past_helper.py
   │     │  │  ├─ profiler.py
   │     │  │  ├─ profile_result_processor.py
   │     │  │  ├─ quantize_helper.py
   │     │  │  ├─ shape_infer_helper.py
   │     │  │  ├─ shape_optimizer.py
   │     │  │  ├─ torch_onnx_export_helper.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ openai
   │     │  ├─ auth
   │     │  │  ├─ _workload.py
   │     │  │  ├─ _x509.py
   │     │  │  └─ __init__.py
   │     │  ├─ helpers
   │     │  │  ├─ local_audio_player.py
   │     │  │  ├─ microphone.py
   │     │  │  └─ __init__.py
   │     │  ├─ lib
   │     │  │  ├─ .keep
   │     │  │  ├─ azure.py
   │     │  │  ├─ bedrock.py
   │     │  │  ├─ streaming
   │     │  │  │  ├─ chat
   │     │  │  │  │  ├─ _completions.py
   │     │  │  │  │  ├─ _events.py
   │     │  │  │  │  ├─ _types.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ responses
   │     │  │  │  │  ├─ _events.py
   │     │  │  │  │  ├─ _responses.py
   │     │  │  │  │  ├─ _types.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _assistants.py
   │     │  │  │  ├─ _deltas.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _azure_websocket.py
   │     │  │  ├─ _bedrock_auth.py
   │     │  │  ├─ _files.py
   │     │  │  ├─ _old_api.py
   │     │  │  ├─ _parsing
   │     │  │  │  ├─ _audio.py
   │     │  │  │  ├─ _completions.py
   │     │  │  │  ├─ _embeddings.py
   │     │  │  │  ├─ _responses.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _pydantic.py
   │     │  │  ├─ _realtime.py
   │     │  │  ├─ _tools.py
   │     │  │  ├─ _validators.py
   │     │  │  ├─ _vector_stores.py
   │     │  │  ├─ _webhooks.py
   │     │  │  ├─ _websocket.py
   │     │  │  └─ __init__.py
   │     │  ├─ pagination.py
   │     │  ├─ providers
   │     │  │  ├─ bedrock.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ resources
   │     │  │  ├─ admin
   │     │  │  │  ├─ admin.py
   │     │  │  │  ├─ organization
   │     │  │  │  │  ├─ admin_api_keys.py
   │     │  │  │  │  ├─ certificates.py
   │     │  │  │  │  ├─ data_retention.py
   │     │  │  │  │  ├─ groups
   │     │  │  │  │  │  ├─ groups.py
   │     │  │  │  │  │  ├─ roles.py
   │     │  │  │  │  │  ├─ users.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ invites.py
   │     │  │  │  │  ├─ organization.py
   │     │  │  │  │  ├─ projects
   │     │  │  │  │  │  ├─ api_keys.py
   │     │  │  │  │  │  ├─ certificates.py
   │     │  │  │  │  │  ├─ data_retention.py
   │     │  │  │  │  │  ├─ groups
   │     │  │  │  │  │  │  ├─ groups.py
   │     │  │  │  │  │  │  ├─ roles.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ hosted_tool_permissions.py
   │     │  │  │  │  │  ├─ model_permissions.py
   │     │  │  │  │  │  ├─ projects.py
   │     │  │  │  │  │  ├─ rate_limits.py
   │     │  │  │  │  │  ├─ roles.py
   │     │  │  │  │  │  ├─ service_accounts
   │     │  │  │  │  │  │  ├─ api_keys.py
   │     │  │  │  │  │  │  ├─ service_accounts.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ spend_alerts.py
   │     │  │  │  │  │  ├─ spend_limit.py
   │     │  │  │  │  │  ├─ users
   │     │  │  │  │  │  │  ├─ roles.py
   │     │  │  │  │  │  │  ├─ users.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ roles.py
   │     │  │  │  │  ├─ spend_alerts.py
   │     │  │  │  │  ├─ spend_limit.py
   │     │  │  │  │  ├─ usage.py
   │     │  │  │  │  ├─ users
   │     │  │  │  │  │  ├─ roles.py
   │     │  │  │  │  │  ├─ users.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ audio
   │     │  │  │  ├─ audio.py
   │     │  │  │  ├─ speech.py
   │     │  │  │  ├─ transcriptions.py
   │     │  │  │  ├─ translations.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ batches.py
   │     │  │  ├─ beta
   │     │  │  │  ├─ assistants.py
   │     │  │  │  ├─ beta.py
   │     │  │  │  ├─ chatkit
   │     │  │  │  │  ├─ chatkit.py
   │     │  │  │  │  ├─ sessions.py
   │     │  │  │  │  ├─ threads.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ realtime
   │     │  │  │  │  ├─ realtime.py
   │     │  │  │  │  ├─ sessions.py
   │     │  │  │  │  ├─ transcription_sessions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ responses
   │     │  │  │  │  ├─ input_items.py
   │     │  │  │  │  ├─ input_tokens.py
   │     │  │  │  │  ├─ responses.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ threads
   │     │  │  │  │  ├─ messages.py
   │     │  │  │  │  ├─ runs
   │     │  │  │  │  │  ├─ runs.py
   │     │  │  │  │  │  ├─ steps.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ threads.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ chat
   │     │  │  │  ├─ chat.py
   │     │  │  │  ├─ completions
   │     │  │  │  │  ├─ completions.py
   │     │  │  │  │  ├─ messages.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ completions.py
   │     │  │  ├─ containers
   │     │  │  │  ├─ containers.py
   │     │  │  │  ├─ files
   │     │  │  │  │  ├─ content.py
   │     │  │  │  │  ├─ files.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ content_provenance_checks.py
   │     │  │  ├─ conversations
   │     │  │  │  ├─ api.md
   │     │  │  │  ├─ conversations.py
   │     │  │  │  ├─ items.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ embeddings.py
   │     │  │  ├─ evals
   │     │  │  │  ├─ evals.py
   │     │  │  │  ├─ runs
   │     │  │  │  │  ├─ output_items.py
   │     │  │  │  │  ├─ runs.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ files.py
   │     │  │  ├─ fine_tuning
   │     │  │  │  ├─ alpha
   │     │  │  │  │  ├─ alpha.py
   │     │  │  │  │  ├─ graders.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ checkpoints
   │     │  │  │  │  ├─ checkpoints.py
   │     │  │  │  │  ├─ permissions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ fine_tuning.py
   │     │  │  │  ├─ jobs
   │     │  │  │  │  ├─ checkpoints.py
   │     │  │  │  │  ├─ jobs.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ images.py
   │     │  │  ├─ models.py
   │     │  │  ├─ moderations.py
   │     │  │  ├─ realtime
   │     │  │  │  ├─ api.md
   │     │  │  │  ├─ calls.py
   │     │  │  │  ├─ client_secrets.py
   │     │  │  │  ├─ realtime.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ responses
   │     │  │  │  ├─ api.md
   │     │  │  │  ├─ input_items.py
   │     │  │  │  ├─ input_tokens.py
   │     │  │  │  ├─ responses.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ safety
   │     │  │  │  ├─ alerts.py
   │     │  │  │  ├─ safety.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ skills
   │     │  │  │  ├─ content.py
   │     │  │  │  ├─ skills.py
   │     │  │  │  ├─ versions
   │     │  │  │  │  ├─ content.py
   │     │  │  │  │  ├─ versions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ uploads
   │     │  │  │  ├─ parts.py
   │     │  │  │  ├─ uploads.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vector_stores
   │     │  │  │  ├─ files.py
   │     │  │  │  ├─ file_batches.py
   │     │  │  │  ├─ vector_stores.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ videos.py
   │     │  │  ├─ webhooks
   │     │  │  │  ├─ api.md
   │     │  │  │  ├─ webhooks.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ types
   │     │  │  ├─ admin
   │     │  │  │  ├─ organization
   │     │  │  │  │  ├─ admin_api_key.py
   │     │  │  │  │  ├─ admin_api_key_create_params.py
   │     │  │  │  │  ├─ admin_api_key_create_response.py
   │     │  │  │  │  ├─ admin_api_key_delete_response.py
   │     │  │  │  │  ├─ admin_api_key_list_params.py
   │     │  │  │  │  ├─ audit_log_list_params.py
   │     │  │  │  │  ├─ audit_log_list_response.py
   │     │  │  │  │  ├─ certificate.py
   │     │  │  │  │  ├─ certificate_activate_params.py
   │     │  │  │  │  ├─ certificate_activate_response.py
   │     │  │  │  │  ├─ certificate_create_params.py
   │     │  │  │  │  ├─ certificate_deactivate_params.py
   │     │  │  │  │  ├─ certificate_deactivate_response.py
   │     │  │  │  │  ├─ certificate_delete_response.py
   │     │  │  │  │  ├─ certificate_list_params.py
   │     │  │  │  │  ├─ certificate_list_response.py
   │     │  │  │  │  ├─ certificate_retrieve_params.py
   │     │  │  │  │  ├─ certificate_update_params.py
   │     │  │  │  │  ├─ cost_quantity_unit.py
   │     │  │  │  │  ├─ data_retention_update_params.py
   │     │  │  │  │  ├─ group.py
   │     │  │  │  │  ├─ groups
   │     │  │  │  │  │  ├─ organization_group_user.py
   │     │  │  │  │  │  ├─ role_create_params.py
   │     │  │  │  │  │  ├─ role_create_response.py
   │     │  │  │  │  │  ├─ role_delete_response.py
   │     │  │  │  │  │  ├─ role_list_params.py
   │     │  │  │  │  │  ├─ role_list_response.py
   │     │  │  │  │  │  ├─ role_retrieve_response.py
   │     │  │  │  │  │  ├─ user_create_params.py
   │     │  │  │  │  │  ├─ user_create_response.py
   │     │  │  │  │  │  ├─ user_delete_response.py
   │     │  │  │  │  │  ├─ user_list_params.py
   │     │  │  │  │  │  ├─ user_retrieve_response.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ group_create_params.py
   │     │  │  │  │  ├─ group_delete_response.py
   │     │  │  │  │  ├─ group_list_params.py
   │     │  │  │  │  ├─ group_update_params.py
   │     │  │  │  │  ├─ group_update_response.py
   │     │  │  │  │  ├─ invite.py
   │     │  │  │  │  ├─ invite_create_params.py
   │     │  │  │  │  ├─ invite_delete_response.py
   │     │  │  │  │  ├─ invite_list_params.py
   │     │  │  │  │  ├─ organization_data_retention.py
   │     │  │  │  │  ├─ organization_spend_alert.py
   │     │  │  │  │  ├─ organization_spend_alert_deleted.py
   │     │  │  │  │  ├─ organization_spend_limit.py
   │     │  │  │  │  ├─ organization_spend_limit_deleted.py
   │     │  │  │  │  ├─ organization_user.py
   │     │  │  │  │  ├─ project.py
   │     │  │  │  │  ├─ projects
   │     │  │  │  │  │  ├─ api_key_delete_response.py
   │     │  │  │  │  │  ├─ api_key_list_params.py
   │     │  │  │  │  │  ├─ certificate_activate_params.py
   │     │  │  │  │  │  ├─ certificate_activate_response.py
   │     │  │  │  │  │  ├─ certificate_deactivate_params.py
   │     │  │  │  │  │  ├─ certificate_deactivate_response.py
   │     │  │  │  │  │  ├─ certificate_list_params.py
   │     │  │  │  │  │  ├─ certificate_list_response.py
   │     │  │  │  │  │  ├─ data_retention_update_params.py
   │     │  │  │  │  │  ├─ groups
   │     │  │  │  │  │  │  ├─ role_create_params.py
   │     │  │  │  │  │  │  ├─ role_create_response.py
   │     │  │  │  │  │  │  ├─ role_delete_response.py
   │     │  │  │  │  │  │  ├─ role_list_params.py
   │     │  │  │  │  │  │  ├─ role_list_response.py
   │     │  │  │  │  │  │  ├─ role_retrieve_response.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ group_create_params.py
   │     │  │  │  │  │  ├─ group_delete_response.py
   │     │  │  │  │  │  ├─ group_list_params.py
   │     │  │  │  │  │  ├─ group_retrieve_params.py
   │     │  │  │  │  │  ├─ hosted_tool_permission_update_params.py
   │     │  │  │  │  │  ├─ model_permission_update_params.py
   │     │  │  │  │  │  ├─ project_api_key.py
   │     │  │  │  │  │  ├─ project_data_retention.py
   │     │  │  │  │  │  ├─ project_group.py
   │     │  │  │  │  │  ├─ project_hosted_tool_permissions.py
   │     │  │  │  │  │  ├─ project_model_permissions.py
   │     │  │  │  │  │  ├─ project_model_permissions_deleted.py
   │     │  │  │  │  │  ├─ project_rate_limit.py
   │     │  │  │  │  │  ├─ project_service_account.py
   │     │  │  │  │  │  ├─ project_spend_alert.py
   │     │  │  │  │  │  ├─ project_spend_alert_deleted.py
   │     │  │  │  │  │  ├─ project_spend_limit.py
   │     │  │  │  │  │  ├─ project_spend_limit_deleted.py
   │     │  │  │  │  │  ├─ project_user.py
   │     │  │  │  │  │  ├─ rate_limit_list_rate_limits_params.py
   │     │  │  │  │  │  ├─ rate_limit_update_rate_limit_params.py
   │     │  │  │  │  │  ├─ role_create_params.py
   │     │  │  │  │  │  ├─ role_delete_response.py
   │     │  │  │  │  │  ├─ role_list_params.py
   │     │  │  │  │  │  ├─ role_update_params.py
   │     │  │  │  │  │  ├─ service_accounts
   │     │  │  │  │  │  │  ├─ api_key_create_params.py
   │     │  │  │  │  │  │  ├─ api_key_create_response.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ service_account_create_params.py
   │     │  │  │  │  │  ├─ service_account_create_response.py
   │     │  │  │  │  │  ├─ service_account_delete_response.py
   │     │  │  │  │  │  ├─ service_account_list_params.py
   │     │  │  │  │  │  ├─ service_account_update_params.py
   │     │  │  │  │  │  ├─ spend_alert_create_params.py
   │     │  │  │  │  │  ├─ spend_alert_list_params.py
   │     │  │  │  │  │  ├─ spend_alert_update_params.py
   │     │  │  │  │  │  ├─ spend_limit_update_params.py
   │     │  │  │  │  │  ├─ users
   │     │  │  │  │  │  │  ├─ role_create_params.py
   │     │  │  │  │  │  │  ├─ role_create_response.py
   │     │  │  │  │  │  │  ├─ role_delete_response.py
   │     │  │  │  │  │  │  ├─ role_list_params.py
   │     │  │  │  │  │  │  ├─ role_list_response.py
   │     │  │  │  │  │  │  ├─ role_retrieve_response.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ user_create_params.py
   │     │  │  │  │  │  ├─ user_delete_response.py
   │     │  │  │  │  │  ├─ user_list_params.py
   │     │  │  │  │  │  ├─ user_update_params.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ project_create_params.py
   │     │  │  │  │  ├─ project_list_params.py
   │     │  │  │  │  ├─ project_residency.py
   │     │  │  │  │  ├─ project_update_params.py
   │     │  │  │  │  ├─ role.py
   │     │  │  │  │  ├─ role_create_params.py
   │     │  │  │  │  ├─ role_delete_response.py
   │     │  │  │  │  ├─ role_list_params.py
   │     │  │  │  │  ├─ role_update_params.py
   │     │  │  │  │  ├─ spend_alert_create_params.py
   │     │  │  │  │  ├─ spend_alert_list_params.py
   │     │  │  │  │  ├─ spend_alert_update_params.py
   │     │  │  │  │  ├─ spend_limit_update_params.py
   │     │  │  │  │  ├─ usage_audio_speeches_params.py
   │     │  │  │  │  ├─ usage_audio_speeches_response.py
   │     │  │  │  │  ├─ usage_audio_transcriptions_params.py
   │     │  │  │  │  ├─ usage_audio_transcriptions_response.py
   │     │  │  │  │  ├─ usage_code_interpreter_sessions_params.py
   │     │  │  │  │  ├─ usage_code_interpreter_sessions_response.py
   │     │  │  │  │  ├─ usage_completions_params.py
   │     │  │  │  │  ├─ usage_completions_response.py
   │     │  │  │  │  ├─ usage_costs_params.py
   │     │  │  │  │  ├─ usage_costs_response.py
   │     │  │  │  │  ├─ usage_embeddings_params.py
   │     │  │  │  │  ├─ usage_embeddings_response.py
   │     │  │  │  │  ├─ usage_file_search_calls_params.py
   │     │  │  │  │  ├─ usage_file_search_calls_response.py
   │     │  │  │  │  ├─ usage_images_params.py
   │     │  │  │  │  ├─ usage_images_response.py
   │     │  │  │  │  ├─ usage_moderations_params.py
   │     │  │  │  │  ├─ usage_moderations_response.py
   │     │  │  │  │  ├─ usage_vector_stores_params.py
   │     │  │  │  │  ├─ usage_vector_stores_response.py
   │     │  │  │  │  ├─ usage_web_search_calls_params.py
   │     │  │  │  │  ├─ usage_web_search_calls_response.py
   │     │  │  │  │  ├─ users
   │     │  │  │  │  │  ├─ role_create_params.py
   │     │  │  │  │  │  ├─ role_create_response.py
   │     │  │  │  │  │  ├─ role_delete_response.py
   │     │  │  │  │  │  ├─ role_list_params.py
   │     │  │  │  │  │  ├─ role_list_response.py
   │     │  │  │  │  │  ├─ role_retrieve_response.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ user_delete_response.py
   │     │  │  │  │  ├─ user_list_params.py
   │     │  │  │  │  ├─ user_update_params.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ audio
   │     │  │  │  ├─ speech_create_params.py
   │     │  │  │  ├─ speech_model.py
   │     │  │  │  ├─ transcription.py
   │     │  │  │  ├─ transcription_create_params.py
   │     │  │  │  ├─ transcription_create_response.py
   │     │  │  │  ├─ transcription_diarized.py
   │     │  │  │  ├─ transcription_diarized_segment.py
   │     │  │  │  ├─ transcription_include.py
   │     │  │  │  ├─ transcription_language.py
   │     │  │  │  ├─ transcription_segment.py
   │     │  │  │  ├─ transcription_stream_event.py
   │     │  │  │  ├─ transcription_text_delta_event.py
   │     │  │  │  ├─ transcription_text_done_event.py
   │     │  │  │  ├─ transcription_text_segment_event.py
   │     │  │  │  ├─ transcription_verbose.py
   │     │  │  │  ├─ transcription_word.py
   │     │  │  │  ├─ translation.py
   │     │  │  │  ├─ translation_create_params.py
   │     │  │  │  ├─ translation_create_response.py
   │     │  │  │  ├─ translation_verbose.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ audio_model.py
   │     │  │  ├─ audio_response_format.py
   │     │  │  ├─ auto_file_chunking_strategy_param.py
   │     │  │  ├─ batch.py
   │     │  │  ├─ batch_create_params.py
   │     │  │  ├─ batch_error.py
   │     │  │  ├─ batch_list_params.py
   │     │  │  ├─ batch_request_counts.py
   │     │  │  ├─ batch_usage.py
   │     │  │  ├─ beta
   │     │  │  │  ├─ assistant.py
   │     │  │  │  ├─ assistant_create_params.py
   │     │  │  │  ├─ assistant_deleted.py
   │     │  │  │  ├─ assistant_list_params.py
   │     │  │  │  ├─ assistant_response_format_option.py
   │     │  │  │  ├─ assistant_response_format_option_param.py
   │     │  │  │  ├─ assistant_stream_event.py
   │     │  │  │  ├─ assistant_tool.py
   │     │  │  │  ├─ assistant_tool_choice.py
   │     │  │  │  ├─ assistant_tool_choice_function.py
   │     │  │  │  ├─ assistant_tool_choice_function_param.py
   │     │  │  │  ├─ assistant_tool_choice_option.py
   │     │  │  │  ├─ assistant_tool_choice_option_param.py
   │     │  │  │  ├─ assistant_tool_choice_param.py
   │     │  │  │  ├─ assistant_tool_param.py
   │     │  │  │  ├─ assistant_update_params.py
   │     │  │  │  ├─ beta_apply_patch_tool.py
   │     │  │  │  ├─ beta_apply_patch_tool_param.py
   │     │  │  │  ├─ beta_compacted_response.py
   │     │  │  │  ├─ beta_computer_action.py
   │     │  │  │  ├─ beta_computer_action_list.py
   │     │  │  │  ├─ beta_computer_action_list_param.py
   │     │  │  │  ├─ beta_computer_action_param.py
   │     │  │  │  ├─ beta_computer_tool.py
   │     │  │  │  ├─ beta_computer_tool_param.py
   │     │  │  │  ├─ beta_computer_use_preview_tool.py
   │     │  │  │  ├─ beta_computer_use_preview_tool_param.py
   │     │  │  │  ├─ beta_container_auto.py
   │     │  │  │  ├─ beta_container_auto_param.py
   │     │  │  │  ├─ beta_container_network_policy_allowlist.py
   │     │  │  │  ├─ beta_container_network_policy_allowlist_param.py
   │     │  │  │  ├─ beta_container_network_policy_disabled.py
   │     │  │  │  ├─ beta_container_network_policy_disabled_param.py
   │     │  │  │  ├─ beta_container_network_policy_domain_secret.py
   │     │  │  │  ├─ beta_container_network_policy_domain_secret_param.py
   │     │  │  │  ├─ beta_container_reference.py
   │     │  │  │  ├─ beta_container_reference_param.py
   │     │  │  │  ├─ beta_custom_tool.py
   │     │  │  │  ├─ beta_custom_tool_param.py
   │     │  │  │  ├─ beta_easy_input_message.py
   │     │  │  │  ├─ beta_easy_input_message_param.py
   │     │  │  │  ├─ beta_file_search_tool.py
   │     │  │  │  ├─ beta_file_search_tool_param.py
   │     │  │  │  ├─ beta_function_shell_tool.py
   │     │  │  │  ├─ beta_function_shell_tool_param.py
   │     │  │  │  ├─ beta_function_tool.py
   │     │  │  │  ├─ beta_function_tool_param.py
   │     │  │  │  ├─ beta_image_detail.py
   │     │  │  │  ├─ beta_inline_skill.py
   │     │  │  │  ├─ beta_inline_skill_param.py
   │     │  │  │  ├─ beta_inline_skill_source.py
   │     │  │  │  ├─ beta_inline_skill_source_param.py
   │     │  │  │  ├─ beta_local_environment.py
   │     │  │  │  ├─ beta_local_environment_param.py
   │     │  │  │  ├─ beta_local_skill.py
   │     │  │  │  ├─ beta_local_skill_param.py
   │     │  │  │  ├─ beta_mcp_tool_call_error.py
   │     │  │  │  ├─ beta_mcp_tool_call_error_param.py
   │     │  │  │  ├─ beta_namespace_tool.py
   │     │  │  │  ├─ beta_namespace_tool_param.py
   │     │  │  │  ├─ beta_response.py
   │     │  │  │  ├─ beta_responses_client_event.py
   │     │  │  │  ├─ beta_responses_client_event_param.py
   │     │  │  │  ├─ beta_responses_server_event.py
   │     │  │  │  ├─ beta_response_apply_patch_tool_call.py
   │     │  │  │  ├─ beta_response_apply_patch_tool_call_output.py
   │     │  │  │  ├─ beta_response_audio_delta_event.py
   │     │  │  │  ├─ beta_response_audio_done_event.py
   │     │  │  │  ├─ beta_response_audio_transcript_delta_event.py
   │     │  │  │  ├─ beta_response_audio_transcript_done_event.py
   │     │  │  │  ├─ beta_response_code_interpreter_call_code_delta_event.py
   │     │  │  │  ├─ beta_response_code_interpreter_call_code_done_event.py
   │     │  │  │  ├─ beta_response_code_interpreter_call_completed_event.py
   │     │  │  │  ├─ beta_response_code_interpreter_call_interpreting_event.py
   │     │  │  │  ├─ beta_response_code_interpreter_call_in_progress_event.py
   │     │  │  │  ├─ beta_response_code_interpreter_tool_call.py
   │     │  │  │  ├─ beta_response_code_interpreter_tool_call_param.py
   │     │  │  │  ├─ beta_response_compaction_item.py
   │     │  │  │  ├─ beta_response_compaction_item_param.py
   │     │  │  │  ├─ beta_response_compaction_item_param_param.py
   │     │  │  │  ├─ beta_response_completed_event.py
   │     │  │  │  ├─ beta_response_computer_tool_call.py
   │     │  │  │  ├─ beta_response_computer_tool_call_output_item.py
   │     │  │  │  ├─ beta_response_computer_tool_call_output_screenshot.py
   │     │  │  │  ├─ beta_response_computer_tool_call_output_screenshot_param.py
   │     │  │  │  ├─ beta_response_computer_tool_call_param.py
   │     │  │  │  ├─ beta_response_configuration_update_item.py
   │     │  │  │  ├─ beta_response_configuration_update_item_param.py
   │     │  │  │  ├─ beta_response_configuration_update_item_param_param.py
   │     │  │  │  ├─ beta_response_container_reference.py
   │     │  │  │  ├─ beta_response_content_part_added_event.py
   │     │  │  │  ├─ beta_response_content_part_done_event.py
   │     │  │  │  ├─ beta_response_conversation_param.py
   │     │  │  │  ├─ beta_response_conversation_param_param.py
   │     │  │  │  ├─ beta_response_created_event.py
   │     │  │  │  ├─ beta_response_custom_tool_call.py
   │     │  │  │  ├─ beta_response_custom_tool_call_input_delta_event.py
   │     │  │  │  ├─ beta_response_custom_tool_call_input_done_event.py
   │     │  │  │  ├─ beta_response_custom_tool_call_item.py
   │     │  │  │  ├─ beta_response_custom_tool_call_output.py
   │     │  │  │  ├─ beta_response_custom_tool_call_output_item.py
   │     │  │  │  ├─ beta_response_custom_tool_call_output_param.py
   │     │  │  │  ├─ beta_response_custom_tool_call_param.py
   │     │  │  │  ├─ beta_response_error.py
   │     │  │  │  ├─ beta_response_error_event.py
   │     │  │  │  ├─ beta_response_failed_event.py
   │     │  │  │  ├─ beta_response_file_search_call_completed_event.py
   │     │  │  │  ├─ beta_response_file_search_call_in_progress_event.py
   │     │  │  │  ├─ beta_response_file_search_call_searching_event.py
   │     │  │  │  ├─ beta_response_file_search_tool_call.py
   │     │  │  │  ├─ beta_response_file_search_tool_call_param.py
   │     │  │  │  ├─ beta_response_format_text_config.py
   │     │  │  │  ├─ beta_response_format_text_config_param.py
   │     │  │  │  ├─ beta_response_format_text_json_schema_config.py
   │     │  │  │  ├─ beta_response_format_text_json_schema_config_param.py
   │     │  │  │  ├─ beta_response_function_call_arguments_delta_event.py
   │     │  │  │  ├─ beta_response_function_call_arguments_done_event.py
   │     │  │  │  ├─ beta_response_function_call_output_item.py
   │     │  │  │  ├─ beta_response_function_call_output_item_list.py
   │     │  │  │  ├─ beta_response_function_call_output_item_list_param.py
   │     │  │  │  ├─ beta_response_function_call_output_item_param.py
   │     │  │  │  ├─ beta_response_function_shell_call_output_content.py
   │     │  │  │  ├─ beta_response_function_shell_call_output_content_param.py
   │     │  │  │  ├─ beta_response_function_shell_tool_call.py
   │     │  │  │  ├─ beta_response_function_shell_tool_call_output.py
   │     │  │  │  ├─ beta_response_function_tool_call.py
   │     │  │  │  ├─ beta_response_function_tool_call_item.py
   │     │  │  │  ├─ beta_response_function_tool_call_output_item.py
   │     │  │  │  ├─ beta_response_function_tool_call_param.py
   │     │  │  │  ├─ beta_response_function_web_search.py
   │     │  │  │  ├─ beta_response_function_web_search_param.py
   │     │  │  │  ├─ beta_response_image_gen_call_completed_event.py
   │     │  │  │  ├─ beta_response_image_gen_call_generating_event.py
   │     │  │  │  ├─ beta_response_image_gen_call_in_progress_event.py
   │     │  │  │  ├─ beta_response_image_gen_call_partial_image_event.py
   │     │  │  │  ├─ beta_response_includable.py
   │     │  │  │  ├─ beta_response_incomplete_event.py
   │     │  │  │  ├─ beta_response_inject_created_event.py
   │     │  │  │  ├─ beta_response_inject_event.py
   │     │  │  │  ├─ beta_response_inject_event_param.py
   │     │  │  │  ├─ beta_response_inject_failed_event.py
   │     │  │  │  ├─ beta_response_input.py
   │     │  │  │  ├─ beta_response_input_content.py
   │     │  │  │  ├─ beta_response_input_content_param.py
   │     │  │  │  ├─ beta_response_input_file.py
   │     │  │  │  ├─ beta_response_input_file_content.py
   │     │  │  │  ├─ beta_response_input_file_content_param.py
   │     │  │  │  ├─ beta_response_input_file_param.py
   │     │  │  │  ├─ beta_response_input_image.py
   │     │  │  │  ├─ beta_response_input_image_content.py
   │     │  │  │  ├─ beta_response_input_image_content_param.py
   │     │  │  │  ├─ beta_response_input_image_param.py
   │     │  │  │  ├─ beta_response_input_item.py
   │     │  │  │  ├─ beta_response_input_item_param.py
   │     │  │  │  ├─ beta_response_input_message_content_list.py
   │     │  │  │  ├─ beta_response_input_message_content_list_param.py
   │     │  │  │  ├─ beta_response_input_message_item.py
   │     │  │  │  ├─ beta_response_input_param.py
   │     │  │  │  ├─ beta_response_input_text.py
   │     │  │  │  ├─ beta_response_input_text_content.py
   │     │  │  │  ├─ beta_response_input_text_content_param.py
   │     │  │  │  ├─ beta_response_input_text_param.py
   │     │  │  │  ├─ beta_response_in_progress_event.py
   │     │  │  │  ├─ beta_response_item.py
   │     │  │  │  ├─ beta_response_local_environment.py
   │     │  │  │  ├─ beta_response_mcp_call_arguments_delta_event.py
   │     │  │  │  ├─ beta_response_mcp_call_arguments_done_event.py
   │     │  │  │  ├─ beta_response_mcp_call_completed_event.py
   │     │  │  │  ├─ beta_response_mcp_call_failed_event.py
   │     │  │  │  ├─ beta_response_mcp_call_in_progress_event.py
   │     │  │  │  ├─ beta_response_mcp_list_tools_completed_event.py
   │     │  │  │  ├─ beta_response_mcp_list_tools_failed_event.py
   │     │  │  │  ├─ beta_response_mcp_list_tools_in_progress_event.py
   │     │  │  │  ├─ beta_response_output_item.py
   │     │  │  │  ├─ beta_response_output_item_added_event.py
   │     │  │  │  ├─ beta_response_output_item_done_event.py
   │     │  │  │  ├─ beta_response_output_message.py
   │     │  │  │  ├─ beta_response_output_message_param.py
   │     │  │  │  ├─ beta_response_output_refusal.py
   │     │  │  │  ├─ beta_response_output_refusal_param.py
   │     │  │  │  ├─ beta_response_output_text.py
   │     │  │  │  ├─ beta_response_output_text_annotation_added_event.py
   │     │  │  │  ├─ beta_response_output_text_param.py
   │     │  │  │  ├─ beta_response_prompt.py
   │     │  │  │  ├─ beta_response_prompt_param.py
   │     │  │  │  ├─ beta_response_queued_event.py
   │     │  │  │  ├─ beta_response_reasoning_item.py
   │     │  │  │  ├─ beta_response_reasoning_item_param.py
   │     │  │  │  ├─ beta_response_reasoning_summary_part_added_event.py
   │     │  │  │  ├─ beta_response_reasoning_summary_part_done_event.py
   │     │  │  │  ├─ beta_response_reasoning_summary_text_delta_event.py
   │     │  │  │  ├─ beta_response_reasoning_summary_text_done_event.py
   │     │  │  │  ├─ beta_response_reasoning_text_delta_event.py
   │     │  │  │  ├─ beta_response_reasoning_text_done_event.py
   │     │  │  │  ├─ beta_response_refusal_delta_event.py
   │     │  │  │  ├─ beta_response_refusal_done_event.py
   │     │  │  │  ├─ beta_response_shell_call_command_added_event.py
   │     │  │  │  ├─ beta_response_shell_call_command_delta_event.py
   │     │  │  │  ├─ beta_response_shell_call_command_done_event.py
   │     │  │  │  ├─ beta_response_shell_call_output_content_delta_event.py
   │     │  │  │  ├─ beta_response_shell_call_output_content_done_event.py
   │     │  │  │  ├─ beta_response_status.py
   │     │  │  │  ├─ beta_response_steer_accepted_event.py
   │     │  │  │  ├─ beta_response_steer_error_code.py
   │     │  │  │  ├─ beta_response_steer_event.py
   │     │  │  │  ├─ beta_response_steer_event_param.py
   │     │  │  │  ├─ beta_response_steer_failed_event.py
   │     │  │  │  ├─ beta_response_steer_input.py
   │     │  │  │  ├─ beta_response_steer_input_content.py
   │     │  │  │  ├─ beta_response_steer_input_content_param.py
   │     │  │  │  ├─ beta_response_steer_input_param.py
   │     │  │  │  ├─ beta_response_steer_pending_event.py
   │     │  │  │  ├─ beta_response_steer_pending_reason.py
   │     │  │  │  ├─ beta_response_steer_required_input.py
   │     │  │  │  ├─ beta_response_stream_event.py
   │     │  │  │  ├─ beta_response_text_config.py
   │     │  │  │  ├─ beta_response_text_config_param.py
   │     │  │  │  ├─ beta_response_text_delta_event.py
   │     │  │  │  ├─ beta_response_text_done_event.py
   │     │  │  │  ├─ beta_response_tool_search_call.py
   │     │  │  │  ├─ beta_response_tool_search_output_item.py
   │     │  │  │  ├─ beta_response_tool_search_output_item_param.py
   │     │  │  │  ├─ beta_response_tool_search_output_item_param_param.py
   │     │  │  │  ├─ beta_response_usage.py
   │     │  │  │  ├─ beta_response_web_search_call_completed_event.py
   │     │  │  │  ├─ beta_response_web_search_call_in_progress_event.py
   │     │  │  │  ├─ beta_response_web_search_call_searching_event.py
   │     │  │  │  ├─ beta_service_tier.py
   │     │  │  │  ├─ beta_skill_reference.py
   │     │  │  │  ├─ beta_skill_reference_param.py
   │     │  │  │  ├─ beta_tool.py
   │     │  │  │  ├─ beta_tool_choice_allowed.py
   │     │  │  │  ├─ beta_tool_choice_allowed_param.py
   │     │  │  │  ├─ beta_tool_choice_apply_patch.py
   │     │  │  │  ├─ beta_tool_choice_apply_patch_param.py
   │     │  │  │  ├─ beta_tool_choice_custom.py
   │     │  │  │  ├─ beta_tool_choice_custom_param.py
   │     │  │  │  ├─ beta_tool_choice_function.py
   │     │  │  │  ├─ beta_tool_choice_function_param.py
   │     │  │  │  ├─ beta_tool_choice_mcp.py
   │     │  │  │  ├─ beta_tool_choice_mcp_param.py
   │     │  │  │  ├─ beta_tool_choice_options.py
   │     │  │  │  ├─ beta_tool_choice_shell.py
   │     │  │  │  ├─ beta_tool_choice_shell_param.py
   │     │  │  │  ├─ beta_tool_choice_types.py
   │     │  │  │  ├─ beta_tool_choice_types_param.py
   │     │  │  │  ├─ beta_tool_param.py
   │     │  │  │  ├─ beta_tool_search_tool.py
   │     │  │  │  ├─ beta_tool_search_tool_param.py
   │     │  │  │  ├─ beta_web_search_preview_tool.py
   │     │  │  │  ├─ beta_web_search_preview_tool_param.py
   │     │  │  │  ├─ beta_web_search_tool.py
   │     │  │  │  ├─ beta_web_search_tool_param.py
   │     │  │  │  ├─ chat
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ chatkit
   │     │  │  │  │  ├─ chatkit_attachment.py
   │     │  │  │  │  ├─ chatkit_response_output_text.py
   │     │  │  │  │  ├─ chatkit_thread.py
   │     │  │  │  │  ├─ chatkit_thread_assistant_message_item.py
   │     │  │  │  │  ├─ chatkit_thread_item_list.py
   │     │  │  │  │  ├─ chatkit_thread_user_message_item.py
   │     │  │  │  │  ├─ chatkit_widget_item.py
   │     │  │  │  │  ├─ chat_session.py
   │     │  │  │  │  ├─ chat_session_automatic_thread_titling.py
   │     │  │  │  │  ├─ chat_session_chatkit_configuration.py
   │     │  │  │  │  ├─ chat_session_chatkit_configuration_param.py
   │     │  │  │  │  ├─ chat_session_expires_after_param.py
   │     │  │  │  │  ├─ chat_session_file_upload.py
   │     │  │  │  │  ├─ chat_session_history.py
   │     │  │  │  │  ├─ chat_session_rate_limits.py
   │     │  │  │  │  ├─ chat_session_rate_limits_param.py
   │     │  │  │  │  ├─ chat_session_status.py
   │     │  │  │  │  ├─ chat_session_workflow_param.py
   │     │  │  │  │  ├─ session_create_params.py
   │     │  │  │  │  ├─ thread_delete_response.py
   │     │  │  │  │  ├─ thread_list_items_params.py
   │     │  │  │  │  ├─ thread_list_params.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ chatkit_workflow.py
   │     │  │  │  ├─ code_interpreter_tool.py
   │     │  │  │  ├─ code_interpreter_tool_param.py
   │     │  │  │  ├─ file_search_tool.py
   │     │  │  │  ├─ file_search_tool_param.py
   │     │  │  │  ├─ function_tool.py
   │     │  │  │  ├─ function_tool_param.py
   │     │  │  │  ├─ realtime
   │     │  │  │  │  ├─ conversation_created_event.py
   │     │  │  │  │  ├─ conversation_item.py
   │     │  │  │  │  ├─ conversation_item_content.py
   │     │  │  │  │  ├─ conversation_item_content_param.py
   │     │  │  │  │  ├─ conversation_item_created_event.py
   │     │  │  │  │  ├─ conversation_item_create_event.py
   │     │  │  │  │  ├─ conversation_item_create_event_param.py
   │     │  │  │  │  ├─ conversation_item_deleted_event.py
   │     │  │  │  │  ├─ conversation_item_delete_event.py
   │     │  │  │  │  ├─ conversation_item_delete_event_param.py
   │     │  │  │  │  ├─ conversation_item_input_audio_transcription_completed_event.py
   │     │  │  │  │  ├─ conversation_item_input_audio_transcription_delta_event.py
   │     │  │  │  │  ├─ conversation_item_input_audio_transcription_failed_event.py
   │     │  │  │  │  ├─ conversation_item_param.py
   │     │  │  │  │  ├─ conversation_item_retrieve_event.py
   │     │  │  │  │  ├─ conversation_item_retrieve_event_param.py
   │     │  │  │  │  ├─ conversation_item_truncated_event.py
   │     │  │  │  │  ├─ conversation_item_truncate_event.py
   │     │  │  │  │  ├─ conversation_item_truncate_event_param.py
   │     │  │  │  │  ├─ conversation_item_with_reference.py
   │     │  │  │  │  ├─ conversation_item_with_reference_param.py
   │     │  │  │  │  ├─ error_event.py
   │     │  │  │  │  ├─ input_audio_buffer_append_event.py
   │     │  │  │  │  ├─ input_audio_buffer_append_event_param.py
   │     │  │  │  │  ├─ input_audio_buffer_cleared_event.py
   │     │  │  │  │  ├─ input_audio_buffer_clear_event.py
   │     │  │  │  │  ├─ input_audio_buffer_clear_event_param.py
   │     │  │  │  │  ├─ input_audio_buffer_committed_event.py
   │     │  │  │  │  ├─ input_audio_buffer_commit_event.py
   │     │  │  │  │  ├─ input_audio_buffer_commit_event_param.py
   │     │  │  │  │  ├─ input_audio_buffer_speech_started_event.py
   │     │  │  │  │  ├─ input_audio_buffer_speech_stopped_event.py
   │     │  │  │  │  ├─ rate_limits_updated_event.py
   │     │  │  │  │  ├─ realtime_client_event.py
   │     │  │  │  │  ├─ realtime_client_event_param.py
   │     │  │  │  │  ├─ realtime_connect_params.py
   │     │  │  │  │  ├─ realtime_response.py
   │     │  │  │  │  ├─ realtime_response_status.py
   │     │  │  │  │  ├─ realtime_response_usage.py
   │     │  │  │  │  ├─ realtime_server_event.py
   │     │  │  │  │  ├─ response_audio_delta_event.py
   │     │  │  │  │  ├─ response_audio_done_event.py
   │     │  │  │  │  ├─ response_audio_transcript_delta_event.py
   │     │  │  │  │  ├─ response_audio_transcript_done_event.py
   │     │  │  │  │  ├─ response_cancel_event.py
   │     │  │  │  │  ├─ response_cancel_event_param.py
   │     │  │  │  │  ├─ response_content_part_added_event.py
   │     │  │  │  │  ├─ response_content_part_done_event.py
   │     │  │  │  │  ├─ response_created_event.py
   │     │  │  │  │  ├─ response_create_event.py
   │     │  │  │  │  ├─ response_create_event_param.py
   │     │  │  │  │  ├─ response_done_event.py
   │     │  │  │  │  ├─ response_function_call_arguments_delta_event.py
   │     │  │  │  │  ├─ response_function_call_arguments_done_event.py
   │     │  │  │  │  ├─ response_output_item_added_event.py
   │     │  │  │  │  ├─ response_output_item_done_event.py
   │     │  │  │  │  ├─ response_text_delta_event.py
   │     │  │  │  │  ├─ response_text_done_event.py
   │     │  │  │  │  ├─ session.py
   │     │  │  │  │  ├─ session_created_event.py
   │     │  │  │  │  ├─ session_create_params.py
   │     │  │  │  │  ├─ session_create_response.py
   │     │  │  │  │  ├─ session_updated_event.py
   │     │  │  │  │  ├─ session_update_event.py
   │     │  │  │  │  ├─ session_update_event_param.py
   │     │  │  │  │  ├─ transcription_session.py
   │     │  │  │  │  ├─ transcription_session_create_params.py
   │     │  │  │  │  ├─ transcription_session_update.py
   │     │  │  │  │  ├─ transcription_session_updated_event.py
   │     │  │  │  │  ├─ transcription_session_update_param.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ responses
   │     │  │  │  │  ├─ beta_response_item_list.py
   │     │  │  │  │  ├─ input_item_list_params.py
   │     │  │  │  │  ├─ input_token_count_params.py
   │     │  │  │  │  ├─ input_token_count_response.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ response_compact_params.py
   │     │  │  │  ├─ response_create_params.py
   │     │  │  │  ├─ response_retrieve_params.py
   │     │  │  │  ├─ thread.py
   │     │  │  │  ├─ threads
   │     │  │  │  │  ├─ annotation.py
   │     │  │  │  │  ├─ annotation_delta.py
   │     │  │  │  │  ├─ file_citation_annotation.py
   │     │  │  │  │  ├─ file_citation_delta_annotation.py
   │     │  │  │  │  ├─ file_path_annotation.py
   │     │  │  │  │  ├─ file_path_delta_annotation.py
   │     │  │  │  │  ├─ image_file.py
   │     │  │  │  │  ├─ image_file_content_block.py
   │     │  │  │  │  ├─ image_file_content_block_param.py
   │     │  │  │  │  ├─ image_file_delta.py
   │     │  │  │  │  ├─ image_file_delta_block.py
   │     │  │  │  │  ├─ image_file_param.py
   │     │  │  │  │  ├─ image_url.py
   │     │  │  │  │  ├─ image_url_content_block.py
   │     │  │  │  │  ├─ image_url_content_block_param.py
   │     │  │  │  │  ├─ image_url_delta.py
   │     │  │  │  │  ├─ image_url_delta_block.py
   │     │  │  │  │  ├─ image_url_param.py
   │     │  │  │  │  ├─ message.py
   │     │  │  │  │  ├─ message_content.py
   │     │  │  │  │  ├─ message_content_delta.py
   │     │  │  │  │  ├─ message_content_part_param.py
   │     │  │  │  │  ├─ message_create_params.py
   │     │  │  │  │  ├─ message_deleted.py
   │     │  │  │  │  ├─ message_delta.py
   │     │  │  │  │  ├─ message_delta_event.py
   │     │  │  │  │  ├─ message_list_params.py
   │     │  │  │  │  ├─ message_update_params.py
   │     │  │  │  │  ├─ refusal_content_block.py
   │     │  │  │  │  ├─ refusal_delta_block.py
   │     │  │  │  │  ├─ required_action_function_tool_call.py
   │     │  │  │  │  ├─ run.py
   │     │  │  │  │  ├─ runs
   │     │  │  │  │  │  ├─ code_interpreter_output_image.py
   │     │  │  │  │  │  ├─ code_interpreter_tool_call.py
   │     │  │  │  │  │  ├─ code_interpreter_tool_call_delta.py
   │     │  │  │  │  │  ├─ file_search_tool_call.py
   │     │  │  │  │  │  ├─ file_search_tool_call_delta.py
   │     │  │  │  │  │  ├─ function_tool_call.py
   │     │  │  │  │  │  ├─ function_tool_call_delta.py
   │     │  │  │  │  │  ├─ message_creation_step_details.py
   │     │  │  │  │  │  ├─ run_step.py
   │     │  │  │  │  │  ├─ run_step_delta.py
   │     │  │  │  │  │  ├─ run_step_delta_event.py
   │     │  │  │  │  │  ├─ run_step_delta_message_delta.py
   │     │  │  │  │  │  ├─ run_step_include.py
   │     │  │  │  │  │  ├─ step_list_params.py
   │     │  │  │  │  │  ├─ step_retrieve_params.py
   │     │  │  │  │  │  ├─ tool_call.py
   │     │  │  │  │  │  ├─ tool_calls_step_details.py
   │     │  │  │  │  │  ├─ tool_call_delta.py
   │     │  │  │  │  │  ├─ tool_call_delta_object.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ run_create_params.py
   │     │  │  │  │  ├─ run_list_params.py
   │     │  │  │  │  ├─ run_status.py
   │     │  │  │  │  ├─ run_submit_tool_outputs_params.py
   │     │  │  │  │  ├─ run_update_params.py
   │     │  │  │  │  ├─ text.py
   │     │  │  │  │  ├─ text_content_block.py
   │     │  │  │  │  ├─ text_content_block_param.py
   │     │  │  │  │  ├─ text_delta.py
   │     │  │  │  │  ├─ text_delta_block.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ thread_create_and_run_params.py
   │     │  │  │  ├─ thread_create_params.py
   │     │  │  │  ├─ thread_deleted.py
   │     │  │  │  ├─ thread_update_params.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ chat
   │     │  │  │  ├─ chat_completion.py
   │     │  │  │  ├─ chat_completion_allowed_tools_param.py
   │     │  │  │  ├─ chat_completion_allowed_tool_choice_param.py
   │     │  │  │  ├─ chat_completion_assistant_message_param.py
   │     │  │  │  ├─ chat_completion_audio.py
   │     │  │  │  ├─ chat_completion_audio_param.py
   │     │  │  │  ├─ chat_completion_chunk.py
   │     │  │  │  ├─ chat_completion_content_part_image.py
   │     │  │  │  ├─ chat_completion_content_part_image_param.py
   │     │  │  │  ├─ chat_completion_content_part_input_audio_param.py
   │     │  │  │  ├─ chat_completion_content_part_param.py
   │     │  │  │  ├─ chat_completion_content_part_refusal_param.py
   │     │  │  │  ├─ chat_completion_content_part_text.py
   │     │  │  │  ├─ chat_completion_content_part_text_param.py
   │     │  │  │  ├─ chat_completion_custom_tool_param.py
   │     │  │  │  ├─ chat_completion_deleted.py
   │     │  │  │  ├─ chat_completion_developer_message_param.py
   │     │  │  │  ├─ chat_completion_function_call_option_param.py
   │     │  │  │  ├─ chat_completion_function_message_param.py
   │     │  │  │  ├─ chat_completion_function_tool.py
   │     │  │  │  ├─ chat_completion_function_tool_param.py
   │     │  │  │  ├─ chat_completion_message.py
   │     │  │  │  ├─ chat_completion_message_custom_tool_call.py
   │     │  │  │  ├─ chat_completion_message_custom_tool_call_param.py
   │     │  │  │  ├─ chat_completion_message_function_tool_call.py
   │     │  │  │  ├─ chat_completion_message_function_tool_call_param.py
   │     │  │  │  ├─ chat_completion_message_param.py
   │     │  │  │  ├─ chat_completion_message_tool_call.py
   │     │  │  │  ├─ chat_completion_message_tool_call_param.py
   │     │  │  │  ├─ chat_completion_message_tool_call_union_param.py
   │     │  │  │  ├─ chat_completion_modality.py
   │     │  │  │  ├─ chat_completion_named_tool_choice_custom_param.py
   │     │  │  │  ├─ chat_completion_named_tool_choice_param.py
   │     │  │  │  ├─ chat_completion_prediction_content_param.py
   │     │  │  │  ├─ chat_completion_reasoning_effort.py
   │     │  │  │  ├─ chat_completion_role.py
   │     │  │  │  ├─ chat_completion_store_message.py
   │     │  │  │  ├─ chat_completion_stream_options_param.py
   │     │  │  │  ├─ chat_completion_system_message_param.py
   │     │  │  │  ├─ chat_completion_token_logprob.py
   │     │  │  │  ├─ chat_completion_tool_choice_option_param.py
   │     │  │  │  ├─ chat_completion_tool_message_param.py
   │     │  │  │  ├─ chat_completion_tool_param.py
   │     │  │  │  ├─ chat_completion_tool_union_param.py
   │     │  │  │  ├─ chat_completion_user_message_param.py
   │     │  │  │  ├─ completions
   │     │  │  │  │  ├─ message_list_params.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ completion_create_params.py
   │     │  │  │  ├─ completion_list_params.py
   │     │  │  │  ├─ completion_update_params.py
   │     │  │  │  ├─ parsed_chat_completion.py
   │     │  │  │  ├─ parsed_function_tool_call.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ chat_model.py
   │     │  │  ├─ completion.py
   │     │  │  ├─ completion_choice.py
   │     │  │  ├─ completion_create_params.py
   │     │  │  ├─ completion_usage.py
   │     │  │  ├─ containers
   │     │  │  │  ├─ files
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ file_create_params.py
   │     │  │  │  ├─ file_create_response.py
   │     │  │  │  ├─ file_list_params.py
   │     │  │  │  ├─ file_list_response.py
   │     │  │  │  ├─ file_retrieve_response.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ container_create_params.py
   │     │  │  ├─ container_create_response.py
   │     │  │  ├─ container_list_params.py
   │     │  │  ├─ container_list_response.py
   │     │  │  ├─ container_retrieve_response.py
   │     │  │  ├─ content_provenance_check.py
   │     │  │  ├─ content_provenance_check_create_params.py
   │     │  │  ├─ conversations
   │     │  │  │  ├─ computer_screenshot_content.py
   │     │  │  │  ├─ conversation.py
   │     │  │  │  ├─ conversation_create_params.py
   │     │  │  │  ├─ conversation_deleted_resource.py
   │     │  │  │  ├─ conversation_item.py
   │     │  │  │  ├─ conversation_item_list.py
   │     │  │  │  ├─ conversation_update_params.py
   │     │  │  │  ├─ input_file_content.py
   │     │  │  │  ├─ input_file_content_param.py
   │     │  │  │  ├─ input_image_content.py
   │     │  │  │  ├─ input_image_content_param.py
   │     │  │  │  ├─ input_text_content.py
   │     │  │  │  ├─ input_text_content_param.py
   │     │  │  │  ├─ item_create_params.py
   │     │  │  │  ├─ item_list_params.py
   │     │  │  │  ├─ item_retrieve_params.py
   │     │  │  │  ├─ message.py
   │     │  │  │  ├─ output_text_content.py
   │     │  │  │  ├─ output_text_content_param.py
   │     │  │  │  ├─ refusal_content.py
   │     │  │  │  ├─ refusal_content_param.py
   │     │  │  │  ├─ summary_text_content.py
   │     │  │  │  ├─ text_content.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ create_embedding_response.py
   │     │  │  ├─ deleted_skill.py
   │     │  │  ├─ embedding.py
   │     │  │  ├─ embedding_create_params.py
   │     │  │  ├─ embedding_model.py
   │     │  │  ├─ evals
   │     │  │  │  ├─ create_eval_completions_run_data_source.py
   │     │  │  │  ├─ create_eval_completions_run_data_source_param.py
   │     │  │  │  ├─ create_eval_jsonl_run_data_source.py
   │     │  │  │  ├─ create_eval_jsonl_run_data_source_param.py
   │     │  │  │  ├─ eval_api_error.py
   │     │  │  │  ├─ runs
   │     │  │  │  │  ├─ output_item_list_params.py
   │     │  │  │  │  ├─ output_item_list_response.py
   │     │  │  │  │  ├─ output_item_retrieve_response.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ run_cancel_response.py
   │     │  │  │  ├─ run_create_params.py
   │     │  │  │  ├─ run_create_response.py
   │     │  │  │  ├─ run_delete_response.py
   │     │  │  │  ├─ run_list_params.py
   │     │  │  │  ├─ run_list_response.py
   │     │  │  │  ├─ run_retrieve_response.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ eval_create_params.py
   │     │  │  ├─ eval_create_response.py
   │     │  │  ├─ eval_custom_data_source_config.py
   │     │  │  ├─ eval_delete_response.py
   │     │  │  ├─ eval_list_params.py
   │     │  │  ├─ eval_list_response.py
   │     │  │  ├─ eval_retrieve_response.py
   │     │  │  ├─ eval_stored_completions_data_source_config.py
   │     │  │  ├─ eval_update_params.py
   │     │  │  ├─ eval_update_response.py
   │     │  │  ├─ file_chunking_strategy.py
   │     │  │  ├─ file_chunking_strategy_param.py
   │     │  │  ├─ file_content.py
   │     │  │  ├─ file_create_params.py
   │     │  │  ├─ file_deleted.py
   │     │  │  ├─ file_list_params.py
   │     │  │  ├─ file_object.py
   │     │  │  ├─ file_purpose.py
   │     │  │  ├─ fine_tuning
   │     │  │  │  ├─ alpha
   │     │  │  │  │  ├─ grader_run_params.py
   │     │  │  │  │  ├─ grader_run_response.py
   │     │  │  │  │  ├─ grader_validate_params.py
   │     │  │  │  │  ├─ grader_validate_response.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ checkpoints
   │     │  │  │  │  ├─ permission_create_params.py
   │     │  │  │  │  ├─ permission_create_response.py
   │     │  │  │  │  ├─ permission_delete_response.py
   │     │  │  │  │  ├─ permission_list_params.py
   │     │  │  │  │  ├─ permission_list_response.py
   │     │  │  │  │  ├─ permission_retrieve_params.py
   │     │  │  │  │  ├─ permission_retrieve_response.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ dpo_hyperparameters.py
   │     │  │  │  ├─ dpo_hyperparameters_param.py
   │     │  │  │  ├─ dpo_method.py
   │     │  │  │  ├─ dpo_method_param.py
   │     │  │  │  ├─ fine_tuning_job.py
   │     │  │  │  ├─ fine_tuning_job_event.py
   │     │  │  │  ├─ fine_tuning_job_integration.py
   │     │  │  │  ├─ fine_tuning_job_wandb_integration.py
   │     │  │  │  ├─ fine_tuning_job_wandb_integration_object.py
   │     │  │  │  ├─ jobs
   │     │  │  │  │  ├─ checkpoint_list_params.py
   │     │  │  │  │  ├─ fine_tuning_job_checkpoint.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ job_create_params.py
   │     │  │  │  ├─ job_list_events_params.py
   │     │  │  │  ├─ job_list_params.py
   │     │  │  │  ├─ reinforcement_hyperparameters.py
   │     │  │  │  ├─ reinforcement_hyperparameters_param.py
   │     │  │  │  ├─ reinforcement_method.py
   │     │  │  │  ├─ reinforcement_method_param.py
   │     │  │  │  ├─ supervised_hyperparameters.py
   │     │  │  │  ├─ supervised_hyperparameters_param.py
   │     │  │  │  ├─ supervised_method.py
   │     │  │  │  ├─ supervised_method_param.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ graders
   │     │  │  │  ├─ grader_inputs.py
   │     │  │  │  ├─ grader_inputs_param.py
   │     │  │  │  ├─ label_model_grader.py
   │     │  │  │  ├─ label_model_grader_param.py
   │     │  │  │  ├─ multi_grader.py
   │     │  │  │  ├─ multi_grader_param.py
   │     │  │  │  ├─ python_grader.py
   │     │  │  │  ├─ python_grader_param.py
   │     │  │  │  ├─ score_model_grader.py
   │     │  │  │  ├─ score_model_grader_param.py
   │     │  │  │  ├─ string_check_grader.py
   │     │  │  │  ├─ string_check_grader_param.py
   │     │  │  │  ├─ text_similarity_grader.py
   │     │  │  │  ├─ text_similarity_grader_param.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ image.py
   │     │  │  ├─ images_response.py
   │     │  │  ├─ image_create_variation_params.py
   │     │  │  ├─ image_edit_completed_event.py
   │     │  │  ├─ image_edit_params.py
   │     │  │  ├─ image_edit_partial_image_event.py
   │     │  │  ├─ image_edit_stream_event.py
   │     │  │  ├─ image_generate_params.py
   │     │  │  ├─ image_gen_completed_event.py
   │     │  │  ├─ image_gen_partial_image_event.py
   │     │  │  ├─ image_gen_stream_event.py
   │     │  │  ├─ image_input_reference_param.py
   │     │  │  ├─ image_model.py
   │     │  │  ├─ model.py
   │     │  │  ├─ model_deleted.py
   │     │  │  ├─ moderation.py
   │     │  │  ├─ moderation_create_params.py
   │     │  │  ├─ moderation_create_response.py
   │     │  │  ├─ moderation_image_url_input_param.py
   │     │  │  ├─ moderation_model.py
   │     │  │  ├─ moderation_multi_modal_input_param.py
   │     │  │  ├─ moderation_text_input_param.py
   │     │  │  ├─ other_file_chunking_strategy_object.py
   │     │  │  ├─ realtime
   │     │  │  │  ├─ audio_transcription.py
   │     │  │  │  ├─ audio_transcription_param.py
   │     │  │  │  ├─ call_accept_params.py
   │     │  │  │  ├─ call_create_params.py
   │     │  │  │  ├─ call_refer_params.py
   │     │  │  │  ├─ call_reject_params.py
   │     │  │  │  ├─ client_secret_create_params.py
   │     │  │  │  ├─ client_secret_create_response.py
   │     │  │  │  ├─ conversation_created_event.py
   │     │  │  │  ├─ conversation_item.py
   │     │  │  │  ├─ conversation_item_added.py
   │     │  │  │  ├─ conversation_item_created_event.py
   │     │  │  │  ├─ conversation_item_create_event.py
   │     │  │  │  ├─ conversation_item_create_event_param.py
   │     │  │  │  ├─ conversation_item_deleted_event.py
   │     │  │  │  ├─ conversation_item_delete_event.py
   │     │  │  │  ├─ conversation_item_delete_event_param.py
   │     │  │  │  ├─ conversation_item_done.py
   │     │  │  │  ├─ conversation_item_input_audio_transcription_completed_event.py
   │     │  │  │  ├─ conversation_item_input_audio_transcription_delta_event.py
   │     │  │  │  ├─ conversation_item_input_audio_transcription_failed_event.py
   │     │  │  │  ├─ conversation_item_input_audio_transcription_segment.py
   │     │  │  │  ├─ conversation_item_param.py
   │     │  │  │  ├─ conversation_item_retrieve_event.py
   │     │  │  │  ├─ conversation_item_retrieve_event_param.py
   │     │  │  │  ├─ conversation_item_truncated_event.py
   │     │  │  │  ├─ conversation_item_truncate_event.py
   │     │  │  │  ├─ conversation_item_truncate_event_param.py
   │     │  │  │  ├─ input_audio_buffer_append_event.py
   │     │  │  │  ├─ input_audio_buffer_append_event_param.py
   │     │  │  │  ├─ input_audio_buffer_cleared_event.py
   │     │  │  │  ├─ input_audio_buffer_clear_event.py
   │     │  │  │  ├─ input_audio_buffer_clear_event_param.py
   │     │  │  │  ├─ input_audio_buffer_committed_event.py
   │     │  │  │  ├─ input_audio_buffer_commit_event.py
   │     │  │  │  ├─ input_audio_buffer_commit_event_param.py
   │     │  │  │  ├─ input_audio_buffer_dtmf_event_received_event.py
   │     │  │  │  ├─ input_audio_buffer_speech_started_event.py
   │     │  │  │  ├─ input_audio_buffer_speech_stopped_event.py
   │     │  │  │  ├─ input_audio_buffer_timeout_triggered.py
   │     │  │  │  ├─ log_prob_properties.py
   │     │  │  │  ├─ mcp_list_tools_completed.py
   │     │  │  │  ├─ mcp_list_tools_failed.py
   │     │  │  │  ├─ mcp_list_tools_in_progress.py
   │     │  │  │  ├─ noise_reduction_type.py
   │     │  │  │  ├─ output_audio_buffer_clear_event.py
   │     │  │  │  ├─ output_audio_buffer_clear_event_param.py
   │     │  │  │  ├─ rate_limits_updated_event.py
   │     │  │  │  ├─ realtime_audio_config.py
   │     │  │  │  ├─ realtime_audio_config_input.py
   │     │  │  │  ├─ realtime_audio_config_input_param.py
   │     │  │  │  ├─ realtime_audio_config_output.py
   │     │  │  │  ├─ realtime_audio_config_output_param.py
   │     │  │  │  ├─ realtime_audio_config_param.py
   │     │  │  │  ├─ realtime_audio_formats.py
   │     │  │  │  ├─ realtime_audio_formats_param.py
   │     │  │  │  ├─ realtime_audio_input_turn_detection.py
   │     │  │  │  ├─ realtime_audio_input_turn_detection_param.py
   │     │  │  │  ├─ realtime_client_event.py
   │     │  │  │  ├─ realtime_client_event_param.py
   │     │  │  │  ├─ realtime_connect_params.py
   │     │  │  │  ├─ realtime_conversation_item_assistant_message.py
   │     │  │  │  ├─ realtime_conversation_item_assistant_message_param.py
   │     │  │  │  ├─ realtime_conversation_item_function_call.py
   │     │  │  │  ├─ realtime_conversation_item_function_call_output.py
   │     │  │  │  ├─ realtime_conversation_item_function_call_output_param.py
   │     │  │  │  ├─ realtime_conversation_item_function_call_param.py
   │     │  │  │  ├─ realtime_conversation_item_system_message.py
   │     │  │  │  ├─ realtime_conversation_item_system_message_param.py
   │     │  │  │  ├─ realtime_conversation_item_user_message.py
   │     │  │  │  ├─ realtime_conversation_item_user_message_param.py
   │     │  │  │  ├─ realtime_error.py
   │     │  │  │  ├─ realtime_error_event.py
   │     │  │  │  ├─ realtime_function_tool.py
   │     │  │  │  ├─ realtime_function_tool_param.py
   │     │  │  │  ├─ realtime_mcphttp_error.py
   │     │  │  │  ├─ realtime_mcphttp_error_param.py
   │     │  │  │  ├─ realtime_mcp_approval_request.py
   │     │  │  │  ├─ realtime_mcp_approval_request_param.py
   │     │  │  │  ├─ realtime_mcp_approval_response.py
   │     │  │  │  ├─ realtime_mcp_approval_response_param.py
   │     │  │  │  ├─ realtime_mcp_list_tools.py
   │     │  │  │  ├─ realtime_mcp_list_tools_param.py
   │     │  │  │  ├─ realtime_mcp_protocol_error.py
   │     │  │  │  ├─ realtime_mcp_protocol_error_param.py
   │     │  │  │  ├─ realtime_mcp_tool_call.py
   │     │  │  │  ├─ realtime_mcp_tool_call_param.py
   │     │  │  │  ├─ realtime_mcp_tool_execution_error.py
   │     │  │  │  ├─ realtime_mcp_tool_execution_error_param.py
   │     │  │  │  ├─ realtime_reasoning.py
   │     │  │  │  ├─ realtime_reasoning_effort.py
   │     │  │  │  ├─ realtime_reasoning_param.py
   │     │  │  │  ├─ realtime_response.py
   │     │  │  │  ├─ realtime_response_create_audio_output.py
   │     │  │  │  ├─ realtime_response_create_audio_output_param.py
   │     │  │  │  ├─ realtime_response_create_mcp_tool.py
   │     │  │  │  ├─ realtime_response_create_mcp_tool_param.py
   │     │  │  │  ├─ realtime_response_create_params.py
   │     │  │  │  ├─ realtime_response_create_params_param.py
   │     │  │  │  ├─ realtime_response_status.py
   │     │  │  │  ├─ realtime_response_usage.py
   │     │  │  │  ├─ realtime_response_usage_input_token_details.py
   │     │  │  │  ├─ realtime_response_usage_output_token_details.py
   │     │  │  │  ├─ realtime_server_event.py
   │     │  │  │  ├─ realtime_session_create_request.py
   │     │  │  │  ├─ realtime_session_create_request_param.py
   │     │  │  │  ├─ realtime_session_create_response.py
   │     │  │  │  ├─ realtime_tools_config.py
   │     │  │  │  ├─ realtime_tools_config_param.py
   │     │  │  │  ├─ realtime_tools_config_union.py
   │     │  │  │  ├─ realtime_tools_config_union_param.py
   │     │  │  │  ├─ realtime_tool_choice_config.py
   │     │  │  │  ├─ realtime_tool_choice_config_param.py
   │     │  │  │  ├─ realtime_tracing_config.py
   │     │  │  │  ├─ realtime_tracing_config_param.py
   │     │  │  │  ├─ realtime_transcription_session_audio.py
   │     │  │  │  ├─ realtime_transcription_session_audio_input.py
   │     │  │  │  ├─ realtime_transcription_session_audio_input_param.py
   │     │  │  │  ├─ realtime_transcription_session_audio_input_turn_detection.py
   │     │  │  │  ├─ realtime_transcription_session_audio_input_turn_detection_param.py
   │     │  │  │  ├─ realtime_transcription_session_audio_param.py
   │     │  │  │  ├─ realtime_transcription_session_create_request.py
   │     │  │  │  ├─ realtime_transcription_session_create_request_param.py
   │     │  │  │  ├─ realtime_transcription_session_create_response.py
   │     │  │  │  ├─ realtime_transcription_session_turn_detection.py
   │     │  │  │  ├─ realtime_truncation.py
   │     │  │  │  ├─ realtime_truncation_param.py
   │     │  │  │  ├─ realtime_truncation_retention_ratio.py
   │     │  │  │  ├─ realtime_truncation_retention_ratio_param.py
   │     │  │  │  ├─ response_audio_delta_event.py
   │     │  │  │  ├─ response_audio_done_event.py
   │     │  │  │  ├─ response_audio_transcript_delta_event.py
   │     │  │  │  ├─ response_audio_transcript_done_event.py
   │     │  │  │  ├─ response_cancel_event.py
   │     │  │  │  ├─ response_cancel_event_param.py
   │     │  │  │  ├─ response_content_part_added_event.py
   │     │  │  │  ├─ response_content_part_done_event.py
   │     │  │  │  ├─ response_created_event.py
   │     │  │  │  ├─ response_create_event.py
   │     │  │  │  ├─ response_create_event_param.py
   │     │  │  │  ├─ response_done_event.py
   │     │  │  │  ├─ response_function_call_arguments_delta_event.py
   │     │  │  │  ├─ response_function_call_arguments_done_event.py
   │     │  │  │  ├─ response_mcp_call_arguments_delta.py
   │     │  │  │  ├─ response_mcp_call_arguments_done.py
   │     │  │  │  ├─ response_mcp_call_completed.py
   │     │  │  │  ├─ response_mcp_call_failed.py
   │     │  │  │  ├─ response_mcp_call_in_progress.py
   │     │  │  │  ├─ response_output_item_added_event.py
   │     │  │  │  ├─ response_output_item_done_event.py
   │     │  │  │  ├─ response_text_delta_event.py
   │     │  │  │  ├─ response_text_done_event.py
   │     │  │  │  ├─ session_created_event.py
   │     │  │  │  ├─ session_updated_event.py
   │     │  │  │  ├─ session_update_event.py
   │     │  │  │  ├─ session_update_event_param.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ responses
   │     │  │  │  ├─ apply_patch_tool.py
   │     │  │  │  ├─ apply_patch_tool_param.py
   │     │  │  │  ├─ compacted_response.py
   │     │  │  │  ├─ computer_action.py
   │     │  │  │  ├─ computer_action_list.py
   │     │  │  │  ├─ computer_action_list_param.py
   │     │  │  │  ├─ computer_action_param.py
   │     │  │  │  ├─ computer_tool.py
   │     │  │  │  ├─ computer_tool_param.py
   │     │  │  │  ├─ computer_use_preview_tool.py
   │     │  │  │  ├─ computer_use_preview_tool_param.py
   │     │  │  │  ├─ container_auto.py
   │     │  │  │  ├─ container_auto_param.py
   │     │  │  │  ├─ container_network_policy_allowlist.py
   │     │  │  │  ├─ container_network_policy_allowlist_param.py
   │     │  │  │  ├─ container_network_policy_disabled.py
   │     │  │  │  ├─ container_network_policy_disabled_param.py
   │     │  │  │  ├─ container_network_policy_domain_secret.py
   │     │  │  │  ├─ container_network_policy_domain_secret_param.py
   │     │  │  │  ├─ container_reference.py
   │     │  │  │  ├─ container_reference_param.py
   │     │  │  │  ├─ custom_tool.py
   │     │  │  │  ├─ custom_tool_param.py
   │     │  │  │  ├─ easy_input_message.py
   │     │  │  │  ├─ easy_input_message_param.py
   │     │  │  │  ├─ file_search_tool.py
   │     │  │  │  ├─ file_search_tool_param.py
   │     │  │  │  ├─ function_shell_tool.py
   │     │  │  │  ├─ function_shell_tool_param.py
   │     │  │  │  ├─ function_tool.py
   │     │  │  │  ├─ function_tool_param.py
   │     │  │  │  ├─ image_detail.py
   │     │  │  │  ├─ inline_skill.py
   │     │  │  │  ├─ inline_skill_param.py
   │     │  │  │  ├─ inline_skill_source.py
   │     │  │  │  ├─ inline_skill_source_param.py
   │     │  │  │  ├─ input_item_list_params.py
   │     │  │  │  ├─ input_token_count_params.py
   │     │  │  │  ├─ input_token_count_response.py
   │     │  │  │  ├─ local_environment.py
   │     │  │  │  ├─ local_environment_param.py
   │     │  │  │  ├─ local_skill.py
   │     │  │  │  ├─ local_skill_param.py
   │     │  │  │  ├─ mcp_tool_call_error.py
   │     │  │  │  ├─ mcp_tool_call_error_param.py
   │     │  │  │  ├─ namespace_tool.py
   │     │  │  │  ├─ namespace_tool_param.py
   │     │  │  │  ├─ parsed_response.py
   │     │  │  │  ├─ response.py
   │     │  │  │  ├─ responses_client_event.py
   │     │  │  │  ├─ responses_client_event_param.py
   │     │  │  │  ├─ responses_server_event.py
   │     │  │  │  ├─ response_apply_patch_tool_call.py
   │     │  │  │  ├─ response_apply_patch_tool_call_output.py
   │     │  │  │  ├─ response_audio_delta_event.py
   │     │  │  │  ├─ response_audio_done_event.py
   │     │  │  │  ├─ response_audio_transcript_delta_event.py
   │     │  │  │  ├─ response_audio_transcript_done_event.py
   │     │  │  │  ├─ response_code_interpreter_call_code_delta_event.py
   │     │  │  │  ├─ response_code_interpreter_call_code_done_event.py
   │     │  │  │  ├─ response_code_interpreter_call_completed_event.py
   │     │  │  │  ├─ response_code_interpreter_call_interpreting_event.py
   │     │  │  │  ├─ response_code_interpreter_call_in_progress_event.py
   │     │  │  │  ├─ response_code_interpreter_tool_call.py
   │     │  │  │  ├─ response_code_interpreter_tool_call_param.py
   │     │  │  │  ├─ response_compaction_item.py
   │     │  │  │  ├─ response_compaction_item_param.py
   │     │  │  │  ├─ response_compaction_item_param_param.py
   │     │  │  │  ├─ response_compact_params.py
   │     │  │  │  ├─ response_completed_event.py
   │     │  │  │  ├─ response_computer_tool_call.py
   │     │  │  │  ├─ response_computer_tool_call_output_item.py
   │     │  │  │  ├─ response_computer_tool_call_output_screenshot.py
   │     │  │  │  ├─ response_computer_tool_call_output_screenshot_param.py
   │     │  │  │  ├─ response_computer_tool_call_param.py
   │     │  │  │  ├─ response_configuration_update_item.py
   │     │  │  │  ├─ response_configuration_update_item_param.py
   │     │  │  │  ├─ response_configuration_update_item_param_param.py
   │     │  │  │  ├─ response_container_reference.py
   │     │  │  │  ├─ response_content_part_added_event.py
   │     │  │  │  ├─ response_content_part_done_event.py
   │     │  │  │  ├─ response_conversation_param.py
   │     │  │  │  ├─ response_conversation_param_param.py
   │     │  │  │  ├─ response_created_event.py
   │     │  │  │  ├─ response_create_params.py
   │     │  │  │  ├─ response_custom_tool_call.py
   │     │  │  │  ├─ response_custom_tool_call_input_delta_event.py
   │     │  │  │  ├─ response_custom_tool_call_input_done_event.py
   │     │  │  │  ├─ response_custom_tool_call_item.py
   │     │  │  │  ├─ response_custom_tool_call_output.py
   │     │  │  │  ├─ response_custom_tool_call_output_item.py
   │     │  │  │  ├─ response_custom_tool_call_output_param.py
   │     │  │  │  ├─ response_custom_tool_call_param.py
   │     │  │  │  ├─ response_error.py
   │     │  │  │  ├─ response_error_event.py
   │     │  │  │  ├─ response_failed_event.py
   │     │  │  │  ├─ response_file_search_call_completed_event.py
   │     │  │  │  ├─ response_file_search_call_in_progress_event.py
   │     │  │  │  ├─ response_file_search_call_searching_event.py
   │     │  │  │  ├─ response_file_search_tool_call.py
   │     │  │  │  ├─ response_file_search_tool_call_param.py
   │     │  │  │  ├─ response_format_text_config.py
   │     │  │  │  ├─ response_format_text_config_param.py
   │     │  │  │  ├─ response_format_text_json_schema_config.py
   │     │  │  │  ├─ response_format_text_json_schema_config_param.py
   │     │  │  │  ├─ response_function_call_arguments_delta_event.py
   │     │  │  │  ├─ response_function_call_arguments_done_event.py
   │     │  │  │  ├─ response_function_call_output_item.py
   │     │  │  │  ├─ response_function_call_output_item_list.py
   │     │  │  │  ├─ response_function_call_output_item_list_param.py
   │     │  │  │  ├─ response_function_call_output_item_param.py
   │     │  │  │  ├─ response_function_shell_call_output_content.py
   │     │  │  │  ├─ response_function_shell_call_output_content_param.py
   │     │  │  │  ├─ response_function_shell_tool_call.py
   │     │  │  │  ├─ response_function_shell_tool_call_output.py
   │     │  │  │  ├─ response_function_tool_call.py
   │     │  │  │  ├─ response_function_tool_call_item.py
   │     │  │  │  ├─ response_function_tool_call_output_item.py
   │     │  │  │  ├─ response_function_tool_call_param.py
   │     │  │  │  ├─ response_function_web_search.py
   │     │  │  │  ├─ response_function_web_search_param.py
   │     │  │  │  ├─ response_image_gen_call_completed_event.py
   │     │  │  │  ├─ response_image_gen_call_generating_event.py
   │     │  │  │  ├─ response_image_gen_call_in_progress_event.py
   │     │  │  │  ├─ response_image_gen_call_partial_image_event.py
   │     │  │  │  ├─ response_includable.py
   │     │  │  │  ├─ response_incomplete_event.py
   │     │  │  │  ├─ response_input.py
   │     │  │  │  ├─ response_input_audio.py
   │     │  │  │  ├─ response_input_audio_param.py
   │     │  │  │  ├─ response_input_content.py
   │     │  │  │  ├─ response_input_content_param.py
   │     │  │  │  ├─ response_input_file.py
   │     │  │  │  ├─ response_input_file_content.py
   │     │  │  │  ├─ response_input_file_content_param.py
   │     │  │  │  ├─ response_input_file_param.py
   │     │  │  │  ├─ response_input_image.py
   │     │  │  │  ├─ response_input_image_content.py
   │     │  │  │  ├─ response_input_image_content_param.py
   │     │  │  │  ├─ response_input_image_param.py
   │     │  │  │  ├─ response_input_item.py
   │     │  │  │  ├─ response_input_item_param.py
   │     │  │  │  ├─ response_input_message_content_list.py
   │     │  │  │  ├─ response_input_message_content_list_param.py
   │     │  │  │  ├─ response_input_message_item.py
   │     │  │  │  ├─ response_input_param.py
   │     │  │  │  ├─ response_input_text.py
   │     │  │  │  ├─ response_input_text_content.py
   │     │  │  │  ├─ response_input_text_content_param.py
   │     │  │  │  ├─ response_input_text_param.py
   │     │  │  │  ├─ response_in_progress_event.py
   │     │  │  │  ├─ response_item.py
   │     │  │  │  ├─ response_item_list.py
   │     │  │  │  ├─ response_local_environment.py
   │     │  │  │  ├─ response_mcp_call_arguments_delta_event.py
   │     │  │  │  ├─ response_mcp_call_arguments_done_event.py
   │     │  │  │  ├─ response_mcp_call_completed_event.py
   │     │  │  │  ├─ response_mcp_call_failed_event.py
   │     │  │  │  ├─ response_mcp_call_in_progress_event.py
   │     │  │  │  ├─ response_mcp_list_tools_completed_event.py
   │     │  │  │  ├─ response_mcp_list_tools_failed_event.py
   │     │  │  │  ├─ response_mcp_list_tools_in_progress_event.py
   │     │  │  │  ├─ response_output_item.py
   │     │  │  │  ├─ response_output_item_added_event.py
   │     │  │  │  ├─ response_output_item_done_event.py
   │     │  │  │  ├─ response_output_message.py
   │     │  │  │  ├─ response_output_message_param.py
   │     │  │  │  ├─ response_output_refusal.py
   │     │  │  │  ├─ response_output_refusal_param.py
   │     │  │  │  ├─ response_output_text.py
   │     │  │  │  ├─ response_output_text_annotation_added_event.py
   │     │  │  │  ├─ response_output_text_param.py
   │     │  │  │  ├─ response_prompt.py
   │     │  │  │  ├─ response_prompt_param.py
   │     │  │  │  ├─ response_queued_event.py
   │     │  │  │  ├─ response_reasoning_item.py
   │     │  │  │  ├─ response_reasoning_item_param.py
   │     │  │  │  ├─ response_reasoning_summary_part_added_event.py
   │     │  │  │  ├─ response_reasoning_summary_part_done_event.py
   │     │  │  │  ├─ response_reasoning_summary_text_delta_event.py
   │     │  │  │  ├─ response_reasoning_summary_text_done_event.py
   │     │  │  │  ├─ response_reasoning_text_delta_event.py
   │     │  │  │  ├─ response_reasoning_text_done_event.py
   │     │  │  │  ├─ response_refusal_delta_event.py
   │     │  │  │  ├─ response_refusal_done_event.py
   │     │  │  │  ├─ response_retrieve_params.py
   │     │  │  │  ├─ response_shell_call_command_added_event.py
   │     │  │  │  ├─ response_shell_call_command_delta_event.py
   │     │  │  │  ├─ response_shell_call_command_done_event.py
   │     │  │  │  ├─ response_shell_call_output_content_delta_event.py
   │     │  │  │  ├─ response_shell_call_output_content_done_event.py
   │     │  │  │  ├─ response_status.py
   │     │  │  │  ├─ response_steer_accepted_event.py
   │     │  │  │  ├─ response_steer_error_code.py
   │     │  │  │  ├─ response_steer_event.py
   │     │  │  │  ├─ response_steer_event_param.py
   │     │  │  │  ├─ response_steer_failed_event.py
   │     │  │  │  ├─ response_steer_input.py
   │     │  │  │  ├─ response_steer_input_content.py
   │     │  │  │  ├─ response_steer_input_content_param.py
   │     │  │  │  ├─ response_steer_input_param.py
   │     │  │  │  ├─ response_steer_pending_event.py
   │     │  │  │  ├─ response_steer_pending_reason.py
   │     │  │  │  ├─ response_steer_required_input.py
   │     │  │  │  ├─ response_stream_event.py
   │     │  │  │  ├─ response_text_config.py
   │     │  │  │  ├─ response_text_config_param.py
   │     │  │  │  ├─ response_text_delta_event.py
   │     │  │  │  ├─ response_text_done_event.py
   │     │  │  │  ├─ response_tool_search_call.py
   │     │  │  │  ├─ response_tool_search_output_item.py
   │     │  │  │  ├─ response_tool_search_output_item_param.py
   │     │  │  │  ├─ response_tool_search_output_item_param_param.py
   │     │  │  │  ├─ response_usage.py
   │     │  │  │  ├─ response_web_search_call_completed_event.py
   │     │  │  │  ├─ response_web_search_call_in_progress_event.py
   │     │  │  │  ├─ response_web_search_call_searching_event.py
   │     │  │  │  ├─ service_tier.py
   │     │  │  │  ├─ skill_reference.py
   │     │  │  │  ├─ skill_reference_param.py
   │     │  │  │  ├─ tool.py
   │     │  │  │  ├─ tool_choice_allowed.py
   │     │  │  │  ├─ tool_choice_allowed_param.py
   │     │  │  │  ├─ tool_choice_apply_patch.py
   │     │  │  │  ├─ tool_choice_apply_patch_param.py
   │     │  │  │  ├─ tool_choice_custom.py
   │     │  │  │  ├─ tool_choice_custom_param.py
   │     │  │  │  ├─ tool_choice_function.py
   │     │  │  │  ├─ tool_choice_function_param.py
   │     │  │  │  ├─ tool_choice_mcp.py
   │     │  │  │  ├─ tool_choice_mcp_param.py
   │     │  │  │  ├─ tool_choice_options.py
   │     │  │  │  ├─ tool_choice_shell.py
   │     │  │  │  ├─ tool_choice_shell_param.py
   │     │  │  │  ├─ tool_choice_types.py
   │     │  │  │  ├─ tool_choice_types_param.py
   │     │  │  │  ├─ tool_param.py
   │     │  │  │  ├─ tool_search_tool.py
   │     │  │  │  ├─ tool_search_tool_param.py
   │     │  │  │  ├─ web_search_preview_tool.py
   │     │  │  │  ├─ web_search_preview_tool_param.py
   │     │  │  │  ├─ web_search_tool.py
   │     │  │  │  ├─ web_search_tool_param.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ safety
   │     │  │  │  ├─ safety_alert.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ shared
   │     │  │  │  ├─ all_models.py
   │     │  │  │  ├─ chat_model.py
   │     │  │  │  ├─ comparison_filter.py
   │     │  │  │  ├─ compound_filter.py
   │     │  │  │  ├─ custom_tool_input_format.py
   │     │  │  │  ├─ error_object.py
   │     │  │  │  ├─ function_definition.py
   │     │  │  │  ├─ function_parameters.py
   │     │  │  │  ├─ metadata.py
   │     │  │  │  ├─ oauth_error_code.py
   │     │  │  │  ├─ reasoning.py
   │     │  │  │  ├─ reasoning_effort.py
   │     │  │  │  ├─ responses_model.py
   │     │  │  │  ├─ response_format_json_object.py
   │     │  │  │  ├─ response_format_json_schema.py
   │     │  │  │  ├─ response_format_text.py
   │     │  │  │  ├─ response_format_text_grammar.py
   │     │  │  │  ├─ response_format_text_python.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ shared_params
   │     │  │  │  ├─ chat_model.py
   │     │  │  │  ├─ comparison_filter.py
   │     │  │  │  ├─ compound_filter.py
   │     │  │  │  ├─ custom_tool_input_format.py
   │     │  │  │  ├─ function_definition.py
   │     │  │  │  ├─ function_parameters.py
   │     │  │  │  ├─ metadata.py
   │     │  │  │  ├─ oauth_error_code.py
   │     │  │  │  ├─ reasoning.py
   │     │  │  │  ├─ reasoning_effort.py
   │     │  │  │  ├─ responses_model.py
   │     │  │  │  ├─ response_format_json_object.py
   │     │  │  │  ├─ response_format_json_schema.py
   │     │  │  │  ├─ response_format_text.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ skill.py
   │     │  │  ├─ skills
   │     │  │  │  ├─ deleted_skill_version.py
   │     │  │  │  ├─ skill_version.py
   │     │  │  │  ├─ skill_version_list.py
   │     │  │  │  ├─ versions
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ version_create_params.py
   │     │  │  │  ├─ version_list_params.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ skill_create_params.py
   │     │  │  ├─ skill_list.py
   │     │  │  ├─ skill_list_params.py
   │     │  │  ├─ skill_update_params.py
   │     │  │  ├─ static_file_chunking_strategy.py
   │     │  │  ├─ static_file_chunking_strategy_object.py
   │     │  │  ├─ static_file_chunking_strategy_object_param.py
   │     │  │  ├─ static_file_chunking_strategy_param.py
   │     │  │  ├─ upload.py
   │     │  │  ├─ uploads
   │     │  │  │  ├─ part_create_params.py
   │     │  │  │  ├─ upload_part.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ upload_complete_params.py
   │     │  │  ├─ upload_create_params.py
   │     │  │  ├─ vector_store.py
   │     │  │  ├─ vector_stores
   │     │  │  │  ├─ file_batch_create_params.py
   │     │  │  │  ├─ file_batch_list_files_params.py
   │     │  │  │  ├─ file_content_response.py
   │     │  │  │  ├─ file_create_params.py
   │     │  │  │  ├─ file_list_params.py
   │     │  │  │  ├─ file_update_params.py
   │     │  │  │  ├─ vector_store_file.py
   │     │  │  │  ├─ vector_store_file_batch.py
   │     │  │  │  ├─ vector_store_file_deleted.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vector_store_create_params.py
   │     │  │  ├─ vector_store_deleted.py
   │     │  │  ├─ vector_store_list_params.py
   │     │  │  ├─ vector_store_search_params.py
   │     │  │  ├─ vector_store_search_response.py
   │     │  │  ├─ vector_store_update_params.py
   │     │  │  ├─ video.py
   │     │  │  ├─ video_create_character_params.py
   │     │  │  ├─ video_create_character_response.py
   │     │  │  ├─ video_create_error.py
   │     │  │  ├─ video_create_params.py
   │     │  │  ├─ video_delete_response.py
   │     │  │  ├─ video_download_content_params.py
   │     │  │  ├─ video_edit_params.py
   │     │  │  ├─ video_extend_params.py
   │     │  │  ├─ video_get_character_response.py
   │     │  │  ├─ video_list_params.py
   │     │  │  ├─ video_model.py
   │     │  │  ├─ video_model_param.py
   │     │  │  ├─ video_remix_params.py
   │     │  │  ├─ video_seconds.py
   │     │  │  ├─ video_size.py
   │     │  │  ├─ webhooks
   │     │  │  │  ├─ batch_cancelled_webhook_event.py
   │     │  │  │  ├─ batch_completed_webhook_event.py
   │     │  │  │  ├─ batch_expired_webhook_event.py
   │     │  │  │  ├─ batch_failed_webhook_event.py
   │     │  │  │  ├─ eval_run_canceled_webhook_event.py
   │     │  │  │  ├─ eval_run_failed_webhook_event.py
   │     │  │  │  ├─ eval_run_succeeded_webhook_event.py
   │     │  │  │  ├─ fine_tuning_job_cancelled_webhook_event.py
   │     │  │  │  ├─ fine_tuning_job_failed_webhook_event.py
   │     │  │  │  ├─ fine_tuning_job_succeeded_webhook_event.py
   │     │  │  │  ├─ live_call_incoming_webhook_event.py
   │     │  │  │  ├─ realtime_call_incoming_webhook_event.py
   │     │  │  │  ├─ response_cancelled_webhook_event.py
   │     │  │  │  ├─ response_completed_webhook_event.py
   │     │  │  │  ├─ response_failed_webhook_event.py
   │     │  │  │  ├─ response_incomplete_webhook_event.py
   │     │  │  │  ├─ safety_alert_created_webhook_event.py
   │     │  │  │  ├─ safety_identifier_blocked_webhook_event.py
   │     │  │  │  ├─ safety_org_alert_created_webhook_event.py
   │     │  │  │  ├─ unwrap_webhook_event.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ websocket_connection_options.py
   │     │  │  ├─ websocket_reconnection.py
   │     │  │  └─ __init__.py
   │     │  ├─ version.py
   │     │  ├─ _base_client.py
   │     │  ├─ _client.py
   │     │  ├─ _compat.py
   │     │  ├─ _constants.py
   │     │  ├─ _data_residency.py
   │     │  ├─ _event_handler.py
   │     │  ├─ _exceptions.py
   │     │  ├─ _extras
   │     │  │  ├─ numpy_proxy.py
   │     │  │  ├─ pandas_proxy.py
   │     │  │  ├─ sounddevice_proxy.py
   │     │  │  ├─ _common.py
   │     │  │  └─ __init__.py
   │     │  ├─ _files.py
   │     │  ├─ _httpx2.py
   │     │  ├─ _legacy_response.py
   │     │  ├─ _models.py
   │     │  ├─ _module_client.py
   │     │  ├─ _multipart.py
   │     │  ├─ _provider.py
   │     │  ├─ _qs.py
   │     │  ├─ _resource.py
   │     │  ├─ _response.py
   │     │  ├─ _send_queue.py
   │     │  ├─ _streaming.py
   │     │  ├─ _types.py
   │     │  ├─ _utils
   │     │  │  ├─ _compat.py
   │     │  │  ├─ _datetime_parse.py
   │     │  │  ├─ _json.py
   │     │  │  ├─ _path.py
   │     │  │  ├─ _proxy.py
   │     │  │  ├─ _reflection.py
   │     │  │  ├─ _resources_proxy.py
   │     │  │  ├─ _streams.py
   │     │  │  ├─ _sync.py
   │     │  │  ├─ _transform.py
   │     │  │  ├─ _typing.py
   │     │  │  ├─ _utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ _vendor
   │     │  │  ├─ httpx_aiohttp
   │     │  │  │  ├─ client.py
   │     │  │  │  ├─ FORK.md
   │     │  │  │  ├─ LICENSE
   │     │  │  │  ├─ README.md
   │     │  │  │  ├─ transport.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ packaging
   │     │  ├─ dependency_groups.py
   │     │  ├─ direct_url.py
   │     │  ├─ errors.py
   │     │  ├─ licenses
   │     │  │  ├─ _spdx.py
   │     │  │  └─ __init__.py
   │     │  ├─ markers.py
   │     │  ├─ metadata.py
   │     │  ├─ py.typed
   │     │  ├─ pylock.py
   │     │  ├─ requirements.py
   │     │  ├─ specifiers.py
   │     │  ├─ tags.py
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ _elffile.py
   │     │  ├─ _manylinux.py
   │     │  ├─ _musllinux.py
   │     │  ├─ _parser.py
   │     │  ├─ _structures.py
   │     │  ├─ _tokenizer.py
   │     │  └─ __init__.py
   │     ├─ pathvalidate
   │     │  ├─ argparse.py
   │     │  ├─ click.py
   │     │  ├─ error.py
   │     │  ├─ handler.py
   │     │  ├─ py.typed
   │     │  ├─ _base.py
   │     │  ├─ _common.py
   │     │  ├─ _const.py
   │     │  ├─ _filename.py
   │     │  ├─ _filepath.py
   │     │  ├─ _ltsv.py
   │     │  ├─ _symbol.py
   │     │  ├─ _types.py
   │     │  ├─ __init__.py
   │     │  └─ __version__.py
   │     ├─ PIL
   │     │  ├─ AvifImagePlugin.py
   │     │  ├─ BdfFontFile.py
   │     │  ├─ BlpImagePlugin.py
   │     │  ├─ BmpImagePlugin.py
   │     │  ├─ BufrStubImagePlugin.py
   │     │  ├─ ContainerIO.py
   │     │  ├─ CurImagePlugin.py
   │     │  ├─ DcxImagePlugin.py
   │     │  ├─ DdsImagePlugin.py
   │     │  ├─ EpsImagePlugin.py
   │     │  ├─ ExifTags.py
   │     │  ├─ features.py
   │     │  ├─ FitsImagePlugin.py
   │     │  ├─ FliImagePlugin.py
   │     │  ├─ FontFile.py
   │     │  ├─ FpxImagePlugin.py
   │     │  ├─ FtexImagePlugin.py
   │     │  ├─ GbrImagePlugin.py
   │     │  ├─ GdImageFile.py
   │     │  ├─ GifImagePlugin.py
   │     │  ├─ GimpGradientFile.py
   │     │  ├─ GimpPaletteFile.py
   │     │  ├─ GribStubImagePlugin.py
   │     │  ├─ Hdf5StubImagePlugin.py
   │     │  ├─ IcnsImagePlugin.py
   │     │  ├─ IcoImagePlugin.py
   │     │  ├─ Image.py
   │     │  ├─ ImageChops.py
   │     │  ├─ ImageCms.py
   │     │  ├─ ImageColor.py
   │     │  ├─ ImageDraw.py
   │     │  ├─ ImageDraw2.py
   │     │  ├─ ImageEnhance.py
   │     │  ├─ ImageFile.py
   │     │  ├─ ImageFilter.py
   │     │  ├─ ImageFont.py
   │     │  ├─ ImageGrab.py
   │     │  ├─ ImageMath.py
   │     │  ├─ ImageMode.py
   │     │  ├─ ImageMorph.py
   │     │  ├─ ImageOps.py
   │     │  ├─ ImagePalette.py
   │     │  ├─ ImagePath.py
   │     │  ├─ ImageQt.py
   │     │  ├─ ImageSequence.py
   │     │  ├─ ImageShow.py
   │     │  ├─ ImageStat.py
   │     │  ├─ ImageText.py
   │     │  ├─ ImageTk.py
   │     │  ├─ ImageTransform.py
   │     │  ├─ ImageWin.py
   │     │  ├─ ImImagePlugin.py
   │     │  ├─ ImtImagePlugin.py
   │     │  ├─ IptcImagePlugin.py
   │     │  ├─ Jpeg2KImagePlugin.py
   │     │  ├─ JpegImagePlugin.py
   │     │  ├─ JpegPresets.py
   │     │  ├─ McIdasImagePlugin.py
   │     │  ├─ MicImagePlugin.py
   │     │  ├─ MpegImagePlugin.py
   │     │  ├─ MpoImagePlugin.py
   │     │  ├─ MspImagePlugin.py
   │     │  ├─ PaletteFile.py
   │     │  ├─ PalmImagePlugin.py
   │     │  ├─ PcdImagePlugin.py
   │     │  ├─ PcfFontFile.py
   │     │  ├─ PcxImagePlugin.py
   │     │  ├─ PdfImagePlugin.py
   │     │  ├─ PdfParser.py
   │     │  ├─ PixarImagePlugin.py
   │     │  ├─ PngImagePlugin.py
   │     │  ├─ PpmImagePlugin.py
   │     │  ├─ PsdImagePlugin.py
   │     │  ├─ PSDraw.py
   │     │  ├─ py.typed
   │     │  ├─ QoiImagePlugin.py
   │     │  ├─ report.py
   │     │  ├─ SgiImagePlugin.py
   │     │  ├─ SpiderImagePlugin.py
   │     │  ├─ SunImagePlugin.py
   │     │  ├─ TarIO.py
   │     │  ├─ TgaImagePlugin.py
   │     │  ├─ TiffImagePlugin.py
   │     │  ├─ TiffTags.py
   │     │  ├─ WalImageFile.py
   │     │  ├─ WebPImagePlugin.py
   │     │  ├─ WmfImagePlugin.py
   │     │  ├─ XbmImagePlugin.py
   │     │  ├─ XpmImagePlugin.py
   │     │  ├─ XVThumbImagePlugin.py
   │     │  ├─ _avif.cp313-win_amd64.pyd
   │     │  ├─ _avif.pyi
   │     │  ├─ _binary.py
   │     │  ├─ _deprecate.py
   │     │  ├─ _imaging.cp313-win_amd64.pyd
   │     │  ├─ _imaging.pyi
   │     │  ├─ _imagingcms.cp313-win_amd64.pyd
   │     │  ├─ _imagingcms.pyi
   │     │  ├─ _imagingft.cp313-win_amd64.pyd
   │     │  ├─ _imagingft.pyi
   │     │  ├─ _imagingmath.cp313-win_amd64.pyd
   │     │  ├─ _imagingmath.pyi
   │     │  ├─ _imagingmorph.cp313-win_amd64.pyd
   │     │  ├─ _imagingmorph.pyi
   │     │  ├─ _imagingtk.cp313-win_amd64.pyd
   │     │  ├─ _imagingtk.pyi
   │     │  ├─ _tkinter_finder.py
   │     │  ├─ _typing.py
   │     │  ├─ _util.py
   │     │  ├─ _version.py
   │     │  ├─ _webp.cp313-win_amd64.pyd
   │     │  ├─ _webp.pyi
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ pip
   │     │  ├─ py.typed
   │     │  ├─ _internal
   │     │  │  ├─ build_env.py
   │     │  │  ├─ cache.py
   │     │  │  ├─ cli
   │     │  │  │  ├─ autocompletion.py
   │     │  │  │  ├─ base_command.py
   │     │  │  │  ├─ cmdoptions.py
   │     │  │  │  ├─ command_context.py
   │     │  │  │  ├─ index_command.py
   │     │  │  │  ├─ main.py
   │     │  │  │  ├─ main_parser.py
   │     │  │  │  ├─ parser.py
   │     │  │  │  ├─ progress_bars.py
   │     │  │  │  ├─ req_command.py
   │     │  │  │  ├─ spinners.py
   │     │  │  │  ├─ status_codes.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ commands
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ completion.py
   │     │  │  │  ├─ configuration.py
   │     │  │  │  ├─ debug.py
   │     │  │  │  ├─ download.py
   │     │  │  │  ├─ freeze.py
   │     │  │  │  ├─ hash.py
   │     │  │  │  ├─ help.py
   │     │  │  │  ├─ index.py
   │     │  │  │  ├─ inspect.py
   │     │  │  │  ├─ install.py
   │     │  │  │  ├─ list.py
   │     │  │  │  ├─ search.py
   │     │  │  │  ├─ show.py
   │     │  │  │  ├─ uninstall.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ configuration.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ index
   │     │  │  │  ├─ collector.py
   │     │  │  │  ├─ package_finder.py
   │     │  │  │  ├─ sources.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ locations
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ _sysconfig.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ main.py
   │     │  │  ├─ metadata
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ importlib
   │     │  │  │  │  ├─ _compat.py
   │     │  │  │  │  ├─ _envs.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ pkg_resources.py
   │     │  │  │  ├─ _json.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ models
   │     │  │  │  ├─ candidate.py
   │     │  │  │  ├─ direct_url.py
   │     │  │  │  ├─ format_control.py
   │     │  │  │  ├─ index.py
   │     │  │  │  ├─ installation_report.py
   │     │  │  │  ├─ link.py
   │     │  │  │  ├─ scheme.py
   │     │  │  │  ├─ search_scope.py
   │     │  │  │  ├─ selection_prefs.py
   │     │  │  │  ├─ target_python.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ network
   │     │  │  │  ├─ auth.py
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ download.py
   │     │  │  │  ├─ lazy_wheel.py
   │     │  │  │  ├─ session.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ xmlrpc.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ operations
   │     │  │  │  ├─ build
   │     │  │  │  │  ├─ build_tracker.py
   │     │  │  │  │  ├─ metadata.py
   │     │  │  │  │  ├─ metadata_editable.py
   │     │  │  │  │  ├─ metadata_legacy.py
   │     │  │  │  │  ├─ wheel.py
   │     │  │  │  │  ├─ wheel_editable.py
   │     │  │  │  │  ├─ wheel_legacy.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ freeze.py
   │     │  │  │  ├─ install
   │     │  │  │  │  ├─ editable_legacy.py
   │     │  │  │  │  ├─ wheel.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ prepare.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pyproject.py
   │     │  │  ├─ req
   │     │  │  │  ├─ constructors.py
   │     │  │  │  ├─ req_file.py
   │     │  │  │  ├─ req_install.py
   │     │  │  │  ├─ req_set.py
   │     │  │  │  ├─ req_uninstall.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ resolution
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ legacy
   │     │  │  │  │  ├─ resolver.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ resolvelib
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ candidates.py
   │     │  │  │  │  ├─ factory.py
   │     │  │  │  │  ├─ found_candidates.py
   │     │  │  │  │  ├─ provider.py
   │     │  │  │  │  ├─ reporter.py
   │     │  │  │  │  ├─ requirements.py
   │     │  │  │  │  ├─ resolver.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ self_outdated_check.py
   │     │  │  ├─ utils
   │     │  │  │  ├─ appdirs.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ compatibility_tags.py
   │     │  │  │  ├─ datetime.py
   │     │  │  │  ├─ deprecation.py
   │     │  │  │  ├─ direct_url_helpers.py
   │     │  │  │  ├─ egg_link.py
   │     │  │  │  ├─ entrypoints.py
   │     │  │  │  ├─ filesystem.py
   │     │  │  │  ├─ filetypes.py
   │     │  │  │  ├─ glibc.py
   │     │  │  │  ├─ hashes.py
   │     │  │  │  ├─ logging.py
   │     │  │  │  ├─ misc.py
   │     │  │  │  ├─ packaging.py
   │     │  │  │  ├─ retry.py
   │     │  │  │  ├─ setuptools_build.py
   │     │  │  │  ├─ subprocess.py
   │     │  │  │  ├─ temp_dir.py
   │     │  │  │  ├─ unpacking.py
   │     │  │  │  ├─ urls.py
   │     │  │  │  ├─ virtualenv.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  ├─ _jaraco_text.py
   │     │  │  │  ├─ _log.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vcs
   │     │  │  │  ├─ bazaar.py
   │     │  │  │  ├─ git.py
   │     │  │  │  ├─ mercurial.py
   │     │  │  │  ├─ subversion.py
   │     │  │  │  ├─ versioncontrol.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ wheel_builder.py
   │     │  │  └─ __init__.py
   │     │  ├─ _vendor
   │     │  │  ├─ cachecontrol
   │     │  │  │  ├─ adapter.py
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ caches
   │     │  │  │  │  ├─ file_cache.py
   │     │  │  │  │  ├─ redis_cache.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ controller.py
   │     │  │  │  ├─ filewrapper.py
   │     │  │  │  ├─ heuristics.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ serialize.py
   │     │  │  │  ├─ wrapper.py
   │     │  │  │  ├─ _cmd.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ certifi
   │     │  │  │  ├─ cacert.pem
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ idna
   │     │  │  │  ├─ codec.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ idnadata.py
   │     │  │  │  ├─ intranges.py
   │     │  │  │  ├─ package_data.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ uts46data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ msgpack
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ ext.py
   │     │  │  │  ├─ fallback.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ packaging
   │     │  │  │  ├─ licenses
   │     │  │  │  │  ├─ _spdx.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ metadata.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ requirements.py
   │     │  │  │  ├─ specifiers.py
   │     │  │  │  ├─ tags.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ _elffile.py
   │     │  │  │  ├─ _manylinux.py
   │     │  │  │  ├─ _musllinux.py
   │     │  │  │  ├─ _parser.py
   │     │  │  │  ├─ _structures.py
   │     │  │  │  ├─ _tokenizer.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pkg_resources
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ platformdirs
   │     │  │  │  ├─ android.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ macos.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ unix.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ windows.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ pygments
   │     │  │  │  ├─ cmdline.py
   │     │  │  │  ├─ console.py
   │     │  │  │  ├─ filter.py
   │     │  │  │  ├─ filters
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ formatter.py
   │     │  │  │  ├─ formatters
   │     │  │  │  │  ├─ bbcode.py
   │     │  │  │  │  ├─ groff.py
   │     │  │  │  │  ├─ html.py
   │     │  │  │  │  ├─ img.py
   │     │  │  │  │  ├─ irc.py
   │     │  │  │  │  ├─ latex.py
   │     │  │  │  │  ├─ other.py
   │     │  │  │  │  ├─ pangomarkup.py
   │     │  │  │  │  ├─ rtf.py
   │     │  │  │  │  ├─ svg.py
   │     │  │  │  │  ├─ terminal.py
   │     │  │  │  │  ├─ terminal256.py
   │     │  │  │  │  ├─ _mapping.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ lexer.py
   │     │  │  │  ├─ lexers
   │     │  │  │  │  ├─ python.py
   │     │  │  │  │  ├─ _mapping.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ modeline.py
   │     │  │  │  ├─ plugin.py
   │     │  │  │  ├─ regexopt.py
   │     │  │  │  ├─ scanner.py
   │     │  │  │  ├─ sphinxext.py
   │     │  │  │  ├─ style.py
   │     │  │  │  ├─ styles
   │     │  │  │  │  ├─ _mapping.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ token.py
   │     │  │  │  ├─ unistring.py
   │     │  │  │  ├─ util.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ pyproject_hooks
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ _impl.py
   │     │  │  │  ├─ _in_process
   │     │  │  │  │  ├─ _in_process.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ requests
   │     │  │  │  ├─ adapters.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ auth.py
   │     │  │  │  ├─ certs.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ cookies.py
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ help.py
   │     │  │  │  ├─ hooks.py
   │     │  │  │  ├─ models.py
   │     │  │  │  ├─ packages.py
   │     │  │  │  ├─ sessions.py
   │     │  │  │  ├─ status_codes.py
   │     │  │  │  ├─ structures.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ _internal_utils.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __version__.py
   │     │  │  ├─ resolvelib
   │     │  │  │  ├─ compat
   │     │  │  │  │  ├─ collections_abc.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ providers.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ reporters.py
   │     │  │  │  ├─ resolvers.py
   │     │  │  │  ├─ structs.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ rich
   │     │  │  │  ├─ abc.py
   │     │  │  │  ├─ align.py
   │     │  │  │  ├─ ansi.py
   │     │  │  │  ├─ bar.py
   │     │  │  │  ├─ box.py
   │     │  │  │  ├─ cells.py
   │     │  │  │  ├─ color.py
   │     │  │  │  ├─ color_triplet.py
   │     │  │  │  ├─ columns.py
   │     │  │  │  ├─ console.py
   │     │  │  │  ├─ constrain.py
   │     │  │  │  ├─ containers.py
   │     │  │  │  ├─ control.py
   │     │  │  │  ├─ default_styles.py
   │     │  │  │  ├─ diagnose.py
   │     │  │  │  ├─ emoji.py
   │     │  │  │  ├─ errors.py
   │     │  │  │  ├─ filesize.py
   │     │  │  │  ├─ file_proxy.py
   │     │  │  │  ├─ highlighter.py
   │     │  │  │  ├─ json.py
   │     │  │  │  ├─ jupyter.py
   │     │  │  │  ├─ layout.py
   │     │  │  │  ├─ live.py
   │     │  │  │  ├─ live_render.py
   │     │  │  │  ├─ logging.py
   │     │  │  │  ├─ markup.py
   │     │  │  │  ├─ measure.py
   │     │  │  │  ├─ padding.py
   │     │  │  │  ├─ pager.py
   │     │  │  │  ├─ palette.py
   │     │  │  │  ├─ panel.py
   │     │  │  │  ├─ pretty.py
   │     │  │  │  ├─ progress.py
   │     │  │  │  ├─ progress_bar.py
   │     │  │  │  ├─ prompt.py
   │     │  │  │  ├─ protocol.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ region.py
   │     │  │  │  ├─ repr.py
   │     │  │  │  ├─ rule.py
   │     │  │  │  ├─ scope.py
   │     │  │  │  ├─ screen.py
   │     │  │  │  ├─ segment.py
   │     │  │  │  ├─ spinner.py
   │     │  │  │  ├─ status.py
   │     │  │  │  ├─ style.py
   │     │  │  │  ├─ styled.py
   │     │  │  │  ├─ syntax.py
   │     │  │  │  ├─ table.py
   │     │  │  │  ├─ terminal_theme.py
   │     │  │  │  ├─ text.py
   │     │  │  │  ├─ theme.py
   │     │  │  │  ├─ themes.py
   │     │  │  │  ├─ traceback.py
   │     │  │  │  ├─ tree.py
   │     │  │  │  ├─ _cell_widths.py
   │     │  │  │  ├─ _emoji_codes.py
   │     │  │  │  ├─ _emoji_replace.py
   │     │  │  │  ├─ _export_format.py
   │     │  │  │  ├─ _extension.py
   │     │  │  │  ├─ _fileno.py
   │     │  │  │  ├─ _inspect.py
   │     │  │  │  ├─ _log_render.py
   │     │  │  │  ├─ _loop.py
   │     │  │  │  ├─ _null_file.py
   │     │  │  │  ├─ _palettes.py
   │     │  │  │  ├─ _pick.py
   │     │  │  │  ├─ _ratio.py
   │     │  │  │  ├─ _spinners.py
   │     │  │  │  ├─ _stack.py
   │     │  │  │  ├─ _timer.py
   │     │  │  │  ├─ _win32_console.py
   │     │  │  │  ├─ _windows.py
   │     │  │  │  ├─ _windows_renderer.py
   │     │  │  │  ├─ _wrap.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ tomli
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ _parser.py
   │     │  │  │  ├─ _re.py
   │     │  │  │  ├─ _types.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ truststore
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ _api.py
   │     │  │  │  ├─ _macos.py
   │     │  │  │  ├─ _openssl.py
   │     │  │  │  ├─ _ssl_constants.py
   │     │  │  │  ├─ _windows.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ typing_extensions.py
   │     │  │  ├─ urllib3
   │     │  │  │  ├─ connection.py
   │     │  │  │  ├─ connectionpool.py
   │     │  │  │  ├─ contrib
   │     │  │  │  │  ├─ appengine.py
   │     │  │  │  │  ├─ ntlmpool.py
   │     │  │  │  │  ├─ pyopenssl.py
   │     │  │  │  │  ├─ securetransport.py
   │     │  │  │  │  ├─ socks.py
   │     │  │  │  │  ├─ _appengine_environ.py
   │     │  │  │  │  ├─ _securetransport
   │     │  │  │  │  │  ├─ bindings.py
   │     │  │  │  │  │  ├─ low_level.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ fields.py
   │     │  │  │  ├─ filepost.py
   │     │  │  │  ├─ packages
   │     │  │  │  │  ├─ backports
   │     │  │  │  │  │  ├─ makefile.py
   │     │  │  │  │  │  ├─ weakref_finalize.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ six.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ poolmanager.py
   │     │  │  │  ├─ request.py
   │     │  │  │  ├─ response.py
   │     │  │  │  ├─ util
   │     │  │  │  │  ├─ connection.py
   │     │  │  │  │  ├─ proxy.py
   │     │  │  │  │  ├─ queue.py
   │     │  │  │  │  ├─ request.py
   │     │  │  │  │  ├─ response.py
   │     │  │  │  │  ├─ retry.py
   │     │  │  │  │  ├─ ssltransport.py
   │     │  │  │  │  ├─ ssl_.py
   │     │  │  │  │  ├─ ssl_match_hostname.py
   │     │  │  │  │  ├─ timeout.py
   │     │  │  │  │  ├─ url.py
   │     │  │  │  │  ├─ wait.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _collections.py
   │     │  │  │  ├─ _version.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vendor.txt
   │     │  │  └─ __init__.py
   │     │  ├─ __init__.py
   │     │  ├─ __main__.py
   │     │  └─ __pip-runner__.py
   │     ├─ piper
   │     │  ├─ audio_playback.py
   │     │  ├─ config.py
   │     │  ├─ const.py
   │     │  ├─ download_voices.py
   │     │  ├─ espeak-ng-data
   │     │  │  ├─ af_dict
   │     │  │  ├─ am_dict
   │     │  │  ├─ an_dict
   │     │  │  ├─ ar_dict
   │     │  │  ├─ as_dict
   │     │  │  ├─ az_dict
   │     │  │  ├─ ba_dict
   │     │  │  ├─ be_dict
   │     │  │  ├─ bg_dict
   │     │  │  ├─ bn_dict
   │     │  │  ├─ bpy_dict
   │     │  │  ├─ bs_dict
   │     │  │  ├─ ca_dict
   │     │  │  ├─ chr_dict
   │     │  │  ├─ cmn_dict
   │     │  │  ├─ cs_dict
   │     │  │  ├─ cv_dict
   │     │  │  ├─ cy_dict
   │     │  │  ├─ da_dict
   │     │  │  ├─ de_dict
   │     │  │  ├─ el_dict
   │     │  │  ├─ en_dict
   │     │  │  ├─ eo_dict
   │     │  │  ├─ es_dict
   │     │  │  ├─ et_dict
   │     │  │  ├─ eu_dict
   │     │  │  ├─ fa_dict
   │     │  │  ├─ fi_dict
   │     │  │  ├─ fr_dict
   │     │  │  ├─ ga_dict
   │     │  │  ├─ gd_dict
   │     │  │  ├─ gn_dict
   │     │  │  ├─ grc_dict
   │     │  │  ├─ gu_dict
   │     │  │  ├─ hak_dict
   │     │  │  ├─ haw_dict
   │     │  │  ├─ he_dict
   │     │  │  ├─ hi_dict
   │     │  │  ├─ hr_dict
   │     │  │  ├─ ht_dict
   │     │  │  ├─ hu_dict
   │     │  │  ├─ hy_dict
   │     │  │  ├─ ia_dict
   │     │  │  ├─ id_dict
   │     │  │  ├─ intonations
   │     │  │  ├─ io_dict
   │     │  │  ├─ is_dict
   │     │  │  ├─ it_dict
   │     │  │  ├─ ja_dict
   │     │  │  ├─ jbo_dict
   │     │  │  ├─ ka_dict
   │     │  │  ├─ kk_dict
   │     │  │  ├─ kl_dict
   │     │  │  ├─ kn_dict
   │     │  │  ├─ kok_dict
   │     │  │  ├─ ko_dict
   │     │  │  ├─ ku_dict
   │     │  │  ├─ ky_dict
   │     │  │  ├─ lang
   │     │  │  │  ├─ aav
   │     │  │  │  │  ├─ vi
   │     │  │  │  │  ├─ vi-VN-x-central
   │     │  │  │  │  └─ vi-VN-x-south
   │     │  │  │  ├─ art
   │     │  │  │  │  ├─ eo
   │     │  │  │  │  ├─ ia
   │     │  │  │  │  ├─ io
   │     │  │  │  │  ├─ jbo
   │     │  │  │  │  ├─ lfn
   │     │  │  │  │  ├─ piqd
   │     │  │  │  │  ├─ py
   │     │  │  │  │  ├─ qdb
   │     │  │  │  │  ├─ qya
   │     │  │  │  │  ├─ sjn
   │     │  │  │  │  └─ xex
   │     │  │  │  ├─ azc
   │     │  │  │  │  └─ nci
   │     │  │  │  ├─ bat
   │     │  │  │  │  ├─ lt
   │     │  │  │  │  ├─ ltg
   │     │  │  │  │  └─ lv
   │     │  │  │  ├─ bnt
   │     │  │  │  │  ├─ sw
   │     │  │  │  │  └─ tn
   │     │  │  │  ├─ ccs
   │     │  │  │  │  └─ ka
   │     │  │  │  ├─ cel
   │     │  │  │  │  ├─ cy
   │     │  │  │  │  ├─ ga
   │     │  │  │  │  └─ gd
   │     │  │  │  ├─ cus
   │     │  │  │  │  └─ om
   │     │  │  │  ├─ dra
   │     │  │  │  │  ├─ kn
   │     │  │  │  │  ├─ ml
   │     │  │  │  │  ├─ ta
   │     │  │  │  │  └─ te
   │     │  │  │  ├─ esx
   │     │  │  │  │  └─ kl
   │     │  │  │  ├─ eu
   │     │  │  │  ├─ gmq
   │     │  │  │  │  ├─ da
   │     │  │  │  │  ├─ fo
   │     │  │  │  │  ├─ is
   │     │  │  │  │  ├─ nb
   │     │  │  │  │  └─ sv
   │     │  │  │  ├─ gmw
   │     │  │  │  │  ├─ af
   │     │  │  │  │  ├─ de
   │     │  │  │  │  ├─ en
   │     │  │  │  │  ├─ en-029
   │     │  │  │  │  ├─ en-GB-scotland
   │     │  │  │  │  ├─ en-GB-x-gbclan
   │     │  │  │  │  ├─ en-GB-x-gbcwmd
   │     │  │  │  │  ├─ en-GB-x-rp
   │     │  │  │  │  ├─ en-Shaw
   │     │  │  │  │  ├─ en-US
   │     │  │  │  │  ├─ en-US-nyc
   │     │  │  │  │  ├─ lb
   │     │  │  │  │  └─ nl
   │     │  │  │  ├─ grk
   │     │  │  │  │  ├─ el
   │     │  │  │  │  └─ grc
   │     │  │  │  ├─ inc
   │     │  │  │  │  ├─ as
   │     │  │  │  │  ├─ bn
   │     │  │  │  │  ├─ bpy
   │     │  │  │  │  ├─ gu
   │     │  │  │  │  ├─ hi
   │     │  │  │  │  ├─ kok
   │     │  │  │  │  ├─ mr
   │     │  │  │  │  ├─ ne
   │     │  │  │  │  ├─ or
   │     │  │  │  │  ├─ pa
   │     │  │  │  │  ├─ sd
   │     │  │  │  │  ├─ si
   │     │  │  │  │  └─ ur
   │     │  │  │  ├─ ine
   │     │  │  │  │  ├─ hy
   │     │  │  │  │  ├─ hyw
   │     │  │  │  │  └─ sq
   │     │  │  │  ├─ ira
   │     │  │  │  │  ├─ fa
   │     │  │  │  │  ├─ fa-Latn
   │     │  │  │  │  ├─ ku
   │     │  │  │  │  └─ ps
   │     │  │  │  ├─ iro
   │     │  │  │  │  └─ chr
   │     │  │  │  ├─ itc
   │     │  │  │  │  └─ la
   │     │  │  │  ├─ jpx
   │     │  │  │  │  └─ ja
   │     │  │  │  ├─ ko
   │     │  │  │  ├─ map
   │     │  │  │  │  └─ haw
   │     │  │  │  ├─ miz
   │     │  │  │  │  └─ mto
   │     │  │  │  ├─ myn
   │     │  │  │  │  └─ quc
   │     │  │  │  ├─ poz
   │     │  │  │  │  ├─ id
   │     │  │  │  │  ├─ mi
   │     │  │  │  │  └─ ms
   │     │  │  │  ├─ qu
   │     │  │  │  ├─ roa
   │     │  │  │  │  ├─ an
   │     │  │  │  │  ├─ ca
   │     │  │  │  │  ├─ ca-ba
   │     │  │  │  │  ├─ ca-nw
   │     │  │  │  │  ├─ ca-va
   │     │  │  │  │  ├─ es
   │     │  │  │  │  ├─ es-419
   │     │  │  │  │  ├─ fr
   │     │  │  │  │  ├─ fr-BE
   │     │  │  │  │  ├─ fr-CH
   │     │  │  │  │  ├─ ht
   │     │  │  │  │  ├─ it
   │     │  │  │  │  ├─ pap
   │     │  │  │  │  ├─ pt
   │     │  │  │  │  ├─ pt-BR
   │     │  │  │  │  └─ ro
   │     │  │  │  ├─ sai
   │     │  │  │  │  └─ gn
   │     │  │  │  ├─ sem
   │     │  │  │  │  ├─ am
   │     │  │  │  │  ├─ ar
   │     │  │  │  │  ├─ he
   │     │  │  │  │  ├─ mt
   │     │  │  │  │  └─ ti
   │     │  │  │  ├─ sit
   │     │  │  │  │  ├─ cmn
   │     │  │  │  │  ├─ cmn-Latn-pinyin
   │     │  │  │  │  ├─ hak
   │     │  │  │  │  ├─ my
   │     │  │  │  │  ├─ yue
   │     │  │  │  │  └─ yue-Latn-jyutping
   │     │  │  │  ├─ tai
   │     │  │  │  │  ├─ shn
   │     │  │  │  │  └─ th
   │     │  │  │  ├─ trk
   │     │  │  │  │  ├─ az
   │     │  │  │  │  ├─ ba
   │     │  │  │  │  ├─ cv
   │     │  │  │  │  ├─ kaa
   │     │  │  │  │  ├─ kk
   │     │  │  │  │  ├─ ky
   │     │  │  │  │  ├─ nog
   │     │  │  │  │  ├─ tk
   │     │  │  │  │  ├─ tr
   │     │  │  │  │  ├─ tt
   │     │  │  │  │  ├─ ug
   │     │  │  │  │  └─ uz
   │     │  │  │  ├─ urj
   │     │  │  │  │  ├─ et
   │     │  │  │  │  ├─ fi
   │     │  │  │  │  ├─ hu
   │     │  │  │  │  └─ smj
   │     │  │  │  ├─ zle
   │     │  │  │  │  ├─ be
   │     │  │  │  │  ├─ ru
   │     │  │  │  │  ├─ ru-cl
   │     │  │  │  │  ├─ ru-LV
   │     │  │  │  │  └─ uk
   │     │  │  │  ├─ zls
   │     │  │  │  │  ├─ bg
   │     │  │  │  │  ├─ bs
   │     │  │  │  │  ├─ hr
   │     │  │  │  │  ├─ mk
   │     │  │  │  │  ├─ sl
   │     │  │  │  │  └─ sr
   │     │  │  │  └─ zlw
   │     │  │  │     ├─ cs
   │     │  │  │     ├─ pl
   │     │  │  │     └─ sk
   │     │  │  ├─ la_dict
   │     │  │  ├─ lb_dict
   │     │  │  ├─ lfn_dict
   │     │  │  ├─ lt_dict
   │     │  │  ├─ lv_dict
   │     │  │  ├─ mi_dict
   │     │  │  ├─ mk_dict
   │     │  │  ├─ ml_dict
   │     │  │  ├─ mr_dict
   │     │  │  ├─ ms_dict
   │     │  │  ├─ mto_dict
   │     │  │  ├─ mt_dict
   │     │  │  ├─ my_dict
   │     │  │  ├─ nci_dict
   │     │  │  ├─ ne_dict
   │     │  │  ├─ nl_dict
   │     │  │  ├─ nog_dict
   │     │  │  ├─ no_dict
   │     │  │  ├─ om_dict
   │     │  │  ├─ or_dict
   │     │  │  ├─ pap_dict
   │     │  │  ├─ pa_dict
   │     │  │  ├─ phondata
   │     │  │  ├─ phondata-manifest
   │     │  │  ├─ phonindex
   │     │  │  ├─ phontab
   │     │  │  ├─ piqd_dict
   │     │  │  ├─ pl_dict
   │     │  │  ├─ pt_dict
   │     │  │  ├─ py_dict
   │     │  │  ├─ qdb_dict
   │     │  │  ├─ quc_dict
   │     │  │  ├─ qu_dict
   │     │  │  ├─ qya_dict
   │     │  │  ├─ ro_dict
   │     │  │  ├─ ru_dict
   │     │  │  ├─ sd_dict
   │     │  │  ├─ shn_dict
   │     │  │  ├─ si_dict
   │     │  │  ├─ sjn_dict
   │     │  │  ├─ sk_dict
   │     │  │  ├─ sl_dict
   │     │  │  ├─ smj_dict
   │     │  │  ├─ sq_dict
   │     │  │  ├─ sr_dict
   │     │  │  ├─ sv_dict
   │     │  │  ├─ sw_dict
   │     │  │  ├─ ta_dict
   │     │  │  ├─ te_dict
   │     │  │  ├─ th_dict
   │     │  │  ├─ ti_dict
   │     │  │  ├─ tk_dict
   │     │  │  ├─ tn_dict
   │     │  │  ├─ tr_dict
   │     │  │  ├─ tt_dict
   │     │  │  ├─ ug_dict
   │     │  │  ├─ uk_dict
   │     │  │  ├─ ur_dict
   │     │  │  ├─ uz_dict
   │     │  │  ├─ vi_dict
   │     │  │  ├─ voices
   │     │  │  │  └─ !v
   │     │  │  │     ├─ adam
   │     │  │  │     ├─ Alex
   │     │  │  │     ├─ Alicia
   │     │  │  │     ├─ Andrea
   │     │  │  │     ├─ Andy
   │     │  │  │     ├─ anika
   │     │  │  │     ├─ anikaRobot
   │     │  │  │     ├─ Annie
   │     │  │  │     ├─ announcer
   │     │  │  │     ├─ antonio
   │     │  │  │     ├─ AnxiousAndy
   │     │  │  │     ├─ aunty
   │     │  │  │     ├─ belinda
   │     │  │  │     ├─ benjamin
   │     │  │  │     ├─ boris
   │     │  │  │     ├─ caleb
   │     │  │  │     ├─ croak
   │     │  │  │     ├─ david
   │     │  │  │     ├─ Demonic
   │     │  │  │     ├─ Denis
   │     │  │  │     ├─ Diogo
   │     │  │  │     ├─ ed
   │     │  │  │     ├─ edward
   │     │  │  │     ├─ edward2
   │     │  │  │     ├─ f1
   │     │  │  │     ├─ f2
   │     │  │  │     ├─ f3
   │     │  │  │     ├─ f4
   │     │  │  │     ├─ f5
   │     │  │  │     ├─ fast
   │     │  │  │     ├─ Gene
   │     │  │  │     ├─ Gene2
   │     │  │  │     ├─ grandma
   │     │  │  │     ├─ grandpa
   │     │  │  │     ├─ gustave
   │     │  │  │     ├─ Henrique
   │     │  │  │     ├─ Hugo
   │     │  │  │     ├─ ian
   │     │  │  │     ├─ iven
   │     │  │  │     ├─ iven2
   │     │  │  │     ├─ iven3
   │     │  │  │     ├─ iven4
   │     │  │  │     ├─ Jacky
   │     │  │  │     ├─ john
   │     │  │  │     ├─ kaukovalta
   │     │  │  │     ├─ klatt
   │     │  │  │     ├─ klatt2
   │     │  │  │     ├─ klatt3
   │     │  │  │     ├─ klatt4
   │     │  │  │     ├─ klatt5
   │     │  │  │     ├─ klatt6
   │     │  │  │     ├─ Lee
   │     │  │  │     ├─ linda
   │     │  │  │     ├─ m1
   │     │  │  │     ├─ m2
   │     │  │  │     ├─ m3
   │     │  │  │     ├─ m4
   │     │  │  │     ├─ m5
   │     │  │  │     ├─ m6
   │     │  │  │     ├─ m7
   │     │  │  │     ├─ m8
   │     │  │  │     ├─ marcelo
   │     │  │  │     ├─ Marco
   │     │  │  │     ├─ Mario
   │     │  │  │     ├─ max
   │     │  │  │     ├─ Michael
   │     │  │  │     ├─ michel
   │     │  │  │     ├─ miguel
   │     │  │  │     ├─ Mike
   │     │  │  │     ├─ mike2
   │     │  │  │     ├─ Mr serious
   │     │  │  │     ├─ Nguyen
   │     │  │  │     ├─ norbert
   │     │  │  │     ├─ pablo
   │     │  │  │     ├─ paul
   │     │  │  │     ├─ pedro
   │     │  │  │     ├─ quincy
   │     │  │  │     ├─ Reed
   │     │  │  │     ├─ RicishayMax
   │     │  │  │     ├─ RicishayMax2
   │     │  │  │     ├─ RicishayMax3
   │     │  │  │     ├─ rob
   │     │  │  │     ├─ robert
   │     │  │  │     ├─ robosoft
   │     │  │  │     ├─ robosoft2
   │     │  │  │     ├─ robosoft3
   │     │  │  │     ├─ robosoft4
   │     │  │  │     ├─ robosoft5
   │     │  │  │     ├─ robosoft6
   │     │  │  │     ├─ robosoft7
   │     │  │  │     ├─ robosoft8
   │     │  │  │     ├─ sandro
   │     │  │  │     ├─ shelby
   │     │  │  │     ├─ steph
   │     │  │  │     ├─ steph2
   │     │  │  │     ├─ steph3
   │     │  │  │     ├─ Storm
   │     │  │  │     ├─ travis
   │     │  │  │     ├─ Tweaky
   │     │  │  │     ├─ UniRobot
   │     │  │  │     ├─ victor
   │     │  │  │     ├─ whisper
   │     │  │  │     ├─ whisperf
   │     │  │  │     └─ zac
   │     │  │  └─ yue_dict
   │     │  ├─ espeakbridge.pyd
   │     │  ├─ espeakbridge.pyi
   │     │  ├─ http_server.py
   │     │  ├─ patch_voice_with_alignment.py
   │     │  ├─ phoneme_ids.py
   │     │  ├─ phonemize_chinese.py
   │     │  ├─ phonemize_espeak.py
   │     │  ├─ py.typed
   │     │  ├─ tashkeel
   │     │  │  ├─ hint_id_map.json
   │     │  │  ├─ input_id_map.json
   │     │  │  ├─ model.onnx
   │     │  │  ├─ target_id_map.json
   │     │  │  └─ __init__.py
   │     │  ├─ train
   │     │  │  ├─ export_generator.py
   │     │  │  ├─ export_onnx.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ voice.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ playwright
   │     │  ├─ async_api
   │     │  │  ├─ _context_manager.py
   │     │  │  ├─ _generated.py
   │     │  │  └─ __init__.py
   │     │  ├─ driver
   │     │  │  ├─ LICENSE
   │     │  │  ├─ node.exe
   │     │  │  ├─ package
   │     │  │  │  ├─ api.json
   │     │  │  │  ├─ bin
   │     │  │  │  │  ├─ install_media_pack.ps1
   │     │  │  │  │  ├─ install_webkit_wsl.ps1
   │     │  │  │  │  ├─ reinstall_chrome_beta_linux.sh
   │     │  │  │  │  ├─ reinstall_chrome_beta_mac.sh
   │     │  │  │  │  ├─ reinstall_chrome_beta_win.ps1
   │     │  │  │  │  ├─ reinstall_chrome_stable_linux.sh
   │     │  │  │  │  ├─ reinstall_chrome_stable_mac.sh
   │     │  │  │  │  ├─ reinstall_chrome_stable_win.ps1
   │     │  │  │  │  ├─ reinstall_msedge_beta_linux.sh
   │     │  │  │  │  ├─ reinstall_msedge_beta_mac.sh
   │     │  │  │  │  ├─ reinstall_msedge_beta_win.ps1
   │     │  │  │  │  ├─ reinstall_msedge_dev_linux.sh
   │     │  │  │  │  ├─ reinstall_msedge_dev_mac.sh
   │     │  │  │  │  ├─ reinstall_msedge_dev_win.ps1
   │     │  │  │  │  ├─ reinstall_msedge_stable_linux.sh
   │     │  │  │  │  ├─ reinstall_msedge_stable_mac.sh
   │     │  │  │  │  └─ reinstall_msedge_stable_win.ps1
   │     │  │  │  ├─ browsers.json
   │     │  │  │  ├─ cli.js
   │     │  │  │  ├─ index.d.ts
   │     │  │  │  ├─ index.js
   │     │  │  │  ├─ index.mjs
   │     │  │  │  ├─ lib
   │     │  │  │  │  ├─ bootstrap.js
   │     │  │  │  │  ├─ coreBundle.js
   │     │  │  │  │  ├─ entry
   │     │  │  │  │  │  ├─ cliDaemon.js
   │     │  │  │  │  │  ├─ dashboardApp.js
   │     │  │  │  │  │  ├─ mcp.js
   │     │  │  │  │  │  └─ oopBrowserDownload.js
   │     │  │  │  │  ├─ package.js
   │     │  │  │  │  ├─ server
   │     │  │  │  │  │  ├─ chromium
   │     │  │  │  │  │  ├─ deviceDescriptorsSource.json
   │     │  │  │  │  │  └─ electron
   │     │  │  │  │  │     └─ loader.js
   │     │  │  │  │  ├─ serverRegistry.js
   │     │  │  │  │  ├─ serverRegistry.js.LICENSE
   │     │  │  │  │  ├─ tools
   │     │  │  │  │  │  ├─ cli-client
   │     │  │  │  │  │  │  ├─ channelSessions.js
   │     │  │  │  │  │  │  ├─ cli.js
   │     │  │  │  │  │  │  ├─ help.json
   │     │  │  │  │  │  │  ├─ minimist.js
   │     │  │  │  │  │  │  ├─ output.js
   │     │  │  │  │  │  │  ├─ program.js
   │     │  │  │  │  │  │  ├─ registry.js
   │     │  │  │  │  │  │  ├─ session.js
   │     │  │  │  │  │  │  └─ skill
   │     │  │  │  │  │  │     ├─ references
   │     │  │  │  │  │  │     │  ├─ element-attributes.md
   │     │  │  │  │  │  │     │  ├─ playwright-tests.md
   │     │  │  │  │  │  │     │  ├─ request-mocking.md
   │     │  │  │  │  │  │     │  ├─ running-code.md
   │     │  │  │  │  │  │     │  ├─ session-management.md
   │     │  │  │  │  │  │     │  ├─ spec-driven-testing.md
   │     │  │  │  │  │  │     │  ├─ storage-state.md
   │     │  │  │  │  │  │     │  ├─ test-generation.md
   │     │  │  │  │  │  │     │  ├─ tracing.md
   │     │  │  │  │  │  │     │  └─ video-recording.md
   │     │  │  │  │  │  │     └─ SKILL.md
   │     │  │  │  │  │  ├─ dashboard
   │     │  │  │  │  │  ├─ trace
   │     │  │  │  │  │  │  └─ SKILL.md
   │     │  │  │  │  │  └─ utils
   │     │  │  │  │  │     ├─ extension.js
   │     │  │  │  │  │     └─ socketConnection.js
   │     │  │  │  │  ├─ utilsBundle.js
   │     │  │  │  │  ├─ utilsBundle.js.LICENSE
   │     │  │  │  │  ├─ vite
   │     │  │  │  │  │  ├─ dashboard
   │     │  │  │  │  │  │  ├─ assets
   │     │  │  │  │  │  │  │  ├─ codicon-DCmgc-ay.ttf
   │     │  │  │  │  │  │  │  ├─ firefox-1bWoP6pv.svg
   │     │  │  │  │  │  │  │  ├─ firefox-beta-k3eOH_eK.svg
   │     │  │  │  │  │  │  │  ├─ firefox-nightly-Cp5nfeDT.svg
   │     │  │  │  │  │  │  │  ├─ index-BY2S1tHT.css
   │     │  │  │  │  │  │  │  ├─ index-DpEq2p62.js
   │     │  │  │  │  │  │  │  └─ safari-na3_-uQk.svg
   │     │  │  │  │  │  │  ├─ index.html
   │     │  │  │  │  │  │  └─ playwright-logo.svg
   │     │  │  │  │  │  ├─ htmlReport
   │     │  │  │  │  │  │  ├─ index.html
   │     │  │  │  │  │  │  ├─ report.css
   │     │  │  │  │  │  │  └─ report.js
   │     │  │  │  │  │  ├─ recorder
   │     │  │  │  │  │  │  ├─ assets
   │     │  │  │  │  │  │  │  ├─ codeMirrorModule-BHYmBp6h.js
   │     │  │  │  │  │  │  │  ├─ codeMirrorModule-DYBRYzYX.css
   │     │  │  │  │  │  │  │  ├─ codicon-DCmgc-ay.ttf
   │     │  │  │  │  │  │  │  ├─ index-4ZiSSCmn.css
   │     │  │  │  │  │  │  │  └─ index-DA10QRaq.js
   │     │  │  │  │  │  │  ├─ index.html
   │     │  │  │  │  │  │  └─ playwright-logo.svg
   │     │  │  │  │  │  └─ traceViewer
   │     │  │  │  │  │     ├─ assets
   │     │  │  │  │  │     │  ├─ codeMirrorModule-Ds_H_9Yq.js
   │     │  │  │  │  │     │  ├─ defaultSettingsView-D31xz8zv.js
   │     │  │  │  │  │     │  ├─ urlMatch-BYQrIQwR.js
   │     │  │  │  │  │     │  └─ xtermModule-CsJ4vdCR.js
   │     │  │  │  │  │     ├─ codeMirrorModule.DYBRYzYX.css
   │     │  │  │  │  │     ├─ codicon.DCmgc-ay.ttf
   │     │  │  │  │  │     ├─ defaultSettingsView.BDKsFU3c.css
   │     │  │  │  │  │     ├─ index.BCnMPevh.js
   │     │  │  │  │  │     ├─ index.CzXZzn5A.css
   │     │  │  │  │  │     ├─ index.html
   │     │  │  │  │  │     ├─ manifest.webmanifest
   │     │  │  │  │  │     ├─ playwright-logo.svg
   │     │  │  │  │  │     ├─ snapshot.html
   │     │  │  │  │  │     ├─ snapshot.v8KI4P3m.js
   │     │  │  │  │  │     ├─ sw.bundle.js
   │     │  │  │  │  │     ├─ uiMode.Btcz36p_.css
   │     │  │  │  │  │     ├─ uiMode.C2Efnu2P.js
   │     │  │  │  │  │     ├─ uiMode.html
   │     │  │  │  │  │     └─ xtermModule.DYP7pi_n.css
   │     │  │  │  │  └─ xdg-open
   │     │  │  │  ├─ LICENSE
   │     │  │  │  ├─ NOTICE
   │     │  │  │  ├─ package.json
   │     │  │  │  ├─ protocol.yml
   │     │  │  │  ├─ README.md
   │     │  │  │  ├─ ThirdPartyNotices.txt
   │     │  │  │  └─ types
   │     │  │  │     ├─ protocol.d.ts
   │     │  │  │     ├─ structs.d.ts
   │     │  │  │     └─ types.d.ts
   │     │  │  └─ README.md
   │     │  ├─ py.typed
   │     │  ├─ sync_api
   │     │  │  ├─ _context_manager.py
   │     │  │  ├─ _generated.py
   │     │  │  └─ __init__.py
   │     │  ├─ _impl
   │     │  │  ├─ _api_structures.py
   │     │  │  ├─ _artifact.py
   │     │  │  ├─ _assertions.py
   │     │  │  ├─ _async_base.py
   │     │  │  ├─ _browser.py
   │     │  │  ├─ _browser_context.py
   │     │  │  ├─ _browser_type.py
   │     │  │  ├─ _cdp_session.py
   │     │  │  ├─ _clock.py
   │     │  │  ├─ _connection.py
   │     │  │  ├─ _console_message.py
   │     │  │  ├─ _debugger.py
   │     │  │  ├─ _dialog.py
   │     │  │  ├─ _disposable.py
   │     │  │  ├─ _download.py
   │     │  │  ├─ _driver.py
   │     │  │  ├─ _element_handle.py
   │     │  │  ├─ _errors.py
   │     │  │  ├─ _event_context_manager.py
   │     │  │  ├─ _fetch.py
   │     │  │  ├─ _file_chooser.py
   │     │  │  ├─ _form_data.py
   │     │  │  ├─ _frame.py
   │     │  │  ├─ _glob.py
   │     │  │  ├─ _greenlets.py
   │     │  │  ├─ _har_router.py
   │     │  │  ├─ _helper.py
   │     │  │  ├─ _impl_to_api_mapping.py
   │     │  │  ├─ _input.py
   │     │  │  ├─ _json_pipe.py
   │     │  │  ├─ _js_handle.py
   │     │  │  ├─ _local_utils.py
   │     │  │  ├─ _locator.py
   │     │  │  ├─ _map.py
   │     │  │  ├─ _network.py
   │     │  │  ├─ _object_factory.py
   │     │  │  ├─ _page.py
   │     │  │  ├─ _path_utils.py
   │     │  │  ├─ _playwright.py
   │     │  │  ├─ _screencast.py
   │     │  │  ├─ _selectors.py
   │     │  │  ├─ _set_input_files_helpers.py
   │     │  │  ├─ _stream.py
   │     │  │  ├─ _str_utils.py
   │     │  │  ├─ _sync_base.py
   │     │  │  ├─ _tracing.py
   │     │  │  ├─ _transport.py
   │     │  │  ├─ _video.py
   │     │  │  ├─ _waiter.py
   │     │  │  ├─ _web_error.py
   │     │  │  ├─ _writable_stream.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __pyinstaller
   │     │  │     ├─ hook-playwright.async_api.py
   │     │  │     ├─ hook-playwright.sync_api.py
   │     │  │     └─ __init__.py
   │     │  ├─ _repo_version.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ primp
   │     │  ├─ primp.pyd
   │     │  ├─ py.typed
   │     │  ├─ __init__.py
   │     │  └─ __init__.pyi
   │     ├─ proto
   │     │  ├─ datetime_helpers.py
   │     │  ├─ enums.py
   │     │  ├─ fields.py
   │     │  ├─ marshal
   │     │  │  ├─ collections
   │     │  │  │  ├─ maps.py
   │     │  │  │  ├─ repeated.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ compat.py
   │     │  │  ├─ marshal.py
   │     │  │  ├─ rules
   │     │  │  │  ├─ bytes.py
   │     │  │  │  ├─ dates.py
   │     │  │  │  ├─ enums.py
   │     │  │  │  ├─ field_mask.py
   │     │  │  │  ├─ message.py
   │     │  │  │  ├─ stringy_numbers.py
   │     │  │  │  ├─ struct.py
   │     │  │  │  ├─ wrappers.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ message.py
   │     │  ├─ modules.py
   │     │  ├─ primitives.py
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ _file_info.py
   │     │  ├─ _package_info.py
   │     │  └─ __init__.py
   │     ├─ pyasn1
   │     │  ├─ codec
   │     │  │  ├─ ber
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  ├─ eoo.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cer
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ der
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ native
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ streaming.py
   │     │  │  └─ __init__.py
   │     │  ├─ compat
   │     │  │  ├─ integer.py
   │     │  │  └─ __init__.py
   │     │  ├─ debug.py
   │     │  ├─ error.py
   │     │  ├─ type
   │     │  │  ├─ base.py
   │     │  │  ├─ char.py
   │     │  │  ├─ constraint.py
   │     │  │  ├─ error.py
   │     │  │  ├─ namedtype.py
   │     │  │  ├─ namedval.py
   │     │  │  ├─ opentype.py
   │     │  │  ├─ tag.py
   │     │  │  ├─ tagmap.py
   │     │  │  ├─ univ.py
   │     │  │  ├─ useful.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ pyasn1_modules
   │     │  ├─ pem.py
   │     │  ├─ rfc1155.py
   │     │  ├─ rfc1157.py
   │     │  ├─ rfc1901.py
   │     │  ├─ rfc1902.py
   │     │  ├─ rfc1905.py
   │     │  ├─ rfc2251.py
   │     │  ├─ rfc2314.py
   │     │  ├─ rfc2315.py
   │     │  ├─ rfc2437.py
   │     │  ├─ rfc2459.py
   │     │  ├─ rfc2511.py
   │     │  ├─ rfc2560.py
   │     │  ├─ rfc2631.py
   │     │  ├─ rfc2634.py
   │     │  ├─ rfc2876.py
   │     │  ├─ rfc2985.py
   │     │  ├─ rfc2986.py
   │     │  ├─ rfc3058.py
   │     │  ├─ rfc3114.py
   │     │  ├─ rfc3125.py
   │     │  ├─ rfc3161.py
   │     │  ├─ rfc3274.py
   │     │  ├─ rfc3279.py
   │     │  ├─ rfc3280.py
   │     │  ├─ rfc3281.py
   │     │  ├─ rfc3370.py
   │     │  ├─ rfc3412.py
   │     │  ├─ rfc3414.py
   │     │  ├─ rfc3447.py
   │     │  ├─ rfc3537.py
   │     │  ├─ rfc3560.py
   │     │  ├─ rfc3565.py
   │     │  ├─ rfc3657.py
   │     │  ├─ rfc3709.py
   │     │  ├─ rfc3739.py
   │     │  ├─ rfc3770.py
   │     │  ├─ rfc3779.py
   │     │  ├─ rfc3820.py
   │     │  ├─ rfc3852.py
   │     │  ├─ rfc4010.py
   │     │  ├─ rfc4043.py
   │     │  ├─ rfc4055.py
   │     │  ├─ rfc4073.py
   │     │  ├─ rfc4108.py
   │     │  ├─ rfc4210.py
   │     │  ├─ rfc4211.py
   │     │  ├─ rfc4334.py
   │     │  ├─ rfc4357.py
   │     │  ├─ rfc4387.py
   │     │  ├─ rfc4476.py
   │     │  ├─ rfc4490.py
   │     │  ├─ rfc4491.py
   │     │  ├─ rfc4683.py
   │     │  ├─ rfc4985.py
   │     │  ├─ rfc5035.py
   │     │  ├─ rfc5083.py
   │     │  ├─ rfc5084.py
   │     │  ├─ rfc5126.py
   │     │  ├─ rfc5208.py
   │     │  ├─ rfc5275.py
   │     │  ├─ rfc5280.py
   │     │  ├─ rfc5480.py
   │     │  ├─ rfc5636.py
   │     │  ├─ rfc5639.py
   │     │  ├─ rfc5649.py
   │     │  ├─ rfc5652.py
   │     │  ├─ rfc5697.py
   │     │  ├─ rfc5751.py
   │     │  ├─ rfc5752.py
   │     │  ├─ rfc5753.py
   │     │  ├─ rfc5755.py
   │     │  ├─ rfc5913.py
   │     │  ├─ rfc5914.py
   │     │  ├─ rfc5915.py
   │     │  ├─ rfc5916.py
   │     │  ├─ rfc5917.py
   │     │  ├─ rfc5924.py
   │     │  ├─ rfc5934.py
   │     │  ├─ rfc5940.py
   │     │  ├─ rfc5958.py
   │     │  ├─ rfc5990.py
   │     │  ├─ rfc6010.py
   │     │  ├─ rfc6019.py
   │     │  ├─ rfc6031.py
   │     │  ├─ rfc6032.py
   │     │  ├─ rfc6120.py
   │     │  ├─ rfc6170.py
   │     │  ├─ rfc6187.py
   │     │  ├─ rfc6210.py
   │     │  ├─ rfc6211.py
   │     │  ├─ rfc6402.py
   │     │  ├─ rfc6482.py
   │     │  ├─ rfc6486.py
   │     │  ├─ rfc6487.py
   │     │  ├─ rfc6664.py
   │     │  ├─ rfc6955.py
   │     │  ├─ rfc6960.py
   │     │  ├─ rfc7030.py
   │     │  ├─ rfc7191.py
   │     │  ├─ rfc7229.py
   │     │  ├─ rfc7292.py
   │     │  ├─ rfc7296.py
   │     │  ├─ rfc7508.py
   │     │  ├─ rfc7585.py
   │     │  ├─ rfc7633.py
   │     │  ├─ rfc7773.py
   │     │  ├─ rfc7894.py
   │     │  ├─ rfc7906.py
   │     │  ├─ rfc7914.py
   │     │  ├─ rfc8017.py
   │     │  ├─ rfc8018.py
   │     │  ├─ rfc8103.py
   │     │  ├─ rfc8209.py
   │     │  ├─ rfc8226.py
   │     │  ├─ rfc8358.py
   │     │  ├─ rfc8360.py
   │     │  ├─ rfc8398.py
   │     │  ├─ rfc8410.py
   │     │  ├─ rfc8418.py
   │     │  ├─ rfc8419.py
   │     │  ├─ rfc8479.py
   │     │  ├─ rfc8494.py
   │     │  ├─ rfc8520.py
   │     │  ├─ rfc8619.py
   │     │  ├─ rfc8649.py
   │     │  ├─ rfc8692.py
   │     │  ├─ rfc8696.py
   │     │  ├─ rfc8702.py
   │     │  ├─ rfc8708.py
   │     │  ├─ rfc8769.py
   │     │  └─ __init__.py
   │     ├─ pyaudio
   │     │  ├─ _portaudio.cp313-win_amd64.pyd
   │     │  └─ __init__.py
   │     ├─ pyautogui
   │     │  ├─ _pyautogui_java.py
   │     │  ├─ _pyautogui_osx.py
   │     │  ├─ _pyautogui_win.py
   │     │  ├─ _pyautogui_x11.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ pycparser
   │     │  ├─ ast_transforms.py
   │     │  ├─ c_ast.py
   │     │  ├─ c_generator.py
   │     │  ├─ c_lexer.py
   │     │  ├─ c_parser.py
   │     │  ├─ _ast_gen.py
   │     │  ├─ _c_ast.cfg
   │     │  └─ __init__.py
   │     ├─ pydantic
   │     │  ├─ aliases.py
   │     │  ├─ alias_generators.py
   │     │  ├─ annotated_handlers.py
   │     │  ├─ class_validators.py
   │     │  ├─ color.py
   │     │  ├─ config.py
   │     │  ├─ dataclasses.py
   │     │  ├─ datetime_parse.py
   │     │  ├─ decorator.py
   │     │  ├─ deprecated
   │     │  │  ├─ class_validators.py
   │     │  │  ├─ config.py
   │     │  │  ├─ copy_internals.py
   │     │  │  ├─ decorator.py
   │     │  │  ├─ json.py
   │     │  │  ├─ parse.py
   │     │  │  ├─ tools.py
   │     │  │  └─ __init__.py
   │     │  ├─ env_settings.py
   │     │  ├─ errors.py
   │     │  ├─ error_wrappers.py
   │     │  ├─ experimental
   │     │  │  ├─ arguments_schema.py
   │     │  │  ├─ missing_sentinel.py
   │     │  │  ├─ pipeline.py
   │     │  │  └─ __init__.py
   │     │  ├─ fields.py
   │     │  ├─ functional_serializers.py
   │     │  ├─ functional_validators.py
   │     │  ├─ generics.py
   │     │  ├─ json.py
   │     │  ├─ json_schema.py
   │     │  ├─ main.py
   │     │  ├─ mypy.py
   │     │  ├─ networks.py
   │     │  ├─ parse.py
   │     │  ├─ plugin
   │     │  │  ├─ _loader.py
   │     │  │  ├─ _schema_validator.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ root_model.py
   │     │  ├─ schema.py
   │     │  ├─ tools.py
   │     │  ├─ types.py
   │     │  ├─ type_adapter.py
   │     │  ├─ typing.py
   │     │  ├─ utils.py
   │     │  ├─ v1
   │     │  │  ├─ annotated_types.py
   │     │  │  ├─ class_validators.py
   │     │  │  ├─ color.py
   │     │  │  ├─ config.py
   │     │  │  ├─ dataclasses.py
   │     │  │  ├─ datetime_parse.py
   │     │  │  ├─ decorator.py
   │     │  │  ├─ env_settings.py
   │     │  │  ├─ errors.py
   │     │  │  ├─ error_wrappers.py
   │     │  │  ├─ fields.py
   │     │  │  ├─ generics.py
   │     │  │  ├─ json.py
   │     │  │  ├─ main.py
   │     │  │  ├─ mypy.py
   │     │  │  ├─ networks.py
   │     │  │  ├─ parse.py
   │     │  │  ├─ py.typed
   │     │  │  ├─ schema.py
   │     │  │  ├─ tools.py
   │     │  │  ├─ types.py
   │     │  │  ├─ typing.py
   │     │  │  ├─ utils.py
   │     │  │  ├─ validators.py
   │     │  │  ├─ version.py
   │     │  │  ├─ _hypothesis_plugin.py
   │     │  │  └─ __init__.py
   │     │  ├─ validate_call_decorator.py
   │     │  ├─ validators.py
   │     │  ├─ version.py
   │     │  ├─ warnings.py
   │     │  ├─ _internal
   │     │  │  ├─ _config.py
   │     │  │  ├─ _core_metadata.py
   │     │  │  ├─ _core_utils.py
   │     │  │  ├─ _dataclasses.py
   │     │  │  ├─ _decorators.py
   │     │  │  ├─ _decorators_v1.py
   │     │  │  ├─ _discriminated_union.py
   │     │  │  ├─ _docs_extraction.py
   │     │  │  ├─ _fields.py
   │     │  │  ├─ _forward_ref.py
   │     │  │  ├─ _generate_schema.py
   │     │  │  ├─ _generics.py
   │     │  │  ├─ _git.py
   │     │  │  ├─ _import_utils.py
   │     │  │  ├─ _internal_dataclass.py
   │     │  │  ├─ _known_annotated_metadata.py
   │     │  │  ├─ _mock_val_ser.py
   │     │  │  ├─ _model_construction.py
   │     │  │  ├─ _namespace_utils.py
   │     │  │  ├─ _repr.py
   │     │  │  ├─ _schema_gather.py
   │     │  │  ├─ _schema_generation_shared.py
   │     │  │  ├─ _serializers.py
   │     │  │  ├─ _signature.py
   │     │  │  ├─ _typing_extra.py
   │     │  │  ├─ _utils.py
   │     │  │  ├─ _validate_call.py
   │     │  │  ├─ _validators.py
   │     │  │  └─ __init__.py
   │     │  ├─ _migration.py
   │     │  └─ __init__.py
   │     ├─ pydantic_core
   │     │  ├─ core_schema.py
   │     │  ├─ py.typed
   │     │  ├─ _pydantic_core.cp313-win_amd64.pyd
   │     │  ├─ _pydantic_core.pyi
   │     │  └─ __init__.py
   │     ├─ pyee
   │     │  ├─ asyncio.py
   │     │  ├─ base.py
   │     │  ├─ cls.py
   │     │  ├─ executor.py
   │     │  ├─ py.typed
   │     │  ├─ trio.py
   │     │  ├─ twisted.py
   │     │  ├─ uplift.py
   │     │  └─ __init__.py
   │     ├─ pygetwindow
   │     │  ├─ _pygetwindow_macos.py
   │     │  ├─ _pygetwindow_win.py
   │     │  └─ __init__.py
   │     ├─ pymsgbox
   │     │  ├─ _native_win.py
   │     │  └─ __init__.py
   │     ├─ pyparsing
   │     │  ├─ actions.py
   │     │  ├─ ai
   │     │  │  ├─ best_practices.md
   │     │  │  ├─ show_best_practices
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  └─ __init__.py
   │     │  ├─ common.py
   │     │  ├─ core.py
   │     │  ├─ diagram
   │     │  │  └─ __init__.py
   │     │  ├─ exceptions.py
   │     │  ├─ helpers.py
   │     │  ├─ py.typed
   │     │  ├─ results.py
   │     │  ├─ testing.py
   │     │  ├─ tools
   │     │  │  ├─ cvt_pyparsing_pep8_names.py
   │     │  │  └─ __init__.py
   │     │  ├─ unicode.py
   │     │  ├─ util.py
   │     │  ├─ warnings.py
   │     │  └─ __init__.py
   │     ├─ pyperclip
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ pyrect
   │     │  └─ __init__.py
   │     ├─ pyscreeze
   │     │  └─ __init__.py
   │     ├─ pythoncom.py
   │     ├─ pythonwin
   │     │  ├─ dde.pyd
   │     │  ├─ license.txt
   │     │  ├─ mfc140u.dll
   │     │  ├─ Pythonwin.exe
   │     │  ├─ pywin
   │     │  │  ├─ debugger
   │     │  │  │  ├─ configui.py
   │     │  │  │  ├─ dbgcon.py
   │     │  │  │  ├─ dbgpyapp.py
   │     │  │  │  ├─ debugger.py
   │     │  │  │  ├─ fail.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ default.cfg
   │     │  │  ├─ Demos
   │     │  │  │  ├─ app
   │     │  │  │  │  ├─ basictimerapp.py
   │     │  │  │  │  ├─ customprint.py
   │     │  │  │  │  ├─ demoutils.py
   │     │  │  │  │  ├─ dlgappdemo.py
   │     │  │  │  │  ├─ dojobapp.py
   │     │  │  │  │  └─ helloapp.py
   │     │  │  │  ├─ cmdserver.py
   │     │  │  │  ├─ createwin.py
   │     │  │  │  ├─ demoutils.py
   │     │  │  │  ├─ dibdemo.py
   │     │  │  │  ├─ dlgtest.py
   │     │  │  │  ├─ dyndlg.py
   │     │  │  │  ├─ fontdemo.py
   │     │  │  │  ├─ guidemo.py
   │     │  │  │  ├─ hiertest.py
   │     │  │  │  ├─ menutest.py
   │     │  │  │  ├─ objdoc.py
   │     │  │  │  ├─ ocx
   │     │  │  │  │  ├─ demoutils.py
   │     │  │  │  │  ├─ flash.py
   │     │  │  │  │  ├─ msoffice.py
   │     │  │  │  │  ├─ ocxserialtest.py
   │     │  │  │  │  ├─ ocxtest.py
   │     │  │  │  │  └─ webbrowser.py
   │     │  │  │  ├─ openGLDemo.py
   │     │  │  │  ├─ progressbar.py
   │     │  │  │  ├─ sliderdemo.py
   │     │  │  │  ├─ splittst.py
   │     │  │  │  ├─ threadedgui.py
   │     │  │  │  └─ toolbar.py
   │     │  │  ├─ docking
   │     │  │  │  ├─ DockingBar.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ framework
   │     │  │  │  ├─ app.py
   │     │  │  │  ├─ bitmap.py
   │     │  │  │  ├─ cmdline.py
   │     │  │  │  ├─ dbgcommands.py
   │     │  │  │  ├─ dlgappcore.py
   │     │  │  │  ├─ editor
   │     │  │  │  │  ├─ color
   │     │  │  │  │  │  ├─ coloreditor.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ configui.py
   │     │  │  │  │  ├─ document.py
   │     │  │  │  │  ├─ editor.py
   │     │  │  │  │  ├─ frame.py
   │     │  │  │  │  ├─ ModuleBrowser.py
   │     │  │  │  │  ├─ template.py
   │     │  │  │  │  ├─ vss.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ help.py
   │     │  │  │  ├─ interact.py
   │     │  │  │  ├─ intpyapp.py
   │     │  │  │  ├─ intpydde.py
   │     │  │  │  ├─ scriptutils.py
   │     │  │  │  ├─ sgrepmdi.py
   │     │  │  │  ├─ startup.py
   │     │  │  │  ├─ stdin.py
   │     │  │  │  ├─ toolmenu.py
   │     │  │  │  ├─ window.py
   │     │  │  │  ├─ winout.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ idle
   │     │  │  │  ├─ AutoExpand.py
   │     │  │  │  ├─ AutoIndent.py
   │     │  │  │  ├─ CallTips.py
   │     │  │  │  ├─ FormatParagraph.py
   │     │  │  │  ├─ IdleHistory.py
   │     │  │  │  ├─ PyParse.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ IDLE.cfg
   │     │  │  ├─ mfc
   │     │  │  │  ├─ activex.py
   │     │  │  │  ├─ afxres.py
   │     │  │  │  ├─ dialog.py
   │     │  │  │  ├─ docview.py
   │     │  │  │  ├─ object.py
   │     │  │  │  ├─ thread.py
   │     │  │  │  ├─ window.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ scintilla
   │     │  │  │  ├─ bindings.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ configui.py
   │     │  │  │  ├─ control.py
   │     │  │  │  ├─ document.py
   │     │  │  │  ├─ find.py
   │     │  │  │  ├─ formatter.py
   │     │  │  │  ├─ IDLEenvironment.py
   │     │  │  │  ├─ keycodes.py
   │     │  │  │  ├─ scintillacon.py
   │     │  │  │  ├─ view.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tools
   │     │  │  │  ├─ browseProjects.py
   │     │  │  │  ├─ browser.py
   │     │  │  │  ├─ hierlist.py
   │     │  │  │  ├─ regedit.py
   │     │  │  │  ├─ regpy.py
   │     │  │  │  ├─ TraceCollector.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ scintilla.dll
   │     │  ├─ start_pythonwin.pyw
   │     │  ├─ win32ui.pyd
   │     │  └─ win32uiole.pyd
   │     ├─ pyttsx3
   │     │  ├─ driver.py
   │     │  ├─ drivers
   │     │  │  ├─ avspeech.py
   │     │  │  ├─ dummy.py
   │     │  │  ├─ espeak.py
   │     │  │  ├─ nsss.py
   │     │  │  ├─ sapi5.py
   │     │  │  ├─ _espeak.py
   │     │  │  └─ __init__.py
   │     │  ├─ engine.py
   │     │  ├─ voice.py
   │     │  └─ __init__.py
   │     ├─ pytweening
   │     │  └─ __init__.py
   │     ├─ PyWin32.chm
   │     ├─ pywin32.pth
   │     ├─ pywin32.version.txt
   │     ├─ pywin32_system32
   │     │  ├─ pythoncom313.dll
   │     │  └─ pywintypes313.dll
   │     ├─ redis
   │     │  ├─ asyncio
   │     │  │  ├─ client.py
   │     │  │  ├─ cluster.py
   │     │  │  ├─ connection.py
   │     │  │  ├─ http
   │     │  │  │  ├─ http_client.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ keyspace_notifications.py
   │     │  │  ├─ lock.py
   │     │  │  ├─ multidb
   │     │  │  │  ├─ client.py
   │     │  │  │  ├─ command_executor.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ database.py
   │     │  │  │  ├─ event.py
   │     │  │  │  ├─ failover.py
   │     │  │  │  ├─ failure_detector.py
   │     │  │  │  ├─ healthcheck.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ observability
   │     │  │  │  ├─ recorder.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ retry.py
   │     │  │  ├─ sentinel.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ auth
   │     │  │  ├─ err.py
   │     │  │  ├─ idp.py
   │     │  │  ├─ token.py
   │     │  │  ├─ token_manager.py
   │     │  │  └─ __init__.py
   │     │  ├─ background.py
   │     │  ├─ backoff.py
   │     │  ├─ cache.py
   │     │  ├─ client.py
   │     │  ├─ cluster.py
   │     │  ├─ commands
   │     │  │  ├─ bf
   │     │  │  │  ├─ commands.py
   │     │  │  │  ├─ info.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cluster.py
   │     │  │  ├─ core.py
   │     │  │  ├─ helpers.py
   │     │  │  ├─ json
   │     │  │  │  ├─ commands.py
   │     │  │  │  ├─ decoders.py
   │     │  │  │  ├─ path.py
   │     │  │  │  ├─ _util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ policies.py
   │     │  │  ├─ redismodules.py
   │     │  │  ├─ search
   │     │  │  │  ├─ aggregation.py
   │     │  │  │  ├─ commands.py
   │     │  │  │  ├─ dialect.py
   │     │  │  │  ├─ document.py
   │     │  │  │  ├─ field.py
   │     │  │  │  ├─ hybrid_query.py
   │     │  │  │  ├─ hybrid_result.py
   │     │  │  │  ├─ index_definition.py
   │     │  │  │  ├─ profile_information.py
   │     │  │  │  ├─ query.py
   │     │  │  │  ├─ querystring.py
   │     │  │  │  ├─ reducers.py
   │     │  │  │  ├─ result.py
   │     │  │  │  ├─ suggestion.py
   │     │  │  │  ├─ _util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sentinel.py
   │     │  │  ├─ timeseries
   │     │  │  │  ├─ commands.py
   │     │  │  │  ├─ info.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vectorset
   │     │  │  │  ├─ commands.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ connection.py
   │     │  ├─ crc.py
   │     │  ├─ credentials.py
   │     │  ├─ data_structure.py
   │     │  ├─ driver_info.py
   │     │  ├─ event.py
   │     │  ├─ exceptions.py
   │     │  ├─ http
   │     │  │  ├─ http_client.py
   │     │  │  └─ __init__.py
   │     │  ├─ keyspace_notifications.py
   │     │  ├─ lock.py
   │     │  ├─ maint_notifications.py
   │     │  ├─ multidb
   │     │  │  ├─ circuit.py
   │     │  │  ├─ client.py
   │     │  │  ├─ command_executor.py
   │     │  │  ├─ config.py
   │     │  │  ├─ database.py
   │     │  │  ├─ event.py
   │     │  │  ├─ exception.py
   │     │  │  ├─ failover.py
   │     │  │  ├─ failure_detector.py
   │     │  │  └─ __init__.py
   │     │  ├─ observability
   │     │  │  ├─ attributes.py
   │     │  │  ├─ config.py
   │     │  │  ├─ metrics.py
   │     │  │  ├─ providers.py
   │     │  │  ├─ recorder.py
   │     │  │  ├─ registry.py
   │     │  │  └─ __init__.py
   │     │  ├─ ocsp.py
   │     │  ├─ py.typed
   │     │  ├─ retry.py
   │     │  ├─ sentinel.py
   │     │  ├─ typing.py
   │     │  ├─ utils.py
   │     │  ├─ _defaults.py
   │     │  ├─ _parsers
   │     │  │  ├─ base.py
   │     │  │  ├─ commands.py
   │     │  │  ├─ encoders.py
   │     │  │  ├─ helpers.py
   │     │  │  ├─ hiredis.py
   │     │  │  ├─ resp2.py
   │     │  │  ├─ resp3.py
   │     │  │  ├─ response_callbacks.py
   │     │  │  ├─ socket.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ requests
   │     │  ├─ adapters.py
   │     │  ├─ api.py
   │     │  ├─ auth.py
   │     │  ├─ certs.py
   │     │  ├─ compat.py
   │     │  ├─ cookies.py
   │     │  ├─ exceptions.py
   │     │  ├─ help.py
   │     │  ├─ hooks.py
   │     │  ├─ models.py
   │     │  ├─ packages.py
   │     │  ├─ py.typed
   │     │  ├─ sessions.py
   │     │  ├─ status_codes.py
   │     │  ├─ structures.py
   │     │  ├─ utils.py
   │     │  ├─ _internal_utils.py
   │     │  ├─ _types.py
   │     │  ├─ __init__.py
   │     │  └─ __version__.py
   │     ├─ sniffio
   │     │  ├─ py.typed
   │     │  ├─ _impl.py
   │     │  ├─ _tests
   │     │  │  ├─ test_sniffio.py
   │     │  │  └─ __init__.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ speech_recognition
   │     │  ├─ audio.py
   │     │  ├─ cli.py
   │     │  ├─ exceptions.py
   │     │  ├─ flac-linux-x86
   │     │  ├─ flac-linux-x86_64
   │     │  ├─ flac-mac
   │     │  ├─ flac-win32.exe
   │     │  ├─ pocketsphinx-data
   │     │  │  └─ en-US
   │     │  │     ├─ acoustic-model
   │     │  │     │  ├─ feat.params
   │     │  │     │  ├─ mdef
   │     │  │     │  ├─ means
   │     │  │     │  ├─ noisedict
   │     │  │     │  ├─ README
   │     │  │     │  ├─ sendump
   │     │  │     │  ├─ transition_matrices
   │     │  │     │  └─ variances
   │     │  │     ├─ language-model.lm.bin
   │     │  │     ├─ LICENSE.txt
   │     │  │     └─ pronounciation-dictionary.dict
   │     │  ├─ recognizers
   │     │  │  ├─ cohere_api.py
   │     │  │  ├─ google.py
   │     │  │  ├─ google_cloud.py
   │     │  │  ├─ pocketsphinx.py
   │     │  │  ├─ vosk.py
   │     │  │  ├─ whisper_api
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ groq.py
   │     │  │  │  ├─ openai.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ whisper_local
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ faster_whisper.py
   │     │  │  │  ├─ whisper.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ version.txt
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ spotipy
   │     │  ├─ cache_handler.py
   │     │  ├─ client.py
   │     │  ├─ exceptions.py
   │     │  ├─ oauth2.py
   │     │  ├─ util.py
   │     │  └─ __init__.py
   │     ├─ starlette
   │     │  ├─ applications.py
   │     │  ├─ authentication.py
   │     │  ├─ background.py
   │     │  ├─ concurrency.py
   │     │  ├─ config.py
   │     │  ├─ convertors.py
   │     │  ├─ datastructures.py
   │     │  ├─ endpoints.py
   │     │  ├─ exceptions.py
   │     │  ├─ formparsers.py
   │     │  ├─ middleware
   │     │  │  ├─ authentication.py
   │     │  │  ├─ base.py
   │     │  │  ├─ cors.py
   │     │  │  ├─ errors.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ gzip.py
   │     │  │  ├─ httpsredirect.py
   │     │  │  ├─ sessions.py
   │     │  │  ├─ trustedhost.py
   │     │  │  ├─ wsgi.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ requests.py
   │     │  ├─ responses.py
   │     │  ├─ routing.py
   │     │  ├─ schemas.py
   │     │  ├─ staticfiles.py
   │     │  ├─ status.py
   │     │  ├─ templating.py
   │     │  ├─ testclient.py
   │     │  ├─ types.py
   │     │  ├─ websockets.py
   │     │  ├─ _exception_handler.py
   │     │  ├─ _utils.py
   │     │  └─ __init__.py
   │     ├─ telegram
   │     │  ├─ constants.py
   │     │  ├─ error.py
   │     │  ├─ ext
   │     │  │  ├─ filters.py
   │     │  │  ├─ _aioratelimiter.py
   │     │  │  ├─ _application.py
   │     │  │  ├─ _applicationbuilder.py
   │     │  │  ├─ _basepersistence.py
   │     │  │  ├─ _baseratelimiter.py
   │     │  │  ├─ _baseupdateprocessor.py
   │     │  │  ├─ _callbackcontext.py
   │     │  │  ├─ _callbackdatacache.py
   │     │  │  ├─ _contexttypes.py
   │     │  │  ├─ _defaults.py
   │     │  │  ├─ _dictpersistence.py
   │     │  │  ├─ _extbot.py
   │     │  │  ├─ _handlers
   │     │  │  │  ├─ basehandler.py
   │     │  │  │  ├─ businessconnectionhandler.py
   │     │  │  │  ├─ businessmessagesdeletedhandler.py
   │     │  │  │  ├─ callbackqueryhandler.py
   │     │  │  │  ├─ chatboosthandler.py
   │     │  │  │  ├─ chatjoinrequesthandler.py
   │     │  │  │  ├─ chatmemberhandler.py
   │     │  │  │  ├─ choseninlineresulthandler.py
   │     │  │  │  ├─ commandhandler.py
   │     │  │  │  ├─ conversationhandler.py
   │     │  │  │  ├─ inlinequeryhandler.py
   │     │  │  │  ├─ messagehandler.py
   │     │  │  │  ├─ messagereactionhandler.py
   │     │  │  │  ├─ paidmediapurchasedhandler.py
   │     │  │  │  ├─ pollanswerhandler.py
   │     │  │  │  ├─ pollhandler.py
   │     │  │  │  ├─ precheckoutqueryhandler.py
   │     │  │  │  ├─ prefixhandler.py
   │     │  │  │  ├─ shippingqueryhandler.py
   │     │  │  │  ├─ stringcommandhandler.py
   │     │  │  │  ├─ stringregexhandler.py
   │     │  │  │  ├─ typehandler.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _jobqueue.py
   │     │  │  ├─ _picklepersistence.py
   │     │  │  ├─ _updater.py
   │     │  │  ├─ _utils
   │     │  │  │  ├─ asyncio.py
   │     │  │  │  ├─ networkloop.py
   │     │  │  │  ├─ stack.py
   │     │  │  │  ├─ trackingdict.py
   │     │  │  │  ├─ types.py
   │     │  │  │  ├─ webhookhandler.py
   │     │  │  │  ├─ _update_parsing.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ helpers.py
   │     │  ├─ py.typed
   │     │  ├─ request
   │     │  │  ├─ _baserequest.py
   │     │  │  ├─ _httpxrequest.py
   │     │  │  ├─ _requestdata.py
   │     │  │  ├─ _requestparameter.py
   │     │  │  └─ __init__.py
   │     │  ├─ warnings.py
   │     │  ├─ _birthdate.py
   │     │  ├─ _bot.py
   │     │  ├─ _botcommand.py
   │     │  ├─ _botcommandscope.py
   │     │  ├─ _botdescription.py
   │     │  ├─ _botname.py
   │     │  ├─ _business.py
   │     │  ├─ _callbackquery.py
   │     │  ├─ _chat.py
   │     │  ├─ _chatadministratorrights.py
   │     │  ├─ _chatbackground.py
   │     │  ├─ _chatboost.py
   │     │  ├─ _chatfullinfo.py
   │     │  ├─ _chatinvitelink.py
   │     │  ├─ _chatjoinrequest.py
   │     │  ├─ _chatlocation.py
   │     │  ├─ _chatmember.py
   │     │  ├─ _chatmemberupdated.py
   │     │  ├─ _chatowner.py
   │     │  ├─ _chatpermissions.py
   │     │  ├─ _checklists.py
   │     │  ├─ _choseninlineresult.py
   │     │  ├─ _copytextbutton.py
   │     │  ├─ _dice.py
   │     │  ├─ _directmessagepricechanged.py
   │     │  ├─ _directmessagestopic.py
   │     │  ├─ _files
   │     │  │  ├─ animation.py
   │     │  │  ├─ audio.py
   │     │  │  ├─ chatphoto.py
   │     │  │  ├─ contact.py
   │     │  │  ├─ document.py
   │     │  │  ├─ file.py
   │     │  │  ├─ inputfile.py
   │     │  │  ├─ inputmedia.py
   │     │  │  ├─ inputprofilephoto.py
   │     │  │  ├─ inputsticker.py
   │     │  │  ├─ location.py
   │     │  │  ├─ photosize.py
   │     │  │  ├─ sticker.py
   │     │  │  ├─ venue.py
   │     │  │  ├─ video.py
   │     │  │  ├─ videonote.py
   │     │  │  ├─ videoquality.py
   │     │  │  ├─ voice.py
   │     │  │  ├─ _basemedium.py
   │     │  │  ├─ _basethumbedmedium.py
   │     │  │  ├─ _inputstorycontent.py
   │     │  │  └─ __init__.py
   │     │  ├─ _forcereply.py
   │     │  ├─ _forumtopic.py
   │     │  ├─ _games
   │     │  │  ├─ callbackgame.py
   │     │  │  ├─ game.py
   │     │  │  ├─ gamehighscore.py
   │     │  │  └─ __init__.py
   │     │  ├─ _gifts.py
   │     │  ├─ _giveaway.py
   │     │  ├─ _inline
   │     │  │  ├─ inlinekeyboardbutton.py
   │     │  │  ├─ inlinekeyboardmarkup.py
   │     │  │  ├─ inlinequery.py
   │     │  │  ├─ inlinequeryresult.py
   │     │  │  ├─ inlinequeryresultarticle.py
   │     │  │  ├─ inlinequeryresultaudio.py
   │     │  │  ├─ inlinequeryresultcachedaudio.py
   │     │  │  ├─ inlinequeryresultcacheddocument.py
   │     │  │  ├─ inlinequeryresultcachedgif.py
   │     │  │  ├─ inlinequeryresultcachedmpeg4gif.py
   │     │  │  ├─ inlinequeryresultcachedphoto.py
   │     │  │  ├─ inlinequeryresultcachedsticker.py
   │     │  │  ├─ inlinequeryresultcachedvideo.py
   │     │  │  ├─ inlinequeryresultcachedvoice.py
   │     │  │  ├─ inlinequeryresultcontact.py
   │     │  │  ├─ inlinequeryresultdocument.py
   │     │  │  ├─ inlinequeryresultgame.py
   │     │  │  ├─ inlinequeryresultgif.py
   │     │  │  ├─ inlinequeryresultlocation.py
   │     │  │  ├─ inlinequeryresultmpeg4gif.py
   │     │  │  ├─ inlinequeryresultphoto.py
   │     │  │  ├─ inlinequeryresultsbutton.py
   │     │  │  ├─ inlinequeryresultvenue.py
   │     │  │  ├─ inlinequeryresultvideo.py
   │     │  │  ├─ inlinequeryresultvoice.py
   │     │  │  ├─ inputcontactmessagecontent.py
   │     │  │  ├─ inputinvoicemessagecontent.py
   │     │  │  ├─ inputlocationmessagecontent.py
   │     │  │  ├─ inputmessagecontent.py
   │     │  │  ├─ inputtextmessagecontent.py
   │     │  │  ├─ inputvenuemessagecontent.py
   │     │  │  ├─ preparedinlinemessage.py
   │     │  │  └─ __init__.py
   │     │  ├─ _inputchecklist.py
   │     │  ├─ _keyboardbutton.py
   │     │  ├─ _keyboardbuttonpolltype.py
   │     │  ├─ _keyboardbuttonrequest.py
   │     │  ├─ _linkpreviewoptions.py
   │     │  ├─ _loginurl.py
   │     │  ├─ _menubutton.py
   │     │  ├─ _message.py
   │     │  ├─ _messageautodeletetimerchanged.py
   │     │  ├─ _messageentity.py
   │     │  ├─ _messageid.py
   │     │  ├─ _messageorigin.py
   │     │  ├─ _messagereactionupdated.py
   │     │  ├─ _ownedgift.py
   │     │  ├─ _paidmedia.py
   │     │  ├─ _paidmessagepricechanged.py
   │     │  ├─ _passport
   │     │  │  ├─ credentials.py
   │     │  │  ├─ data.py
   │     │  │  ├─ encryptedpassportelement.py
   │     │  │  ├─ passportdata.py
   │     │  │  ├─ passportelementerrors.py
   │     │  │  ├─ passportfile.py
   │     │  │  └─ __init__.py
   │     │  ├─ _payment
   │     │  │  ├─ invoice.py
   │     │  │  ├─ labeledprice.py
   │     │  │  ├─ orderinfo.py
   │     │  │  ├─ precheckoutquery.py
   │     │  │  ├─ refundedpayment.py
   │     │  │  ├─ shippingaddress.py
   │     │  │  ├─ shippingoption.py
   │     │  │  ├─ shippingquery.py
   │     │  │  ├─ stars
   │     │  │  │  ├─ affiliateinfo.py
   │     │  │  │  ├─ revenuewithdrawalstate.py
   │     │  │  │  ├─ staramount.py
   │     │  │  │  ├─ startransactions.py
   │     │  │  │  ├─ transactionpartner.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ successfulpayment.py
   │     │  │  └─ __init__.py
   │     │  ├─ _poll.py
   │     │  ├─ _proximityalerttriggered.py
   │     │  ├─ _reaction.py
   │     │  ├─ _reply.py
   │     │  ├─ _replykeyboardmarkup.py
   │     │  ├─ _replykeyboardremove.py
   │     │  ├─ _sentwebappmessage.py
   │     │  ├─ _shared.py
   │     │  ├─ _story.py
   │     │  ├─ _storyarea.py
   │     │  ├─ _suggestedpost.py
   │     │  ├─ _switchinlinequerychosenchat.py
   │     │  ├─ _telegramobject.py
   │     │  ├─ _uniquegift.py
   │     │  ├─ _update.py
   │     │  ├─ _user.py
   │     │  ├─ _userprofileaudios.py
   │     │  ├─ _userprofilephotos.py
   │     │  ├─ _userrating.py
   │     │  ├─ _utils
   │     │  │  ├─ argumentparsing.py
   │     │  │  ├─ datetime.py
   │     │  │  ├─ defaultvalue.py
   │     │  │  ├─ entities.py
   │     │  │  ├─ enum.py
   │     │  │  ├─ files.py
   │     │  │  ├─ logging.py
   │     │  │  ├─ markup.py
   │     │  │  ├─ repr.py
   │     │  │  ├─ strings.py
   │     │  │  ├─ types.py
   │     │  │  ├─ usernames.py
   │     │  │  ├─ warnings.py
   │     │  │  ├─ warnings_transition.py
   │     │  │  └─ __init__.py
   │     │  ├─ _version.py
   │     │  ├─ _videochat.py
   │     │  ├─ _webappdata.py
   │     │  ├─ _webappinfo.py
   │     │  ├─ _webhookinfo.py
   │     │  ├─ _writeaccessallowed.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ tenacity
   │     │  ├─ after.py
   │     │  ├─ asyncio
   │     │  │  ├─ retry.py
   │     │  │  └─ __init__.py
   │     │  ├─ before.py
   │     │  ├─ before_sleep.py
   │     │  ├─ nap.py
   │     │  ├─ py.typed
   │     │  ├─ retry.py
   │     │  ├─ stop.py
   │     │  ├─ tornadoweb.py
   │     │  ├─ wait.py
   │     │  ├─ _utils.py
   │     │  └─ __init__.py
   │     ├─ tqdm
   │     │  ├─ asyncio.py
   │     │  ├─ auto.py
   │     │  ├─ autonotebook.py
   │     │  ├─ cli.py
   │     │  ├─ completion.sh
   │     │  ├─ contrib
   │     │  │  ├─ bells.py
   │     │  │  ├─ concurrent.py
   │     │  │  ├─ discord.py
   │     │  │  ├─ itertools.py
   │     │  │  ├─ logging.py
   │     │  │  ├─ slack.py
   │     │  │  ├─ telegram.py
   │     │  │  ├─ utils_worker.py
   │     │  │  └─ __init__.py
   │     │  ├─ dask.py
   │     │  ├─ gui.py
   │     │  ├─ keras.py
   │     │  ├─ notebook.py
   │     │  ├─ rich.py
   │     │  ├─ std.py
   │     │  ├─ tk.py
   │     │  ├─ tqdm.1
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ _main.py
   │     │  ├─ _monitor.py
   │     │  ├─ _tqdm.py
   │     │  ├─ _tqdm_gui.py
   │     │  ├─ _tqdm_notebook.py
   │     │  ├─ _tqdm_pandas.py
   │     │  ├─ _utils.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ truststore
   │     │  ├─ py.typed
   │     │  ├─ _api.py
   │     │  ├─ _macos.py
   │     │  ├─ _openssl.py
   │     │  ├─ _ssl_constants.py
   │     │  ├─ _windows.py
   │     │  └─ __init__.py
   │     ├─ typing_extensions.py
   │     ├─ typing_inspection
   │     │  ├─ introspection.py
   │     │  ├─ py.typed
   │     │  ├─ typing_objects.py
   │     │  ├─ typing_objects.pyi
   │     │  └─ __init__.py
   │     ├─ uritemplate
   │     │  ├─ api.py
   │     │  ├─ orderedset.py
   │     │  ├─ py.typed
   │     │  ├─ template.py
   │     │  ├─ variable.py
   │     │  └─ __init__.py
   │     ├─ urllib3
   │     │  ├─ connection.py
   │     │  ├─ connectionpool.py
   │     │  ├─ contrib
   │     │  │  ├─ emscripten
   │     │  │  │  ├─ connection.py
   │     │  │  │  ├─ emscripten_fetch_worker.js
   │     │  │  │  ├─ fetch.py
   │     │  │  │  ├─ request.py
   │     │  │  │  ├─ response.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pyopenssl.py
   │     │  │  ├─ socks.py
   │     │  │  └─ __init__.py
   │     │  ├─ exceptions.py
   │     │  ├─ fields.py
   │     │  ├─ filepost.py
   │     │  ├─ http2
   │     │  │  ├─ connection.py
   │     │  │  ├─ probe.py
   │     │  │  └─ __init__.py
   │     │  ├─ poolmanager.py
   │     │  ├─ py.typed
   │     │  ├─ response.py
   │     │  ├─ util
   │     │  │  ├─ connection.py
   │     │  │  ├─ proxy.py
   │     │  │  ├─ request.py
   │     │  │  ├─ response.py
   │     │  │  ├─ retry.py
   │     │  │  ├─ ssltransport.py
   │     │  │  ├─ ssl_.py
   │     │  │  ├─ ssl_match_hostname.py
   │     │  │  ├─ timeout.py
   │     │  │  ├─ url.py
   │     │  │  ├─ util.py
   │     │  │  ├─ wait.py
   │     │  │  └─ __init__.py
   │     │  ├─ _base_connection.py
   │     │  ├─ _collections.py
   │     │  ├─ _request_methods.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ uvicorn
   │     │  ├─ config.py
   │     │  ├─ importer.py
   │     │  ├─ lifespan
   │     │  │  ├─ off.py
   │     │  │  ├─ on.py
   │     │  │  └─ __init__.py
   │     │  ├─ logging.py
   │     │  ├─ loops
   │     │  │  ├─ asyncio.py
   │     │  │  ├─ auto.py
   │     │  │  ├─ uvloop.py
   │     │  │  └─ __init__.py
   │     │  ├─ main.py
   │     │  ├─ middleware
   │     │  │  ├─ asgi2.py
   │     │  │  ├─ message_logger.py
   │     │  │  ├─ proxy_headers.py
   │     │  │  ├─ wsgi.py
   │     │  │  └─ __init__.py
   │     │  ├─ protocols
   │     │  │  ├─ http
   │     │  │  │  ├─ auto.py
   │     │  │  │  ├─ flow_control.py
   │     │  │  │  ├─ h11_impl.py
   │     │  │  │  ├─ httptools_impl.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ utils.py
   │     │  │  ├─ websockets
   │     │  │  │  ├─ auto.py
   │     │  │  │  ├─ websockets_impl.py
   │     │  │  │  ├─ websockets_sansio_impl.py
   │     │  │  │  ├─ wsproto_impl.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ server.py
   │     │  ├─ supervisors
   │     │  │  ├─ basereload.py
   │     │  │  ├─ multiprocess.py
   │     │  │  ├─ statreload.py
   │     │  │  ├─ watchfilesreload.py
   │     │  │  └─ __init__.py
   │     │  ├─ workers.py
   │     │  ├─ _compat.py
   │     │  ├─ _subprocess.py
   │     │  ├─ _types.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ watchfiles
   │     │  ├─ cli.py
   │     │  ├─ filters.py
   │     │  ├─ main.py
   │     │  ├─ py.typed
   │     │  ├─ run.py
   │     │  ├─ version.py
   │     │  ├─ _rust_notify.cp313-win_amd64.pyd
   │     │  ├─ _rust_notify.pyi
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ websockets
   │     │  ├─ asyncio
   │     │  │  ├─ async_timeout.py
   │     │  │  ├─ client.py
   │     │  │  ├─ compatibility.py
   │     │  │  ├─ connection.py
   │     │  │  ├─ messages.py
   │     │  │  ├─ router.py
   │     │  │  ├─ server.py
   │     │  │  └─ __init__.py
   │     │  ├─ auth.py
   │     │  ├─ cli.py
   │     │  ├─ client.py
   │     │  ├─ connection.py
   │     │  ├─ datastructures.py
   │     │  ├─ exceptions.py
   │     │  ├─ extensions
   │     │  │  ├─ base.py
   │     │  │  ├─ permessage_deflate.py
   │     │  │  └─ __init__.py
   │     │  ├─ frames.py
   │     │  ├─ headers.py
   │     │  ├─ http.py
   │     │  ├─ http11.py
   │     │  ├─ imports.py
   │     │  ├─ legacy
   │     │  │  ├─ auth.py
   │     │  │  ├─ client.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ framing.py
   │     │  │  ├─ handshake.py
   │     │  │  ├─ http.py
   │     │  │  ├─ protocol.py
   │     │  │  ├─ server.py
   │     │  │  └─ __init__.py
   │     │  ├─ protocol.py
   │     │  ├─ proxy.py
   │     │  ├─ py.typed
   │     │  ├─ server.py
   │     │  ├─ speedups.c
   │     │  ├─ speedups.cp313-win_amd64.pyd
   │     │  ├─ speedups.pyi
   │     │  ├─ streams.py
   │     │  ├─ sync
   │     │  │  ├─ client.py
   │     │  │  ├─ connection.py
   │     │  │  ├─ messages.py
   │     │  │  ├─ router.py
   │     │  │  ├─ server.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ typing.py
   │     │  ├─ uri.py
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ win32
   │     │  ├─ Demos
   │     │  │  ├─ BackupRead_BackupWrite.py
   │     │  │  ├─ BackupSeek_streamheaders.py
   │     │  │  ├─ CopyFileEx.py
   │     │  │  ├─ CreateFileTransacted_MiniVersion.py
   │     │  │  ├─ c_extension
   │     │  │  │  └─ setup.py
   │     │  │  ├─ dde
   │     │  │  │  ├─ ddeclient.py
   │     │  │  │  └─ ddeserver.py
   │     │  │  ├─ desktopmanager.py
   │     │  │  ├─ eventLogDemo.py
   │     │  │  ├─ EvtFormatMessage.py
   │     │  │  ├─ EvtSubscribe_pull.py
   │     │  │  ├─ EvtSubscribe_push.py
   │     │  │  ├─ FileSecurityTest.py
   │     │  │  ├─ getfilever.py
   │     │  │  ├─ GetSaveFileName.py
   │     │  │  ├─ images
   │     │  │  │  ├─ frowny.bmp
   │     │  │  │  └─ smiley.bmp
   │     │  │  ├─ mmapfile_demo.py
   │     │  │  ├─ NetValidatePasswordPolicy.py
   │     │  │  ├─ OpenEncryptedFileRaw.py
   │     │  │  ├─ pipes
   │     │  │  │  ├─ cat.py
   │     │  │  │  └─ runproc.py
   │     │  │  ├─ print_desktop.py
   │     │  │  ├─ rastest.py
   │     │  │  ├─ RegCreateKeyTransacted.py
   │     │  │  ├─ RegRestoreKey.py
   │     │  │  ├─ security
   │     │  │  │  ├─ account_rights.py
   │     │  │  │  ├─ explicit_entries.py
   │     │  │  │  ├─ GetTokenInformation.py
   │     │  │  │  ├─ get_policy_info.py
   │     │  │  │  ├─ list_rights.py
   │     │  │  │  ├─ localized_names.py
   │     │  │  │  ├─ lsaregevent.py
   │     │  │  │  ├─ lsastore.py
   │     │  │  │  ├─ query_information.py
   │     │  │  │  ├─ regsave_sa.py
   │     │  │  │  ├─ regsecurity.py
   │     │  │  │  ├─ sa_inherit.py
   │     │  │  │  ├─ security_enums.py
   │     │  │  │  ├─ setkernelobjectsecurity.py
   │     │  │  │  ├─ setnamedsecurityinfo.py
   │     │  │  │  ├─ setsecurityinfo.py
   │     │  │  │  ├─ setuserobjectsecurity.py
   │     │  │  │  ├─ set_file_audit.py
   │     │  │  │  ├─ set_file_owner.py
   │     │  │  │  ├─ set_policy_info.py
   │     │  │  │  └─ sspi
   │     │  │  │     ├─ fetch_url.py
   │     │  │  │     ├─ simple_auth.py
   │     │  │  │     ├─ socket_server.py
   │     │  │  │     └─ validate_password.py
   │     │  │  ├─ service
   │     │  │  │  ├─ nativePipeTestService.py
   │     │  │  │  ├─ pipeTestService.py
   │     │  │  │  ├─ pipeTestServiceClient.py
   │     │  │  │  └─ serviceEvents.py
   │     │  │  ├─ SystemParametersInfo.py
   │     │  │  ├─ timer_demo.py
   │     │  │  ├─ win32clipboardDemo.py
   │     │  │  ├─ win32clipboard_bitmapdemo.py
   │     │  │  ├─ win32comport_demo.py
   │     │  │  ├─ win32console_demo.py
   │     │  │  ├─ win32cred_demo.py
   │     │  │  ├─ win32fileDemo.py
   │     │  │  ├─ win32gui_demo.py
   │     │  │  ├─ win32gui_devicenotify.py
   │     │  │  ├─ win32gui_dialog.py
   │     │  │  ├─ win32gui_menu.py
   │     │  │  ├─ win32gui_taskbar.py
   │     │  │  ├─ win32netdemo.py
   │     │  │  ├─ win32rcparser_demo.py
   │     │  │  ├─ win32servicedemo.py
   │     │  │  ├─ win32ts_logoff_disconnected.py
   │     │  │  ├─ win32wnet
   │     │  │  │  ├─ testwnet.py
   │     │  │  │  └─ winnetwk.py
   │     │  │  └─ winprocess.py
   │     │  ├─ include
   │     │  │  └─ PyWinTypes.h
   │     │  ├─ lib
   │     │  │  ├─ afxres.py
   │     │  │  ├─ commctrl.py
   │     │  │  ├─ mmsystem.py
   │     │  │  ├─ netbios.py
   │     │  │  ├─ ntsecuritycon.py
   │     │  │  ├─ pywin32_bootstrap.py
   │     │  │  ├─ pywin32_testutil.py
   │     │  │  ├─ pywintypes.py
   │     │  │  ├─ rasutil.py
   │     │  │  ├─ regcheck.py
   │     │  │  ├─ regutil.py
   │     │  │  ├─ sspi.py
   │     │  │  ├─ sspicon.py
   │     │  │  ├─ win2kras.py
   │     │  │  ├─ win32con.py
   │     │  │  ├─ win32cryptcon.py
   │     │  │  ├─ win32evtlogutil.py
   │     │  │  ├─ win32gui_struct.py
   │     │  │  ├─ win32inetcon.py
   │     │  │  ├─ win32netcon.py
   │     │  │  ├─ win32pdhquery.py
   │     │  │  ├─ win32pdhutil.py
   │     │  │  ├─ win32rcparser.py
   │     │  │  ├─ win32serviceutil.py
   │     │  │  ├─ win32timezone.py
   │     │  │  ├─ win32traceutil.py
   │     │  │  ├─ win32verstamp.py
   │     │  │  ├─ winerror.py
   │     │  │  ├─ winioctlcon.py
   │     │  │  ├─ winnt.py
   │     │  │  ├─ winperf.py
   │     │  │  ├─ winxptheme.py
   │     │  │  └─ _win32verstamp_pywin32ctypes.py
   │     │  ├─ libs
   │     │  │  └─ pywintypes.lib
   │     │  ├─ license.txt
   │     │  ├─ mmapfile.pyd
   │     │  ├─ odbc.pyd
   │     │  ├─ perfmon.pyd
   │     │  ├─ perfmondata.dll
   │     │  ├─ pythonservice.exe
   │     │  ├─ scripts
   │     │  │  ├─ backupEventLog.py
   │     │  │  ├─ ControlService.py
   │     │  │  ├─ h2py.py
   │     │  │  ├─ killProcName.py
   │     │  │  ├─ pywin32_postinstall.py
   │     │  │  ├─ pywin32_testall.py
   │     │  │  ├─ rasutil.py
   │     │  │  ├─ regsetup.py
   │     │  │  ├─ setup_d.py
   │     │  │  └─ VersionStamp
   │     │  │     ├─ BrandProject.py
   │     │  │     ├─ bulkstamp.py
   │     │  │     └─ vssutil.py
   │     │  ├─ servicemanager.pyd
   │     │  ├─ test
   │     │  │  ├─ handles.py
   │     │  │  ├─ testall.py
   │     │  │  ├─ test_clipboard.py
   │     │  │  ├─ test_exceptions.py
   │     │  │  ├─ test_odbc.py
   │     │  │  ├─ test_pywintypes.py
   │     │  │  ├─ test_security.py
   │     │  │  ├─ test_sspi.py
   │     │  │  ├─ test_win32api.py
   │     │  │  ├─ test_win32clipboard.py
   │     │  │  ├─ test_win32cred.py
   │     │  │  ├─ test_win32crypt.py
   │     │  │  ├─ test_win32event.py
   │     │  │  ├─ test_win32file.py
   │     │  │  ├─ test_win32gui.py
   │     │  │  ├─ test_win32guistruct.py
   │     │  │  ├─ test_win32inet.py
   │     │  │  ├─ test_win32net.py
   │     │  │  ├─ test_win32pipe.py
   │     │  │  ├─ test_win32print.py
   │     │  │  ├─ test_win32profile.py
   │     │  │  ├─ test_win32rcparser.py
   │     │  │  ├─ test_win32timezone.py
   │     │  │  ├─ test_win32trace.py
   │     │  │  ├─ test_win32ts.py
   │     │  │  ├─ test_win32wnet.py
   │     │  │  └─ win32rcparser
   │     │  │     ├─ python.bmp
   │     │  │     ├─ python.ico
   │     │  │     ├─ test.h
   │     │  │     └─ test.rc
   │     │  ├─ timer.pyd
   │     │  ├─ win32api.pyd
   │     │  ├─ win32clipboard.pyd
   │     │  ├─ win32console.pyd
   │     │  ├─ win32cred.pyd
   │     │  ├─ win32crypt.pyd
   │     │  ├─ win32event.pyd
   │     │  ├─ win32evtlog.pyd
   │     │  ├─ win32file.pyd
   │     │  ├─ win32gui.pyd
   │     │  ├─ win32help.pyd
   │     │  ├─ win32inet.pyd
   │     │  ├─ win32job.pyd
   │     │  ├─ win32lz.pyd
   │     │  ├─ win32net.pyd
   │     │  ├─ win32pdh.pyd
   │     │  ├─ win32pipe.pyd
   │     │  ├─ win32print.pyd
   │     │  ├─ win32process.pyd
   │     │  ├─ win32profile.pyd
   │     │  ├─ win32ras.pyd
   │     │  ├─ win32security.pyd
   │     │  ├─ win32service.pyd
   │     │  ├─ win32trace.pyd
   │     │  ├─ win32transaction.pyd
   │     │  ├─ win32ts.pyd
   │     │  ├─ win32wnet.pyd
   │     │  ├─ winxpgui.py
   │     │  ├─ _win32sysloader.pyd
   │     │  └─ _winxptheme.pyd
   │     ├─ win32com
   │     │  ├─ client
   │     │  │  ├─ build.py
   │     │  │  ├─ CLSIDToClass.py
   │     │  │  ├─ combrowse.py
   │     │  │  ├─ connect.py
   │     │  │  ├─ dynamic.py
   │     │  │  ├─ gencache.py
   │     │  │  ├─ genpy.py
   │     │  │  ├─ makepy.py
   │     │  │  ├─ selecttlb.py
   │     │  │  ├─ tlbrowse.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ demos
   │     │  │  ├─ connect.py
   │     │  │  ├─ dump_clipboard.py
   │     │  │  ├─ eventsApartmentThreaded.py
   │     │  │  ├─ eventsFreeThreaded.py
   │     │  │  ├─ excelAddin.py
   │     │  │  ├─ excelRTDServer.py
   │     │  │  ├─ iebutton.py
   │     │  │  ├─ ietoolbar.py
   │     │  │  ├─ outlookAddin.py
   │     │  │  ├─ trybag.py
   │     │  │  └─ __init__.py
   │     │  ├─ HTML
   │     │  │  ├─ COM_Records.html
   │     │  │  ├─ docindex.html
   │     │  │  ├─ GeneratedSupport.html
   │     │  │  ├─ image
   │     │  │  │  ├─ blank.gif
   │     │  │  │  ├─ BTN_HomePage.gif
   │     │  │  │  ├─ BTN_ManualTop.gif
   │     │  │  │  ├─ BTN_NextPage.gif
   │     │  │  │  ├─ BTN_PrevPage.gif
   │     │  │  │  ├─ pycom_blowing.gif
   │     │  │  │  ├─ pythoncom.gif
   │     │  │  │  └─ www_icon.gif
   │     │  │  ├─ index.html
   │     │  │  ├─ misc.html
   │     │  │  ├─ package.html
   │     │  │  ├─ PythonCOM.html
   │     │  │  ├─ QuickStartClientCom.html
   │     │  │  ├─ QuickStartServerCom.html
   │     │  │  └─ variant.html
   │     │  ├─ include
   │     │  │  ├─ PythonCOM.h
   │     │  │  ├─ PythonCOMRegister.h
   │     │  │  └─ PythonCOMServer.h
   │     │  ├─ libs
   │     │  │  ├─ axscript.lib
   │     │  │  └─ pythoncom.lib
   │     │  ├─ License.txt
   │     │  ├─ makegw
   │     │  │  ├─ makegw.py
   │     │  │  ├─ makegwenum.py
   │     │  │  ├─ makegwparse.py
   │     │  │  └─ __init__.py
   │     │  ├─ olectl.py
   │     │  ├─ readme.html
   │     │  ├─ server
   │     │  │  ├─ connect.py
   │     │  │  ├─ dispatcher.py
   │     │  │  ├─ exception.py
   │     │  │  ├─ factory.py
   │     │  │  ├─ localserver.py
   │     │  │  ├─ policy.py
   │     │  │  ├─ register.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ servers
   │     │  │  ├─ dictionary.py
   │     │  │  ├─ interp.py
   │     │  │  ├─ perfmon.py
   │     │  │  ├─ PythonTools.py
   │     │  │  ├─ test_pycomtest.py
   │     │  │  └─ __init__.py
   │     │  ├─ storagecon.py
   │     │  ├─ test
   │     │  │  ├─ daodump.py
   │     │  │  ├─ errorSemantics.py
   │     │  │  ├─ GenTestScripts.py
   │     │  │  ├─ pippo.idl
   │     │  │  ├─ pippo_server.py
   │     │  │  ├─ policySemantics.py
   │     │  │  ├─ readme.txt
   │     │  │  ├─ testAccess.py
   │     │  │  ├─ testADOEvents.py
   │     │  │  ├─ testall.py
   │     │  │  ├─ testArrays.py
   │     │  │  ├─ testAXScript.py
   │     │  │  ├─ testClipboard.py
   │     │  │  ├─ testCollections.py
   │     │  │  ├─ testConversionErrors.py
   │     │  │  ├─ testDates.py
   │     │  │  ├─ testDCOM.py
   │     │  │  ├─ testDictionary.py
   │     │  │  ├─ testDictionary.vbs
   │     │  │  ├─ testDynamic.py
   │     │  │  ├─ testExchange.py
   │     │  │  ├─ testExplorer.py
   │     │  │  ├─ testGatewayAddresses.py
   │     │  │  ├─ testGIT.py
   │     │  │  ├─ testInterp.vbs
   │     │  │  ├─ testIterators.py
   │     │  │  ├─ testmakepy.py
   │     │  │  ├─ testMarshal.py
   │     │  │  ├─ testMSOffice.py
   │     │  │  ├─ testMSOfficeEvents.py
   │     │  │  ├─ testPersist.py
   │     │  │  ├─ testPippo.py
   │     │  │  ├─ testPyComTest.py
   │     │  │  ├─ Testpys.sct
   │     │  │  ├─ testPyScriptlet.js
   │     │  │  ├─ testROT.py
   │     │  │  ├─ testServers.py
   │     │  │  ├─ testShell.py
   │     │  │  ├─ testStorage.py
   │     │  │  ├─ testStreams.py
   │     │  │  ├─ testvb.py
   │     │  │  ├─ testvbscript_regexp.py
   │     │  │  ├─ testWMI.py
   │     │  │  ├─ testxslt.js
   │     │  │  ├─ testxslt.py
   │     │  │  ├─ testxslt.xsl
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ universal.py
   │     │  ├─ util.py
   │     │  └─ __init__.py
   │     ├─ win32comext
   │     │  ├─ adsi
   │     │  │  ├─ adsi.pyd
   │     │  │  ├─ adsicon.py
   │     │  │  ├─ demos
   │     │  │  │  ├─ objectPicker.py
   │     │  │  │  ├─ scp.py
   │     │  │  │  ├─ search.py
   │     │  │  │  └─ test.py
   │     │  │  └─ __init__.py
   │     │  ├─ authorization
   │     │  │  ├─ authorization.pyd
   │     │  │  ├─ demos
   │     │  │  │  ├─ EditSecurity.py
   │     │  │  │  └─ EditServiceSecurity.py
   │     │  │  └─ __init__.py
   │     │  ├─ axcontrol
   │     │  │  ├─ axcontrol.pyd
   │     │  │  └─ __init__.py
   │     │  ├─ axdebug
   │     │  │  ├─ adb.py
   │     │  │  ├─ codecontainer.py
   │     │  │  ├─ contexts.py
   │     │  │  ├─ debugger.py
   │     │  │  ├─ documents.py
   │     │  │  ├─ dump.py
   │     │  │  ├─ expressions.py
   │     │  │  ├─ gateways.py
   │     │  │  ├─ stackframe.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ axscript
   │     │  │  ├─ asputil.py
   │     │  │  ├─ axscript.pyd
   │     │  │  ├─ client
   │     │  │  │  ├─ debug.py
   │     │  │  │  ├─ error.py
   │     │  │  │  ├─ framework.py
   │     │  │  │  ├─ pydumper.py
   │     │  │  │  ├─ pyscript.py
   │     │  │  │  ├─ pyscript_rexec.py
   │     │  │  │  ├─ scriptdispatch.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Demos
   │     │  │  │  └─ client
   │     │  │  │     ├─ asp
   │     │  │  │     │  ├─ caps.asp
   │     │  │  │     │  ├─ CreateObject.asp
   │     │  │  │     │  ├─ interrupt
   │     │  │  │     │  │  ├─ test.asp
   │     │  │  │     │  │  ├─ test.html
   │     │  │  │     │  │  ├─ test1.asp
   │     │  │  │     │  │  └─ test1.html
   │     │  │  │     │  └─ tut1.asp
   │     │  │  │     ├─ ie
   │     │  │  │     │  ├─ calc.htm
   │     │  │  │     │  ├─ CHARTPY.HTM
   │     │  │  │     │  ├─ dbgtest.htm
   │     │  │  │     │  ├─ demo.htm
   │     │  │  │     │  ├─ demo_check.htm
   │     │  │  │     │  ├─ demo_intro.htm
   │     │  │  │     │  ├─ demo_menu.htm
   │     │  │  │     │  ├─ docwrite.htm
   │     │  │  │     │  ├─ FOO.HTM
   │     │  │  │     │  ├─ foo2.htm
   │     │  │  │     │  ├─ form.htm
   │     │  │  │     │  ├─ marqueeDemo.htm
   │     │  │  │     │  ├─ MarqueeText1.htm
   │     │  │  │     │  ├─ mousetrack.htm
   │     │  │  │     │  └─ pycom_blowing.gif
   │     │  │  │     └─ wsh
   │     │  │  │        ├─ blank.pys
   │     │  │  │        ├─ excel.pys
   │     │  │  │        ├─ registry.pys
   │     │  │  │        └─ test.pys
   │     │  │  ├─ server
   │     │  │  │  ├─ axsite.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ test
   │     │  │  │  ├─ debugTest.pys
   │     │  │  │  ├─ debugTest.vbs
   │     │  │  │  ├─ leakTest.py
   │     │  │  │  ├─ testHost.py
   │     │  │  │  └─ testHost4Dbg.py
   │     │  │  └─ __init__.py
   │     │  ├─ bits
   │     │  │  ├─ bits.pyd
   │     │  │  ├─ test
   │     │  │  │  ├─ show_all_jobs.py
   │     │  │  │  └─ test_bits.py
   │     │  │  └─ __init__.py
   │     │  ├─ directsound
   │     │  │  ├─ directsound.pyd
   │     │  │  ├─ test
   │     │  │  │  ├─ ds_record.py
   │     │  │  │  ├─ ds_test.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ ifilter
   │     │  │  ├─ demo
   │     │  │  │  └─ filterDemo.py
   │     │  │  ├─ ifilter.pyd
   │     │  │  ├─ ifiltercon.py
   │     │  │  └─ __init__.py
   │     │  ├─ internet
   │     │  │  ├─ inetcon.py
   │     │  │  ├─ internet.pyd
   │     │  │  └─ __init__.py
   │     │  ├─ mapi
   │     │  │  ├─ demos
   │     │  │  │  └─ mapisend.py
   │     │  │  ├─ emsabtags.py
   │     │  │  ├─ exchange.pyd
   │     │  │  ├─ mapi.pyd
   │     │  │  ├─ mapitags.py
   │     │  │  ├─ mapiutil.py
   │     │  │  └─ __init__.py
   │     │  ├─ propsys
   │     │  │  ├─ propsys.pyd
   │     │  │  ├─ pscon.py
   │     │  │  ├─ test
   │     │  │  │  └─ testpropsys.py
   │     │  │  └─ __init__.py
   │     │  ├─ shell
   │     │  │  ├─ demos
   │     │  │  │  ├─ browse_for_folder.py
   │     │  │  │  ├─ create_link.py
   │     │  │  │  ├─ dump_link.py
   │     │  │  │  ├─ explorer_browser.py
   │     │  │  │  ├─ IActiveDesktop.py
   │     │  │  │  ├─ IFileOperationProgressSink.py
   │     │  │  │  ├─ IShellLinkDataList.py
   │     │  │  │  ├─ ITransferAdviseSink.py
   │     │  │  │  ├─ IUniformResourceLocator.py
   │     │  │  │  ├─ servers
   │     │  │  │  │  ├─ column_provider.py
   │     │  │  │  │  ├─ context_menu.py
   │     │  │  │  │  ├─ copy_hook.py
   │     │  │  │  │  ├─ empty_volume_cache.py
   │     │  │  │  │  ├─ folder_view.py
   │     │  │  │  │  ├─ icon_handler.py
   │     │  │  │  │  └─ shell_view.py
   │     │  │  │  ├─ shellexecuteex.py
   │     │  │  │  ├─ viewstate.py
   │     │  │  │  └─ walk_shell_folders.py
   │     │  │  ├─ shell.pyd
   │     │  │  ├─ shellcon.py
   │     │  │  ├─ test
   │     │  │  │  ├─ testShellFolder.py
   │     │  │  │  ├─ testShellItem.py
   │     │  │  │  └─ testSHFileOperation.py
   │     │  │  └─ __init__.py
   │     │  └─ taskscheduler
   │     │     ├─ taskscheduler.pyd
   │     │     ├─ test
   │     │     │  ├─ test_addtask.py
   │     │     │  ├─ test_addtask_1.py
   │     │     │  ├─ test_addtask_2.py
   │     │     │  └─ test_localsystem.py
   │     │     └─ __init__.py
   │     ├─ yaml
   │     │  ├─ composer.py
   │     │  ├─ constructor.py
   │     │  ├─ cyaml.py
   │     │  ├─ dumper.py
   │     │  ├─ emitter.py
   │     │  ├─ error.py
   │     │  ├─ events.py
   │     │  ├─ loader.py
   │     │  ├─ nodes.py
   │     │  ├─ parser.py
   │     │  ├─ reader.py
   │     │  ├─ representer.py
   │     │  ├─ resolver.py
   │     │  ├─ scanner.py
   │     │  ├─ serializer.py
   │     │  ├─ tokens.py
   │     │  ├─ _yaml.cp313-win_amd64.pyd
   │     │  └─ __init__.py
   │     ├─ _cffi_backend.cp313-win_amd64.pyd
   │     └─ _yaml
   │        └─ __init__.py
   ├─ pyvenv.cfg
   └─ Scripts
      ├─ activate
      ├─ activate.bat
      ├─ activate.fish
      ├─ Activate.ps1
      ├─ clear_comtypes_cache.exe
      ├─ ddgs.exe
      ├─ deactivate.bat
      ├─ dotenv.exe
      ├─ f2py.exe
      ├─ fastapi.exe
      ├─ httpx.exe
      ├─ httpx2.exe
      ├─ idna.exe
      ├─ normalizer.exe
      ├─ numpy-config.exe
      ├─ onnxruntime_test.exe
      ├─ pip.exe
      ├─ pip3.13.exe
      ├─ pip3.exe
      ├─ piper.exe
      ├─ playwright.exe
      ├─ python.exe
      ├─ pythonw.exe
      ├─ pywin32_postinstall.exe
      ├─ pywin32_postinstall.py
      ├─ pywin32_testall.exe
      ├─ pywin32_testall.py
      ├─ sprc.exe
      ├─ tqdm.exe
      ├─ uvicorn.exe
      ├─ watchfiles.exe
      └─ websockets.exe

```