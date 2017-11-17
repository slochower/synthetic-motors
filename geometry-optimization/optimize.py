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
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwJOfYdVCWJhbGxTY2FsZXEDSwJHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAkc/8AAAAAAAAH2HVQVjb2xvcnEFSwJLAH1xBksBXXEHSwFhc4dVCnJpYmJvblR5cGVxCEsCSwB9h1UKc3RpY2tTY2FsZXEJSwJHP/AAAAAAAAB9h1UMbW1DSUZIZWFkZXJzcQpdcQsoTk5lVQxhcm9tYXRpY01vZGVxDEsCSwF9h1UKdmR3RGVuc2l0eXENSwJHQBQAAAAAAAB9h1UGaGlkZGVucQ5LAol9h1UNYXJvbWF0aWNDb2xvcnEPSwJOfYdVD3JpYmJvblNtb290aGluZ3EQSwJLAH2HVQlhdXRvY2hhaW5xEUsCiH2HVQpwZGJWZXJzaW9ucRJLAksAfYdVCG9wdGlvbmFscRN9cRRVCG9wZW5lZEFzcRWIiUsCKFULMTU0MDQ0MS5jaWZxFk5OSwF0cRd9cRgoVVsvaG9tZS9kc2xvY2hvd2VyL2hnc3QtM3RiLWRhdGEvcHJvamVjdHMvc3ludGhldGljLW1vdG9ycy9nZW9tZXRyeS1vcHRpbWl6YXRpb24vb3B0aW1pemUueHl6cRlVDlhZWiBjb29yZGluYXRlcRpOiXRxG11xHEsBYXOHh3NVD2xvd2VyQ2FzZUNoYWluc3EdSwKJfYdVCWxpbmVXaWR0aHEeSwJHP/AAAAAAAAB9h1UPcmVzaWR1ZUxhYmVsUG9zcR9LAksAfYdVBG5hbWVxIEsCWAsAAAAxNTQwNDQxLmNpZn1xIVgQAAAAdW5rbm93biBtb2xlY3VsZV1xIksBYXOHVQ9hcm9tYXRpY0Rpc3BsYXlxI0sCiX2HVQ9yaWJib25TdGlmZm5lc3NxJEsCRz/pmZmZmZmafYdVCnBkYkhlYWRlcnNxJV1xJih9cSd9cShlVQNpZHNxKUsCSwFLAIZ9cSpLAEsAhl1xK0sAYXOHVQ5zdXJmYWNlT3BhY2l0eXEsSwJHv/AAAAAAAAB9h1UQYXJvbWF0aWNMaW5lVHlwZXEtSwJLAn2HVRRyaWJib25IaWRlc01haW5jaGFpbnEuSwKIfYdVB2Rpc3BsYXlxL0sCiH2HdS4='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksCVQEgfYdVC2ZpbGxEaXNwbGF5cQNLAol9cQSITl1xBUsASwGGcQZhhnOHVQRuYW1lcQdLAlgOAAAAbW9fbW9sYW4zNzhfMG19cQhYAwAAAFVOS11xCUsBYXOHVQVjaGFpbnEKSwJYAQAAACB9h1UOcmliYm9uRHJhd01vZGVxC0sCSwJ9h1UCc3NxDEsCiYmGfYdVCG1vbGVjdWxlcQ1LAksAfXEOSwFOXXEPSwFLAYZxEGGGc4dVC3JpYmJvbkNvbG9ycRFLAksCfXESSwNOXXETSwFLAYZxFGGGc4dVBWxhYmVscRVLAlgAAAAAfYdVCmxhYmVsQ29sb3JxFksCSwJ9cRdLA05dcRhLAUsBhnEZYYZzh1UIZmlsbE1vZGVxGksCSwB9cRtLAU5dcRxLAUsBhnEdYYZzh1UFaXNIZXRxHksCiX1xH4hOXXEgSwBLAYZxIWGGc4dVC2xhYmVsT2Zmc2V0cSJLAk59h1UIcG9zaXRpb25xI11xJChLAUsBhnElSwFLAYZxJmVVDXJpYmJvbkRpc3BsYXlxJ0sCiX2HVQhvcHRpb25hbHEofVUEc3NJZHEpSwJK/////32HdS4='))
	atomInfo = cPickle.loads(base64.b64decode('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LjAwMDgsICAwLjAxMjMsIC0wLjAwMDVdLAogICAgICAgWyAwLjAwMDksIC0wLjAwMDUsICAwLjAxMTJdXSwgZHR5cGU9ZmxvYXQzMilxxlV7YXJyYXkoW1sgMC4wMDk0LCAtMC4wMDExLCAgMC4wMDI1XSwKICAgICAgIFstMC4wMDExLCAgMC4wMTAyLCAgMC4wMDEzXSwKICAgICAgIFsgMC4wMDI1LCAgMC4wMDEzLCAgMC4wMTA2XV0sIGR0eXBlPWZsb2F0MzIpccdVe2FycmF5KFtbIDAuMDE1MywgIDAuICAgICwgIDAuMDAzNV0sCiAgICAgICBbIDAuICAgICwgIDAuMDE1ICwgLTAuMDAyNV0sCiAgICAgICBbIDAuMDAzNSwgLTAuMDAyNSwgIDAuMDExNl1dLCBkdHlwZT1mbG9hdDMyKXHIVQROb25lcclVe2FycmF5KFtbIDAuMDA5MSwgLTAuMDAyMiwgIDAuMDA0M10sCiAgICAgICBbLTAuMDAyMiwgIDAuMDEwMSwgLTAuMDAxMV0sCiAgICAgICBbIDAuMDA0MywgLTAuMDAxMSwgIDAuMDEzNl1dLCBkdHlwZT1mbG9hdDMyKXHKVXthcnJheShbWyAwLjAxMjcsICAwLjAwMTMsICAwLjAwMzldLAogICAgICAgWyAwLjAwMTMsICAwLjAxMjYsICAwLjAwMDddLAogICAgICAgWyAwLjAwMzksICAwLjAwMDcsICAwLjAxNDFdXSwgZHR5cGU9ZmxvYXQzMilxy1UETm9uZXHMVXthcnJheShbWyAwLjAxNDIsIC0wLjAwMDIsICAwLjAwMjldLAogICAgICAgWy0wLjAwMDIsICAwLjAwOCAsICAwLjAwMDNdLAogICAgICAgWyAwLjAwMjksICAwLjAwMDMsICAwLjAyICBdXSwgZHR5cGU9ZmxvYXQzMilxzVUETm9uZXHOVcxhcnJheShbWyAgOS4yMDAwMDAyMGUtMDMsICAgNi4wMDAwMDAyOGUtMDQsICAtOS45OTk5OTk3NWUtMDVdLAogICAgICAgWyAgNi4wMDAwMDAyOGUtMDQsICAgOS4xMDAwMDAzN2UtMDMsICAgMC4wMDAwMDAwMGUrMDBdLAogICAgICAgWyAtOS45OTk5OTk3NWUtMDUsICAgMC4wMDAwMDAwMGUrMDAsICAgMS4xNTAwMDAwMGUtMDJdXSwgZHR5cGU9ZmxvYXQzMilxz1V7YXJyYXkoW1sgMC4wMTczLCAgMC4wMDI4LCAgMC4wMDQ5XSwKICAgICAgIFsgMC4wMDI4LCAgMC4wMTEgLCAgMC4wMDAyXSwKICAgICAgIFsgMC4wMDQ5LCAgMC4wMDAyLCAgMC4wMTEgXV0sIGR0eXBlPWZsb2F0MzIpcdBVe2FycmF5KFtbIDAuMDEzNywgIDAuMDAyMiwgIDAuMDA5MV0sCiAgICAgICBbIDAuMDAyMiwgIDAuMDExICwgIDAuMDAyMV0sCiAgICAgICBbIDAuMDA5MSwgIDAuMDAyMSwgIDAuMDIyIF1dLCBkdHlwZT1mbG9hdDMyKXHRVQROb25lcdJVe2FycmF5KFtbIDAuMDE0NiwgIDAuMDAwOCwgIDAuMDAxIF0sCiAgICAgICBbIDAuMDAwOCwgIDAuMDEwOCwgLTAuMDA0MV0sCiAgICAgICBbIDAuMDAxICwgLTAuMDA0MSwgIDAuMDE2IF1dLCBkdHlwZT1mbG9hdDMyKXHTVQROb25lcdRVe2FycmF5KFtbIDAuMDA5MywgLTAuMDAwNCwgIDAuMDA1M10sCiAgICAgICBbLTAuMDAwNCwgIDAuMDA5NiwgIDAuMDAwOF0sCiAgICAgICBbIDAuMDA1MywgIDAuMDAwOCwgIDAuMDE2MV1dLCBkdHlwZT1mbG9hdDMyKXHVVXthcnJheShbWyAwLjAxMjcsICAwLjAwMyAsICAwLjAwMzddLAogICAgICAgWyAwLjAwMyAsICAwLjAxMDgsICAwLjAwMjZdLAogICAgICAgWyAwLjAwMzcsICAwLjAwMjYsICAwLjAxMTldXSwgZHR5cGU9ZmxvYXQzMilx1lUETm9uZXHXVXthcnJheShbWyAwLjAwOTEsICAwLjAwMTksICAwLjAwMTddLAogICAgICAgWyAwLjAwMTksICAwLjAwOSAsIC0wLjAwMDNdLAogICAgICAgWyAwLjAwMTcsIC0wLjAwMDMsICAwLjAxMjZdXSwgZHR5cGU9ZmxvYXQzMilx2FV7YXJyYXkoW1sgMC4wMTIxLCAgMC4wMDEgLCAgMC4wMDM3XSwKICAgICAgIFsgMC4wMDEgLCAgMC4wMTA3LCAgMC4wMDI4XSwKICAgICAgIFsgMC4wMDM3LCAgMC4wMDI4LCAgMC4wMTQ4XV0sIGR0eXBlPWZsb2F0MzIpcdlVe2FycmF5KFtbIDAuMDA4NiwgLTAuMDAwMiwgIDAuMDA0Ml0sCiAgICAgICBbLTAuMDAwMiwgIDAuMDA5MywgIDAuMDAyNV0sCiAgICAgICBbIDAuMDA0MiwgIDAuMDAyNSwgIDAuMDE0Ml1dLCBkdHlwZT1mbG9hdDMyKXHaVXthcnJheShbWyAwLjAxNTMsICAwLjAwOCAsICAwLjAwNjddLAogICAgICAgWyAwLjAwOCAsICAwLjAxNyAsICAwLjAwNzZdLAogICAgICAgWyAwLjAwNjcsICAwLjAwNzYsICAwLjAyMSBdXSwgZHR5cGU9ZmxvYXQzMilx21UETm9uZXHcVcxhcnJheShbWyAgMS45MzAwMDAwN2UtMDIsICAgMy4xOTk5OTk5MmUtMDMsICAgMS43OTk5OTk5N2UtMDNdLAogICAgICAgWyAgMy4xOTk5OTk5MmUtMDMsICAgMS42NTk5OTk5N2UtMDIsICAgOS45OTk5OTk3NWUtMDVdLAogICAgICAgWyAgMS43OTk5OTk5N2UtMDMsICAgOS45OTk5OTk3NWUtMDUsICAgMS4zNjAwMDAwMmUtMDJdXSwgZHR5cGU9ZmxvYXQzMilx3VUETm9uZXHeVXthcnJheShbWyAwLjAyMDUsIC0wLjAwNjksICAwLjAwODNdLAogICAgICAgWy0wLjAwNjksICAwLjAxNjYsIC0wLjAwODFdLAogICAgICAgWyAwLjAwODMsIC0wLjAwODEsICAwLjAxOTVdXSwgZHR5cGU9ZmxvYXQzMilx31UETm9uZXHgVXthcnJheShbWyAwLjAxNjcsIC0wLjAwMzEsICAwLjAwMDldLAogICAgICAgWy0wLjAwMzEsICAwLjAyMjksIC0wLjAwMjVdLAogICAgICAgWyAwLjAwMDksIC0wLjAwMjUsICAwLjAxMzNdXSwgZHR5cGU9ZmxvYXQzMilx4VUETm9uZXHiVXthcnJheShbWyAwLjAwODEsIC0wLjAwMTgsICAwLjAwNTFdLAogICAgICAgWy0wLjAwMTgsICAwLjAxMTQsIC0wLjAwMDNdLAogICAgICAgWyAwLjAwNTEsIC0wLjAwMDMsICAwLjAxNzFdXSwgZHR5cGU9ZmxvYXQzMilx41V7YXJyYXkoW1sgMC4wMjYyLCAgMC4wMDM3LCAgMC4wMTAzXSwKICAgICAgIFsgMC4wMDM3LCAgMC4wMTE3LCAgMC4wMDA3XSwKICAgICAgIFsgMC4wMTAzLCAgMC4wMDA3LCAgMC4wMTQ3XV0sIGR0eXBlPWZsb2F0MzIpceRVe2FycmF5KFtbIDAuMDEzMSwgIDAuMDA1NiwgIDAuMDAyOF0sCiAgICAgICBbIDAuMDA1NiwgIDAuMDIgICwgIDAuMDA0OV0sCiAgICAgICBbIDAuMDAyOCwgIDAuMDA0OSwgIDAuMDE1M11dLCBkdHlwZT1mbG9hdDMyKXHlVQROb25lceZVBE5vbmVx51UETm9uZXHoVXthcnJheShbWyAwLjAxNzksICAwLjAwMjMsICAwLjAwNTddLAogICAgICAgWyAwLjAwMjMsICAwLjAwOTUsICAwLjAwMiBdLAogICAgICAgWyAwLjAwNTcsICAwLjAwMiAsICAwLjAxNTddXSwgZHR5cGU9ZmxvYXQzMilx6VUETm9uZXHqVQROb25lcetVe2FycmF5KFtbIDAuMDEyNywgLTAuMDAyMSwgIDAuMDAzMV0sCiAgICAgICBbLTAuMDAyMSwgIDAuMDE0ICwgIDAuMDAwNF0sCiAgICAgICBbIDAuMDAzMSwgIDAuMDAwNCwgIDAuMDE1OV1dLCBkdHlwZT1mbG9hdDMyKXHsVQROb25lce1Ve2FycmF5KFtbIDAuMDE5MSwgLTAuMDA0NSwgIDAuMDA0M10sCiAgICAgICBbLTAuMDA0NSwgIDAuMDIxOSwgLTAuMDA5MV0sCiAgICAgICBbIDAuMDA0MywgLTAuMDA5MSwgIDAuMDE3OV1dLCBkdHlwZT1mbG9hdDMyKXHuVQROb25lce9Ve2FycmF5KFtbIDAuMDE1MiwgIDAuMDA1MSwgIDAuMDAyOV0sCiAgICAgICBbIDAuMDA1MSwgIDAuMDIxOSwgIDAuMDA0MV0sCiAgICAgICBbIDAuMDAyOSwgIDAuMDA0MSwgIDAuMDE0Ml1dLCBkdHlwZT1mbG9hdDMyKXHwVQROb25lcfFVe2FycmF5KFtbIDAuMDE1MywgLTAuMDAwNywgIDAuMDA1OF0sCiAg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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS4ZOfYdVBWF0b21zcQNdcQQoXXEFKEsHSwRlXXEGKEs7SwRlXXEHKEsFSxFlXXEIKEsFSxBlXXEJKEsFSwllXXEKKEsISwZlXXELKEsGSxdlXXEMKEsGSxllXXENKEsHSxRlXXEOKEsHSxBlXXEPKEsISxtlXXEQKEsISwtlXXERKEsJSyBlXXESKEsLSyRlXXETKEsLSy1lXXEUKEsMSzFlXXEVKEsMSxtlXXEWKEsOSxRlXXEXKEsOSxplXXEYKEsQSxllXXEZKEsRSx5lXXEaKEsRSyVlXXEbKEsWSxJlXXEcKEsSSxxlXXEdKEsWSyRlXXEeKEsWSxtlXXEfKEsXSyplXXEgKEsXSyZlXXEhKEsZSxplXXEiKEsaSyplXXEjKEscSzFlXXEkKEseSz9lXXElKEsgSzllXXEmKEsiSy9lXXEnKEsiSy1lXXEoKEskSzNlXXEpKEslSzVlXXEqKEslSzllXXErKEsvSzNlXXEsKEs1SzdlXXEtKEs3Sz9lXXEuKEsJSwplXXEvKEsMSw1lXXEwKEsOSw9lXXExKEsSSxNlXXEyKEsUSxVlXXEzKEsXSxhlXXE0KEscSx1lXXE1KEseSx9lXXE2KEsgSyFlXXE3KEsiSyNlXXE4KEsmSydlXXE5KEsmSyhlXXE6KEsmSyllXXE7KEsqSytlXXE8KEsqSyxlXXE9KEstSy5lXXE+KEsvSzBlXXE/KEsxSzJlXXFAKEszSzRlXXFBKEs1SzZlXXFCKEs3SzhlXXFDKEs5SzplXXFEKEs7SzxlXXFFKEs7Sz1lXXFGKEs7Sz5lXXFHKEs/S0BlXXFIKEtBS0RlXXFJKEtBS3hlXXFKKEtCS0ZlXXFLKEtCS01lXXFMKEtCS05lXXFNKEtDS0VlXXFOKEtDS1RlXXFPKEtDS1ZlXXFQKEtES01lXXFRKEtES1FlXXFSKEtFS0hlXXFTKEtFS1hlXXFUKEtGS0dlXXFVKEtGS11lXXFWKEtIS2FlXXFXKEtIS2plXXFYKEtJS0plXXFZKEtJS1hlXXFaKEtJS25lXXFbKEtLS0xlXXFcKEtLS1FlXXFdKEtLS1dlXXFeKEtNS1ZlXXFfKEtOS1tlXXFgKEtOS2JlXXFhKEtPS1BlXXFiKEtPS1NlXXFjKEtPS1llXXFkKEtRS1JlXXFlKEtTS1hlXXFmKEtTS2FlXXFnKEtUS1VlXXFoKEtUS2NlXXFpKEtUS2dlXXFqKEtWS1dlXXFrKEtXS2dlXXFsKEtZS1plXXFtKEtZS25lXXFuKEtbS1xlXXFvKEtbS3xlXXFwKEtdS15lXXFxKEtdS3ZlXXFyKEtfS2BlXXFzKEtfS2plXXF0KEtfS2xlXXF1KEthS3BlXXF2KEtiS3JlXXF3KEtiS3ZlXXF4KEtjS2RlXXF5KEtjS2VlXXF6KEtjS2ZlXXF7KEtnS2hlXXF8KEtnS2llXXF9KEtqS2tlXXF+KEtsS21lXXF/KEtsS3BlXXGAKEtuS29lXXGBKEtwS3FlXXGCKEtyS3NlXXGDKEtyS3RlXXGEKEt0S3VlXXGFKEt0S3xlXXGGKEt2S3dlXXGHKEt4S3llXXGIKEt4S3plXXGJKEt4S3tlXXGKKEt8S31lZVUFbGFiZWxxi0uGWAAAAAB9h1UIaGFsZmJvbmRxjEuGiH2HVQZyYWRpdXNxjUuGRz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cY5Lhk59h1UIZHJhd01vZGVxj0uGSwF9h1UIb3B0aW9uYWxxkH1VB2Rpc3BsYXlxkUuGSwJ9h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {u'': ((0.823529, 0.705882, 0.54902), 1, u''), u'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), u'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), u'Rf': ((0.8, 0, 0.34902), 1, u'default'), u'Ra': ((0, 0.490196, 0), 1, u'default'), u'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), u'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), u'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), u'Be': ((0.760784, 1, 0), 1, u'default'), u'Ba': ((0, 0.788235, 0), 1, u'default'), u'Bh': ((0.878431, 0, 0.219608), 1, u'default'), u'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), u'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), u'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), u'H': ((1, 1, 1), 1, u'default'), u'P': ((1, 0.501961, 0), 1, u'default'), u'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), u'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), u'Gd': ((0.270588, 1, 0.780392), 1, u'default'), u'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), u'Pr': ((0.85098, 1, 0.780392), 1, u'default'), u'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'),
