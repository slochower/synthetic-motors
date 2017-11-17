import cPickle, base64
try:
	from SimpleSession.versions.v65 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 12, 41613])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v65 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwFOfYdVCWJhbGxTY2FsZXEDSwFHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAUc/8AAAAAAAAH2HVQVjb2xvcnEFSwFLAH2HVQpyaWJib25UeXBlcQZLAUsAfYdVCnN0aWNrU2NhbGVxB0sBRz/wAAAAAAAAfYdVDG1tQ0lGSGVhZGVyc3EIXXEJTmFVDGFyb21hdGljTW9kZXEKSwFLAX2HVQp2ZHdEZW5zaXR5cQtLAUdAFAAAAAAAAH2HVQZoaWRkZW5xDEsBiX2HVQ1hcm9tYXRpY0NvbG9ycQ1LAU59h1UPcmliYm9uU21vb3RoaW5ncQ5LAUsAfYdVCWF1dG9jaGFpbnEPSwGIfYdVCnBkYlZlcnNpb25xEEsBSwB9h1UIb3B0aW9uYWxxEX1xElUIb3BlbmVkQXNxE4iJSwEoVQsxNTQwNDQxLmNpZnEUTk5LAXRxFX2Hh3NVD2xvd2VyQ2FzZUNoYWluc3EWSwGJfYdVCWxpbmVXaWR0aHEXSwFHP/AAAAAAAAB9h1UPcmVzaWR1ZUxhYmVsUG9zcRhLAUsAfYdVBG5hbWVxGUsBWAsAAAAxNTQwNDQxLmNpZn2HVQ9hcm9tYXRpY0Rpc3BsYXlxGksBiX2HVQ9yaWJib25TdGlmZm5lc3NxG0sBRz/pmZmZmZmafYdVCnBkYkhlYWRlcnNxHF1xHX1xHmFVA2lkc3EfSwFLAEsAhn2HVQ5zdXJmYWNlT3BhY2l0eXEgSwFHv/AAAAAAAAB9h1UQYXJvbWF0aWNMaW5lVHlwZXEhSwFLAn2HVRRyaWJib25IaWRlc01haW5jaGFpbnEiSwGIfYdVB2Rpc3BsYXlxI0sBiH2HdS4='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksBVQEgfYdVC2ZpbGxEaXNwbGF5cQNLAYl9h1UEbmFtZXEESwFYDgAAAG1vX21vbGFuMzc4XzBtfYdVBWNoYWlucQVLAVgBAAAAIH2HVQ5yaWJib25EcmF3TW9kZXEGSwFLAn2HVQJzc3EHSwGJiYZ9h1UIbW9sZWN1bGVxCEsBSwB9h1ULcmliYm9uQ29sb3JxCUsBSwF9h1UFbGFiZWxxCksBWAAAAAB9h1UKbGFiZWxDb2xvcnELSwFLAX2HVQhmaWxsTW9kZXEMSwFLAH2HVQVpc0hldHENSwGIfYdVC2xhYmVsT2Zmc2V0cQ5LAU59h1UIcG9zaXRpb25xD11xEEsBSwGGcRFhVQ1yaWJib25EaXNwbGF5cRJLAYl9h1UIb3B0aW9uYWxxE31VBHNzSWRxFEsBSv////99h3Uu'))
	atomInfo = cPickle.loads(base64.b64decode('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/0sBhnFxSv////9LAYZxckr/////SwGGcXNK/////0sBhnF0Sv////9LAYZxdUr/////SwGGcXZK/////0sBhnF3Sv////9LAYZxeEr/////SwGGcXlK/////0sBhnF6Sv////9LAYZxe0r/////SwGGcXxK/////0sBhnF9Sv////9LAYZxfkr/////SwGGcX9K/////0sBhnGASv////9LAYZxgUr/////SwGGcYJK/////0sBhnGDSv////9LAYZxhEr/////SwGGcYVK/////0sBhnGGSv////9LAYZxh0r/////SwGGcYhK/////0sBhnGJSv////9LAYZxikr/////SwGGcYtK/////0sBhnGMSv////9LAYZxjUr/////SwGGcY5K/////0sBhnGPSv////9LAYZxkEr/////SwGGcZFK/////0sBhnGSSv////9LAYZxk0r/////SwGGcZRK/////0sBhnGVSv////9LAYZxlkr/////SwGGcZdK/////0sBhnGYSv////9LAYZxmUr/////SwGGcZpK/////0sBhnGbSv////9LAYZxnEr/////SwGGcZ1K/////0sBhnGeSv////9LAYZxn0r/////SwGGcaBK/////0sBhnGhSv////9LAYZxokr/////SwGGcaNlh1UHYmZhY3RvcnGkiIlLPUcAAAAAAAAAAH2Hh1UJb2NjdXBhbmN5caWIiUs9Rz/wAAAAAAAAfYeHVQZhbmlzb1VxpomJSz1OXXGnKFV7YXJyYXkoW1sgMC4wMjcgLCAgMC4wMDAyLCAgMC4wMDY5XSwKICAgICAgIFsgMC4wMDAyLCAgMC4wMTI3LCAtMC4wMDI4XSwKICAgICAgIFsgMC4wMDY5LCAtMC4wMDI4LCAgMC4wMTE2XV0sIGR0eXBlPWZsb2F0MzIpcahVe2FycmF5KFtbIDAuMDEzICwgIDAuMDAwOSwgIDAuMDA0Nl0sCiAgICAgICBbIDAuMDAwOSwgIDAuMDA4OCwgLTAuMDAxOV0sCiAgICAgICBbIDAuMDA0NiwgLTAuMDAxOSwgIDAuMDEwMl1dLCBkdHlwZT1mbG9hdDMyKXGpVXthcnJheShbWyAwLjAwNzgsIC0wLjAwMDYsICAwLjAwMiBdLAogICAgICAgWy0wLjAwMDYsICAwLjAxMSAsICAwLjAwMTJdLAogICAgICAgWyAwLjAwMiAsICAwLjAwMTIsICAwLjAxMDFdXSwgZHR5cGU9ZmxvYXQzMilxqlV7YXJyYXkoW1sgMC4wMTE4LCAgMC4wMDA4LCAgMC4wMDA5XSwKICAgICAgIFsgMC4wMDA4LCAgMC4wMTIzLCAtMC4wMDA1XSwKICAgICAgIFsgMC4wMDA5LCAtMC4wMDA1LCAgMC4wMTEyXV0sIGR0eXBlPWZsb2F0MzIpcatVe2FycmF5KFtbIDAuMDA5NCwgLTAuMDAxMSwgIDAuMDAyNV0sCiAgICAgICBbLTAuMDAxMSwgIDAuMDEwMiwgIDAuMDAxM10sCiAgICAgICBbIDAuMDAyNSwgIDAuMDAxMywgIDAuMDEwNl1dLCBkdHlwZT1mbG9hdDMyKXGsVXthcnJheShbWyAwLjAxNTMsICAwLiAgICAsICAwLjAwMzVdLAogICAgICAgWyAwLiAgICAsICAwLjAxNSAsIC0wLjAwMjVdLAogICAgICAgWyAwLjAwMzUsIC0wLjAwMjUsICAwLjAxMTZdXSwgZHR5cGU9ZmxvYXQzMilxrVUETm9uZXGuVXthcnJheShbWyAwLjAwOTEsIC0wLjAwMjIsICAwLjAwNDNdLAogICAgICAgWy0wLjAwMjIsICAwLjAxMDEsIC0wLjAwMTFdLAogICAgICAgWyAwLjAwNDMsIC0wLjAwMTEsICAwLjAxMzZdXSwgZHR5cGU9ZmxvYXQzMilxr1V7YXJyYXkoW1sgMC4wMTI3LCAgMC4wMDEzLCAgMC4wMDM5XSwKICAgICAgIFsgMC4wMDEzLCAgMC4wMTI2LCAgMC4wMDA3XSwKICAgICAgIFsgMC4wMDM5LCAgMC4wMDA3LCAgMC4wMTQxXV0sIGR0eXBlPWZsb2F0MzIpcbBVBE5vbmVxsVV7YXJyYXkoW1sgMC4wMTQyLCAtMC4wMDAyLCAgMC4wMDI5XSwKICAgICAgIFstMC4wMDAyLCAgMC4wMDggLCAgMC4wMDAzXSwKICAgICAgIFsgMC4wMDI5LCAgMC4wMDAzLCAgMC4wMiAgXV0sIGR0eXBlPWZsb2F0MzIpcbJVBE5vbmVxs1XMYXJyYXkoW1sgIDkuMjAwMDAwMjBlLTAzLCAgIDYuMDAwMDAwMjhlLTA0LCAgLTkuOTk5OTk5NzVlLTA1XSwKICAgICAgIFsgIDYuMDAwMDAwMjhlLTA0LCAgIDkuMTAwMDAwMzdlLTAzLCAgIDAuMDAwMDAwMDBlKzAwXSwKICAgICAgIFsgLTkuOTk5OTk5NzVlLTA1LCAgIDAuMDAwMDAwMDBlKzAwLCAgIDEuMTUwMDAwMDBlLTAyXV0sIGR0eXBlPWZsb2F0MzIpcbRVe2FycmF5KFtbIDAuMDE3MywgIDAuMDAyOCwgIDAuMDA0OV0sCiAgICAgICBbIDAuMDAyOCwgIDAuMDExICwgIDAuMDAwMl0sCiAgICAgICBbIDAuMDA0OSwgIDAuMDAwMiwgIDAuMDExIF1dLCBkdHlwZT1mbG9hdDMyKXG1VXthcnJheShbWyAwLjAxMzcsICAwLjAwMjIsICAwLjAwOTFdLAogICAgICAgWyAwLjAwMjIsICAwLjAxMSAsICAwLjAwMjFdLAogICAgICAgWyAwLjAwOTEsICAwLjAwMjEsICAwLjAyMiBdXSwgZHR5cGU9ZmxvYXQzMilxtlUETm9uZXG3VXthcnJheShbWyAwLjAxNDYsICAwLjAwMDgsICAwLjAwMSBdLAogICAgICAgWyAwLjAwMDgsICAwLjAxMDgsIC0wLjAwNDFdLAogICAgICAgWyAwLjAwMSAsIC0wLjAwNDEsICAwLjAxNiBdXSwgZHR5cGU9ZmxvYXQzMilxuFUETm9uZXG5VXthcnJheShbWyAwLjAwOTMsIC0wLjAwMDQsICAwLjAwNTNdLAogICAgICAgWy0wLjAwMDQsICAwLjAwOTYsICAwLjAwMDhdLAogICAgICAgWyAwLjAwNTMsICAwLjAwMDgsICAwLjAxNjFdXSwgZHR5cGU9ZmxvYXQzMilxulV7YXJyYXkoW1sgMC4wMTI3LCAgMC4wMDMgLCAgMC4wMDM3XSwKICAgICAgIFsgMC4wMDMgLCAgMC4wMTA4LCAgMC4wMDI2XSwKICAgICAgIFsgMC4wMDM3LCAgMC4wMDI2LCAgMC4wMTE5XV0sIGR0eXBlPWZsb2F0MzIpcbtVBE5vbmVxvFV7YXJyYXkoW1sgMC4wMDkxLCAgMC4wMDE5LCAgMC4wMDE3XSwKICAgICAgIFsgMC4wMDE5LCAgMC4wMDkgLCAtMC4wMDAzXSwKICAgICAgIFsgMC4wMDE3LCAtMC4wMDAzLCAgMC4wMTI2XV0sIGR0eXBlPWZsb2F0MzIpcb1Ve2FycmF5KFtbIDAuMDEyMSwgIDAuMDAxICwgIDAuMDAzN10sCiAgICAgICBbIDAuMDAxICwgIDAuMDEwNywgIDAuMDAyOF0sCiAgICAgICBbIDAuMDAzNywgIDAuMDAyOCwgIDAuMDE0OF1dLCBkdHlwZT1mbG9hdDMyKXG+VXthcnJheShbWyAwLjAwODYsIC0wLjAwMDIsICAwLjAwNDJdLAogICAgICAgWy0wLjAwMDIsICAwLjAwOTMsICAwLjAwMjVdLAogICAgICAgWyAwLjAwNDIsICAwLjAwMjUsICAwLjAxNDJdXSwgZHR5cGU9ZmxvYXQzMilxv1V7YXJyYXkoW1sgMC4wMTUzLCAgMC4wMDggLCAgMC4wMDY3XSwKICAgICAgIFsgMC4wMDggLCAgMC4wMTcgLCAgMC4wMDc2XSwKICAgICAgIFsgMC4wMDY3LCAgMC4wMDc2LCAgMC4wMjEgXV0sIGR0eXBlPWZsb2F0MzIpccBVBE5vbmVxwVXMYXJyYXkoW1sgIDEuOTMwMDAwMDdlLTAyLCAgIDMuMTk5OTk5OTJlLTAzLCAgIDEuNzk5OTk5OTdlLTAzXSwKICAgICAgIFsgIDMuMTk5OTk5OTJlLTAzLCAgIDEuNjU5OTk5OTdlLTAyLCAgIDkuOTk5OTk5NzVlLTA1XSwKICAgICAgIFsgIDEuNzk5OTk5OTdlLTAzLCAgIDkuOTk5OTk5NzVlLTA1LCAgIDEuMzYwMDAwMDJlLTAyXV0sIGR0eXBlPWZsb2F0MzIpccJVBE5vbmVxw1V7YXJyYXkoW1sgMC4wMjA1LCAtMC4wMDY5LCAgMC4wMDgzXSwKICAgICAgIFstMC4wMDY5LCAgMC4wMTY2LCAtMC4wMDgxXSwKICAgICAgIFsgMC4wMDgzLCAtMC4wMDgxLCAgMC4wMTk1XV0sIGR0eXBlPWZsb2F0MzIpccRVBE5vbmVxxVV7YXJyYXkoW1sgMC4wMTY3LCAtMC4wMDMxLCAgMC4wMDA5XSwKICAgICAgIFstMC4wMDMxLCAgMC4wMjI5LCAtMC4wMDI1XSwKICAgICAgIFsgMC4wMDA5LCAtMC4wMDI1LCAgMC4wMTMzXV0sIGR0eXBlPWZsb2F0MzIpccZVBE5vbmVxx1V7YXJyYXkoW1sgMC4wMDgxLCAtMC4wMDE4LCAgMC4wMDUxXSwKICAgICAgIFstMC4wMDE4LCAgMC4wMTE0LCAtMC4wMDAzXSwKICAgICAgIFsgMC4wMDUxLCAtMC4wMDAzLCAgMC4wMTcxXV0sIGR0eXBlPWZsb2F0MzIpcchVe2FycmF5KFtbIDAuMDI2MiwgIDAuMDAzNywgIDAuMDEwM10sCiAgICAgICBbIDAuMDAzNywgIDAuMDExNywgIDAuMDAwN10sCiAgICAgICBbIDAuMDEwMywgIDAuMDAwNywgIDAuMDE0N11dLCBkdHlwZT1mbG9hdDMyKXHJVXthcnJheShbWyAwLjAxMzEsICAwLjAwNTYsICAwLjAwMjhdLAogICAgICAgWyAwLjAwNTYsICAwLjAyICAsICAwLjAwNDldLAogICAgICAgWyAwLjAwMjgsICAwLjAwNDksICAwLjAxNTNdXSwgZHR5cGU9ZmxvYXQzMilxylUETm9uZXHLVQROb25lccxVBE5vbmVxzVV7YXJyYXkoW1sgMC4wMTc5LCAgMC4wMDIzLCAgMC4wMDU3XSwKICAgICAgIFsgMC4wMDIzLCAgMC4wMDk1LCAgMC4wMDIgXSwKICAgICAgIFsgMC4wMDU3LCAgMC4wMDIgLCAgMC4wMTU3XV0sIGR0eXBlPWZsb2F0MzIpcc5VBE5vbmVxz1UETm9uZXHQVXthcnJheShbWyAwLjAxMjcsIC0wLjAwMjEsICAwLjAwMzFdLAogICAgICAgWy0wLjAwMjEsICAwLjAxNCAsICAwLjAwMDRdLAogICAgICAgWyAwLjAwMzEsICAwLjAwMDQsICAwLjAxNTldXSwgZHR5cGU9ZmxvYXQzMilx0VUETm9uZXHSVXthcnJheShbWyAwLjAxOTEsIC0wLjAwNDUsICAwLjAwNDNdLAogICAgICAgWy0wLjAwNDUsICAwLjAyMTksIC0wLjAwOTFdLAogICAgICAgWyAwLjAwNDMsIC0wLjAwOTEsICAwLjAxNzldXSwgZHR5cGU9ZmxvYXQzMilx01UETm9uZXHUVXthcnJheShbWyAwLjAxNTIsICAwLjAwNTEsICAwLjAwMjldLAogICAgICAgWyAwLjAwNTEsICAwLjAyMTksICAwLjAwNDFdLAogICAgICAgWyAwLjAwMjksICAwLjAwNDEsICAwLjAxNDJdXSwgZHR5cGU9ZmxvYXQzMilx1VUETm9uZXHWVXthcnJheShbWyAwLjAxNTMsIC0wLjAwMDcsICAwLjAwNThdLAogICAgICAgWy0wLjAwMDcsICAwLjAxMyAsIC0wLjAwNDldLAogICAgICAgWyAwLjAwNTgsIC0wLjAwNDksICAwLjAyMjZdXSwgZHR5cGU9ZmxvYXQzMilx11UETm9uZXHYVXthcnJheShbWyAwLjA0MTIsICAwLjAwODUsICAwLjAxMyBdLAogICAgICAgWyAwLjAwODUsICAwLjAxMzgsICAwLjAwNjVdLAogICAgICAgWyAwLjAxMyAsICAwLjAwNjUsICAwLjAyMDFdXSwgZHR5cGU9ZmxvYXQzMilx2VUETm9uZXHaVXthcnJheShbWyAwLjA0MDIsICAwLjAxNDEsICAwLjAwMzddLAogICAgICAgWyAwLjAxNDEsICAwLjAyNzcsICAwLjAwNzldLAogICAgICAgWyAwLjAwMzcsICAwLjAwNzksICAwLjAxNDhdXSwgZHR5cGU9ZmxvYXQzMilx21UETm9uZXHcVXthcnJheShbWyAwLjAyOTgsIC0wLjAwMzQsICAwLjAxNDZdLAogICAgICAgWy0wLjAwMzQsICAwLjAwOTQsIC0wLjAwMyBdLAogICAgICAgWyAwLjAxNDYsIC0wLjAwMyAsICAwLjAyMjNdXSwgZHR5cGU9ZmxvYXQzMilx3VUETm9uZXHeVXthcnJheShbWyAwLjAzMTEsIC0wLjAwMjIsICAwLjAxMDRdLAogICAgICAgWy0wLjAwMjIsICAwLjAxODQsIC0wLjAwNzVdLAogICAgICAgWyAwLjAxMDQsIC0wLjAwNzUsICAwLjAxNzRdXSwgZHR5cGU9ZmxvYXQzMilx31UETm9uZXHgVQROb25lceFVBE5vbmVx4lV7YXJyYXkoW1sgMC4wMjQ3LCAgMC4wMDc0LCAtMC4wMDE1XSwKICAgICAgIFsgMC4wMDc0LCAgMC4wMjgzLCAgMC4wMDA0XSwKICAgICAgIFstMC4wMDE1LCAgMC4wMDA0LCAgMC4wMTU3XV0sIGR0eXBlPWZsb2F0MzIpceNVBE5vbmVx5GWHh3VVB2Rpc3BsYXlx5Us9iH1x5olOXXHnKEsGSwGGcehLCUsBhnHpSwtLAYZx6ksPSwGGcetLEUsBhnHsSxRLAYZx7UsZSwGGce5LG0sBhnHvSx1LAYZx8EsfSwGGcfFLI0sDhnHySydLAoZx80sqSwGGcfRLLEsBhnH1Sy5LAYZx9kswSwGGcfdLMksBhnH4SzRLAYZx+Us2SwGGcfpLOEsDhnH7SzxLAYZx/GWGc4d1Lg=='))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS0NOfYdVBWF0b21zcQNdcQQoXXEFKEsFSwJlXXEGKEs5SwJlXXEHKEsDSw9lXXEIKEsDSw5lXXEJKEsDSwdlXXEKKEsGSwRlXXELKEsESxVlXXEMKEsESxdlXXENKEsFSxJlXXEOKEsFSw5lXXEPKEsGSxllXXEQKEsGSwllXXERKEsHSx5lXXESKEsJSyJlXXETKEsJSytlXXEUKEsKSy9lXXEVKEsKSxllXXEWKEsMSxJlXXEXKEsMSxhlXXEYKEsOSxdlXXEZKEsPSxxlXXEaKEsPSyNlXXEbKEsUSxBlXXEcKEsQSxplXXEdKEsUSyJlXXEeKEsUSxllXXEfKEsVSyhlXXEgKEsVSyRlXXEhKEsXSxhlXXEiKEsYSyhlXXEjKEsaSy9lXXEkKEscSz1lXXElKEseSzdlXXEmKEsgSy1lXXEnKEsgSytlXXEoKEsiSzFlXXEpKEsjSzNlXXEqKEsjSzdlXXErKEstSzFlXXEsKEszSzVlXXEtKEs1Sz1lXXEuKEsHSwhlXXEvKEsKSwtlXXEwKEsMSw1lXXExKEsQSxFlXXEyKEsSSxNlXXEzKEsVSxZlXXE0KEsaSxtlXXE1KEscSx1lXXE2KEseSx9lXXE3KEsgSyFlXXE4KEskSyVlXXE5KEskSyZlXXE6KEskSydlXXE7KEsoSyllXXE8KEsoSyplXXE9KEsrSyxlXXE+KEstSy5lXXE/KEsvSzBlXXFAKEsxSzJlXXFBKEszSzRlXXFCKEs1SzZlXXFDKEs3SzhlXXFEKEs5SzplXXFFKEs5SztlXXFGKEs5SzxlXXFHKEs9Sz5lZVUFbGFiZWxxSEtDWAAAAAB9h1UIaGFsZmJvbmRxSUtDiH2HVQZyYWRpdXNxSktDRz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cUtLQ059h1UIZHJhd01vZGVxTEtDSwF9h1UIb3B0aW9uYWxxTX1VB2Rpc3BsYXlxTktDSwJ9h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {u'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), u'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), u'Rf': ((0.8, 0, 0.34902), 1, u'default'), u'Ra': ((0, 0.490196, 0), 1, u'default'), u'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), u'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), u'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), u'Be': ((0.760784, 1, 0), 1, u'default'), u'Ba': ((0, 0.788235, 0), 1, u'default'), u'Bh': ((0.878431, 0, 0.219608), 1, u'default'), u'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), u'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), u'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), u'H': ((1, 1, 1), 1, u'default'), u'P': ((1, 0.501961, 0), 1, u'default'), u'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), u'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), u'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), u'Gd': ((0.270588, 1, 0.780392), 1, u'default'), u'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), u'Pr': ((0.85098, 1, 0.780392), 1, u'default'), u'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'),
