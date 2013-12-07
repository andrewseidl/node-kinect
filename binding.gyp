{
  'targets': [
    {
      'target_name': 'kinect',
      'sources': [
        'src/kinect.cc',
      ],
      'libraries': [
        'libfreenect.a',
      ],
      'include_dirs': [
        '/usr/local/include',
      ],
    }
  ]
}