u'Pu': ((0, 0.419608, 1), 1, u'default'), u'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), u'grey': ((0.745098, 0.745098, 0.745098), 1, u'default'), u'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), u'Pa': ((0, 0.631373, 1), 1, u'default'), u'Pd': ((0, 0.411765, 0.521569), 1, u'default'), u'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), u'Po': ((0.670588, 0.360784, 0), 1, u'default'), u'Pm': ((0.639216, 1, 0.780392), 1, u'default'), u'Hs': ((0.901961, 0, 0.180392), 1, u'default'), u'Ho': ((0, 1, 0.611765), 1, u'default'), u'Hf': ((0.301961, 0.760784, 1), 1, u'default'), u'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), u'He': ((0.85098, 1, 1), 1, u'default'), u'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), u'Mg': ((0.541176, 1, 0), 1, u'default'), u'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), u'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), u'O': ((1, 0.0509804, 0.0509804), 1, u'default'), u'Mt': ((0.921569, 0, 0.14902), 1, u'default'), u'S': ((1, 1, 0.188235), 1, u'default'), u'W': ((0.129412, 0.580392, 0.839216), 1, u'default'),
u'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), u'Eu': ((0.380392, 1, 0.780392), 1, u'default'), u'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), u'Er': ((0, 0.901961, 0.458824), 1, u'default'), u'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), u'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), u'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), u'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), u'Nd': ((0.780392, 1, 0.780392), 1, u'default'), u'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), u'Np': ((0, 0.501961, 1), 1, u'default'), u'Fr': ((0.258824, 0, 0.4), 1, u'default'), u'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), u'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), u'B': ((1, 0.709804, 0.709804), 1, u'default'), u'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), u'Sr': ((0, 1, 0), 1, u'default'), u'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), u'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), u'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), u'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'),
u'Sm': ((0.560784, 1, 0.780392), 1, u'default'), u'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), u'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), u'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), u'Sg': ((0.85098, 0, 0.270588), 1, u'default'), u'Se': ((1, 0.631373, 0), 1, u'default'), u'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), u'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), u'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), u'Ca': ((0.239216, 1, 0), 1, u'default'), u'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), u'Ce': ((1, 1, 0.780392), 1, u'default'), u'Cd': ((1, 0.85098, 0.560784), 1, u'default'), u'Lu': ((0, 0.670588, 0.141176), 1, u'default'), u'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), u'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), u'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), u'La': ((0.439216, 0.831373, 1), 1, u'default'), u'Li': ((0.8, 0.501961, 1), 1, u'default'), u'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), u'Tm': ((0, 0.831373, 0.321569), 1, u'default'), u'Lr': ((0.780392, 0, 0.4), 1, u'default'),
u'Th': ((0, 0.729412, 1), 1, u'default'), u'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), u'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), u'Te': ((0.831373, 0.478431, 0), 1, u'default'), u'Tb': ((0.188235, 1, 0.780392), 1, u'default'), u'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), u'Ta': ((0.301961, 0.65098, 1), 1, u'default'), u'Yb': ((0, 0.74902, 0.219608), 1, u'default'), u'Db': ((0.819608, 0, 0.309804), 1, u'default'), u'Dy': ((0.121569, 1, 0.780392), 1, u'default'), u'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), u'I': ((0.580392, 0, 0.580392), 1, u'default'), u'medium purple': ((0.576471, 0.439216, 0.858824), 1, u'default'), u'U': ((0, 0.560784, 1), 1, u'default'), u'Y': ((0.580392, 1, 1), 1, u'default'), u'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), u'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), u'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), u'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), u'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), u'As': ((0.741176, 0.501961, 0.890196), 1, u'default'),
u'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), u'Au': ((1, 0.819608, 0.137255), 1, u'default'), u'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), u'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), u'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default')}
	materials = {u'': ((0, 0, 0), 30), u'default': ((0, 0, 0), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'labelOffset': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 7, {}), 'optional': {'fixedLabels': (True, False, (1, 0, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (10, (u'', (1, 1, 1, 1)), {(u'', (0.106829, 0.702586, 0.652042, 1)): [1], (u'', (1, 0.0509804, 0.0509804, 1)): [4], (u'grey', (0.745098, 0.745098, 0.745098, 1)): [2], (u'', (0.823529, 0.705882, 0.54902, 1)): [0], (u'blue', (0, 0, 1, 1)): [6], (u'', (0.4, 0, 1, 1)): [9], (u'red', (1, 0, 0, 1)): [3], (u'yellow', (1, 1, 0, 1)): [7]})
	viewerInfo = {'cameraAttrs': {'center': (-8.4267747606795e-16, -1.3104271766067e-16, 9.8877432912934), 'fieldOfView': 18.849684534934, 'nearFar': (14.976217964974, -1.0107092541845), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 8.7265950464312}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': True, 'showShadows': False, 'viewSize': 8.8688270917569, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 1.3348363022014, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 9, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 8}

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
	formattedPositions = {'session-start': (1.155351159691909, 8.86882709175692, (1.3395405316555724, 3.9505837500000003, 8.726595046431203), (16.370238401985695, 1.165040645195333), 8.726595046431203, {(2, 0): ((-6.879216832661181, 1.2434449094635127, 13.102330090486209), (-0.7791729689523519, 0.43582107891998634, -0.450499136095727, 109.18718989286837)), (1, 0): ((-6.879216832661183, 1.2434449094635125, 13.10233009048621), (-0.7791729689523519, 0.43582107891998634, -0.45049913609572706, 109.18718989286837)), (0, 0): ((-6.879216832661183, 1.2434449094635125, 13.10233009048621), (-0.7791729689523519, 0.43582107891998634, -0.45049913609572706, 109.18718989286837))}, {(0, 0, 'Molecule'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, False, 5.0)}, 4, (1.3892258043886745, 3.93424088720653, 8.767639523590514), False, 18.84968453493425)}
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
   'cap_attributes': [ ],
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
	residueData = [(2, 'Chimera default', 'rounded', u'unknown'), (3, 'Chimera default', 'rounded', u'unknown')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDVUMY3VzdG9tX3NjZW5lcQ5VBG1vZGVxD1UGbGluZWFycRB1YlUIa2V5ZnJhbWVxEWgFKYFxEn1xEyhoCEsUaAlLAWgKXXEUaAxhaA1VCGtleWZyYW1lcRVoD2gQdWJVBXNjZW5lcRZoBSmBcRd9cRgoaAhLAWgJSwFoCl1xGWgMYWgNVQVzY2VuZXEaaA9oEHVidWIu'
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
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 0.0], 'back': [(0.3574067443365933, 0.6604015517481455, -0.6604015517481456), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.3574067443365933, 0.6604015517481455, 0.6604015517481456), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.2505628070857316, 0.2505628070857316, 0.9351131265310294), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")

angleInfo = [[17, 5, 16, 7]]

try:
	from StructMeasure.gui import restoreAngles
	restoreAngles(angleInfo)
except:
	reportRestoreError("Error restoring angle monitors in session")


def restoreRemainder():
	from SimpleSession.versions.v65 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (1007, 831)
	xformMap = {0: (((-0.46560320491151, 0.83113298065088, -0.30402569636548), 71.810897199969), (-8.0073385672252, -4.7404999850896, 6.9815513769962), True), 1: (((-0.53079441682714, 0.74454127528215, -0.40486488667995), 64.051503316534), (0.65338768073829, -0.29300568496615, 7.6865179071593), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 1: True, 260: True}

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