u'Pu': ((0, 0.419608, 1), 1, u'default'), u'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), u'grey': ((0.745098, 0.745098, 0.745098), 1, u'default'), u'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), u'Pa': ((0, 0.631373, 1), 1, u'default'), u'Pd': ((0, 0.411765, 0.521569), 1, u'default'), u'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), u'Po': ((0.670588, 0.360784, 0), 1, u'default'), u'Pm': ((0.639216, 1, 0.780392), 1, u'default'), u'Hs': ((0.901961, 0, 0.180392), 1, u'default'), u'Ho': ((0, 1, 0.611765), 1, u'default'), u'Hf': ((0.301961, 0.760784, 1), 1, u'default'), u'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), u'He': ((0.85098, 1, 1), 1, u'default'), u'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), u'Mg': ((0.541176, 1, 0), 1, u'default'), u'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), u'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), u'O': ((1, 0.0509804, 0.0509804), 1, u'default'), u'Mt': ((0.921569, 0, 0.14902), 1, u'default'), u'S': ((1, 1, 0.188235), 1, u'default'), u'W': ((0.129412, 0.580392, 0.839216), 1, u'default'),
u'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), u'Eu': ((0.380392, 1, 0.780392), 1, u'default'), u'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), u'Er': ((0, 0.901961, 0.458824), 1, u'default'), u'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), u'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), u'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), u'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), u'Nd': ((0.780392, 1, 0.780392), 1, u'default'), u'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), u'Np': ((0, 0.501961, 1), 1, u'default'), u'Fr': ((0.258824, 0, 0.4), 1, u'default'), u'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), u'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), u'B': ((1, 0.709804, 0.709804), 1, u'default'), u'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), u'Sr': ((0, 1, 0), 1, u'default'), u'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), u'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), u'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), u'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'),
u'Sm': ((0.560784, 1, 0.780392), 1, u'default'), u'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), u'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), u'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), u'Sg': ((0.85098, 0, 0.270588), 1, u'default'), u'Se': ((1, 0.631373, 0), 1, u'default'), u'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), u'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), u'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), u'Ca': ((0.239216, 1, 0), 1, u'default'), u'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), u'Ce': ((1, 1, 0.780392), 1, u'default'), u'Cd': ((1, 0.85098, 0.560784), 1, u'default'), u'Tm': ((0, 0.831373, 0.321569), 1, u'default'), u'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), u'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), u'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), u'La': ((0.439216, 0.831373, 1), 1, u'default'), u'Li': ((0.8, 0.501961, 1), 1, u'default'), u'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), u'Lu': ((0, 0.670588, 0.141176), 1, u'default'), u'Lr': ((0.780392, 0, 0.4), 1, u'default'),
u'Th': ((0, 0.729412, 1), 1, u'default'), u'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), u'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), u'Te': ((0.831373, 0.478431, 0), 1, u'default'), u'Tb': ((0.188235, 1, 0.780392), 1, u'default'), u'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), u'Ta': ((0.301961, 0.65098, 1), 1, u'default'), u'Yb': ((0, 0.74902, 0.219608), 1, u'default'), u'Db': ((0.819608, 0, 0.309804), 1, u'default'), u'Dy': ((0.121569, 1, 0.780392), 1, u'default'), u'I': ((0.580392, 0, 0.580392), 1, u'default'), u'medium purple': ((0.576471, 0.439216, 0.858824), 1, u'default'), u'U': ((0, 0.560784, 1), 1, u'default'), u'Y': ((0.580392, 1, 1), 1, u'default'), u'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), u'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), u'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), u'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), u'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), u'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), u'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'),
u'Au': ((1, 0.819608, 0.137255), 1, u'default'), u'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), u'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), u'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default')}
	materials = {u'default': ((0, 0, 0), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'labelOffset': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 4, {}), 'optional': {'fixedLabels': (True, False, (1, 0, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (7, (u'H', (1, 1, 1, 1)), {(u'', (1, 1, 1, 1)): [5], (u'O', (1, 0.0509804, 0.0509804, 1)): [2], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'grey', (0.745098, 0.745098, 0.745098, 1)): [1], (u'yellow', (1, 1, 0, 1)): [4], (u'', (0.4, 0, 1, 1)): [6]})
	viewerInfo = {'cameraAttrs': {'center': (1.3395405316556, 3.95058375, 8.7265950464312), 'fieldOfView': 18.849684534934, 'nearFar': (16.370238401986, 1.1650406451953), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 8.7265950464312}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': True, 'showShadows': False, 'viewSize': 8.8688270917569, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 1.1553511596919, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 6, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 5}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v65 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restore_cap_attributes():
 cap_attributes = \
  {
   'cap_attributes': [
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 1, 0, ),
      'version': 1,
     },
    ],
   'cap_color': None,
   'cap_offset': 0.01,
   'class': 'Caps_State',
   'default_cap_offset': 0.01,
   'mesh_style': False,
   'shown': True,
   'subdivision_factor': 1.0,
   'version': 1,
  }
 import SurfaceCap.session
 SurfaceCap.session.restore_cap_attributes(cap_attributes)
registerAfterModelsCB(restore_cap_attributes)


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [ ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = []
	userXSections = []
	userResidueClasses = []
	residueData = [(1, 'Chimera default', 'rounded', u'unknown')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDWgEVQRtb2RlcQ5VBmxpbmVhcnEPdWJVCGtleWZyYW1lcRBoBSmBcRF9cRIoaAhLFGgJSwFoCl1xE2gMYWgNaBBoDmgPdWJVBXNjZW5lcRRoBSmBcRV9cRYoaAhLAWgJSwFoCl1xF2gMYWgNaBRoDmgPdWJ1Yi4='
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 0.0], 'back': [(0.35740674433659325, 0.6604015517481454, -0.6604015517481455), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.35740674433659325, 0.6604015517481454, 0.6604015517481455), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.25056280708573153, 0.25056280708573153, 0.9351131265310293), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


def restoreRemainder():
	from SimpleSession.versions.v65 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (1007, 831)
	xformMap = {0: (((-0.40316560742266, 0.88341604946458, -0.23881703569871), 65.779607196638), (-6.9111333244389, -1.0220903251563, 7.8002263788571), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 130: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v65 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v65 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

