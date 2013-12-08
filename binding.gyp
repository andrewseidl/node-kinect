{
  'targets': [
    {
      'target_name': 'kinect',
      'sources': [
        'src/kinect.cc',
      ],
      'libraries': [
        '/usr/local/lib/libfreenect.a','/usr/local/lib/libusb-1.0.so'
      ],
      'include_dirs': [
	'/usr/local/include'
        
      ],
    }
  ]
}
