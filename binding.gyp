{
  'targets': [
    {
      'target_name': 'kinect',
      'sources': [
        'src/kinect.cc',
      ],
      'libraries': [
        '/usr/local/lib/libfreenect.a',
      ],
      'include_dirs': [
        '/usr/local/include',
      ],
    }
  ]
}
